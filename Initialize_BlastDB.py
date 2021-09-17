#!/usr/bin/env python

## SEE https://docs.dhtmlx.com/suite/tree__api__refs__tree.html // new version 7 must load from json file
# this script creates a list of json objects that allows the dhtmlx javascript library
# to parse and show a taxonomy tree (Written for HOMD)
##
import os, sys
import json
#from json import JSONEncoder
import argparse
#import ast

import datetime
ranks = ['domain','phylum','klass','order','family','genus','species']
today = str(datetime.date.today())

from connect import MyConnection



query_seq ="""
SELECT otid, refseqid, seqname, strain, genbank, seq_trim9
FROM taxon_refseqid
"""

def create_fasta(args):
    result = myconn.execute_fetch_select_dict(query_seq) 
    f = open(args.outfileprefix, "a")
    for n in result:
        txt =''
        defline= '>'+str(n['otid'])+'|'+n['refseqid']+'|'+n['seqname']+'|'+n['strain']+'|'+n['genbank']
        seq = n['seq_trim9']
        txt = defline+'\n'+seq+'\n'
        f.write(txt)
    f.close()
if __name__ == "__main__":

    usage = """
    USAGE:
        blast
        
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=False,  action="store",   dest = "infile", default='none',
                                                    help=" ")
    parser.add_argument("-o", "--outfileprefix",   required=False,  action="store",   dest = "outfileprefix", default='homdData-Refseq.fa',
                                                    help=" ")
    parser.add_argument("-outdir", "--out_directory", required = False, action = 'store', dest = "outdir", default = './',
                         help = "Not usually needed if -host is accurate")
    parser.add_argument("-host", "--host",
                        required = False, action = 'store', dest = "dbhost", default = 'localhost',
                        help = "choices=['homd',  'localhost']")
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", default=False,
                                                    help="verbose print()") 
    args = parser.parse_args()
    #parser.print_help(usage)
    if not os.path.exists(args.outdir):
        print("\nThe out put directory doesn't exist:: using the current dir instead\n")
        args.outdir = './'                         
    if args.dbhost == 'homd':
        #args.json_file_path = '/groups/vampsweb/vamps/nodejs/json'
        args.DATABASE  = 'homd'
        dbhost = '192.168.1.40'
        

    elif args.dbhost == 'localhost':
        #args.json_file_path = '/Users/avoorhis/programming/homd-data/json'
        args.DATABASE  = 'homd'
        dbhost='localhost'
        
    else:
        sys.exit('dbhost - error')
    
    
    myconn = MyConnection(host=dbhost, db=args.DATABASE,   read_default_file = "~/.my.cnf_node")
   

    print(args)
    print('running taxa (run defs in order)')
    create_fasta(args)
    


    
