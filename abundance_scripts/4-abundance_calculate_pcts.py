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
    
def run_pcts(args):
    file1 = []
    file_lookup = {}
    subject_summer = {}
    site_subject_summer = {}
    with open(args.infile) as csv_file:  #BLAST
        
        csv_reader = csv.DictReader(csv_file, delimiter='\t') # 
        #file1.append( {rows[0]:rows[1] for rows in reader} )
        for row in csv_reader:
            oligotype  = row['OLIGOTYPE']
            file_lookup[oligotype] = row
            
            for item in row:
                header_parts = item.split('-')
                if len(header_parts) == 2 and header_parts[1] in site_order:
                    
                    subject_summer[header_parts[0]] = 1
                    if item in site_subject_summer:
                        site_subject_summer[item] += int(row[item])
                        
                    else:
                        site_subject_summer[item] = int(row[item])
#     for site in site_order:
#         summer[site] = 0
    print('\nThere are ',len(subject_summer), ' subjects')
    print('and ',len(site_subject_summer),' subject-sites\n')
    for subjsite in site_subject_summer:
          print('Subject='+subjsite, 'SumOfCounts='+str(site_subject_summer[subjsite]))
    
      
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
        for head in header_list:
            items = head.split('-')
            if len(items) == 2 and items[1] in site_order:
                #subj = items[0]
                txt += str( round(100*(float(file_lookup[oligo][head]) / float(site_subject_summer[head])),4 ))+'\t'
            else:
                txt +=  file_lookup[oligo][head]+'\t'
            
        txt = txt.strip()+'\n'
   
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
       --source must be in ['eren2014_v1v3','eren2014_v3v5','dewhirst_35x9']
           
       ./4-abundance_calculate_pcts.py -i NEW-BLAST_PARSE_RESULT-JMWcuration_wcounts.csv
       
       use NEW-BLAST_PARSE_RESULT-JMWcuration_wcounts.csv as -i input
      
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=False,  action="store",   dest = "infile", default=False,
                                                    help="BLAST_PARSE_RESULT.csv")
    # parser.add_argument("-i2", "--original2",   required=False,  action="store",   dest = "infile2", default=False,
#                                                     help="pnas_counts_per_oligo.csv from pnas: https://www.pnas.org/content/111/28/E2875/tab-figures-data DS:S1")
    parser.add_argument("-host", "--host", required = False, action = 'store', dest = "dbhost", default = 'localhost',
                                                   help="") 
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", default=False,
                                                    help="verbose print()") 
    parser.add_argument("-outfile", "--out_file", required = False, action = 'store', dest = "outfile", default = 'BLAST_PARSE_RESULT_wpcts',
                         help = "")
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
    if not args.infile:
        print(usage)
        sys.exit()
    run_pcts(args)
