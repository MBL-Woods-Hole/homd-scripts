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


       
def writeFile(name, data):
    f = open(name, "w")
    f.write(data)
    f.close()
    
def run_combine(args):
    file1 = []
    file1_newlookup = {}
    file2_oldlookup = {}
    with open(args.infile1) as csv_file:  #BLAST
        #csv_reader = csv.reader(csv_file, delimiter=',')  # AV comma
        delimiter = 'tab'
        #reader = csv.reader(csv_file1, delimiter='\t')
        csv_reader1 = csv.DictReader(csv_file, delimiter='\t') # KK tab
        #file1.append( {rows[0]:rows[1] for rows in reader} )
        for row in csv_reader1:
            if 'BEST_FULL_PCT_ID' not in row:
                sys.exit('no BEST_FULL_PCT_ID column found in infile1: BLAST PARSE RESULT')
            file1_newlookup[row['OLIGOTYPE']] = row
            
    with open(args.infile2) as csv_file:  #BLAST
        #csv_reader = csv.reader(csv_file, delimiter=',')  # AV comma
        delimiter = ','
        #reader = csv.reader(csv_file1, delimiter='\t')
        csv_reader = csv.DictReader(csv_file, delimiter=',') # KK tab
        #file1.append( {rows[0]:rows[1] for rows in reader} )
        for row in csv_reader:
            if row['OLIGOTYPE_NAME']:
                file2_oldlookup[row['OLIGOTYPE_NAME']] = {}
                file2_oldlookup[row['OLIGOTYPE_NAME']]['ABUNDANT_IN']   = row['ABUNDANT_IN']
            

   
    
    txt = ''
    
    header = 'OLIGOTYPE\tPHYLUM\tABUNDANT_IN\tNUM_BEST_HITS\tBEST_PCT_ID\tBEST_FULL_PCT_ID\tHMTs\tHOMD_SPECIES\tSTRAIN_CLONE\tHOMD_REFSEQ_ID\tGB_NCBI_ID\tHOMD_STATUS\n'
    
    #header += 'BM-MEAN\tBM-SD\tHP-MEAN\tHP-SD\tKG-MEAN\tKG-SD\tPT-MEAN\tPT-SD\tST-MEAN\tST-SD\t'
    #header += 'SUBP-MEAN\tSUBPSD\tSUPP-MEAN\tSUPP-SD\tSV-MEAN\tSV-SD\tTD-MEAN\tTD-SD\tTH-MEAN\tTH-SD\n'

    fout = open(args.outfile,'w')
    fout.write(header)
    for oligotype in file1_newlookup:
            txt = oligotype+'\t'
            txt += file1_newlookup[oligotype]['PHYLUM']+'\t'
            txt += file2_oldlookup[oligotype]['ABUNDANT_IN']+'\t'
            txt += file1_newlookup[oligotype]['NUM_BEST_HITS']+'\t'
            txt += file1_newlookup[oligotype]['BEST_PCT_ID']+'\t'
            txt += file1_newlookup[oligotype]['BEST_FULL_PCT_ID']+'\t'
            txt += file1_newlookup[oligotype]['HMTs']+'\t'
            txt += file1_newlookup[oligotype]['HOMD_SPECIES']+'\t'
            txt += file1_newlookup[oligotype]['STRAIN_CLONE']+'\t'
            txt += file1_newlookup[oligotype]['HOMD_REFSEQ_ID']+'\t'
            txt += file1_newlookup[oligotype]['GB_NCBI_ID']+'\t'
            txt += file1_newlookup[oligotype]['HOMD_STATUS']+'\n'
            
            fout.write(txt)
    fout.close()
            
    #print(file2_oldlookup[show])
    
    
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
           eren2014_combine_csv_files.py -i1 BLAST_PARSE_RESULT.csv -i2 V1-V3-BodySiteList-Curated-218-Firmicutes_fixed.csv
       
       -i1/--blastparse1  This is the BLAST-PARSE-OUTPUT from the eren2014_abundance_parser.py script
       -i2/--original2    This the original input file to eren2014_abundance_parser.py that has 
                          the oligotype names and counts/prev/sd for each oral site
       

    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i1", "--blastparse1",   required=False,  action="store",   dest = "infile1", default=False,
                                                    help="BLAST_PARSE_RESULT.csv")
    parser.add_argument("-i2", "--i2",   required=False,  action="store",   dest = "infile2", default=False,
                                                    help="V1-V3-BodySiteList-Curated-218-Firmicutes.csv")
    parser.add_argument("-host", "--host", required = False, action = 'store', dest = "dbhost", default = 'localhost',
                                                   help="") 
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", default=False,
                                                    help="verbose print()") 
    parser.add_argument("-outfile", "--out_file", required = False, action = 'store', dest = "outfile", default = 'NEW-Eren2014_BLAST_PARSE-1abundant_in.csv',
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
    
    run_combine(args)
