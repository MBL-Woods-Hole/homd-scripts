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
def make_object(args):

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

def run(args):
    """ date not used"""
    #global master_lookup
    master_lookup = {}
    qinit = "SELECT distinct gid from annotation.genome"
    base_result = myconn.execute_fetch_select(qinit)
    for row in base_result:
        gid = row[0]
        if gid not in master_lookup:
            master_lookup[gid] = {}
        master_lookup[gid]['prokka'] = make_object(args)
        master_lookup[gid]['ncbi']   = make_object(args)
    
    
    #print(master_lookup)
    
    # PROKKA FIRST
    anno = 'prokka'    
    q = "SELECT * from annotation.prokka_info"
    result = myconn.execute_fetch_select_dict(q)
    for row in result:
        gid = row['gid']
        for n in row:
            if n in master_lookup[gid]['prokka']:
                master_lookup[gid]['prokka'][n] = row[n]
    
    ## NEXT NCBI
    anno = 'ncbi' 
    for row in base_result:
        gid = row[0]
        #print(gid)
        # organism
        q1 = "select organism from annotation.ncbi_info where gid ='"+gid+"'"
        resultq1 = myconn.execute_fetch_one(q1)
        organism = resultq1[0]
        master_lookup[gid]['ncbi']['organism'] = organism
        master_lookup[gid]['ncbi']['gid'] = gid
        where_clause = "WHERE gid='"+gid+"' AND annotation='ncbi'"
        # for CDS,rrna,trna,tmrna
        q2 = "SELECT `type`,count(*) AS count from annotation.gff "+where_clause+" group by `type`"
        #print(q2)
        result2 = myconn.execute_fetch_select_dict(q2)
        for row in result2:
            #print(row)
            if row['type'] == 'CDS':
               master_lookup[gid]['ncbi']['CDS'] = row['count']
            if row['type'] == 'rRNA':
               master_lookup[gid]['ncbi']['rRNA'] = row['count']
            if row['type'] == 'tmRNA':
               master_lookup[gid]['ncbi']['tmRNA'] = row['count']
            if row['type'] == 'tRNA':
               master_lookup[gid]['ncbi']['tRNA'] = row['count']  
         
        q3 = "SELECT sum(bps) AS bases, count(*) AS contigs FROM annotation.molecule "+where_clause
        result3 = myconn.execute_fetch_select_dict(q3)
        for row in result3:
            #print(row)
            master_lookup[gid]['ncbi']['bases']=int(row['bases'])
            master_lookup[gid]['ncbi']['contigs']=int(row['contigs'])
        
        print(master_lookup[gid]['ncbi'])
    
    
    
    file =  os.path.join(args.outdir,args.outfileprefix+'Lookup.json')  
    print_dict(file, master_lookup) 

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
    
    