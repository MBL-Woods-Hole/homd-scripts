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
import glob
sys.path.append('/Users/avoorhis/programming/')
sys.path.append('/home/ubuntu/homd-work/')
from connect import MyConnection
import datetime
ranks = ['domain','phylum','klass','order','family','genus','species']
today = str(datetime.date.today())


all_genomes_list = []

def get_genomes(table):
    q = "SELECT genome_id from homd.`"+table+'`'
    print(q)
    
    rows = myconn.execute_fetch_select_dict(q)
    for row in rows:
        #print(row)
        all_genomes_list.append(  row['genome_id']  )
    
    
def run(table):
    
    exts = ['faa','ffn','fna']
    yes_no = {}
    outfile = 'GCA_NO_NCBI_DB.csv'
    fh = open(outfile, 'w')
    for genome_id in all_genomes_list:
        yes_no[genome_id] = 'no'
    
        faa_testpath = os.path.join(ncbi_blast_db_dir,'faa',genome_id+'*')
        
        #sys.exit()
        testpath = os.path.join(ncbi_blast_db_dir,'*',genome_id+'*')
        #print(testpath)
        tp = [n for n in glob.glob(testpath) if os.path.isfile(n)]
        if len(tp) > 0:
            #print('file_path',file_path)
            yes_no[genome_id] = 'yes'
            
    for gid in yes_no:
        if yes_no[gid] == 'yes':
            print(gid,'yes')
        else:
            fh.write(gid+'\tNo NCBI BLAST db\n')
        # continue
#         
#         fna_testpath = os.path.join(ncbi_blast_db_dir,'fna','genome_id*')
#         ffn_testpath = os.path.join(ncbi_blast_db_dir,'ffn','genome_id*')
#         faa = [n for n in glob.glob(faa_testpath) if os.path.isfile(n)]
#         
#         fna = [n for n in glob.glob(fna_testpath) if os.path.isfile(n)]
#         ffn = [n for n in glob.glob(ffn_testpath) if os.path.isfile(n)]
#         print('faa',faa)
        #if os.path.isfile(os.path.join(base, n))]
        
    #for ext in exts:
    #    path = ncbi_blast_db_dir+ext
        
    


if __name__ == "__main__":

    usage = """
    USAGE:
        ./Must be on 1.61 the SS server to access blast db directory
        Then move out put file to web:homd-data dir

    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=False,  action="store",   dest = "infile", default='none',
                                                    help=" ")
#    parser.add_argument("-s", "--source",   required=True,  action="store",   dest = "source", 
#                                                    help="ONLY segata dewhirst eren")
    parser.add_argument("-w", "--write",   required=False,  action="store_true",   dest = "write2db", default=False,
                                                    help=" ")
    parser.add_argument("-host", "--host",
                        required = False, action = 'store', dest = "dbhost", default = 'localhost',
                        help = "choices=['homd',  'localhost']")
    
    parser.add_argument("-d", "--delimiter", required = False, action = 'store', dest = "delimiter", default = 'tab',
                         help = "Delimiter: commaAV[Default]: 'comma' or tabKK: 'tab'")
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", default=False,
                                                    help="verbose print()") 
    args = parser.parse_args()
    
    #parser.print_help(usage)
    
    genomes_table = 'genomesV11.0'
    
    if args.dbhost == 'homd_dev':
        args.DATABASE = 'homd'
        dbhost = '192.168.1.46'
        ncbi_blast_db_dir = '/mnt/xvdb/blastdb/genomes_ncbi/V11.0/' # fna,ffn,faa
    elif args.dbhost == 'homd_prod':
        args.DATABASE = 'homd'
        dbhost = '192.168.1.42'
    elif args.dbhost == 'localhost':
        args.DATABASE = 'homd'
        dbhost = 'localhost'
        ncbi_blast_db_dir = '/Users/avoorhis/programming/blast_db/genomes_ncbi/' # fna,ffn,faa
        
    else:
        sys.exit('dbhost - error')
    
    #myconn = MyConnection(host=dbhost, db=args.DATABASE,   read_default_file = "~/.my.cnf_node")
    myconn = MyConnection(host=dbhost,   read_default_file = "~/.my.cnf_node")
    
    #myconn_new = MyConnection(host=dbhost_new, db=args.NEW_DATABASE,  read_default_file = "~/.my.cnf_node")
#     if args.source not in ['segata','dewhirst','eren']:
#         sys.exit('no valid source')
#     if args.source.lower() not in args.infile.lower():
#         sys.exit('file/source mismatch')
    genomes = get_genomes(genomes_table)
    run(genomes_table)
    
    
   
    