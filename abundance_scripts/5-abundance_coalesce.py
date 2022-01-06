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
dropped = []
hmt_notes = {}
sample_site_list = []
def writeFile(name, data):
    f = open(name, "w")
    f.write(data)
    f.close()
delim = '\t'
#delim=','
def get_hmts_from_db(args):
    
    q = "SELECT otid,status FROM otid_prime ORDER BY otid"
    rows = myconn_new.execute_fetch_select(q)
    for row in rows:
        #print(f'{row[0]:03}')
        hmt = 'HMT-'+f'{row[0]:03}'
        #print(row)
        if row[1] == 'Dropped':
            dropped.append(hmt)
        else:
            HMTs[hmt] = {'TaxonAbundanceNotes':''}  # pad left to 3 digits
            hmt_notes[hmt] = {}
    HMTs['gut_taxa'] = {'TaxonAbundanceNotes':''}
    HMTs['no_98.5pct_match_in_HOMD'] = {'TaxonAbundanceNotes':''} 
    with open(args.infile) as csv_file: 
        csv_reader = csv.DictReader(csv_file, delimiter=delim) # 
        for row in csv_reader:
            pass
    
    for key in row.keys():
        items = key.split('-')
        #print('items',items)
        if len(items) == 2 and items[1] in site_order:
            #print('appending',key)
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
    
    note_field = 'Add_Note'
    
    file1 = []
    file_lookup = {}
    problem_list =[]
    subject_summer = {}
    site_subject_summer = {}
    with open(args.infile) as csv_file: 
        csv_reader = csv.DictReader(csv_file, delimiter=delim)
        #csv_reader = csv.DictReader(csv_file, delimiter='\t') # 
        #file1.append( {rows[0]:rows[1] for rows in reader} )
        gut_count = 0
        nomatch_count = 0
        for row in csv_reader:
            #if "Assign_reads_to" says "gut", add those % abundances to "gut taxa",
            # if row['Add_Note'].startswith('intent here is to assign'):
#                row['Add_Note'] = 'intent'
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
                                
                            HMTs[hmt1][sample] += get_value(row[sample], '50')
                            
                        if row[note_field]:
                            
                            hmt_notes[hmt1][row[note_field]]=1
                    else:
                        problem_list.append(row['OLIGOTYPE']) # see oligo V1V3_004_Firmicutes
                    if hmt2 in HMTs:  # if single HMT
                        for sample in sample_site_list:
                            
                            HMTs[hmt2][sample] += get_value(row[sample], '50')
                        if row[note_field]:
                           
                            hmt_notes[hmt2][row[note_field]]=1
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
                            HMTs[hmt][sample] += get_value(row[sample], '100')
                        if row[note_field]:
                            hmt_notes[hmt][row[note_field]]=1
                    else:
                        problem_list.append(row['OLIGOTYPE']) # see oligo V1V3_004_Firmicutes
            
            elif row['Assign_reads_to'] in ['121 gut oligotypes', 'gut']:
                gut_count += 1
                for sample in sample_site_list:
                    HMTs['gut_taxa'][sample] += get_value(row[sample], '100')
                    if row[note_field]:
                        hmt_notes['gut_taxa'][row[note_field]]=1
            
            elif row['Assign_reads_to'] in ['no close hit in HOMD','no_close_match_in_HOMD']:
                nomatch_count += 1
                for sample in sample_site_list:
                    # ie head === 123454321-BM add row[head] to HMTs['gut_taxa'][head
                    HMTs['no_98.5pct_match_in_HOMD'][sample] += get_value(row[sample], '100')
                    if row[note_field]:
                        hmt_notes['no_98.5pct_match_in_HOMD'][row[note_field]]=1
            
            elif len(row['Assign_reads_to'].split(',')) == len(row['HMTs'].split(',')):
                # 
                hmt_list = row['HMTs'].split(',')
                pct_list = row['Assign_reads_to'].split(',')
                for hmt in hmt_list:
                    if hmt not in dropped:
                        for sample in sample_site_list:
                            #HMTs[hmt][sample] += ( float(row[sample]) * float(pct_list[hmt_list.index(hmt)])/100.0 )
                            
                            multiplier = pct_list[hmt_list.index(hmt)]
                            HMTs[hmt][sample] += get_value(row[sample], multiplier)
                        if row[note_field]:
                            #HMTs[hmt]['TaxonAbundanceNotes'][row['Add_Note']]=1
                            hmt_notes[hmt][row[note_field]]=1
            
            else:
                #file_lookup[oligotype] = row
                # first unique the hmts
                
                
                hmt_list = row['HMTs'].split(',')
                pct_list = row['Assign_reads_to'].split(',')
                tmp = {}
                for pct in pct_list:
                   tmp[pct] = 1
                if len(tmp) == 1:  # catch if all the same
                    for hmt in set(hmt_list):
                        if hmt not in dropped:
                            for sample in sample_site_list:
                                HMTs[hmt][sample] += get_value(row[sample], pct_list[0])
                            if row[note_field]:
                                hmt_notes[hmt][row[note_field]]=1
                elif row['Assign_reads_to'] == '0,100' or row['Assign_reads_to'] == '100,0':
                    hmt_list = row['HMTs'].split(',')
                    pct_list = row['Assign_reads_to'].split(',')
                    
                    for i,hmt in enumerate(list(set(hmt_list))):
                        for sample in sample_site_list:
                            HMTs[hmt][sample] += get_value(row[sample], pct_list[i])
                        if row[note_field]:
                            hmt_notes[hmt][row[note_field]]=1
                    
                   
                else:
                    print('MUST Catch:',row['Assign_reads_to'])
                    
                    # zero to S.pneumoniae HMT-734
                    #pct = pct_list[0]  # there are only multiples w/ one zero
                    print('set(hmt_list)',set(hmt_list),'note:',row[note_field])
                    if args.source == 'eren2014_v1v3':
                        # CUSTOM
                        for hmt in set(hmt_list):
                            if hmt == 'HMT-734':  # HMT-734 == S.pneumonieae  NO Counts allotted
                                continue
                            for sample in sample_site_list:
                                HMTs[hmt][sample] += get_value(row[sample], pct_list[0])  # either 8.3333 or 9.0909
                            if row[note_field]:
                                if row[note_field].startswith('intent'):
                                    hmt_notes[hmt]['reads equally close to S. infantis, S. mitis, S. oralis, S. australis, S. cristatus, S. parasanguinis clade 721, S. pneumoniae, and S. sp. HMT 061, 064, 066, 074, 423 were divided equally among taxa except not assigned to S. pneumoniae']=1
                                else:
                                    
                                    hmt_notes[hmt][row[note_field]]=1

                    elif args.source == 'eren2014_v3v5':
                        #CUSTOM
                        if row['Assign_reads_to'] == '100,0,0':
                            # {'HMT-152', 'HMT-755', 'HMT-021'}
                            for hmt in set(hmt_list):
                                if hmt == 'HMT-152':   # S. salivarius
                                    for sample in sample_site_list:
                                        HMTs[hmt][sample] += get_value(row[sample], '100')
                                    if row[note_field]:
                                        hmt_notes[hmt][row[note_field]]=1
                                        
                        elif row['Assign_reads_to'] == '50,0,0,50':
                            #  {'HMT-543', 'HMT-152', 'HMT-755', 'HMT-021'}
                            for hmt in set(hmt_list):
                                if hmt == 'HMT-543':   # assigned half to S. salivarius and half to S. anginosus.
                                    for sample in sample_site_list:
                                        HMTs[hmt][sample] += get_value(row[sample], '50')
                                    if row[note_field]:
                                        hmt_notes[hmt][row[note_field]]=1
                                if hmt == 'HMT-021':   # assigned half to S. salivarius and half to S. anginosus.
                                    for sample in sample_site_list:
                                        HMTs[hmt][sample] += get_value(row[sample], '50')
                                    if row[note_field]:
                                        hmt_notes[hmt][row[note_field]]=1
                        else:
                            sys.exit('error in Assign Reads to')
                    else:
                        sys.exit('error in args.source')
              
    for hmt in hmt_notes:
        notes = '' 
        for note in hmt_notes[hmt]:
            notes += note +'; '
        HMTs[hmt]['TaxonAbundanceNotes'] = notes
            
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
       
       --source must be in ['eren2014_v1v3','eren2014_v3v5','dewhirst_35x9']    
       copy "wpcts" file to 'ENDPOINT1' file
       
       ./5-abundance_coalesce.py -i {source}_BLAST_PARSE_RESULT_wpcts_{date}.csv
       
      
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=False,  action="store",   dest = "infile", default=False,
                                                    help="HOMD-endpoint1-wpcts.csv")
    
    parser.add_argument("-host", "--host", required = False, action = 'store', dest = "dbhost", default = 'localhost',
                                                   help="") 
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", default=False,
                                                    help="verbose print()") 
    parser.add_argument("-outfile", "--out_file", required = False, action = 'store', dest = "outfile", 
                default = 'coalesce', help = "")
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
        
    get_hmts_from_db(args)
    run_coalesce(args)
