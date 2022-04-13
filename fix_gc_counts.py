#!/usr/bin/env python

import os,sys
import argparse
import datetime
import requests
import json
import csv
sys.path.append('../homd-data/')
from connect import MyConnection




def run(args):
    print(args)
    q = 'SELECT seq_id,GC from annotated_org'
    result=myconn_tax.execute_fetch_select_dict(q)
    
    for row in result:
       #print(row)
       seqid = str(row['seq_id'])
       gc = str(row['GC'])
       q2 = "UPDATE genomes set gc='"+gc+"' where seq_id='"+seqid+"'"
       print(q2)
       myconn_new.execute_no_fetch(q2)
    
if __name__ == "__main__":

    usage = """
    USAGE:
        ./fix_gc_counts.py
        
        
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    #parser.add_argument("-i", "--infile",   required=True,  action="store",   dest = "infile", default='none',
    #                                                help=" ")
#    parser.add_argument("-s", "--source",   required=True,  action="store",   dest = "source", 
#                                                    help="ONLY segata dewhirst eren")
    
    parser.add_argument("-host", "--host",
                        required = False, action = 'store', dest = "dbhost", default = 'localhost',
                        help = "choices=['homd',  'localhost']")
    
     
    args = parser.parse_args()
    #parser.print_help(usage)
                       
    if args.dbhost == 'homd':
        #args.json_file_path = '/groups/vampsweb/vamps/nodejs/json'
        args.TAX_DATABASE = 'HOMD_genomes_new'
        args.NEW_DATABASE = 'homd'
        dbhost_old = '192.168.1.51'
        dbhost_new= '192.168.1.40'
        
        args.prettyprint = False

    elif args.dbhost == 'localhost':
        #args.json_file_path = '/Users/avoorhis/programming/homd-data/json'
        args.TAX_DATABASE  = 'HOMD_genomes_new'
        args.NEW_DATABASE = 'homd'
        dbhost_new = 'localhost'
        dbhost_old = 'localhost'
        
    else:
        sys.exit('dbhost - error')
    args.indent = None
    
    myconn_tax = MyConnection(host=dbhost_old, db=args.TAX_DATABASE,   read_default_file = "~/.my.cnf_node")
    #myconn = MyConnection(host=dbhost_old,   read_default_file = "~/.my.cnf_node")

    myconn_new = MyConnection(host=dbhost_new, db=args.NEW_DATABASE,  read_default_file = "~/.my.cnf_node")
    
    
    #parser.print_help(usage)
                        

    
    run(args)
   



