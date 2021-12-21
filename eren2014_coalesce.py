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

#header = 'OLIGOTYPE\tPHYLUM\tNUM_BEST_HITS\tBEST_HIT_%ID\tBEST_HIT_%COV\tOVERALL_%IDENT\tHMTs\tHOMD_SPECIES\tSTRAIN_CLONE\tHOMD_REFSEQ_ID\tGB_NCBI_ID\tHOMD_STATUS\n'
#header = 'OLIGOTYPE\tPHYLUM\tNUM_BEST_HITS\tBEST_PCT_ID\tBEST_FULL_PCT_ID\tHMTs\tHOMD_SPECIES\tSTRAIN_CLONE\tHOMD_REFSEQ_ID\tGB_NCBI_ID\tHOMD_STATUS\n'
site_order = ['BM','HP','KG','PT','ST','SUBP','SUPP','SV','TD','TH']
HMTs = {}
sample_site_list = []
def writeFile(name, data):
    f = open(name, "w")
    f.write(data)
    f.close()
    
def get_hmts_from_db(args):
    q = 'SELECT otid FROM otid_prime ORDER BY otid'
    rows = myconn_new.execute_fetch_select(q)
    for row in rows:
        #print(f'{row[0]:03}')
        HMTs['HMT-'+f'{row[0]:03}'] = {'TaxonAbundanceNotes':''}  # pad left to 3 digits
    HMTs['gut_taxa'] = {'TaxonAbundanceNotes':''}
    HMTs['no_98.5pct_match_in_HOMD'] = {'TaxonAbundanceNotes':''} 
    with open(args.infile) as csv_file: 
        csv_reader = csv.DictReader(csv_file, delimiter='\t') # 
        for row in csv_reader:
            pass
    
    for key in row.keys():
        items = key.split('-')
        if len(items) == 2 and items[1] in site_order:
            sample_site_list.append(key)
            for hmt in HMTs:
                HMTs[hmt][key] = 0
    for hmt in HMTs:
        #print('len',hmt,len(HMTs[hmt]))
        pass       
def get_value(pct, multiplier_pct):
    #print('pct-from table',pct,'multiplier',multiplier_pct)
    return float(pct) * (float(multiplier_pct))/100
    
def run_coalesce(args):
    file1 = []
    file_lookup = {}
    problem_list =[]
    subject_summer = {}
    site_subject_summer = {}
    with open(args.infile) as csv_file: 
        
        csv_reader = csv.DictReader(csv_file, delimiter='\t') # 
        #file1.append( {rows[0]:rows[1] for rows in reader} )
        gut_count = 0
        nomatch_count = 0
        for row in csv_reader:
            #if "Assign_reads_to" says "gut", add those % abundances to "gut taxa",
            if row['Add_Note'].startswith('intent here is to assign'):
               row['Add_Note'] = ''
            oligo  = row['OLIGOTYPE']
            
            if row['Assign_reads_to'] == '50,50':
                hmt_list = row['HMTs'].split(',')
                tmp = {}
                tmp = list(set(hmt_list))
                
                if len(tmp) > 2:
                    problem_list.append(row['OLIGOTYPE']) 
                else:
                    hmt1 = tmp[0]
                    hmt2 = tmp[1]
                    if hmt1 in HMTs:  # if single HMT
                        #print(hmt1)
                        for sample in sample_site_list:
                            if hmt1=='HMT-667':
                                print('HMT-667',float(row[sample]))
                                
                            HMTs[hmt1][sample] += get_value(row[sample], '50')
                            #HMTs[hmt1][sample] += float(row[sample]) * 0.5
                        if row['Add_Note']:
                            HMTs[hmt1]['TaxonAbundanceNotes'] += row['Add_Note']
                    else:
                        problem_list.append(row['OLIGOTYPE']) # see oligo V1V3_004_Firmicutes
                    if hmt2 in HMTs:  # if single HMT
                        for sample in sample_site_list:
                            #HMTs[hmt2][sample] += float(row[sample]) * 0.5
                            HMTs[hmt2][sample] += get_value(row[sample], '50')
                        if row['Add_Note']:
                            HMTs[hmt2]['TaxonAbundanceNotes'] += row['Add_Note']
                    else:
                        problem_list.append(row['OLIGOTYPE'])
            elif row['Assign_reads_to'] == '100':
                
                hmt_list = row['HMTs'].split(',')
                tmp = {}
                for hmt in hmt_list:
                   tmp[hmt] = 1
                if len(tmp) > 1:
                    problem_list.append(row['OLIGOTYPE']) 
                else:
                    hmt = list(tmp.keys())[0]
                    if hmt in HMTs:  # if single HMT
                        for sample in sample_site_list:
                            #HMTs[hmt][sample] += float(row[sample])
                            HMTs[hmt][sample] += get_value(row[sample], '100')
                        if row['Add_Note']:
                            HMTs[hmt]['TaxonAbundanceNotes'] += row['Add_Note']
                    else:
                        problem_list.append(row['OLIGOTYPE']) # see oligo V1V3_004_Firmicutes
            
            elif row['Assign_reads_to'] == 'gut':
                gut_count += 1
                for sample in sample_site_list:
                    HMTs['gut_taxa'][sample] += get_value(row[sample], '100')
                    if row['Add_Note']:
                        HMTs['gut_taxa']['TaxonAbundanceNotes'] += row['Add_Note']
 
            
            elif row['Assign_reads_to'] == 'no_close_match_in_HOMD':
                nomatch_count += 1
                
                for sample in sample_site_list:
                    
                    # ie head === 123454321-BM add row[head] to HMTs['gut_taxa'][head
                    HMTs['no_98.5pct_match_in_HOMD'][sample] += get_value(row[sample], '100')
                    if row['Add_Note']:
                        HMTs['gut_taxa']['TaxonAbundanceNotes'] += row['Add_Note']+'; '
            
            elif len(row['Assign_reads_to'].split(',')) == len(row['HMTs'].split(',')):
                hmt_list = row['HMTs'].split(',')
                pct_list = row['Assign_reads_to'].split(',')
                for hmt in hmt_list:
                    for sample in sample_site_list:
                        #HMTs[hmt][sample] += ( float(row[sample]) * float(pct_list[hmt_list.index(hmt)])/100.0 )
                        multiplier = pct_list[hmt_list.index(hmt)]
                        HMTs[hmt][sample] += get_value(row[sample], multiplier)
                    if row['Add_Note']:
                        HMTs[hmt]['TaxonAbundanceNotes'] += row['Add_Note']+'; '
            
            else:
                #file_lookup[oligotype] = row
                # first unique the hmts
                
                hmt_list = row['HMTs'].split(',')
                pct_list = row['Assign_reads_to'].split(',')
                tmp = {}
                for pct in pct_list:
                   tmp[pct] = 1
                if len(tmp) == 1:
                    for hmt in set(hmt_list):
                        for sample in sample_site_list:
                            #HMTs[hmt][sample] += (float(row[sample]) * float(pct_list[0])/100.0)
                            HMTs[hmt][sample] += get_value(row[sample], pct_list[0])
                        if row['Add_Note']:
                            HMTs[hmt]['TaxonAbundanceNotes'] += row['Add_Note']+'; '
                elif row['Assign_reads_to'] == '0,100' or row['Assign_reads_to'] == '100,0':
                    hmt_list = row['HMTs'].split(',')
                    pct_list = row['Assign_reads_to'].split(',')
                    
                    for i,hmt in enumerate(list(set(hmt_list))):
                        for sample in sample_site_list:
                            #HMTs[hmt][sample] += (float(row[sample]) * float(pct_list[i])/100.0)
                            HMTs[hmt][sample] += get_value(row[sample], pct_list[i])
                        if row['Add_Note']:
                            HMTs[hmt]['TaxonAbundanceNotes'] += row['Add_Note']+'; '
                    
                   
                else:
                    # zero to S.pneumoniae HMT-734
                    pct = pct_list[0]  # there are only multiples w/ one zero
                    for hmt in set(hmt_list):
                        if hmt == 'HMT-734':  # S.pneumonieae
                            continue
                        for sample in sample_site_list:
                            #HMTs[hmt][sample] += (float(row[sample]) * float(pct_list[0])/100.0)
                            HMTs[hmt][sample] += get_value(row[sample], pct_list[0])
                        if row['Add_Note']:
                            HMTs[hmt]['TaxonAbundanceNotes'] += row['Add_Note']+'; '
                    
#                 tmp = {}
#                 for hmt in hmt_list:
#                    tmp[hmt] = 1
#                 if len(tmp) != len(row['Assign_reads_to'].split(',')):
#                     problem_list.append(row['OLIGOTYPE']) # 
                
                    
                pass

    print('\nGut Oligotypes:',gut_count)
    print('NoClose Match :',nomatch_count)
    print('problems',problem_list)
    #print(HMTs['no_98.5pct_match_in_HOMD'])
      
    #header = 'OLIGOTYPE\tBODY_SITE\tPHYLUM\tNUM_BEST_HITS\tBEST_PCT_ID\tBEST_FULL_PCT_ID\tAssign_reads_to\tAdd_Note\tHMTs\tHOMD_SPECIES\tSTRAIN_CLONE\tHOMD_REFSEQ_ID\tGB_NCBI_ID\tHOMD_STATUS'
    
    #header_list  =[] 
    # for key in row.keys():
#         header_list.append(key)
    header = 'HMT\tNotes\t'+'\t'.join(sample_site_list)+"\n"
  
    fout = open(args.outfile,'w')
    fout.write(header)
    #for oligotype in file1_newlookup:
    
    for hmt in HMTs:
        txt =  hmt+'\t'
        txt += HMTs[hmt]['TaxonAbundanceNotes']+'\t'
        for sample in sample_site_list:
            txt += str(round(HMTs[hmt][sample],3))+'\t'
            
        txt = txt.strip()+'\n'
   
        fout.write(txt)
    fout.close()
            
    
    


if __name__ == "__main__":

    usage = """
    USAGE:
       
           
       ./eren2014_coalesce.py -i HOMD-endpoint1-wpcts.csv
       
      
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=False,  action="store",   dest = "infile", default=False,
                                                    help="HOMD-endpoint1-wpcts.csv")
    
    parser.add_argument("-host", "--host", required = False, action = 'store', dest = "dbhost", default = 'localhost',
                                                   help="") 
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", default=False,
                                                    help="verbose print()") 
    parser.add_argument("-outfile", "--out_file", required = False, action = 'store', dest = "outfile", default = 'HOMD_NEWcoalesce01.csv',
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
        
    get_hmts_from_db(args)
    run_coalesce(args)
