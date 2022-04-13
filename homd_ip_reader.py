#!/usr/bin/env python

import os,sys
import argparse
import datetime
import requests
import json
import csv
import pycountry


def get(ip):
    #https://pytutorial.com/python-get-country-from-ip-python
    endpoint = f'https://ipinfo.io/{ip}/json'
    response = requests.get(endpoint, verify = True)
    
    if response.status_code != 200:
        return 'Status:', response.status_code, 'Problem with the request. Exiting.'
        exit()

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
    report = '\nHOMD BLAST+ IP/Country Report\n'
    report += "\nFrom: "+mindate+"   To: "+maxdate+"\n"
    report += ' '+'_'*75+"\n"
   
    report += "| "+f'{"Date":<20}'+'| '+f'{"IP":<20}'+'| '+f'{"Country":<30}'+"|"+"\n"
    report += "|"+'_'*75+"|"+"\n"
    for item in save_list:
        print(item)
        report += '| '+f'{item["date"]:<20}'
        report += '| '+f'{item["ip"]:<20}'
        report += '| '+f'{item["country"]:<30}'+'|\n'
    report += "|"+'_'*75+"|"+"\n"
    return report
    
def run(args):
    print(args)
    country_collector = {}
    ip_collector = {}
    fxn_collector = {}
    fxn_collector['refseq'] = 0
    fxn_collector['genome'] = 0
    save_list = []
    
    with open(args.infile) as csv_file: 
        csv_reader = csv.reader(csv_file, delimiter='\t') # KK tab
        loglist = list(csv_reader)
        #print(loglist)
        if args.mindate:
            mindate = args.mindate
        else:
            mindate = loglist[0][0]
        if args.maxdate:
            maxdate = args.maxdate
        else:
            maxdate = loglist[len(loglist)-1][0]
        #print ('min',mindate,'max',maxdate)
        for row in loglist:
            #print(row)
            date_str = row[0]
            ip = row[1]
            fxn = row[2]
            if date_str >= mindate and date_str <= maxdate:
                
                #print(ip)
                obj = {}
                
                if ip in ip_collector:
                    ip_collector[ip] += 1
                else:
                    ip_collector[ip] = 1
                if fxn in fxn_collector:
                    fxn_collector[fxn] +=1
                data = get(ip)
                #print('data',data)
                my_country_code = 'unknown'
                if 'country' in data:
                    my_country_code = data['country']
                
                c = pycountry.countries.get(alpha_2=my_country_code)
                obj['date'] = date_str
                obj['ip'] = ip
                obj['country'] = my_country_code
                if c:
                    obj['country'] = c.name
                    #print(c.name)
                    if c.name in country_collector:
                        country_collector[c.name] += 1
                    else:
                        country_collector[c.name] = 1

                save_list.append(obj)
            
    #print(save_list)
    report = format_report(mindate, maxdate, save_list)
    
    print(report)
    print('Dates:',mindate,'To:',maxdate)
    print('IP Totals')
    print(json.dumps(ip_collector, indent=4, sort_keys=True))
    print('\nCountry Totals')
    print(json.dumps(country_collector, indent=4, sort_keys=True))
    print('\nHOMD Function Totals')
    print(json.dumps(fxn_collector, indent=4, sort_keys=True))
    print()
    
    
if __name__ == "__main__":

    usage = """
    USAGE:
        ./homd_ip_reader.py -i infile
        
        Infile (tab delimited):  [date	IP	fxn](ie 2022-04-06	98.247.104.245	refseq)
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
    parser.add_argument("-min", "--min", required = False, action = 'store', dest = "mindate", default = None,
                                                  help = "")
    parser.add_argument("-max", "--max",   required=False,  action="store",    dest = "maxdate", default=None,
                                                    help="") 
    
    args = parser.parse_args()
    
    #parser.print_help(usage)
                        

    
    run(args)
   



