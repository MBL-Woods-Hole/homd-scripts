#!/usr/bin/env python

import os, sys, stat
import json
#from json import JSONEncoder
import argparse
import csv
#from connect import MyConnection

import datetime
ranks = ['domain','phylum','klass','order','family','genus','species']
today = str(datetime.date.today())

"""
input csv file:   Eren2014-FromDatasetS1-oligotypesV1V3.csv
from col D3 each sequence gets blasted (blastn) against
  blastdb_refseq_V15.22.p9/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta*

"""
# blast_db_path = '../blastdb_refseq_V15.22.p9'
# blast_db = 'HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta'
# full_blast_db = os.path.join(blast_db_path,blast_db)
# blast_script = "blast.sh"
directory_to_search = './'

def run_parse(args):

    for file in os.listdir(directory_to_search):
        if file.endswith(".out"):
            fileid = file.split('.')[0]
            print(fileid)
            with open(file) as f:
              
              line = f.readline()
              line_count = 1
              max_bitscore = 0
              while line:
                  line = f.readline().strip()
                  
                  line_items = line.split('\t')
                  #print(line_count,line_items)
                  if line_count == 1:
                      max_bitscore = line_items[0]
                      
                  
                  if max_bitscore == line_items[0]:
                      grab_data(line_items)
                         
                      
                      
                      
                  line_count += 1
                  
            
def grab_data(line_array):
    print(line_array)
    
    # line_array[0] == best bitscore
    # line_array[1] == BEST_HIT_ID
    # line_array[2] == BEST_HIT_COV
    # also want NUM_BEST_HITS
    data = line_array[len(line_array)-1].split('|')
    if len(data) == 8:
      id = data[0].strip()
      name = data[1].strip()
      hmt = data[2].strip()
      clone = data[3].strip()
      gb = data[4].strip()
      status = data[5].strip()
      habitat = data[6].strip()
      genome = data[7].strip()
    else:
      sys.exit('error in ID line from refseq db')
    
    
    
def writeFile(name, data):
    f = open(name, "w")
    f.write(data)
    f.close()
    

    
    
if __name__ == "__main__":

    usage = """
    USAGE:
       ./eren2014_blast_parser.py
       
       
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)
    
    parser.add_argument("-host", "--host",
                        required = False, action = 'store', dest = "dbhost", default = 'localhost',
                        help = "choices=['homd',  'localhost']")
    parser.add_argument("-pp", "--prettyprint",
                        required = False, action = 'store_true', dest = "prettyprint", default = False,
                        help = "output file is human friendly")
    parser.add_argument("-d", "--delimiter", required = False, action = 'store', dest = "delimiter", default = ',',
                         help = "Delimiter: commaAV[Default]: 'comma' or tabKK: 'tab'")
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", default=False,
                                                    help="verbose print()") 
    args = parser.parse_args()
    
    #parser.print_help(usage)
    
    args.outdir = './'                         
    if args.dbhost == 'homd':
        #args.json_file_path = '/groups/vampsweb/vamps/nodejs/json'
        #args.TAX_DATABASE = 'HOMD_taxonomy'
        args.NEW_DATABASE = 'homd'
        #dbhost_old = '192.168.1.51'
        dbhost_new= '192.168.1.40'
        args.outdir = '../homd-startup-data/'
        args.prettyprint = False

    elif args.dbhost == 'localhost':
        #args.json_file_path = '/Users/avoorhis/programming/homd-data/json'
        #args.TAX_DATABASE  = 'HOMD_taxonomy'
        args.NEW_DATABASE = 'homd'
        dbhost_new = 'localhost'
        #dbhost_old = 'localhost'
        
    else:
        sys.exit('dbhost - error')
    args.indent = None
    if args.prettyprint:
        args.indent = 4
    #myconn_tax = MyConnection(host=dbhost_old, db=args.TAX_DATABASE,   read_default_file = "~/.my.cnf_node")
    #myconn_new = MyConnection(host=dbhost_new, db=args.NEW_DATABASE,  read_default_file = "~/.my.cnf_node")
    
    
    run_parse(args)
   