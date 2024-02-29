#!/usr/bin/env python

import os,sys,re
import argparse
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
    width = 100
    report = '\nHOMD BLAST+ IP/Country Report\n'
    report += "\nFrom: "+mindate+"   To: "+maxdate+"\n"
    report += ' '+'_' * width+"\n"
   
    report += "| "+f'{"Date":<27}'+'| '+f'{"IP":<20}'+'| '+f'{"Country":<30}'+"|"+f'{"Region":<17}'+"|"+"\n"
    report += "|"+'_' * width+"|"+"\n"
    for item1 in save_list:
        for ip in item1:
            for item2 in item1[ip]:
        #print('item',item)
                if item2 not in ['country','region']:
                    report += '| '+f'{item2:<27}'
                    report += '| '+f'{ip:<20}'
                    report += '| '+f'{item1[ip]["country"]:<30}'
                    report += '| '+f'{item1[ip]["region"]:<16}'+'|\n'
    report += "|"+'_' * width+"|"+"\n"
    return report
    
def run(args):
    print(args)
    country_collector = {}
    ip_collector = {}
    fxn_collector = {}
    fxn_collector['refseq'] = 0
    fxn_collector['genome'] = 0
    date_collector = []
    save_list = []
    #date_str =  22/Feb/2024:10:28:31 -0500
    date_format = '%d/%b/%Y:%H:%M:%S %z'
    # js date format
    #date_str =  2024-02-28 22:24:07
    date_format2 = '%Y-%m-%d %H:%M:%S'
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
        urls2 = ['refseq_blast', 'genome_blast','genome_blast_single_ncbi','genome_blast_single_prokka']
        ip = 0
        #matches  = re.findall(r"\[\s*(\d+/\D+/.*?)\]", line)
        matches2 = re.findall(r"\[\s*(\d+\-\d+\-.*?)\]", line)
        #print('matches2',matches2)
        if len(matches2) > 0:
            # good line means: IP date sequence
                
            if 'IP' in line:
                seq20 = ''
                for pt in pts:
                    if pt.startswith('Sequence'):
                        seq20 = pt.split(':')[1]
                if seq20:
                    print('line',line)
                    date_str = matches2[0] # [2024-02-28 22:24:07] or ['22/Feb/2024:03:27:19 -0500']
                    date_short = date_str.split(' ')[0]
                    date_obj = datetime.strptime(date_str, date_format2)
                    date_collector.append({"date_short":date_short,"date_obj":date_obj})
            for url in urls2:
                #if url in line and line.startswith('RemoteIP'):
                if url in line and 'IP' in line:
                    seq20 = ''
                    for pt in pts:
                        if pt.startswith('IP:'):
                            ip = pt.split(':')[1]
                        if pt.startswith('Sequence'):
                            seq20 = pt.split(':')[1]
                    if seq20:
                        
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
    print(ip_collector)
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
        #print(loglist)
       #  if args.mindate:
#             mindate = args.mindate
#         else:
#             mindate = loglist[0][0]
#         if args.maxdate:
#             maxdate = args.maxdate
#         else:
#             maxdate = loglist[len(loglist)-1][0]
        #print ('min',mindate,'max',maxdate)
        
            #print(row)
#       date_str = row[0]
#       ip = row[1]
#       fxn = row[2]
#       if date_str >= mindate and date_str <= maxdate:

        # country_code = 'unknown'
#         if 'country' in data:
#             country_code = data['country']
#         if 'region' in data:
#             obj['region'] = data['region']
#         c = pycountry.countries.get(alpha_2=country_code)
#         
#         obj['date'] = ip_collector[ip]["date"]
#         
#         obj['country'] = country_code
#         if c:
#             obj['country'] = c.name
#             #print(c.name)
#             if c.name in country_collector:
#                 country_collector[c.name] += 1
#             else:
#                 country_collector[c.name] = 1

        save_list.append(obj)
        print(obj)
    
    report = format_report(str(mindate), str(maxdate), save_list)
    print()
    print('Dates:',mindate,'To:',maxdate)
    
    #print(json.dumps(ip_collector, indent=4, sort_keys=True))
    print('\nCountry Totals per IP')
    print(json.dumps(country_collector, indent=4, sort_keys=True))
    #print('\nHOMD Function Totals')
    #print(json.dumps(fxn_collector, indent=4, sort_keys=True))
    print()
    print(report)
    
if __name__ == "__main__":

    usage = """
    USAGE:
        ./homd_ip_reader.py -i infile
        
        Infile (tab delimited):  [date  IP  fxn](ie 2022-04-06  98.247.104.245  refseq)
          ../homd-stats/homd_blast_ip.log

        Optional date range:
          -min/--min  date [Dafault none] (required format: YYYY-MM-DD)
          -max/--max  date [Default none] (required format: YYYY-MM-DD)
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=True,  action="store",   dest = "infile", default='none',
                                                    help=" ")
#    parser.add_argument("-s", "--source",   required=True,  action="store",   dest = "source", 
#                                                    help="ONLY segata dewhirst eren")
    
    parser.add_argument("-host", "--host",
                        required = False, action = 'store', dest = "dbhost", default = 'localhost',
                        help = "choices=['homd',  'localhost']")
    
    parser.add_argument("-d", "--delimiter", required = False, action = 'store', dest = "delimiter", default = 'tab',
                         help = "Delimiter: commaAV[Default]: 'comma' or tabKK: 'tab'")
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

    
    run(args)
   



