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

def format_report(mindate, maxdate, save_list):
    width = 100  # should be 7 more than sum of cols
    report = '\nHOMD BLAST+ IP/Country Report\n'
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
    
def format_report2(save_list):
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
            obj["num"] = num
            obj["country"] = ipline[ip]["country"]
            obj["region"]  = ''
            if ipline[ip]["region"]:
                obj["region"]  = ipline[ip]["region"]
            master.append(obj)
    width = 100  # should be 7 more than sum of cols
    report = '\nHOMD BLAST+ IP/Country Report2\n'
    report += ' '+'_' * width+"\n"
    
    #master.sort(key=lambda x: x['country'], reverse=False)
    #s = sorted(master, key = operator.itemgetter(1, 2))
    s = sorted(master, key = lambda x: (x['country'], x['region']))
    #print(master)
    report += "| "+f'{"IP":<17}'+ '| '+f'{"Num":<12}'+'| '
    report += f'{"Country":<30}'  + '| '+f'{"Region":<34}'+"|"+"\n"
    report += "|"+'_' * width+"|"+"\n"
    for item in s:
        # {'128.205.81.202': {'2024-02-27': {'refseq_blast': 1}, '2024-02-29': {'refseq_blast': 16}, 'region': 'New York', 'country': 'United States'}}
        ip      = item['ip']
        num     = item['num']
        country = item['country']
        region  = item['region']
        report += '| '+f'{ip:<17}'
        report += '| '+f'{num:<12}'
        report += '| '+f'{country:<30}'
        report += '| '+f'{region:<34}'+'|\n'
    report += "|"+'_' * width+"|"+"\n"
    return report

def blast_run(args):
    print(args)
    country_collector = {}
    ip_collector = {}
    total_hits = 0
    urls = ['refseq_blast', 'genome_blast','genome_blast_single_ncbi','genome_blast_single_prokka']
    fxn_collector = {}
    for url in urls:
        fxn_collector[url] = 0
    # fxn_collector['refseq'] = 0
#     fxn_collector['genome'] = 0
    date_collector = []
    save_list = []
    #date_str =  22/Feb/2024:10:28:31 -0500
    #date_format = '%d/%b/%Y:%H:%M:%S %z'
    # js date format
    #date_str =  2024-02-28 22:24:07
    date_format = '%Y-%m-%d %H:%M:%S'
    fp = open(args.infile, 'r')
    for line in fp:
        line = line.strip()
        if not line:
            continue
        pts = line.split(' ') # IP will be pts[1] IF 'RemoteIP in line
        #print(line)
        # just want the IP and the count of lines per blast type or jbrowse
        # RemoteIP:171.96.190.241:::ffff:127.0.0.1 - [22/Feb/2024:10:28:31 -0500] "GET /blast_per_genome HTTP/1.1" 200 1766456 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6,2 Safari/605.1.15"
        #urls  = ["blast_sserver?type=refseq","blast_sserver?type=genome","blast_per_genome",'blast_ss_single','jbrowse','refseq_blastn']
        # [2024-02-28 22:24:07] INFO  IP:128.205.81.202: Type:refseq_blast: Requested:/
        
        ip = 0
        #matches  = re.findall(r"\[\s*(\d+/\D+/.*?)\]", line)
        matches = re.findall(r"\[\s*(\d+\-\d+\-.*?)\]", line)
        #print('matches',matches)
        if len(matches) > 0:
            # good line means: IP date sequence
                
            if 'IP' in line:
                seq20 = ''
                # for pt in pts:
#                     if pt.startswith('Sequence'):
#                         seq20 = pt.split(':')[1]
                # if seq20:
#                     print('line',line)
#                     total_hits += 1
#                     date_str = matches[0] # [2024-02-28 22:24:07] or ['22/Feb/2024:03:27:19 -0500']
#                     date_short = date_str.split(' ')[0]
#                     date_obj = datetime.strptime(date_str, date_format)
#                     date_collector.append({"date_short":date_short,"date_obj":date_obj})
#             
                url = ''
                for pt in pts:
                    if pt.startswith('IP:'):
                        ip = pt.split(':')[1]
                    if pt.startswith('Sequence'):
                        seq20 = pt.split(':')[1]
                    if pt.startswith('URL:'):
                        url = pt.split(':')[1]
                if seq20 and url in urls:
                    print('line',line)
                    total_hits += 1
                    date_str = matches[0] # [2024-02-28 22:24:07] or ['22/Feb/2024:03:27:19 -0500']
                    date_short = date_str.split(' ')[0]
                    date_obj = datetime.strptime(date_str, date_format)
                    date_collector.append({"date_short":date_short,"date_obj":date_obj})
            
                    fxn_collector[url] += 1
                    if ip not in ip_collector:
                        ip_collector[ip] = {}
            
                    if date_short not in ip_collector[ip]:
                        ip_collector[ip][date_short] = {}
                
                    if url not in ip_collector[ip][date_short]:
                        ip_collector[ip][date_short][url] = 1
                    else:
                        ip_collector[ip][date_short][url] += 1
            
    sdates = [o["date_short"] for o in date_collector]  #.map(n => n["date_short"])
    date_obs = [o["date_obj"] for o in date_collector]
    #sys.exit()
    
    mindate = min(date_obs)
    maxdate = max(date_obs)
    #print('ip_collector',ip_collector)
    print()
    
    for ip in ip_collector:
        obj = {}
        obj[ip] = ip_collector[ip]
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
    
    report = format_report(str(mindate), str(maxdate), save_list)
    print('save_list',save_list)
    # save_list [{'128.205.81.202': {'2024-02-27': {'refseq_blast': 1}, '2024-02-29': {'refseq_blast': 15, 'genome_blast_single_prokka': 1}, 'region': 'New York', 'country': 'United States'}}, 
#                {'134.130.15.1': {'2024-03-01': {'genome_blast_single_prokka': 9}, 'region': 'North Rhine-Westphalia', 'country': 'Germany'}}, 
#                {'90.65.20.62': {'2024-03-01': {'genome_blast': 17}, 'region': 'Auvergne-Rhône-Alpes', 'country': 'France'}}]
    report2 = format_report2(save_list)
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
        print_to_file(args,mindate,maxdate,country_collector,fxn_collector)

def jb_run(args, search_for):
    print(args)
    country_collector = {}
    ip_collector = {}
    urls = ['jbrowse_ajax']
    fxn_collector = 0
    
    # fxn_collector['refseq'] = 0
#     fxn_collector['genome'] = 0
    date_collector = []
    save_list = []
    
    date_format = '%d/%b/%Y:%H:%M:%S %z'  # 22/Feb/2024:10:28:31 -0500
    # js date format
    
    #date_format = '%Y-%m-%d %H:%M:%S'  # 2024-02-28 22:24:07
    fp = open(args.infile, 'r')
    for line in fp:
        line = line.strip()
        if not line:
            continue
        ip = 0
        if 'RemoteIP' in line and search_for in line:
            pts = line.split(':') # IP will be pts[1] IF 'RemoteIP in line
            
            ip = pts[1]
            #print(ip,line)
            #matches  = re.findall(r"\[\s*(\d+/\D+/.*?)\]", line)
            matches = re.findall(r"\[(\d+\/.*\/\d+.*?)\]", line)
            #matches = re.findall(r"\[(.*?)\]", line)
            print('matches',matches)
            
            if len(matches) > 0:
                # good line means: IP date sequence
                fxn_collector += 1
                date_str = matches[0] # [2024-02-28 22:24:07] or ['22/Feb/2024:03:27:19 -0500']
                #date_short = date_str.split(' ')[0]
                date_obj = datetime.strptime(date_str, date_format)
                date_short = str(date_obj).split(' ')[0]
                date_collector.append({"date_short":date_short,"date_obj":date_obj})
                
                #for url in urls2:
                    #if url in line and line.startswith('RemoteIP'):
     #            if 'IP' in line:
#                     seq20 = ''
#                     url = ''
#                     for pt in pts:
#                         if pt.startswith('IP:'):
#                             ip = pt.split(':')[1]
#                         if pt.startswith('Sequence'):
#                             seq20 = pt.split(':')[1]
#                         if pt.startswith('URL:'):
#                             url = pt.split(':')[1]
#                     if seq20 and url in urls:
#                         fxn_collector[url] += 1
                if ip not in ip_collector:
                    ip_collector[ip] = {}
                    #ip_collector[ip]['num'] = 0
                if date_short not in ip_collector[ip]:
                    ip_collector[ip][date_short] = {'num':1}
                else:
                    ip_collector[ip][date_short]['num'] += 1
    
    if len(ip_collector.keys()) == 0:
        sys.exit('no data')
    sdates = [o["date_short"] for o in date_collector]  #.map(n => n["date_short"])
    date_obs = [o["date_obj"] for o in date_collector]
    #sys.exit()
    
    mindate = min(date_obs)
    maxdate = max(date_obs)
    #print(ip_collector)
    print()
    for ip in ip_collector:
        obj = {}
        obj[ip] = ip_collector[ip]
        data = get(ip)
        # {'14.139.216.174': {'22/Feb/2024': {'blast_sserver?type=refseq': 1, 'jbrowse': 1}}
        print('data',data)
        country_code = 'unknown'
        region = 'unknown'
        if 'country' in data:
            country_code = data['country']
        if 'region' in data:
            region = data['region']
        
        c = pycountry.countries.get(alpha_2=country_code)
        obj[ip]['country'] = country_code
        obj[ip]['region'] = region
        if c:
            obj[ip]['country'] = c.name
            #print(c.name)
            if c.name in country_collector:
                country_collector[c.name] += 1
            else:
                country_collector[c.name] = 1

        save_list.append(obj)
        print(obj)
    
    report = format_report(str(mindate), str(maxdate), save_list)
    print('save_list',save_list)
    #save_list [{'75.67.63.113': {'2024-03-13': {'num': 20}, '2024-03-14': {'num': 1}, 'country': 'United States', 'region': 'Massachusetts'}}]
    report2 = format_report2(save_list)
    print()
    print('Dates:',mindate,'To:',maxdate)
    
    
    
    
    print()
    print(report)
    print(report2)
    print('\nTotal Line Count:',fxn_collector)
    if args.toprinttofile:
        print_to_file(args,mindate,maxdate,country_collector,fxn_collector)
        
def print_to_file(args,mindate,maxdate,country_collector,fxn_collector):
    fp = open(args.outfile,'w')
    fp.write('\nHOMD '+args.info+' Log: '+today+'\n')
    fp.write('Dates: '+str(mindate)+' To: '+str(maxdate)+'\n')
    fp.write('\nCountry Totals per IP\n')
    fp.write(json.dumps(country_collector, indent=4, sort_keys=True)+'\n')
    fp.write('\nHOMD Function Totals')
    fp.write(json.dumps(fxn_collector, indent=4, sort_keys=True))
    fp.write('\n')
    fp.write(report+'\n')
    fp.close()
    
if __name__ == "__main__":

    usage = """
    USAGE:
        ./homd_ip_reader.py -i infile -fxn [ss (blast), jb (jbrowse), pg (anvio-pangenomes)]
        
        Infile (tab delimited):  [date  IP  fxn](ie 2022-04-06  98.247.104.245  refseq)

          -i /mnt/efs/homd-dev/sequenceserver-access.log -o  (blast ips only)
          -i /mnt/efs/homd/homd-access.log -o   (has jbrowse and pangenomes)
          
        Adding -o/--outfile will print to file
          
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=True,  action="store",   dest = "infile", default='none',
                                                    help=" ")
    parser.add_argument("-fxn", "--fxn",      required=True,  action="store",   dest = "fxn", 
                                                   help="blast, jbrowse or pangenome")
    parser.add_argument("-o", "--outfile",  required=False,  action="store_true",   dest = "outfile", default=False,
                                                   help="outfile")
    
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", default=False,
                                                    help="verbose print()") 
    parser.add_argument("-min", "--min", required = False, action = 'store', dest = "mindate", default = '2023-01-01',
                                                  help = "")
    parser.add_argument("-max", "--max",   required=False,  action="store",    dest = "maxdate", default=None,
                                                    help="") 
    
    args = parser.parse_args()
    # if not args.maxdate:
#         args.maxdate = today
#     #parser.print_help(usage)
#     print(today)                
    if args.fxn not in ['ss','pg','jb']:
        sys.exit('-fxn not in (ss, pg, jb)')
    if args.fxn == 'ss': #sequence server
        args.toprinttofile = False
        args.info = 'BLAST_geolocation'
        if args.outfile:
           args.toprinttofile = True
           args.outfile = 'HOMD_'+args.info+'_'+today+'.log'
    
        blast_run(args)
    elif args.fxn == 'jb':
        args.toprinttofile = False
        args.info = 'JBrowse_geolocation'
        if args.outfile:
           args.toprinttofile = True
           args.outfile = 'HOMD_'+args.info+'_'+today+'.log'
        jb_run(args, 'jbrowse_ajax')
    elif args.fxn == 'pg':
        args.toprinttofile = False
        args.info = 'Pangenomes_geolocation'
        if args.outfile:
           args.toprinttofile = True
           args.outfile = 'HOMD_'+args.info+'_'+today+'.log'
        jb_run(args, 'anvio_post')
    else:
        print('ERROR No fxn matches')
   



