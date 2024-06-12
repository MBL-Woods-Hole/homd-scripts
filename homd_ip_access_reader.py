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

    return details
    #else:
    #    return 'unknown: '+ip
        

# def validate(date_text):
#     try:
#         datetime.datetime.strptime(date_text, '%Y-%m-%d')
#     except ValueError:
#         raise ValueError("Incorrect data format, should be YYYY-MM-DD")

# def format_report3(mindate, maxdate, country_region_collector):
#     mykeys = country_region_collector.keys()
#     a = list(mykeys)
#     a.sort()
#     
#     width = 100  # should be 7 more than sum of cols
#     report = '\nHOMD BLAST+ Country/Region Report\n'
#     report += "\nFrom: "+mindate+"   To: "+maxdate+"\n"
#     report += ' '+'_' * width+"\n"
#    
#     report += "| "+f'{"Country":<35}'  + '| '+f'{"Region":<35}'+"| "
#     #report += f'{"RegionCount":<26}'+"|"+"\n"
#     report += f'{"RegionCount":<13}'  + '| '+f'{"IP Count":<13}'+"|"+"\n"
#     report += "|"+'_' * width+"|"+"\n"
#     
#     
#     #print(a)
#     for key in a:
#         creg = key
#         print('num',creg)
#         print('num2',country_region_collector[creg])
#         pts = creg.split(':')
#         rcnt = str(country_region_collector[creg]['region'])
#         cnt = 0
#         for c in country_region_collector[creg]:
#             if c != 'region':
#                cnt += country_region_collector[creg][c]
#         ipcnt = str(cnt)
#         report += '| '+f'{pts[0]:<35}'
#         report += '| '+f'{pts[1]:<35}'
#         report += '| '+f'{rcnt:<13}'
#         report += '| '+f'{ipcnt:<13}'+'|\n'
#     report += "|"+'_' * width+"|"+"\n"
#     return report
    
def ip_report(mindate, maxdate, ip_collector, line_list, report_title):
    width = 100  # should be 7 more than sum of cols
    report = '\n'+report_title+'\n'
    report += "From: "+mindate+"   To: "+maxdate+"\n"
    report += ' '+'_' * width+"\n"
   
    report += "| "+f'{"Date":<12}'+ '| '+f'{"IP":<17}'+'| '
    report += f'{"Country":<30}'  + '| '+f'{"Region":<34}'+"|"+"\n"
    report += "|"+'_' * width+"|"+"\n"
    
    for line in line_list:
        ip = line['ip']
        date_pts = line['date'].split(':')
        date = date_pts[0]
        country = ip_collector[ip]['country']
        region = ip_collector[ip]['region']
        
        report += '| '+f'{date:<12}'
        report += '| '+f'{ip:<17}'
        report += '| '+f'{country:<30}'
        report += '| '+f'{region:<34}'+'|\n'
    report += "|"+'_' * width+"|"+"\n"
    report += "| Total Count:"+ str(len(line_list))+'\n'
    report += "|"+'_' * width+"|"+"\n"
    print(report)

def counts_report(mindate, maxdate, ip_collector, line_list, report_title):
    creg_lookup = {}
    for line in line_list:
        ip = line['ip']
        country = ip_collector[ip]['country']
        region = ip_collector[ip]['region']
        creg = country+'--'+region
        if creg not in creg_lookup:
            creg_lookup[creg] = 0
        creg_lookup[creg] += 1
    
    width = 100  # should be 7 more than sum of cols
    report = '\n'+report_title+'\n'
    report += "From: "+mindate+"   To: "+maxdate+"\n"
    report += ' '+'_' * width+"\n"
    
    report += "| "+f'{"Country":<34}'  + '| '+f'{"Region":<33}'+"|"
    report += f'{"Count":<29}'+ '|\n'
    
    report += "|"+'_' * width+"|"+"\n"
    mykeys = creg_lookup.keys()
    a = list(mykeys)
    a.sort()
    for creg in a:
        cnt = str(creg_lookup[creg])
        pts = creg.split('--')
        country = pts[0]
        region = pts[1]
        
        report += '| '+f'{country:<34}'
        report += '| '+f'{region:<33}'
        report += '| '+f'{cnt:<28}'+'|\n'
    report += "|"+'_' * width+"|"+"\n"
    print(report)
       

def run(args):
    print(args)
    country_collector = {}
    ip_collector = {}
    urls = ['jbrowse_ajax']
    jbrowse_collector = []
    explorer_collector = []
    ecology_collector = []
    pangenome_collector=[]
    
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
        jbrowse_obj = {}
        explorer_obj = {}
        ecology_obj = {}
        pangenome_obj={}
        
        line = line.strip()
        if not line:
            continue
        ip = 0
        #matches  = re.findall(r"\[\s*(\d+/\D+/.*?)\]", line)
        matches = re.findall(r"\[(\d+\/.*\/\d+.*?)\]", line)   # date
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
                #print(line)
                
                for pt in pts:
                    if pt.startswith('RemoteIP:'):
                        ip = pt.split(':')[1]
                if ip:
                    date_str = matches[0] # [2024-02-28 22:24:07] or ['22/Feb/2024:03:27:19 -0500']
                    date_short = date_str.split(' ')[0]
                    #print('date_short',date_short)
                    date_obj = datetime.strptime(date_str, date_format)
                    date_collector.append({"date_short":date_short,"date_obj":date_obj})
                    ip_collector[ip] = {'country':'unknown','region':'unknown'}
                        
                        #ip_collector[ip]['count'] = 1
                    
                    #print(ip)
    
                    if 'ecology' in line:
                        ecology_obj = {"ip":ip,"date":date_short}
                        ecology_collector.append(ecology_obj)
                    if 'explorer' in line:
                        explorer_obj = {"ip":ip,"date":date_short}
                        explorer_collector.append(explorer_obj)
                    if 'jbrowse' in line:
                        jbrowse_obj = {"ip":ip,"date":date_short}
                        jbrowse_collector.append(jbrowse_obj)
                    if 'pangenome' in line:
                        pangenome_obj = {"ip":ip,"date":date_short}
                        pangenome_collector.append(pangenome_obj)
    for ip in ip_collector:
        try:
            print('Fetching data',ip)
            data = get(ip)
            #print(data)
        
            cc = data.country
            c = pycountry.countries.get(alpha_2=cc)
            if c:
                ip_collector[ip]['country'] = c.name
                ip_collector[ip]['region'] = data.region
        except:
            print('HTTP FAILED',ip)
            ip_collector[ip]['country'] = 'unknown'
            ip_collector[ip]['region'] = 'unknown'
    sdates = [o["date_short"] for o in date_collector]  #.map(n => n["date_short"])
    date_obs = [o["date_obj"] for o in date_collector]
    #sys.exit()
    mindate = min(date_obs)
    maxdate = max(date_obs)
    ip_report(str(mindate), str(maxdate), ip_collector, explorer_collector,'HOMD Genome Explorer Raw Hits+ Date/IP/Country/Region Report')
    counts_report(str(mindate), str(maxdate), ip_collector, explorer_collector,'HOMD Genome Explorer Hits+ Country/Region/Counts Report')
    print('Total Explorer Hits',str(len(explorer_collector)))
    ip_report(str(mindate), str(maxdate), ip_collector, ecology_collector,'HOMD Ecology Raw Hits+ Date/IP/Country/Region Report')
    counts_report(str(mindate), str(maxdate), ip_collector, ecology_collector,'HOMD Ecology Hits+ Country/Region/Counts Report')
    print('Total Ecology Hits',str(len(ecology_collector)))
    ip_report(str(mindate), str(maxdate), ip_collector, pangenome_collector,'HOMD Raw Pangenome Hits+ Date/IP/Country/Region Report')
    counts_report(str(mindate), str(maxdate), ip_collector, pangenome_collector,'HOMD Pangenome Hits+ Country/Region/Counts Report')
    print('Total Pangenome Hits',str(len(pangenome_collector)))
    ip_report(str(mindate), str(maxdate), ip_collector, jbrowse_collector,'HOMD Raw JBrowse Hits+ Date/IP/Country/Region Report')
    counts_report(str(mindate), str(maxdate), ip_collector, jbrowse_collector,'HOMD JBrowse Hits+ Country/Region/Counts Report')
    print('Total JBrowse Hits',str(len(jbrowse_collector)))
    # print('eco',ecology_collector)
#     print('exp',explorer_collector)
#     print('jb',jbrowse_collector)
#     print('pg',pangenome_collector)
        
        
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
        ./homd_access_ip_reader.py -i ../homd-access.log
        
         will print to file by default
          
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=True,  action="store",   dest = "infile", default='none',
                                                    help=" ")
    
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
    # if args.fxn not in ['ss','pg','jb']:
#         sys.exit('-fxn not in (ss, pg, jb)')
#     if args.fxn == 'ss': #sequence server
#         args.info = 'BLAST_geolocation'
#         args.toprinttofile = True
#         args.outfile = 'HOMD_'+args.info+'_'+today+'.log'
#     
#         blast_run(args)
#     elif args.fxn == 'jb':
#         args.info = 'JBrowse_geolocation'
#         args.toprinttofile = True
#         args.outfile = 'HOMD_'+args.info+'_'+today+'.log'
#         jb_run(args, 'jbrowse_ajax')
#     elif args.fxn == 'pg':
#         args.info = 'Pangenomes_geolocation'
#         args.toprinttofile = True
#         args.outfile = 'HOMD_'+args.info+'_'+today+'.log'
#         jb_run(args, 'anvio_post')
#     else:
#         print('ERROR No fxn matches')
    run(args)



