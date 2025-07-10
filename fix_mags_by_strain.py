#!/usr/bin/env python

## SEE https://docs.dhtmlx.com/suite/tree__api__refs__tree.html // new version 7 must load from json file
# this script creates a list of json objects that allows the dhtmlx javascript library
# to parse and show a taxonomy tree (Written for HOMD)
##
import os, sys
import json
#from json import JSONEncoder
import argparse
import csv
sys.path.append('/Users/avoorhis/programming/')
sys.path.append('/home/ubuntu/homd-work/')
from connect import MyConnection
import datetime
ranks = ['domain','phylum','klass','order','family','genus','species']
today = str(datetime.date.today())


genomes_collector = {}

def get_genomes(table):
    q = "SELECT genome_id, strain from `"+table+'`'
    print(q)
    
    rows = myconn.execute_fetch_select_dict(q)
    for row in rows:
        #print(row)
        genomes_collector[row['genome_id']] = row['strain']
    
    
def run(table):
    for gid in genomes_collector:
        if 'MAG' in genomes_collector[gid] or 'bin' in genomes_collector[gid]:
            #print(gid, genomes_collector[gid])
            q = "UPDATE `"+table+"` set MAG = 'yes' WHERE genome_id ='%s'" % (gid)
            if args.write2db:
               myconn.execute_no_fetch(q)
            else:
                print(q)


if __name__ == "__main__":

    usage = """
    USAGE:
        ./add_genomes_to_db.py -i infile
        
        infile tab delimited
          SEQID_info_V9.15-corrected.csv

    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=False,  action="store",   dest = "infile", default='none',
                                                    help=" ")
#    parser.add_argument("-s", "--source",   required=True,  action="store",   dest = "source", 
#                                                    help="ONLY segata dewhirst eren")
    parser.add_argument("-w", "--write",   required=False,  action="store_true",   dest = "write2db", default=False,
                                                    help=" ")
    parser.add_argument("-host", "--host",
                        required = False, action = 'store', dest = "dbhost", default = 'localhost',
                        help = "choices=['homd',  'localhost']")
    
    parser.add_argument("-d", "--delimiter", required = False, action = 'store', dest = "delimiter", default = 'tab',
                         help = "Delimiter: commaAV[Default]: 'comma' or tabKK: 'tab'")
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", default=False,
                                                    help="verbose print()") 
    args = parser.parse_args()
    
    #parser.print_help(usage)
    
    genomes_table = 'genomesV11.0'
    
    if args.dbhost == 'homd_dev':
        args.DATABASE = 'homd'
        dbhost = '192.168.1.46'
    elif args.dbhost == 'homd_prod':
        args.DATABASE = 'homd'
        dbhost = '192.168.1.42'
    elif args.dbhost == 'localhost':
        args.DATABASE = 'homd'
        dbhost = 'localhost'
        
    else:
        sys.exit('dbhost - error')
    
    myconn = MyConnection(host=dbhost, db=args.DATABASE,   read_default_file = "~/.my.cnf_node")
    #myconn_new = MyConnection(host=dbhost_new, db=args.NEW_DATABASE,  read_default_file = "~/.my.cnf_node")
#     if args.source not in ['segata','dewhirst','eren']:
#         sys.exit('no valid source')
#     if args.source.lower() not in args.infile.lower():
#         sys.exit('file/source mismatch')
    genomes = get_genomes(genomes_table)
    run(genomes_table)
    
    if args.write2db:
       print('Done writing')
    else:
       print('Add -w to command line to write to db')
   
    