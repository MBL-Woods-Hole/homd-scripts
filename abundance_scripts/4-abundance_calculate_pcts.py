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
# directory_to_search = './'
# blast_db_path = '../BLASTDB_ABUND'
# blast_db = 'HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta'
# full_blast_db = os.path.join(blast_db_path,blast_db)
# blast_script_path = "./blast.sh"


#header = 'OLIGOTYPE\tPHYLUM\tNUM_BEST_HITS\tBEST_HIT_%ID\tBEST_HIT_%COV\tOVERALL_%IDENT\tHMTs\tHOMD_SPECIES\tSTRAIN_CLONE\tHOMD_REFSEQ_ID\tGB_NCBI_ID\tHOMD_STATUS\n'
#header = 'OLIGOTYPE\tPHYLUM\tNUM_BEST_HITS\tBEST_PCT_ID\tBEST_FULL_PCT_ID\tHMTs\tHOMD_SPECIES\tSTRAIN_CLONE\tHOMD_REFSEQ_ID\tGB_NCBI_ID\tHOMD_STATUS\n'
site_order = ['BM','HP','KG','PT','ST','SUBP','SUPP','SV','TD','TH']
site_order_dewhirst = ['-BM','-HP','-KG','-PT','-SUBP','-SUPP','-SV','-TD','-TH']  # no STool
       
def writeFile(name, data):
    f = open(name, "w")
    f.write(data)
    f.close()
    
def run_pct_dewhirst(args):
    subject_summer = {}
    site_subject_summer = {}
    header_list  =[] 
    row_collector = []
    with open(args.infile) as csv_file: 
        csv_reader = csv.DictReader(csv_file, delimiter=',') # 
        #file1.append( {rows[0]:rows[1] for rows in reader} )
        row_count=0
        for row in csv_reader:
            row_count += 1
            row_collector.append(row)
            if row_count==1:
                for key in row.keys():
                    header_list.append(key)
                header = "\t".join(header_list)+"\n"
                fout = open(args.outfile,'w')
                fout.write(header)
            for item in row: 
                # get data col headers
                header_parts = item.split('-')
                
                if len(header_parts) == 2 and ''.join([i for i in header_parts[1] if not i.isdigit()]) in site_order:  #header_parts[1] in site_order:
                    #print(item, row[item])
                    subject_summer[header_parts[0]] = 1
                    if row[item]:
                        if item in site_subject_summer:
                            site_subject_summer[item] += int(row[item])
                        else:
                            site_subject_summer[item] = int(row[item])
                    
                    else:
                        #print('before',item)
                        if item in site_subject_summer:
                            site_subject_summer[item] += 0
                        else:
                            site_subject_summer[item] = 0
                            
    # num_tax_classified,tax_id,HOT_ID,percentage to each,note,    
                            
    for row in row_collector:
        #print(row) 
        txt = ''
        for head in header_list:
            items = head.split('-')
            #print(head,row[head])
            
            if len(items) == 2 and ''.join([i for i in items[1] if not i.isdigit()]) in site_order:
                #subj = items[0]
                #print('num_tax_classified',row['num_tax_classified'])
                #print(head, row[head])
                txt += str( round(100*(float(row[head]) / float(site_subject_summer[head])),4 ))+'\t'
                
            else:
                txt +=  row[head]+'\t'
            
        txt = txt.strip()+'\n'
   
        fout.write(txt) 
    fout.close()                      
    print('\nThere are ',len(subject_summer), ' subjects')
    print('and ',len(site_subject_summer),' subject-sites\n')
    #for subjsite in site_subject_summer:
    #      print('Subject='+subjsite, 'SumOfCounts='+str(site_subject_summer[subjsite]))            
            
def run_pcts(args):
    file1 = []
    file_lookup = {}
    subject_summer = {}
    site_subject_summer = {}
    with open(args.infile) as csv_file: 
        
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
    parser.add_argument("-outfile", "--out_file", required = False, action = 'store', dest = "outfile", 
                default = 'BLAST_PARSE_RESULT_wpcts', help = "")
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
    
    
    myconn_new = MyConnection(host=dbhost_new, db=args.NEW_DATABASE,  read_default_file = "~/.my.cnf_node")
    if args.verbose:
        print()
    if not args.infile:
        print(usage)
        sys.exit()
    if args.source == 'dewhirst_35x9':
        args.outfile = args.source+'_CountsMatrix_wpcts_'+today+'_homd.csv'
        run_pct_dewhirst(args)
    else:
        args.outfile = args.source+'_'+args.outfile +'_'+today+'_homd.csv'
        run_pcts(args)
