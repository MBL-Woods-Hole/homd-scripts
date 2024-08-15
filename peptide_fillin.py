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
    
    seq_id_collector = {}
    for r in result1:
        accno = r['Protein_Accession']  # SEQF8115.1_00860
        #seq_id = accno.split('_')[0]
        #seq_id_collector[seq_id] = 1
        
        q2_base = "SELECT accession as molecule from PROKKA_meta.orf where protein_id ='%s'"
    #for gid in seq_id_collector:
        q_mol = q2_base % (accno)
        print(q_mol)
        result_mol = myconn.execute_fetch_select(q_mol)
        print(result_mol)
        if result_mol:
            mol=result_mol[0][0]
            
        else:
            mol=''
        print('accno',accno,'mol',mol)
        
        
        if mol:
           
           #q3 = "UPDATE protein_peptide set product = '%s' where Protein_Accession = '%s'" % (prod,accno)
           q3 = "UPDATE IGNORE protein_peptide set Molecule = '%s' where Protein_Accession = '%s'" % (mol,accno)
           print(q3)
           myconn.execute_no_fetch(q3)
def run_has_hsp(args):
    q1 = "SELECT distinct SUBSTRING_INDEX(Protein_Accession, '_', 1) as gid from protein_peptide"
    result1 = myconn.execute_fetch_select_dict(q1)
    for r in result1:
        gid = r['gid']  # SEQF8115.1_00860
        print(gid)
        
        q2 = "UPDATE genomes SET has_hsp_study='1' where seq_id='%s'" % (gid)
        print(q2)
        myconn.execute_no_fetch(q2)

def fillin_seq_id(args):
    #q1 = "SELECT distinct SUBSTRING_INDEX(Protein_Accession, '_', 1) as gid from protein_peptide"
    q1 = "SELECT distinct Protein_Accession as pa from protein_peptide"
    result1 = myconn.execute_fetch_select_dict(q1)
    for r in result1:
        pa = r['pa']
        gid = pa.split('_')[0] # SEQF8115.1_00860
        print(gid)
        
        q2 = "UPDATE protein_peptide SET seq_id='%s' where Protein_Accession='%s'" % (gid,pa)
        print(q2)
        myconn.execute_no_fetch(q2)
        
def fillin_counts(args):
    #q1 = "SELECT distinct SUBSTRING_INDEX(Protein_Accession, '_', 1) as gid from protein_peptide"
    q1 = "SELECT distinct seq_id from protein_peptide"
    result1 = myconn.execute_fetch_select_dict(q1)
    for r in result1:
       
        gid = r['seq_id']
        print(gid)
        q_otid = "select otid from genomes where seq_id='%s'" % (gid)
        r1 = myconn.execute_fetch_select_dict(q_otid)
        print(r1)
        otid = r1[0]['otid']
        q_protC = "select count(distinct protein_id) as cprot from protein_peptide where seq_id='%s'" % (gid)
        r2 = myconn.execute_fetch_select_dict(q_protC)
        cprot = r2[0]['cprot']
        q_pepC  = "select count(distinct peptide) as cpep from protein_peptide where seq_id='%s'" % (gid)
        r3 = myconn.execute_fetch_select_dict(q_pepC)
        cpep = r3[0]['cpep']
        
        q2 = "INSERT into protein_peptide_counts (seq_id,otid,protein_count,peptide_count)"
        q2 += " VALUES('%s','%s','%s','%s')" % (gid,otid,cprot,cpep)
        print(q2)
        myconn.execute_no_fetch(q2)
        
        
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
    
    
    #run(args)
    #run_has_hsp(args)
    #fillin_seq_id(args)
    fillin_counts(args)

    
