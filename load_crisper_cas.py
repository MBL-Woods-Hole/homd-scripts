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

# should add these: 
# Missing: isolate origin, Sequencing status??, Combined length, GC percentage, ATCC stuff, num_contigs


    
def run(args):
    #for root, dirs, files in os.walk(args.indir):
    global genome_collector
    # George:I think if there is no CRISPR_Cas.tab file, then there is no good prediction
    genome_collector =[]
    for d in os.walk(args.ftp_base):
        print(d)
    
   #  r = requests.get(args.url_base) 
#     lines = r.text.split('\n')
#     for line in lines:
#         #dir_to_check = args.url_base
#         result =  re.findall('SEQF\d{4,5}\.\d',line) 
#         if len(result) >0:
#             #print('gid',result[0])
#             genome_collector.append(result[0])
#         else:
#             print('line',line)
#         # if 'SEQF' in line:
# #             print(line)
#                   
#     counter = 0
#     for gid in genome_collector:
#        #print(gid)
#        q = "update `"+args.DATABASE+"`.`genomes` set crisper_cas='1' where seq_id='"+gid+"'"
#        print(q)
#        res = myconn.execute_no_fetch(q)
#        counter += 1
#     print('count',counter)


        
if __name__ == "__main__":

    usage = """
    USAGE:
        ./add_genomes_to_NCBI_METAV10_1.py 
        
        host and annotation will determine directory to search
        
        -host/--host [homd]  default:localhost
       
        

    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    #parser.add_argument("-i", "--infile",   required=True,  action="store",   dest = "infile", default='none',
    #                                                help=" ")
    parser.add_argument("-a", "--anno",   required=False,  action="store",   dest = "anno",  default='ncbi',
                                                    help="")
    parser.add_argument("-w", "--write",   required=False,  action="store_true",   dest = "write2db", default=False,
                                                    help=" ")
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",   dest = "verbose", default=False,
                                                    help=" ")
    parser.add_argument("-host", "--host",
                        required = False, action = 'store', dest = "dbhost", default = 'localhost',
                        help = "choices=['homd',  'localhost']")
    
    parser.add_argument("-s", "--start_digit",   required=False,  action="store",   dest = "start_digit", default='1',
                                                    help=" ")
    parser.add_argument("-o", "--outfile",   required=False,  action="store",    dest = "out", default='ncbi_meta_info.tsv',
                                                    help="verbose print()")
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
    #myconn_new = MyConnection(host=dbhost_new, db=args.NEW_DATABASE,  read_default_file = "~/.my.cnf_node")
#     if args.source not in ['segata','dewhirst','eren']:
#         sys.exit('no valid source')
#     if args.source.lower() not in args.infile.lower():
#         sys.exit('file/source mismatch')
    args.url_base = 'https://www.homd.org/'
    args.ftp_base = '/mnt/efs/lv1_dev/homd_ftp/genomes/CRISPR_Cas/CCTyper/'
    
    run(args)
    

    
