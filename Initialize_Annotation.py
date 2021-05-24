#!/usr/bin/env python

## SEE https://docs.dhtmlx.com/suite/tree__api__refs__tree.html // new version 7 must load from json file
# this script creates a list of json objects that allows the dhtmlx javascript library
# to parse and show a taxonomy tree (Written for HOMD)

import os, sys
import json
import argparse

import datetime
from datetime import datetime,date
ranks = ['domain','phylum','klass','order','family','genus','species']
today = str(date.today())
from connect import MyConnection
usable_annotations = ['ncbi','prokka']
# obj = {seqid:[]}             
def run(args):
    """ date not used"""
    #global master_lookup
    master_lookup = {}
    
    #for anno in usable_annotations:
        # ncbi is way different
    # PROKKA FIRST
    anno = 'prokka'    
    q = "SELECT * from annotation.prokka_info"

    #print(first_genomes_query)
    result = myconn.execute_fetch_select_dict(q)

    #print(result)
    for row in result:
        seq_id = row['gid']
        if seq_id not in master_lookup:
            master_lookup[seq_id] = {}
            master_lookup[seq_id][anno] ={}
        obj = {}
        for n in row:
            #print(n,row[n])
            obj[n] = row[n]
        master_lookup[seq_id][anno] = row
     
     
    anno = 'ncbi' 
    q = "SELECT distinct gid from annotation.genome where annotation = 'ncbi'"
    
    result = myconn.execute_fetch_select(q)
    for row in result:
        gid = row[0]
        print(gid)
        # organism
        where_clause = "WHERE gid='"+gid+"' AND annotation='ncbi'"
     # for CDS,rrna,trna,tmrna
        q2 = "SELECT `type`,count(*) AS count from annotation.gff "+where_clause+" group by `type`"
        print(q2)
        result2 = myconn.execute_fetch_select_dict(q2)
        for item in result2:
            print(item)
            
#      "organism": "Acinetobacter baumannii SDF",
#             "contigs": 4,
#             "bases": 3477996,
#             "CDS": 3542,
#             "rRNA": 15,
#             "tmRNA": 1,
#             "tRNA": 64,
    # bases:
    #q = "select sum(bps) from molecule where gid='SEQF1595' and annotation='ncbi' "
    # contigs:
    #q = "SELECT count(*) from `molecule` where gid='SEQF1595' and annotation='ncbi'
    q = "SELECT sum(bps) AS bases, count(*) AS contigs FROM molecule "+where_clause
    #print(master_lookup)
    
    
    
    file =  os.path.join(args.outdir,args.outfileprefix+'Lookup.json')  
    #print_dict(file, master_lookup) 

def print_dict(filename, dict):
    print('writing',filename)
    with open(filename, 'w') as outfile:
        json.dump(dict, outfile, indent=args.indent)            
            
if __name__ == "__main__":

    usage = """
    USAGE:
        homd_init_genome_data.py
        
        will print out the need initialization files for homd
        Needs MySQL: tries to read your ~/.my.cnf_node
        
           -outdir Output directory [default]
        for homd site
           -host homd
           
        for debugging
          -pp  pretty print
          -o <outfile>  Change outfile name from 'taxonomy'*
        
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=False,  action="store",   dest = "infile", default='none',
                                                    help=" ")
    parser.add_argument("-o", "--outfileprefix",   required=False,  action="store",   dest = "outfileprefix", default='homdData-Annotation',
                                                    help=" ")
    parser.add_argument("-outdir", "--out_directory", required = False, action = 'store', dest = "outdir", default = './',
                         help = "Not usually needed if -host is accurate")
    #parser.add_argument("-anno", "--annotation", required = True, action = 'store', dest = "anno",
    #                     help = "PROKKA or NCBI")
    parser.add_argument("-host", "--host",
                        required = False, action = 'store', dest = "dbhost", default = 'localhost',
                        help = "choices=['homd',  'localhost']")
    parser.add_argument("-pp", "--prettyprint",
                        required = False, action = 'store_true', dest = "prettyprint", default = False,
                        help = "output file is human friendly")
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", default=False,
                                                    help="verbose print()") 
    args = parser.parse_args()
    
    if not os.path.exists(args.outdir):
        print("\nThe out put directory doesn't exist:: using the current dir instead\n")
        args.outdir = './'                         
    if args.dbhost == 'homd':
        args.DATABASE  = 'homd'
        dbhost = '192.168.1.40'
        args.outdir = '../homd-startup-data/'
        args.prettyprint = False
        
    elif args.dbhost == 'localhost':  #default
        args.DATABASE = 'homd'
        dbhost = 'localhost'
    else:
        sys.exit('dbhost - error')
    args.indent = None
    if args.prettyprint:
        args.indent = 4
    print()
    myconn = MyConnection(host=dbhost,   read_default_file = "~/.my.cnf_node")

    print(args)
    
    run(args)
    
    