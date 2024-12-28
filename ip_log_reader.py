#!/usr/bin/env python

import os,sys,re
import argparse
import operator
from datetime import datetime,date
import requests
import json
import csv
import pycountry
today = str(date.today())
# print(today)
def get(ip):
    #https://pytutorial.com/python-get-country-from-ip-python
    endpoint = f'https://ipinfo.io/{ip}/json'
    response = requests.get(endpoint, verify = True)
    
    if response.status_code != 200:
        return 'Status:', response.status_code, 'Problem with the request. Exiting.'
        sys.exit()

    data = response.json()
    #if 'country' in data:
    return data
    #else:
    #    return 'unknown: '+ip
        

def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")

def format_report(info, mindate, maxdate, save_list):
    width = 100  # should be 7 more than sum of cols
    report = '\nHOMD '+info+' IP/Country Report\n'
    report += "\nFrom: "+mindate+"   To: "+maxdate+"\n"
    report += ' '+'_' * width+"\n"
   
    report += "| "+f'{"Date":<12}'+ '| '+f'{"IP":<17}'+'| '
    report += f'{"Country":<30}'  + '| '+f'{"Region":<34}'+"|"+"\n"
    report += "|"+'_' * width+"|"+"\n"
    for item1 in save_list:
        for ip in item1:
            for item2 in item1[ip]:
        #print('item',item)
                if item2 not in ['country','region']:
                    report += '| '+f'{item2:<12}'
                    report += '| '+f'{ip:<17}'
                    report += '| '+f'{item1[ip]["country"]:<30}'
                    report += '| '+f'{item1[ip]["region"]:<34}'+'|\n'
    report += "|"+'_' * width+"|"+"\n"
    return report
    
def format_report2(info,save_list):
    master = []
    
    for ipline in save_list:
        
        for ip in ipline:
            obj = {}
            obj['ip'] = ip
            num = 0
            for date in ipline[ip]:
                if date not in ['country','region']:
                    for fxn in ipline[ip][date]:
                        num += int(ipline[ip][date][fxn])
            obj["fxn"] = fxn
            obj["num"] = num
            obj["country"] = ipline[ip]["country"]
            obj["region"]  = ''
            if ipline[ip]["region"]:
                obj["region"]  = ipline[ip]["region"]
            master.append(obj)
    width = 128 # should be 7 more than sum of cols
    report = '\nHOMD '+info+' IP/Country Report2\n'
    report += ' '+'_' * width+"\n"
    
    #master.sort(key=lambda x: x['country'], reverse=False)
    #s = sorted(master, key = operator.itemgetter(1, 2))
    s = sorted(master, key = lambda x: (x['country'], x['region']))
    #print(master)
    report += "| "+f'{"IP":<17}'+ '| '+f'{"Num":<12}'+'| '+f'{"Fxn":<26}'+'| '
    report += f'{"Country":<30}'  + '| '+f'{"Region":<34}'+"|"+"\n"
    report += "|"+'_' * width+"|"+"\n"
    for item in s:
        # {'128.205.81.202': {'2024-02-27': {'refseq_blast': 1}, '2024-02-29': {'refseq_blast': 16}, 'region': 'New York', 'country': 'United States'}}
        print('item',item)
        ip      = item['ip']
        num     = item['num']
        country = item['country']
        region  = item['region']
        fxn = item['fxn']
        report += '| '+f'{ip:<17}'
        report += '| '+f'{num:<12}'
        report += '| '+f'{fxn:<26}'
        report += '| '+f'{country:<30}'
        report += '| '+f'{region:<34}'+'|\n'
    report += "|"+'_' * width+"|"+"\n"
    return report
    
def process_line(fxn, dpattern, dformat, l):
    matches = re.findall(dpattern, l)
    print('matches',fxn,dpattern,matches,l)
    if len(matches) == 0:
        #  \[\s*(\d+\-\d+\-.*?)\]
        #ss matches blast \[\s*(\d+\-\d+\-.*?)\] ['2024-10-31 20:59:54'] [2024-10-31 20:59:54] INFO  IP:132.247.104.166: URL:genome_blast_single_prokka Method:blastn Sequence20:GAGTTTGATCCTGGCTCAGG
        sys.exit('date match error')
        
    date_str = matches[0]
    date_obj = datetime.strptime(date_str, dformat)
    
    #print(fxn, date_str, date_obj, date_short)
    #
    ip_pattern = r"IP:(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
    matches = re.findall(ip_pattern, l)
    if len(matches) == 0:
        sys.exit('ip match error')
    ip = matches[0]
    #print('ip',ip)
    
    if fxn in ('jb','pg'):
        url = fxn
    else:
        pts = l.split(' ')
        url ='blast'
        url_pattern = r"URL:([^\s]+)"
        matches = re.findall(url_pattern, l)
        if len(matches) > 0:
            url = matches[0]
    return [ip, date_obj, url]
        
def run(args):
    print(args)
    country_collector = {}
    ip_collector = {}
    total_hits = 0
    #urls = ['refseq_blast', 'genome_blast','genome_blast_single_ncbi','genome_blast_single_prokka']
    fxn_collector = {}
    
    # fxn_collector['refseq'] = 0
#     fxn_collector['genome'] = 0
    date_collector = []
    save_list = []
    
    
    fp = open(args.infile, 'r')
    for line in fp:
        line = line.strip()
        fxn = ''
        if not line:
            continue
         # IP will be pts[1] IF 'RemoteIP in line
        #print(line)
        # just want the IP and the count of lines per blast type or jbrowse
        # RemoteIP:171.96.190.241:::ffff:127.0.0.1 - [22/Feb/2024:10:28:31 -0500] "GET /blast_per_genome HTTP/1.1" 200 1766456 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6,2 Safari/605.1.15"
        #urls  = ["blast_sserver?type=refseq","blast_sserver?type=genome","blast_per_genome",'blast_ss_single','jbrowse','refseq_blastn']
        # [2024-02-28 22:24:07] INFO  IP:128.205.81.202: Type:refseq_blast: Requested:/
        if 'blast' in line and args.fxn =='ss':
            fxn = 'blast'
            #date_str =  2024-02-28 22:24:07
            date_format = '%Y-%m-%d %H:%M:%S'
            date_pattern = r"\[\s*(\d+\-\d+\-.*?)\]"
            info1 = 'BLAST_geolocation'
            info2 = 'BLAST'
        elif 'anvio' in line:
            fxn = 'pg'
            #date_str =  22/Feb/2024:10:28:31 -0500
            date_format = '%d/%b/%Y:%H:%M:%S %z'
            date_pattern = r"\[(\d+\/.*\/\d+.*?)\]"
            info1 = 'JBrowseNPG_geolocation'
            info2 = 'Jbrowse and Pangenome(Anvio)'
        elif 'jbrowse' in line:
            fxn = 'jb'
            #date_str =  22/Feb/2024:10:28:31 -0500
            date_format = '%d/%b/%Y:%H:%M:%S %z'
            date_pattern = r"\[(\d+\/.*\/\d+.*?)\]"
            info1 = 'JBrowseNPG_geolocation'
            info2 = 'Jbrowse and Pangenome(Anvio)'
        else:
            info1 = 'NONE'
            info2 = 'NONE'
            continue
        if fxn:
            result = process_line(fxn, date_pattern, date_format, line)
            # result = [ip, date_obj,url]
            #print('l',line)
            print('res',result)
            ip = result[0]
            dobj = result[1]
            url = result[2]
            date_short = str(dobj).split(' ')[0]
            print('date_short',date_short)
            date_collector.append({"date_short":date_short,"date_obj":dobj,})
                 
            print(fxn,url,ip)
            if fxn not in fxn_collector:
                fxn_collector[fxn] = {}
            if url not in fxn_collector[fxn]:
                fxn_collector[fxn][url] = 0
            fxn_collector[fxn][url] += 1
            if fxn not in ip_collector:
                ip_collector[fxn] = {}
            if ip not in ip_collector[fxn]:
                ip_collector[fxn][ip] = {}
    
            if date_short not in ip_collector[fxn][ip]:
                ip_collector[fxn][ip][date_short] = {}
        
            if url not in ip_collector[fxn][ip][date_short]:
                ip_collector[fxn][ip][date_short][url] = 1
            else:
                ip_collector[fxn][ip][date_short][url] += 1
    
    
    sdates = [o["date_short"] for o in date_collector]  #.map(n => n["date_short"])
    date_obs = [o["date_obj"] for o in date_collector]
    #sys.exit()
    mindate = 0
    maxdate = 0
    if date_obs:
        mindate = min(date_obs)
        maxdate = max(date_obs)
        
    print('ip_collector',ip_collector)
    print()
    for fxn in ip_collector:
        print('fxn',fxn)
        for ip in ip_collector[fxn]:
            print('ip',ip)
            obj = {}
            obj[ip] = ip_collector[fxn][ip]
            data = get(ip)
            # {'14.139.216.174': {'22/Feb/2024': {'blast_sserver?type=refseq': 1, 'jbrowse': 1}}
            #print('data',data)
            country_code = 'unknown'
            if 'country' in data:
                country_code = data['country']
            if 'region' in data:
                obj[ip]['region'] = data['region']
            c = pycountry.countries.get(alpha_2=country_code)
            obj[ip]['country'] = country_code
            if c:
                obj[ip]['country'] = c.name
                #print(c.name)
                if c.name in country_collector:
                    country_collector[c.name] += 1
                else:
                    country_collector[c.name] = 1

            save_list.append(obj)
            #print('obj',obj)
    
    report = format_report(info2, str(mindate), str(maxdate), save_list)
    print('save_list',save_list)
    # save_list [{'128.205.81.202': {'2024-02-27': {'refseq_blast': 1}, '2024-02-29': {'refseq_blast': 15, 'genome_blast_single_prokka': 1}, 'region': 'New York', 'country': 'United States'}}, 
#                {'134.130.15.1': {'2024-03-01': {'genome_blast_single_prokka': 9}, 'region': 'North Rhine-Westphalia', 'country': 'Germany'}}, 
#                {'90.65.20.62': {'2024-03-01': {'genome_blast': 17}, 'region': 'Auvergne-Rhône-Alpes', 'country': 'France'}}]
    report2 = format_report2(info2, save_list)
    print()
    print('Dates:',mindate,'To:',maxdate)
    
    #print(json.dumps(ip_collector, indent=4, sort_keys=True))
    # print('\nCountry Totals per IP')
#     print(json.dumps(country_collector, indent=4, sort_keys=True))
    print('\nHOMD Function Totals')
    print(json.dumps(fxn_collector, indent=4, sort_keys=True))
    print()
    print(report)
    print(report2)
    print('Total Hits:',total_hits)
    if args.toprinttofile:
        print_to_file(info1,mindate,maxdate,country_collector,fxn_collector,report,report2)


        
def print_to_file(info, mindate, maxdate, country_collector, fxn_collector,report,report2):
    args.outfile = 'HOMD_'+info+'_'+today+'.log'
    fp = open(args.outfile,'w')
    fp.write('\nHOMD '+info+' Log: '+today+'\n')
    fp.write('Dates: '+str(mindate)+' To: '+str(maxdate)+'\n')
    fp.write('\nCountry Totals per IP\n')
    fp.write(json.dumps(country_collector, indent=4, sort_keys=True)+'\n')
    fp.write('\nHOMD Function Totals')
    fp.write(json.dumps(fxn_collector, indent=4, sort_keys=True))
    fp.write('\n')
    fp.write(report+'\n')
    fp.write(report2+'\n')
    fp.close()
    
if __name__ == "__main__":

    usage = """
    USAGE:
        ./ip_log_reader.py -i infile 
        
        Infile (tab delimited):  [date  IP  fxn](ie 2022-04-06  98.247.104.245  refseq)

          -i /mnt/efs/homd-dev/sequenceserver-access.log -o  (blast ips only)
          -i /mnt/efs/homd/homd-access.log -o   (has jbrowse and pangenomes)
          
        Will print to file with todays date
        MUST RENAME
        
        Try These
        -fxn ss
        ./ip_log_reader.py -i /mnt/s3/homd_log/sequenceserver-access2024.12.01.log
        
        -fxn [default]
        ./ip_log_reader.py -i /mnt/s3/homd_log/homd-access2024.12.01.log
        
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=True,  action="store",   dest = "infile", default='none',
                                                    help=" ")
    parser.add_argument("-fxn", "--fxn",      required=True,  action="store",   dest = "fxn", default='none',
                                                   help="(ss)blast, (jb)jbrowse or (anvio)pangenome")
                                                   
    parser.add_argument("-o", "--outfile",  required=False,  action="store_true",   dest = "outfile", default=False,
                                                   help="outfile")
    
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", default=False,
                                                    help="verbose print()") 
    parser.add_argument("-min", "--min", required = False, action = 'store', dest = "mindate", default = '2023-01-01',
                                                  help = "")
    parser.add_argument("-max", "--max",   required=False,  action="store",    dest = "maxdate", default=None,
                                                    help="") 
    
    args = parser.parse_args()
    args.toprinttofile = True
    # if not args.maxdate:
#         args.maxdate = today
#     #parser.print_help(usage)
#     print(today)                
#     if args.fxn not in ['ss','pg','jb']:
#         sys.exit('-fxn not in (ss, pg, jb)')
#     if args.fxn == 'ss': #sequence server
#         args.toprinttofile = False
#         args.info = 'BLAST_geolocation'
#         if args.outfile:
#            args.toprinttofile = True
#            args.outfile = 'HOMD_'+args.info+'_'+today+'.log'
#     
#         blast_run(args)
#     elif args.fxn == 'jb':
#         args.toprinttofile = False
#         args.info = 'JBrowse_geolocation'
#         if args.outfile:
#            args.toprinttofile = True
#            args.outfile = 'HOMD_'+args.info+'_'+today+'.log'
#         jb_run(args, 'jbrowse_ajax')
#     elif args.fxn == 'pg':
#         args.toprinttofile = False
#         args.info = 'Pangenomes_geolocation'
#         if args.outfile:
#            args.toprinttofile = True
#            args.outfile = 'HOMD_'+args.info+'_'+today+'.log'
#         jb_run(args, 'anvio_post')
#     else:
#         print('ERROR No fxn matches')
    
    run(args)



