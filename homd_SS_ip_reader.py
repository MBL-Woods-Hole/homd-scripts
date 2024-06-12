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
import ipinfo
access_token = 'dde8a6c92662fe'
handler = ipinfo.getHandler(access_token)

# print(today)
def get(ip):
    #https://pytutorial.com/python-get-country-from-ip-python
    details = handler.getDetails(ip)
    # endpoint = f'https://ipinfo.io/{ip}/json'
#     response = requests.get(endpoint, verify = True)
#     
#     if response.status_code != 200:
#         return 'Status:', response.status_code, 'Problem with the request. Exiting.'
#         sys.exit()
# 
#     data = response.json()
    #if 'country' in data:
    return details
    #else:
    #    return 'unknown: '+ip
        

def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")

def get_rpt3(mindate, maxdate, lst):
    # {'ip': '172.85.50.14', 'url': 'refseq_blast', 'date': '2024-05-31', 'country': 'United States', 'region': 'Massachusetts'}
    # this report will be by sorted country/region
    creg_collector ={}
    for item in lst:
        creg = item['country']+':'+item['region']
        ip = item['ip']
        if creg in creg_collector:
            if ip in creg_collector[creg]:
                creg_collector[creg][ip] += 1
            else:
                creg_collector[creg][ip] = 1
            creg_collector[creg]['reg_cnt'] += 1
        else:
            creg_collector[creg] = {'reg_cnt':1,ip:1}
    #print('creg_collector',creg_collector)
    
    mykeys = creg_collector.keys()
    a = list(mykeys)
    a.sort()
    width = 100  # should be 7 more than sum of cols
    report = '\nHOMD BLAST+ Country/Region Report\n'
    report += "\nFrom: "+mindate+"   To: "+maxdate+"\n"
    report += ' '+'_' * width+"\n"
   
    report += "| "+f'{"Country":<35}'  + '| '+f'{"Region":<35}'+"| "
    #report += f'{"RegionCount":<26}'+"|"+"\n"
    report += f'{"Count":<13}'  +"\n"
    report += "|"+'_' * width+"|"+"\n"
    for key in a:
        creg = key
        
        #print('num',creg)
        #print('num2',creg_collector[creg])
        pts = creg.split(':')
        rcnt = str(creg_collector[creg]['reg_cnt'])
        cnt = 0
        for ip in creg_collector[creg]:
            if ip != 'region':
               cnt += creg_collector[creg][ip]
        ipcnt = str(cnt)
        report += '| '+f'{pts[0]:<35}'
        report += '| '+f'{pts[1]:<35}'
        #report += '| '+f'{rcnt:<13}'
        report += '| '+f'{rcnt:<13}'+'|\n'
    report += "|"+'_' * width+"|"+"\n"
    return report
    
def format_report3(mindate, maxdate, country_region_collector):
    mykeys = country_region_collector.keys()
    a = list(mykeys)
    a.sort()
    
    width = 100  # should be 7 more than sum of cols
    report = '\nHOMD BLAST+ Country/Region Report\n'
    report += "\nFrom: "+mindate+"   To: "+maxdate+"\n"
    report += ' '+'_' * width+"\n"
   
    report += "| "+f'{"Country":<35}'  + '| '+f'{"Region":<35}'+"| "
    #report += f'{"RegionCount":<26}'+"|"+"\n"
    report += f'{"RegionCount":<13}'  + '| '+f'{"IP Count":<13}'+"|"+"\n"
    report += "|"+'_' * width+"|"+"\n"
    
    
    #print(a)
    for key in a:
        creg = key
        #print('num',creg)
        #print('num2',country_region_collector[creg])
        pts = creg.split(':')
        rcnt = str(country_region_collector[creg]['region'])
        cnt = 0
        for c in country_region_collector[creg]:
            if c != 'region':
               cnt += country_region_collector[creg][c]
        ipcnt = str(cnt)
        report += '| '+f'{pts[0]:<35}'
        report += '| '+f'{pts[1]:<35}'
        report += '| '+f'{rcnt:<13}'
        report += '| '+f'{ipcnt:<13}'+'|\n'
    report += "|"+'_' * width+"|"+"\n"
    return report
    
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
    line_collector = [] # ip,country,region
    date_collector = []
    urls = ['refseq_blast', 'genome_blast','genome_blast_single_ncbi','genome_blast_single_prokka']
    date_format = '%Y-%m-%d %H:%M:%S'
    fxn_collector = 0
    total_hits = 0
    fp = open(args.infile, 'r')
    for line in fp:
        line = line.strip()
        if not line:
            continue
        
        ip = 0
        #matches  = re.findall(r"\[\s*(\d+/\D+/.*?)\]", line)
        matches = re.findall(r"\[\s*(\d+\-\d+\-.*?)\]", line)
        #print('matches',matches)
        if len(matches) > 0:
            # good line means: IP date sequence
            fxn_collector += 1
            if 'IP' in line:
                #()print(line)
                line_obj = {}
                pts = line.split(' ') # IP will be pts[1] IF 'RemoteIP in line
                url   = ''
                seq20 = ''
                for pt in pts:
                    if pt.startswith('IP:'):
                        ip = pt.split(':')[1]
                    if pt.startswith('Sequence'):
                        seq20 = pt.split(':')[1]
                    if pt.startswith('URL:'):
                        url = pt.split(':')[1]
                if seq20 and url in urls:
                    total_hits += 1
                    date_str = matches[0] # [2024-02-28 22:24:07] or ['22/Feb/2024:03:27:19 -0500']
                    date_short = date_str.split(' ')[0]
                    date_obj = datetime.strptime(date_str, date_format)
                    date_collector.append({"date_short":date_short,"date_obj":date_obj})
                    line_obj['ip'] = ip
                    line_obj['url'] = url
                    line_obj['date'] = date_short
                    line_obj['country'] = 'unknown'
                    line_obj['region'] = 'unknown'
                    try:
                        print('fetching data',ip)
                        data = get(ip)
                        #print('data',data)
                        cc = data.country
                        c = pycountry.countries.get(alpha_2=cc)
                        if c:
                            line_obj['country'] = c.name
                            line_obj['region'] = data.region
                    except:
                        line_obj['country'] = 'unknown'
                        line_obj['region'] = 'unknown'
                    #print(line_obj)
                    line_collector.append(line_obj)
    
    sdates = [o["date_short"] for o in date_collector]  #.map(n => n["date_short"])
    date_obs = [o["date_obj"] for o in date_collector]
    #sys.exit()
    
    mindate = min(date_obs)
    maxdate = max(date_obs)
    rpt3 = get_rpt3(str(mindate), str(maxdate),line_collector) # basic country/region, count
    print(rpt3)
    
    print('\nTotal Line Count:',len(line_collector))
    if args.toprinttofile:
        print_to_file(args,mindate,maxdate,country_collector,fxn_collector,report1,report2)
        pass

        
def print_to_file(args,mindate,maxdate,country_collector,fxn_collector,r1,r2):
    fp = open(args.outfile,'w')
    fp.write('\nHOMD '+args.info+' Log: '+today+'\n')
    fp.write('Dates: '+str(mindate)+' To: '+str(maxdate)+'\n')
    fp.write('\nCountry Totals per IP\n')
    fp.write(json.dumps(country_collector, indent=4, sort_keys=True)+'\n')
    fp.write('\nHOMD Function Totals')
    fp.write(json.dumps(fxn_collector, indent=4, sort_keys=True))
    fp.write('\n')
    fp.write(r1+'\n')
    fp.write(r2+'\n')
    fp.close()
    
if __name__ == "__main__":

    usage = """
    USAGE:
        ./homd_ip_reader.py -i infile -fxn [ss (blast), jb (jbrowse), pg (anvio-pangenomes)]
        
        Infile (tab delimited):  [date  IP  fxn](ie 2022-04-06  98.247.104.245  refseq)

          -i /mnt/s3/homd_log/sequenceserver-access2024XXX.log   (blast ips only)
          
         will print to file by default
          
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=True,  action="store",   dest = "infile", default='none',
                                                    help=" ")
    #parser.add_argument("-fxn", "--fxn",      required=False,  action="store",   dest = "fxn", 
    #                                               help="blast, jbrowse or pangenome")
    parser.add_argument("-o", "--outfile",  required=False,  action="store_true",   dest = "outfile", default=False,
                                                   help="outfile")
    
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", default=False,
                                                    help="verbose print()") 
    parser.add_argument("-min", "--min", required = False, action = 'store', dest = "mindate", default = '2023-01-01',
                                                  help = "")
    parser.add_argument("-max", "--max",   required=False,  action="store",    dest = "maxdate", default=None,
                                                    help="") 
    
    args = parser.parse_args()

    args.info = 'BLAST_geolocation'
    args.toprinttofile = False
    args.outfile = 'HOMD_'+args.info+'_'+today+'.log'
    
    blast_run(args)
   



