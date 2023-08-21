#!/usr/bin/env python

## SEE https://docs.dhtmlx.com/suite/tree__api__refs__tree.html // new version 7 must load from json file
# this script creates a list of json objects that allows the dhtmlx javascript library
# to parse and show a taxonomy tree (Written for HOMD)
##
import os, sys
import gzip
import json
#from json import JSONEncoder
import argparse
import csv,re
from Bio import SeqIO
sys.path.append('../homd-data/')
sys.path.append('../../homd-data/')

from connect import MyConnection,mysql
import datetime
import requests
global mysql_errors
mysql_errors = []
"""

"""
today = str(datetime.date.today())

#spreadsheet file:  HOMD_NCBI_Taxonomy_Compairson_V2-fd-12.csv
#['_997', '995.2', '', '997', '1017', 'HOMD', 'HMT-997', 'Bacteria', 'Gracilibacteria_(GN02)', 'Gracilibacteria_(GN02)_[C-1]', 'Gracilibacteria_(GN02)_[O-1]', 'Gracilibacteria_(GN02)_[F-1]', 'Gracilibacteria_(GN02)_[G-4]', 'bacterium_HMT_997', 'NCBI', '363464', 'Bacteria', 'Candidatus Gracilibacteria', 'NA', 'NA', 'NA', 'NA', 'NA', '', '', 'NCBI', '363464', 'HMT-997', 'Bacteria', 'Candidatus Gracilibacteria (GN02)', 'Gracilibacteria_[C-1]', 'Gracilibacteria_[O-1]', 'Gracilibacteria_[F-1]', 'Gracilibacteria_[G-4]', 'bacterium_HMT_997', 'y']


def clean_hmt(s):
    
    return str(int(s.split('-')[1]))  # strips zeros HMT-058 => 58
    
def get_fixed_ids():
    collect = {}
    q = "SELECT tax_rank_id, tax_string from taxonomy_ranked_clean"
    result = myconn.execute_fetch_select(q)
    for row in result:
        
        collect[str(row[1])] = str(row[0])
    return collect



def run_segata():
    tax_obj = get_fixed_ids()
    
    
    q = "UPDATE IGNORE abundance_segata set tax_rank_id='%s' WHERE UPDATEDTaxonomy='%s'"
    for tax in tax_obj:
        q2 = q % (tax_obj[tax],tax)
        print(q2)
        myconn.execute_no_fetch(q2)
        
if __name__ == "__main__":

    usage = """
    USAGE:
        ./add_fixed_id_2segata.py 
         
        
        
        
        
        -host/--host [homd]  default:localhost
       
        

    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i1", "--infile1",   required=False,  action="store",   dest = "infile1", default='none',
                                                   help=" ")
    parser.add_argument("-i2", "--infile2",   required=False,  action="store",   dest = "infile2", default='none',
                                                   help=" ")
    
    parser.add_argument("-w", "--write",   required=False,  action="store_true",   dest = "write2db", default=False,
                                                help=" ")
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",   dest = "verbose", default=False,
                                                    help=" ")
    parser.add_argument("-host", "--host",
                        required = False, action = 'store', dest = "dbhost", default = 'localhost',
                        help = "choices=['homd',  'localhost']")
    # parser.add_argument("-t", "--taxonomy",   required=False,  action="store_true",   dest = "taxonomy", default=False,
#                                                     help=" ")
#     parser.add_argument("-s", "--synonyms",   required=False,  action="store_true",   dest = "synonyms", default=False,
#                                                     help=" ")
#     parser.add_argument("-tid", "--taxonid",   required=False,  action="store_true",   dest = "taxid", default=False,
#                                                     help=" ")
#     parser.add_argument("-ssp", "--subspecies",   required=False,  action="store_true",   dest = "sspecies", default=False,
#                                                     help=" ")
#     parser.add_argument("-a", "--abundance",   required=False,  action="store_true",   dest = "abundance", default=False,
#                                                     help=" ")
    # parser.add_argument("-s", "--start_digit",   required=False,  action="store",   dest = "start_digit", default='1',
#                                                     help=" ")
    parser.add_argument("-o", "--outfile",   required=False,  action="store",    dest = "outfile", default='segata_editUPDATED.tsv',
                                                    help="")
    args = parser.parse_args()
    
    #parser.print_help(usage)
                        
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

    args.indent = 4
    
    #run_segata()
    run_segata()
    
    

    
