#!/usr/bin/env python

## SEE https://docs.dhtmlx.com/suite/tree__api__refs__tree.html // new version 7 must load from json file
# this script creates a list of json objects that allows the dhtmlx javascript library
# to parse and show a taxonomy tree (Written for HOMD)
##
import os, sys
import gzip
import json
#from json import JSONEncoder
from pprint import pprint
import argparse
import csv,re
from Bio import SeqIO
sys.path.append('/home/ubuntu/homd-work/')
sys.path.append('/Users/avoorhis/programming/')
from connect import MyConnection,mysql
import datetime
import requests
global mysql_errors
mysql_errors = []
"""

"""
today = str(datetime.date.today())
  

def run(args):
    q1 = "SELECT distinct Protein_Accession from protein_peptide"
    result1 = myconn.execute_fetch_select_dict(q1)
    
    #q2_base = "SELECT accession from PROKKA_meta.orf where protein_id ='%s'"
    q2_base = "SELECT accession from PROKKA_meta.orf where seq_id ='%s'"
    seq_id_collector = {}
    for r in result1:
        accno = r['Protein_Accession']  # SEQF8115.1_00860
        seq_id = accno.split('_')[0]
        seq_id_collector[seq_id] = 1
        
        
    for gid in seq_id_collector:
        q_mol = q2_base % (gid)
        print(q_mol)
        result_mol = myconn.execute_fetch_select(q_mol)
        #print(result_mol)
        if result_mol:
            mol=result_mol[0][1]
            sys.exit()
        else:
            mol=''
        #print('gid',gid,'mol',mol)
        
#         q2 = q2_base % (accno)
#         result2 = myconn.execute_fetch_select(q2)
#         if result2:
#            prod = result2[0][0]
#            #print(prod)
#            #q3 = "UPDATE protein_peptide set product = '%s' where Protein_Accession = '%s'" % (prod,accno)
#            q3 = "UPDATE IGNORE protein_peptide set product = '%s',organism='%s',otid='%s' where Protein_Accession = '%s'" % (prod,org,otid,accno)
#            #print(q3)
#            myconn.execute_no_fetch(q3)
     
if __name__ == "__main__":

    usage = """
    USAGE:
    


                 
        Break down a large file
        sed -n 8001,9000p assm_accs_full.txt > assm_accs_1000_9.txt
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    
    parser.add_argument("-i", "--infile",   required=False,  action="store",   dest = "infile", 
                                                   help=" ")
   
    
    parser.add_argument("-host", "--host",
                        required = False, action = 'store', dest = "dbhost", default = 'localhost',
                        help = "choices=['homd',  'localhost']")
    
    

    args = parser.parse_args()
    
    
    
                        
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
    
    
    myconn = MyConnection(host=dbhost, db=args.DATABASE,  read_default_file = "~/.my.cnf_node")
    
    
    run(args)
   
    

    
