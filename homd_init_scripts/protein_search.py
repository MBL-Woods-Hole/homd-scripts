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
sys.path.append('../../homd-data/')
from connect import MyConnection
usable_annotations = ['ncbi','prokka']
# obj = {seqid:[]}             
def make_anno_object():

    new_obj={}
    new_obj['gid'] = ''
    new_obj['organism'] = ''
    new_obj['contigs'] = ''
    new_obj['bases'] = ''
    new_obj['CDS'] = ''
    new_obj['rRNA'] = ''
    new_obj['tRNA'] = ''
    new_obj['tmRNA'] = ''
    ## ignore for now repeat_region, misc_RNA
    return new_obj

def find_databases(args):
    
    
    dbs = {}
    dbs['ncbi'] = []
    dbs['prokka'] = []
    for anno in dbs:
        q = "SHOW DATABASES LIKE '"+anno.upper()+"\_%'"
        print(q)
        result = myconn_old.execute_fetch_select(q)
        
        for row in result:
            db = row[0]
            print('found db ',db)
            if db[-8:] == 'template':
                continue
            dbs[anno].append(db)
    return dbs
    
# def fix_typo(dbs):
# 	""" RISKY Don't Change the db"""
# 	for db in dbs['ncbi']:
# 	    print(db)  
# 	    
# 	    q = "ALTER TABLE "+db+".`assembly_report' CHANGE `filed_value` `field_value` TEXT"  
	    
def run(args, dbs):
    #global master_lookup
    master_lookup = []
    q1 = "INSERT into `homd`.`protein_search` (gid,PID,anno,gene,product) VALUES"
    
    # prokka first
    for db in dbs['prokka']:
        print('Running1 prokka',db)
        gid = db.split('_')[1]
        anno = 'prokka'
        
        # pid = {anno,gid,gene,product}
        #if pid not in master_lookup:
        #    master_lookup[pid] = {}
            
        
        q = "SELECT gene,PID,product from "+db+".ORF_seq"
        #print(q)
        result = myconn_old.execute_fetch_select_dict(q)
        
        lines = []
        for row in result:
            #print(row)
            pid  = str(row['PID'])
            gene = str(row['gene']).replace("'","")
            prod = row['product'].replace("'","")
            lines.append("('"+gid+"','"+pid+"','"+anno+"','"+gene+"','"+prod+"')")
            
            
        q1 = q1 +  ','.join(lines)
        #q1 = q1 +  "('SEQF1003','SEQF1003_01531','prokka','None','hypothetical protein')"
        print(q1)
        myconn_new.execute_no_fetch(q1)
        #sys.exit()
#                         
    for db in dbs['ncbi']:
        print('Running1 prokka',db)
        gid = db.split('_')[1]
        anno = 'ncbi'
        
        # pid = {anno,gid,gene,product}
        #if pid not in master_lookup:
        #    master_lookup[pid] = {}
            
        
        q = "SELECT gene,PID,product from "+db+".ORF_seq"
        #print(q)
        result = myconn_old.execute_fetch_select_dict(q)
        
        lines = []
        for row in result:
            #print(row)
            pid  = str(row['PID'])
            gene = str(row['gene']).replace("'","")
            prod = row['product'].replace("'","")
            lines.append("('"+gid+"','"+pid+"','"+anno+"','"+gene+"','"+prod+"')")
            
        q2 = q1 +  ','.join(lines)  
        myconn_new.execute_no_fetch(q2)
    
    
    

# def print_dict(filename, dict):
#     print('writing',filename)
#     with open(filename, 'w') as outfile:
#         json.dump(dict, outfile, indent=args.indent)            
            
if __name__ == "__main__":

    usage = """
    USAGE:
        protein_search.py 
         --reads data from the ORIGINAL PROKKA and NCBI annotation DBs
         ie:  PROKKA_SEQF3654 and NCBI_SEQF3654
        
        puts data in homd.protein_search table for use with homd db search
        
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    #parser.add_argument("-i", "--infile",   required=False,  action="store",   dest = "infile", default='none',
    #                                                help=" ")
    
    
    #parser.add_argument("-anno", "--annotation", required = True, action = 'store', dest = "anno",
    #                     help = "PROKKA or NCBI")
    parser.add_argument("-host", "--host",
                        required = False, action = 'store', dest = "dbhost", default = 'localhost',
                        help = "choices=['homd',  'localhost']")
    
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", default=False,
                                                    help="verbose print()") 
    args = parser.parse_args()
    
                                
    if args.dbhost == 'homd':
        #args.DATABASE  = 'homd'
        dbhost_old = '192.168.1.51'
        dbhost_new = '192.168.1.40'
        
    elif args.dbhost == 'localhost':  #default
        #args.DATABASE = 'homd'
        dbhost_old = 'localhost'
        dbhost_new = 'localhost'
    else:
        sys.exit('dbhost - error')
    
    
    myconn_old = MyConnection(host=dbhost_old, read_default_file = "~/.my.cnf_node")
    myconn_new = MyConnection(host=dbhost_new, read_default_file = "~/.my.cnf_node")
    print(args)
    
    databases = find_databases(args)
    
    #print('dbs',databases)
    
    run(args,databases)
    
    
