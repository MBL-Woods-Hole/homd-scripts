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



#header = 'OLIGOTYPE\tPHYLUM\tNUM_BEST_HITS\tBEST_HIT_%ID\tBEST_HIT_%COV\tOVERALL_%IDENT\tHMTs\tHOMD_SPECIES\tSTRAIN_CLONE\tHOMD_REFSEQ_ID\tGB_NCBI_ID\tHOMD_STATUS\n'
#header = 'OLIGOTYPE\tPHYLUM\tNUM_BEST_HITS\tBEST_PCT_ID\tBEST_FULL_PCT_ID\tHMTs\tHOMD_SPECIES\tSTRAIN_CLONE\tHOMD_REFSEQ_ID\tGB_NCBI_ID\tHOMD_STATUS\n'
site_order = ['BM','HP','KG','PT','ST','SUBP','SUPP','SV','TD','TH']
site_order_dewhirst = ['-BM','-HP','-KG','-PT','-SUBP','-SUPP','-SV','-TD','-TH']  # no STool
nasal = {}   # ucount, HMTs, Assign_reads_to, UCXX-NS

main_row_collector = {}
nasal_row_collector = {}   
site_subject_summer = {} 
site_subject_headers = {} 
def writeFile(name, data):
    f = open(name, "w")
    f.write(data)
    f.close()

def gather_nasal_counts(args):
    
    # ID type,FeatureID,HMT,Kingdom,Phylum,Class,Order,Family,Genus,Species,Assign_reads_to,
    with open(args.nasal) as csv_file: 
        csv_reader = csv.DictReader(csv_file, delimiter=',') # 
        #file1.append( {rows[0]:rows[1] for rows in reader} )
        row_count=1
        
        for row in csv_reader:
            #print(row)
            # ignoring rows without HTMs
            if row['HMT']:
                nasal_idx = 'nasal-'+str(row_count)
                nasal_row_collector[nasal_idx] = {'HMTs':row['HMT'],'Assign_reads_to':row['Assign_reads_to'],'Notes':''}
                for header_item in row:
                   
                   if header_item.startswith('UC'):
                        item = header_item+'-NS'
                        site_subject_headers[item] = 1
                        nasal_row_collector[nasal_idx][item] = row[header_item]
                        if row[header_item]:
                            if item in site_subject_summer:
                                site_subject_summer[item] += int(row[header_item])
                            else:
                                site_subject_summer[item] = int(row[header_item])
                    
                        else:
                            #print('before',item)
                            if item in site_subject_summer:
                                site_subject_summer[item] += 0
                            else:
                                site_subject_summer[item] = 0
                row_count += 1
            
    
    
def run_pct_dewhirst(args):
    # num_tax_classified,tax_id,HOT_ID,percentage to each,note,
    # nasal = {}   # ucount, HMTs, Assign_reads_to, UCXX-NS
    
    with open(args.infile) as csv_file: 
        csv_reader = csv.DictReader(csv_file, delimiter=',') # 
        #file1.append( {rows[0]:rows[1] for rows in reader} )
        row_count = 1
        for row in csv_reader:
            main_idx = 'main-'+str(row_count)
            
            if row['percentage to each']:
                main_row_collector[main_idx] = {'HMTs':row['HOT_ID'],'Assign_reads_to':row['percentage to each'],'Notes':row['note']}
            # if row_count==1:
#                 for key in row.keys():
#                     header_list.append(key)
#                 header = "\t".join(header_list)+"\n"
#                 fout = open(args.outfile,'w')
#                 fout.write(header)
                for item in row: 
                    # get data col headers
                    header_parts = item.split('-')
                
                    if len(header_parts) == 2 and ''.join([i for i in header_parts[1] if not i.isdigit()]) in site_order:  #header_parts[1] in site_order:
                        #print(item, row[item])
                        #subject_summer[header_parts[0]] = 1
                        main_row_collector[main_idx][item] = row[item]
                        site_subject_headers[item] = 1
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
                row_count += 1
            
    # NASAL
    # for idx in nasal_row_collector:
#         row = nasal_row_collector[idx]
#         for item in row:
#             if item in nasal_headers:
#         
#                 if item in site_subject_summer:
#                     site_subject_summer[item] += int(row[item])
#                 else:
#                     site_subject_summer[item] = int(row[item])
    print(site_subject_summer) 
    site_subject_order = list(site_subject_headers.keys())
    print('len site_subject_order',len(site_subject_order)) 
     
    # define header
    
    print('site_subject_order',site_subject_order)
    header = 'ROW_INDEX\tHMTs\tAssign_reads_to\tNOTES\t' + '\t'.join(site_subject_order) +'\n'# plus ssites                  
    # num_tax_classified,tax_id,HOT_ID,percentage to each,note,    
    print('header',header)
    
    fout = open(args.outfile,'w')
    fout.write(header)
    
    for idx in main_row_collector: 
        txt = ''
        row = main_row_collector[idx]
        #print(row)
        txt += idx +'\t'+row['HMTs']+'\t'+row['Assign_reads_to']+'\t'+row['Notes']
        for item in site_subject_order:
            if item in row:
                txt += '\t'+ str( round(100*(float(row[item]) / float(site_subject_summer[item])),4 ))
            else:
                txt += '\t0'
        txt += '\n'
        fout.write(txt) 
    
                       
    for idx in nasal_row_collector:
        #print(row) 
        txt = '' 
        row = nasal_row_collector[idx]
        #print(row)
        txt += idx +'\t'+row['HMTs']+'\t'+row['Assign_reads_to']+'\t'+row['Notes']
        for item in site_subject_order:
            if item in row:
                txt += '\t'+ str( round(100*(float(row[item]) / float(site_subject_summer[item])),4 ))
            else:
                txt += '\t0'
        txt += '\n'
        fout.write(txt) 
    fout.close()                      
    
    print('and ',len(site_subject_summer),' subject-sites\n')
    #for subjsite in site_subject_summer:
    #      print('Subject='+subjsite, 'SumOfCounts='+str(site_subject_summer[subjsite]))            
            
def run_pcts(args):  # NOT dewhirst new data
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
       
       -i2 Nasal counts (dewhirst only)
      
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=True,  action="store",   dest = "infile", default=False,
                                                    help="BLAST_PARSE_RESULT.csv")
    parser.add_argument("-i2", "--nasal2",   required=False,  action="store",   dest = "nasal", default=False,
                                                    help="")
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
    
    if args.nasal and args.source != 'dewhirst_35x9':
        sys.exit('nasal data - args.source mismatch')
    myconn_new = MyConnection(host=dbhost_new, db=args.NEW_DATABASE,  read_default_file = "~/.my.cnf_node")
    if args.verbose:
        print()
    if not args.infile:
        print(usage)
        sys.exit()
    if args.source == 'dewhirst_35x9':
        args.outfile = args.source+'_CountsMatrix_wpcts_'+today+'_homd.csv'
        if args.nasal:
            gather_nasal_counts(args)
        run_pct_dewhirst(args)
    else:
        args.outfile = args.source+'_'+args.outfile +'_'+today+'_homd.csv'
        run_pcts(args)
