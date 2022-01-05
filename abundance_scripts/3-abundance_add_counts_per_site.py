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
    
def run_combine(args):
    file1 = []
    file1_newlookup = {}
    file2_lookup = {}
    with open(args.infile1) as csv_file:  #BLAST
        
        csv_reader1 = csv.DictReader(csv_file, delimiter=',') # 
        #file1.append( {rows[0]:rows[1] for rows in reader} )
        for row in csv_reader1:
            oligotype  = row['OLIGOTYPE']
            file1_newlookup[oligotype] = row
    
#     for site in site_order:
#         summer[site] = 0
    
    with open(args.infile2) as csv_file:  #BLAST
        
        csv_reader = csv.DictReader(csv_file, delimiter='\t') # KK tab
        #file1.append( {rows[0]:rows[1] for rows in reader} )
        for row in csv_reader:
            oligotype  = row['OLIGOTYPE_NAME']
            file2_lookup[oligotype] = row
            
            
        
        subject_keys = row.keys()
          
   
    # same as input file1: BLAST_PARSE_RESULT-JMWcuration.csv 
    header = 'OLIGOTYPE\tBODY_SITE\tPHYLUM\tNUM_BEST_HITS\tBEST_PCT_ID\tBEST_FULL_PCT_ID\tAssign_reads_to\tAdd_Note\tHMTs\tHOMD_SPECIES\tSTRAIN_CLONE\tHOMD_REFSEQ_ID\tGB_NCBI_ID\tHOMD_STATUS'
    for key in subject_keys:
        if key != 'OLIGOTYPE_NAME':
            header += '\t'+key
    header += '\n'
    
    
    fout = open(args.outfile,'w')
    fout.write(header)
    oligo_keys = list(file1_newlookup.keys())
    #oligo_arry.sort()
    oligo_keys.sort()
    for oligo in oligo_keys:
        txt =   oligo+'\t'
        #txt =   file1_newlookup[oligo]['OLIGOTYPE']+'\t'
        txt +=  file1_newlookup[oligo]['BODY_SITE']+'\t'
        txt +=  file1_newlookup[oligo]['PHYLUM']+'\t'
        txt +=  file1_newlookup[oligo]['NUM_BEST_HITS']+'\t'
        txt +=  file1_newlookup[oligo]['BEST_PCT_ID']+'\t'
        txt +=  file1_newlookup[oligo]['BEST_FULL_PCT_ID']+'\t'
        txt +=  file1_newlookup[oligo]['Assign_reads_to']+'\t'
        txt +=  file1_newlookup[oligo]['Notes']+'\t'
        txt +=  file1_newlookup[oligo]['HMTs']+'\t'
        txt +=  file1_newlookup[oligo]['HOMD_SPECIES']+'\t'
        txt +=  file1_newlookup[oligo]['STRAIN_CLONE']+'\t'
        txt +=  file1_newlookup[oligo]['HOMD_REFSEQ_ID']+'\t'
        txt +=  file1_newlookup[oligo]['GB_NCBI_ID']+'\t'
        txt +=  file1_newlookup[oligo]['HOMD_STATUS']
        
        for key in subject_keys:
            if key != 'OLIGOTYPE_NAME':
                txt += '\t'+str(file2_lookup[oligo][key])
        txt += '\n'
        fout.write(txt)
    fout.close()
            
    
    
def get_qlength(seqfilename):
    with open(seqfilename) as f:
        seq = ''
        for line in f:
            if line.startswith('>'):
                continue
            seq += line.strip().replace('-','')
    return len(seq)
    
    


if __name__ == "__main__":

    usage = """
    USAGE:
       To create and run BLAST on seqs from file
           
       ../3-abundance_add_counts_per_site.py -i1 BLAST_PARSE_RESULT-JMWcuration.csv -i2 pnas_counts_per_oligo.csv
       
       use BLAST_PARSE_RESULT-JMWcuration.csv as -i1 input
       -i2 should be pnas_counts_per_oligo.csv
       step 1: add counts per site to csv
       step 2 calculate totals per subject
       step 3 calculate pct for each data point and add it to spredsheet
       
       ../3-abundance_add_counts_per_site.py -i1 BLAST_PARSE_RESULT-JMWcuration.csv -i2 pnas_counts_per_oligo.csv


--source must be in ['eren2014_v1v3','eren2014_v3v5','dewhirst_35x9']

    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i1", "--blastparse1",   required=False,  action="store",   dest = "infile1", default=False,
                                                    help="BLAST_PARSE_RESULT.csv")
    parser.add_argument("-i2", "--original2",   required=False,  action="store",   dest = "infile2", default=False,
                                                    help="pnas_counts_per_oligo.csv from pnas: https://www.pnas.org/content/111/28/E2875/tab-figures-data DS:S1")
    parser.add_argument("-host", "--host", required = False, action = 'store', dest = "dbhost", default = 'localhost',
                                                   help="") 
    parser.add_argument("-outfile", "--out_file", required = False, action = 'store', dest = "outfile", default = 'BLAST_PARSE_RESULT_wcounts',
                         help = "")
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", default=False,
                                                    help="verbose print()") 
    parser.add_argument("-s", "--source", required = True, action = 'store', dest = "source", 
                         help = "['eren2014_v1v3','eren2014_v3v5','dewhirst_35x9']")
    args = parser.parse_args()
    
    if args.source not in ['eren2014_v1v3','eren2014_v3v5','dewhirst_35x9']:
        print(usage)
        sys.exit()
                            
    if args.dbhost == 'homd':
        args.NEW_DATABASE = 'homd'
        dbhost_new= '192.168.1.40'

    elif args.dbhost == 'localhost':
        args.NEW_DATABASE = 'homd'
        dbhost_new = 'localhost'
        
    else:
        sys.exit('dbhost - error')
    
    args.outfile = args.source+'_'+args.outfile +'_'+today+'_homd.csv'
    myconn_new = MyConnection(host=dbhost_new, db=args.NEW_DATABASE,  read_default_file = "~/.my.cnf_node")
    if args.verbose:
        print()
    if not args.infile1 or not args.infile2:
        print(usage)
        sys.exit()
    run_combine(args)
