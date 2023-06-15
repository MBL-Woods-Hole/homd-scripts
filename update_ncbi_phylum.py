#!/usr/bin/env python

## SEE https://docs.dhtmlx.com/suite/tree__api__refs__tree.html // new version 7 must load from json file
# this script creates a list of json objects that allows the dhtmlx javascript library
# to parse and show a taxonomy tree (Written for HOMD)
##
import os, sys
import gzip
import json
#from json import JSONEncoder
import argparse
import csv,re
from Bio import SeqIO
sys.path.append('../homd-data/')
sys.path.append('../../homd-data/')
from connect import MyConnection,mysql
import datetime
import requests
global mysql_errors
mysql_errors = []
"""

"""
today = str(datetime.date.today())



    
def run(args):
    #for root, dirs, files in os.walk(args.indir):
    fp = open(args.infile,'r')
    collector = {}
    pcollector={}
    start = 1
    new_phylum =''
    old_phylum = ''
    otid=''
    new_taxonid=''
    for line in fp:
        line = line.strip()
        
        parts = line.split('\t')
        if parts[0] == 'Taxonomy Source':
            continue
        
        #print('0',parts)
        
        if start==1 and parts[0]=='HOMD':
            #print('1',parts)
            otid = int(parts[1].split('-')[1])
            collector[otid] = {}
            collector[otid]["old_phylum"] = parts[3]
            #old_phylum = parts[3]
            if len(parts) >= 11 and parts[10]:
               new_taxonid = parts[10]
               collector[otid]["new_taxonid"] = parts[10]
        elif start==1 and parts[0]=='NCBI':
            start = 0 
            #new_phylum = parts[3]
            collector[otid]["new_phylum"] = parts[3]
            pcollector[parts[3]]=1
        elif parts[0] == '':
            start = 1
            new_phylum = ''
            old_phylum = ''
            otid = ''
            new_taxonid = ''    
        #if otid and new_phylum and old_phylum:
        #    print('otid',otid,'new:',new_phylum,'old:',old_phylum)
    #print(collector) 
    newpcollector = {}
    for otid in collector:
        if 'new_taxonid' in collector[otid]:
            #print(otid, collector[otid])
            q = "UPDATE `homd`.`otid_prime` set ncbi_taxon_id='%s' WHERE otid='%s'"
            q = q % (collector[otid]['new_taxonid'], otid)
            print(q)
            myconn.execute_no_fetch(q % ())
        else:
            newpcollector[collector[otid]['new_phylum']] = {'otid':otid,'old':collector[otid]['old_phylum']}
    
    for p in newpcollector: 
        #print('new',p,' all',newpcollector[p])
        pass
def print_dict(filename, dict):
    print('writing',filename)
    with open(filename, 'w') as outfile:
        json.dump(dict, outfile, indent=args.indent)

        
if __name__ == "__main__":

    usage = """
    USAGE:
        ./add_genomes_to_NCBI_METAV10_1.py 
        
        host and annotation will determine directory to search
        
        -host/--host [homd]  default:localhost
       
        

    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=True,  action="store",   dest = "infile", default='none',
                                                   help=" ")
    # parser.add_argument("-a", "--anno",   required=False,  action="store",   dest = "anno",  default='ncbi',
#                                                     help="")
#     parser.add_argument("-w", "--write",   required=False,  action="store_true",   dest = "write2db", default=False,
#                                                     help=" ")
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",   dest = "verbose", default=False,
                                                    help=" ")
    parser.add_argument("-host", "--host",
                        required = False, action = 'store', dest = "dbhost", default = 'localhost',
                        help = "choices=['homd',  'localhost']")
    
    # parser.add_argument("-s", "--start_digit",   required=False,  action="store",   dest = "start_digit", default='1',
#                                                     help=" ")
#     parser.add_argument("-o", "--outfile",   required=False,  action="store",    dest = "out", default='ncbi_meta_info.tsv',
#                                                     help="verbose print()")
    args = parser.parse_args()
    
    #parser.print_help(usage)
                        
    if args.dbhost == 'homd_dev':
        #args.json_file_path = '/groups/vampsweb/vamps/nodejs/json'
        #args.TAX_DATABASE = 'HOMD_taxonomy'
        args.DATABASE = 'homd'
        #dbhost_old = '192.168.1.51'
        dbhost= '192.168.1.46'   #TESTING is 1.46  PRODUCTION is 1.42
        #dbhost= '192.168.1.42' 
        args.prettyprint = False
        #args.ncbi_dir = '/mnt/efs/bioinfo/projects/homd_add_genomes_V10.1/GCA_V10.1_all'
        #args.prokka_dir = '/mnt/efs/bioinfo/projects/homd_add_genomes_V10.1/prokka_V10.1_all'
    elif args.dbhost == 'homd_prod':  
        args.DATABASE = 'homd'
        #dbhost_old = '192.168.1.51'
        dbhost= '192.168.1.42' 
    elif args.dbhost == 'localhost':
        #args.json_file_path = '/Users/avoorhis/programming/homd-data/json'
        #args.TAX_DATABASE  = 'HOMD_taxonomy'
        args.DATABASE = 'homd'
        dbhost = 'localhost'
        
        #dbhost_old = 'localhost'
    else:
        sys.exit('dbhost - error')
    
    
    myconn = MyConnection(host=dbhost,   read_default_file = "~/.my.cnf_node")

    args.indent = 4
    
    
    run(args)
    

    
