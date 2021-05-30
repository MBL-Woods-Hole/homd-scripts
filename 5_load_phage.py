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
from connect import MyConnection
import datetime
ranks = ['domain','phylum','klass','order','family','genus','species']
today = str(datetime.date.today())
# these MUST match phage_data table fields
ncbi_headers=['Assembly','SRA_Accession','Submitters','Release_Date','Species','Genus','Family','Molecule_type',
'Sequence_Type','Genotype','Publications','Geo_Location','USA','Host','Isolation_Source','Collection_Date',
'BioSample','GenBank_Title']
            


 


def run_phage_csv(args): 
    
   
    with open(args.infile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        data_rows = []
        for row in csv_reader:
            if line_count == 0:
                next
            else:
                r = [n.replace("'",'') for n in row]
                data_rows.append(r)
                    
            line_count += 1
    
    #print(data_rows[0])
    
    q = "INSERT IGNORE INTO `phage_data` ("
    for h in ncbi_headers:
        q += h+"_NCBI,"  # add _NCBI to match fields
    q = q[:-1]+') VALUES'
    #print(q)
    for n in data_rows:
        q += (str(n)).replace('[','(').replace(']',')')+','
    q = q[:-1]
    #print(q)
    myconn_new.execute_no_fetch(q) 
        
if __name__ == "__main__":

    usage = """
    USAGE:
        takes the phage csv from the old homd to the new
        
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=True,  action="store",   dest = "infile", default='none',
                                                    help=" ")
    parser.add_argument("-o", "--outfileprefix",   required=False,  action="store",   dest = "outfileprefix", default='homd_data',
                                                    help=" ")
    parser.add_argument("-outdir", "--out_directory", required = False, action = 'store', dest = "outdir", default = './',
                         help = "Not usually needed if -host is accurate")
    parser.add_argument("-host", "--host",
                        required = False, action = 'store', dest = "dbhost", default = 'localhost',
                        help = "choices=['homd',  'localhost']")
    parser.add_argument("-pp", "--prettyprint",
                        required = False, action = 'store_true', dest = "prettyprint", default = False,
                        help = "output file is human friendly")
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", default=False,
                                                    help="verbose print()") 
    args = parser.parse_args()
    #parser.print_help(usage)
    if not os.path.exists(args.outdir):
        print("\nThe out put directory doesn't exist:: using the current dir instead\n")
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
    myconn_new = MyConnection(host=dbhost_new, db=args.NEW_DATABASE,  read_default_file = "~/.my.cnf_node")
    
    
    run_phage_csv(args)
   
    