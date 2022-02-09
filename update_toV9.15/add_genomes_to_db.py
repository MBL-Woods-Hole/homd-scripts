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
sys.path.append('../../homd-data/')
from connect import MyConnection
import datetime
ranks = ['domain','phylum','klass','order','family','genus','species']
today = str(datetime.date.today())




def run_csv(): 
    collector = {}
    with open(args.infile) as csv_file: 
        csv_reader = csv.DictReader(csv_file, delimiter='\t') # KK tab
        
        for row in csv_reader:
            print()
            print(row)
            print(row['HMT_ID'],row['SEQ_ID'],row['Genus'],row['Species'])
            otid = row['HMT_ID']
            seqid = row['SEQ_ID']
            genus = row['Genus']  # dont need this we have otid
            species = row['Species']  # dont need this we have otid
            contigs = row['Contigs']
            strain = row['Strain']
            combined_size = row['Combined_Size']
            habitat = row['Habitat']
            seq_source = row['Sequence_Source']
            seq_source_parts = seq_source.split('/')[-1].split('_')
            print(seq_source_parts[-1])
            gca = seq_source_parts[0]+seq_source_parts[1]
            asm = seq_source_parts[2]
            print('asm',asm,'gca',gca)
            seq_center = 'The Forsyth Center'
            ncbi_taxon_id ='' # from extra table
            status = '' #from exta table: Complete or
            
            q1 = "INSERT into genomes (seq_id,otid,sequence_center,culture_collection,number_contigs,combined_length)"
            q2 = "INSERT into genomes_homd_extra (seq_id, gc_comment)"
        
    

        
if __name__ == "__main__":

    usage = """
    USAGE:
        ./add_genomes_to_db.py -i infile
        
        infile tab delimited
          SEQID_info_V9.15-corrected.csv

    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=True,  action="store",   dest = "infile", default='none',
                                                    help=" ")
#    parser.add_argument("-s", "--source",   required=True,  action="store",   dest = "source", 
#                                                    help="ONLY segata dewhirst eren")
    
    parser.add_argument("-host", "--host",
                        required = False, action = 'store', dest = "dbhost", default = 'localhost',
                        help = "choices=['homd',  'localhost']")
    
    parser.add_argument("-d", "--delimiter", required = False, action = 'store', dest = "delimiter", default = 'tab',
                         help = "Delimiter: commaAV[Default]: 'comma' or tabKK: 'tab'")
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", default=False,
                                                    help="verbose print()") 
    args = parser.parse_args()
    
    #parser.print_help(usage)
                        
    if args.dbhost == 'homd':
        #args.json_file_path = '/groups/vampsweb/vamps/nodejs/json'
        #args.TAX_DATABASE = 'HOMD_taxonomy'
        args.DATABASE = 'homd'
        #dbhost_old = '192.168.1.51'
        dbhost= '192.168.1.40'
        args.prettyprint = False

    elif args.dbhost == 'localhost':
        #args.json_file_path = '/Users/avoorhis/programming/homd-data/json'
        #args.TAX_DATABASE  = 'HOMD_taxonomy'
        args.DATABASE = 'homd'
        dbhost = 'localhost'
        #dbhost_old = 'localhost'
        
    else:
        sys.exit('dbhost - error')
    
    myconn = MyConnection(host=dbhost, db=args.DATABASE,   read_default_file = "~/.my.cnf_node")
    #myconn_new = MyConnection(host=dbhost_new, db=args.NEW_DATABASE,  read_default_file = "~/.my.cnf_node")
#     if args.source not in ['segata','dewhirst','eren']:
#         sys.exit('no valid source')
#     if args.source.lower() not in args.infile.lower():
#         sys.exit('file/source mismatch')
    
    run_csv()
   
    