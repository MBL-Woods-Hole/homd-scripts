#!/usr/bin/env python

import os, sys, stat
import json
import argparse
import csv
from connect import MyConnection
import datetime
ranks = ['domain','phylum','klass','order','family','genus','species']
today = str(datetime.date.today())

"""

"""
directory_to_search = './'
blast_db_path = '../BLASTDB_ABUND'
blast_db = 'HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta'
full_blast_db = os.path.join(blast_db_path,blast_db)
blast_script_path = "./blast.sh"

# Fields: bit score, % identity, % query coverage per hsp, subject title
#blast_outfmt = "'7 bitscore pident qcovhsp stitle'"  #  qseqid sseqid
blast_outfmt = "'7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps'"
#blast_outfmt = "'7 qseqid bitscore nident pident qstart qend stitle'"
# Fields: identical, % identity, % query coverage per hsp, % query coverage per subject, subject title
#blast_outfmt = "'7 qseqid bitscore nident pident qcovs stitle'"
filename = 'queryfile.fa'
blast_cmd =  "blastn  -db %s -query %s"
blast_cmd += " -out %s.out"
blast_cmd += " -outfmt %s"
blast_cmd += " -max_target_seqs 30\n"
#header = 'OLIGOTYPE\tPHYLUM\tNUM_BEST_HITS\tBEST_HIT_%ID\tBEST_HIT_%COV\tOVERALL_%IDENT\tHMTs\tHOMD_SPECIES\tSTRAIN_CLONE\tHOMD_REFSEQ_ID\tGB_NCBI_ID\tHOMD_STATUS\n'
#header = 'OLIGOTYPE\tPHYLUM\tNUM_BEST_HITS\tBEST_PCT_ID\tBEST_FULL_PCT_ID\tHMTs\tHOMD_SPECIES\tSTRAIN_CLONE\tHOMD_REFSEQ_ID\tGB_NCBI_ID\tHOMD_STATUS\n'
site_order = ['BM','HP','KG','PT','ST','SUBP','SUPP','SV','TD','TH']

       
def writeFile(name, data):
    f = open(name, "w")
    f.write(data)
    f.close()
    
def run_coalesce(args):
    file1 = []
    file_lookup = {}
    subject_summer = {}
    site_subject_summer = {}
    with open(args.infile) as csv_file:  #BLAST
        
        csv_reader = csv.DictReader(csv_file, delimiter='\t') # 
        #file1.append( {rows[0]:rows[1] for rows in reader} )
        gut_count = 0
        nomatch_count = 0
        for row in csv_reader:
            oligotype  = row['OLIGOTYPE']

            
            if row['Assign_reads_to'] == 'gut':
                
                if 'gut_oligotypes99' in file_lookup:
                    file_lookup['gut_oligotypes99'] += row['HMTs'].split(',')
                else:
                    file_lookup['gut_oligotypes99'] = row['HMTs'].split(',')
                gut_count += 1
            
            
            elif row['Assign_reads_to'] == 'no_close_match_in_HOMD':
                if 'no_98.5pct_match_in_HOMD' in file_lookup:
                    file_lookup['no_98.5pct_match_in_HOMD'] += row['HMTs'].split(',')
                else:
                    file_lookup['no_98.5pct_match_in_HOMD'] = row['HMTs'].split(',')
                nomatch_count += 1
            
            
            else:
                file_lookup[oligotype] = row
#     for site in site_order:
#         summer[site] = 0
    
      
    #header = 'OLIGOTYPE\tBODY_SITE\tPHYLUM\tNUM_BEST_HITS\tBEST_PCT_ID\tBEST_FULL_PCT_ID\tAssign_reads_to\tAdd_Note\tHMTs\tHOMD_SPECIES\tSTRAIN_CLONE\tHOMD_REFSEQ_ID\tGB_NCBI_ID\tHOMD_STATUS'
    
    header_list  =[] 
    for key in row.keys():
        header_list.append(key)
    header = "\t".join(header_list)+"\n"
  
    fout = open(args.outfile,'w')
    fout.write(header)
    #for oligotype in file1_newlookup:
    oligo_keys = list(file_lookup.keys())
    #oligo_arry.sort()
    oligo_keys.sort()
    for oligo in oligo_keys:
        txt = ''
        if oligo in ['gut_oligotypes99', 'no_98.5pct_match_in_HOMD']:
            txt += oligo+'\t\t\t\t\t\t\t\t'+','.join(set(file_lookup[oligo]))+'\t'
        
        else:
            for head in header_list:
                txt +=  file_lookup[oligo][head]+'\t'
            
            
        txt = txt.strip()+'\n'
   
        fout.write(txt)
    fout.close()
            
    
    


if __name__ == "__main__":

    usage = """
    USAGE:
       
           
       ./eren2014_coalesce.py -i HOMD-endpoint1-wpcts.csv
       
       use NEW-BLAST_PARSE_RESULT-JMWcuration_wpcts.csv as -i input
      
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=False,  action="store",   dest = "infile", default=False,
                                                    help="HOMD-endpoint1-wpcts.csv")
    
    parser.add_argument("-host", "--host", required = False, action = 'store', dest = "dbhost", default = 'localhost',
                                                   help="") 
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", default=False,
                                                    help="verbose print()") 
    parser.add_argument("-outfile", "--out_file", required = False, action = 'store', dest = "outfile", default = 'HOMD_coalesce01.csv',
                         help = "")
    args = parser.parse_args()
    
    #parser.print_help(usage)
    
    args.outdir = './'                         
    if args.dbhost == 'homd':
        args.NEW_DATABASE = 'homd'
        dbhost_new= '192.168.1.40'

    elif args.dbhost == 'localhost':
        args.NEW_DATABASE = 'homd'
        dbhost_new = 'localhost'
        
    else:
        sys.exit('dbhost - error')
    args.indent = None
    
    myconn_new = MyConnection(host=dbhost_new, db=args.NEW_DATABASE,  read_default_file = "~/.my.cnf_node")
    if args.verbose:
        print()
    if not args.infile:
        print(usage)
        sys.exit()
    run_coalesce(args)
