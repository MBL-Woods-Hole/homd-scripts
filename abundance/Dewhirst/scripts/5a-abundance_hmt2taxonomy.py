#!/usr/bin/env python

import os, sys, stat
import json
import argparse
import csv
sys.path.append('/home/ubuntu/homd-work/')
sys.path.append('/Users/avoorhis/programming/')
from connect import MyConnection
import datetime
ranks = ['domain','phylum','klass','order','family','genus','species']
today = str(datetime.date.today())
from statistics import mean,stdev
from collections import OrderedDict
"""

"""
directory_to_search = './'

#header = 'OLIGOTYPE\tPHYLUM\tNUM_BEST_HITS\tBEST_HIT_%ID\tBEST_HIT_%COV\tOVERALL_%IDENT\tHMTs\tHOMD_SPECIES\tSTRAIN_CLONE\tHOMD_REFSEQ_ID\tGB_NCBI_ID\tHOMD_STATUS\n'
#header = 'OLIGOTYPE\tPHYLUM\tNUM_BEST_HITS\tBEST_PCT_ID\tBEST_FULL_PCT_ID\tHMTs\tHOMD_SPECIES\tSTRAIN_CLONE\tHOMD_REFSEQ_ID\tGB_NCBI_ID\tHOMD_STATUS\n'
#site_order = ['BM','HP','KG','PT','ST','SUBP','SUPP','SV','TD','TH','NS']
HMTs = {}
hmt_notes = {}
sample_site_list = []
def writeFile(name, data):
    f = open(name, "w")
    f.write(data)
    f.close()
taxquery = """
    SELECT
   `domain`.`domain` AS `domain`,
   `phylum`.`phylum` AS `phylum`,
   `klass`.`klass` AS `klass`,
   `order`.`order` AS `order`,
   `family`.`family` AS `family`,
   `genus`.`genus` AS `genus`,
   `species`.`species` AS `species`,
   `subspecies`.`subspecies` AS `subspecies`
FROM (((((((((`otid_prime` join `taxonomy` on((`otid_prime`.`taxonomy_id` = `taxonomy`.`taxonomy_id`))) join `domain` on((`taxonomy`.`domain_id` = `domain`.`domain_id`))) join `phylum` on((`taxonomy`.`phylum_id` = `phylum`.`phylum_id`))) join `klass` on((`taxonomy`.`klass_id` = `klass`.`klass_id`))) join `order` on((`taxonomy`.`order_id` = `order`.`order_id`))) join `family` on((`taxonomy`.`family_id` = `family`.`family_id`))) join `genus` on((`taxonomy`.`genus_id` = `genus`.`genus_id`))) join `species` on((`taxonomy`.`species_id` = `species`.`species_id`))) join `subspecies` on((`taxonomy`.`subspecies_id` = `subspecies`.`subspecies_id`)))
where otid='%s'
"""
new_names_lookup = {}
new_names_lookup['ANA'] ='NS'
new_names_lookup['AKE']='KG'
new_names_lookup['BMU']='BM'
new_names_lookup['HPA']='HP'
new_names_lookup['LAF']=''
new_names_lookup['LRC']=''
new_names_lookup['MVA']=''
new_names_lookup['PTO']='PT'
new_names_lookup['PFO']=''
new_names_lookup['RAF']=''
new_names_lookup['RRC']=''
new_names_lookup['SAL']='SV'
new_names_lookup['STO']='ST'
new_names_lookup['SUBP']='SubP'
new_names_lookup['SUPP']='SupP'
new_names_lookup['THR']='TH'
new_names_lookup['TDO']='TD'
new_names_lookup['VIN']=''

old_names_lookup = {}
old_names_lookup['NS'] = 'ANA'
old_names_lookup['KG'] = 'AKE'
old_names_lookup['KG1'] = 'AKE1'
old_names_lookup['KG2'] = 'AKE2'
old_names_lookup['KG3'] = 'AKE3'
old_names_lookup['KG4'] = 'AKE4'
old_names_lookup['KG5'] = 'AKE5'
old_names_lookup['KG6'] = 'AKE6'
old_names_lookup['KG7'] = 'AKE7'
old_names_lookup['KG9'] = 'AKE9'
old_names_lookup['BM'] = 'BMU'
old_names_lookup['BM1'] = 'BMU1'
old_names_lookup['BM2'] = 'BMU2'
old_names_lookup['HP'] = 'HPA'
old_names_lookup['PT'] = 'PTO'
old_names_lookup['PT1'] = 'PTO1'
old_names_lookup['SV'] = 'SAL'
old_names_lookup['SV1'] = 'SAL1'
old_names_lookup['SV2'] = 'SAL2'
old_names_lookup['SV3'] = 'SAL3'
old_names_lookup['SV4'] = 'SAL4'
old_names_lookup['ST'] = 'STO'
old_names_lookup['SUBP'] = 'SUBP'
old_names_lookup['SUBP1'] = 'SUBP1'
old_names_lookup['SUBP2'] = 'SUBP2'
old_names_lookup['SUBP3'] = 'SUBP3'
old_names_lookup['SUPP'] = 'SUPP'
old_names_lookup['SUPP1'] = 'SUPP1'
old_names_lookup['TH'] = 'THR'
old_names_lookup['TD'] = 'TDO'
old_names_lookup['TD1'] = 'TDO1'
old_names_lookup['TD2'] = 'TDO2'
old_names_lookup['TD3'] = 'TDO3'
old_names_lookup['TD4'] = 'TDO4'
old_names_lookup['TD5'] = 'TDO5'
old_names_lookup['TD10'] = 'TDO10'
old_names_lookup['TD11'] = 'TDO11'
old_names_lookup['TD12'] = 'TDO12'

def update_site_abrv(row):
    new_sample_names = []
    #print('so',sample_order)
    
    for name,value in row.items():
        # ('UC28-BM', '0.0')
        #print('name',name,'val',value)
        pts = name.split('-')
        if len(pts) == 2 and pts[1] in old_names_lookup:
            new = pts[0] +'-'+old_names_lookup[pts[1]]
            new_sample_names.append([new,value])
        else:
            print('missing site',name,value)
            #sys.exit()
        
    return OrderedDict(new_sample_names) 
    
def get_taxonomy_from_db(hmt):
    print('hmt',hmt)
    if hmt:
        row = myconn.execute_fetch_one(taxquery % hmt)
        print('row',row)
        tmp = list(row)
        # combine sp and subsp
        if tmp[7]:
            tmp[6] = tmp[6]+' '+tmp[7]
        tmp = tmp[:7]
        
        return ';'.join(tmp)
    else:
        return 0
    
def get_otid_from_hmt(hmt):
    if hmt.startswith('HMT'):
        return str(int(hmt.split('-')[1]))  # strips zeros HMT-058 => 58
    else:
        return 0
               

def run(args):
    file1 = []
    lookup = {}
    notelookup = {}
    problem_list =[]
    subject_summer = {}
    site_subject_summer = {}
    hmts_w_data = {}
    with open(args.infile) as csv_file: 
        
        csv_reader = csv.DictReader(csv_file, delimiter='\t') # 
        #file1.append( {rows[0]:rows[1] for rows in reader} )
        rowcount = 0
        nomatch_count = 0
        fout = open(args.outfile,'w')
        
        for row in csv_reader:
            #taxonomy = row['Taxonomy']
            #hmt = row['HMT']
            
            
            hmt = row.pop('HMT', None)
            note = row.pop('Notes', None)
            #print('row',row)
            new_row = update_site_abrv(row)
            lookup[hmt] = new_row
            
            #print('new_row',new_row)
            notelookup[hmt] = note
    samplesite_order = [] #list(new_row.keys())
    for x in new_row:
        samplesite_order.append(x)
    header = 'Taxonomy\tHMT\tNotes'
    for samplesite in samplesite_order:
        header += '\t'+samplesite
    header += '\n'
    fout = open(args.outfile,'w')
    fout.write(header)
    for hmt in lookup:
        
        otid = get_otid_from_hmt(hmt)
        if otid == 0:
            continue
        taxonomy = get_taxonomy_from_db(otid)
        
        #print(hmt)
        data = []
        for key,val in lookup[hmt].items():
            #print(key,val)
            data.append(float(val))
        if mean(data) >0:
            strdata = [str(x) for x in data]
            fout.write(taxonomy+'\t'+hmt+'\t'+notelookup[hmt]+'\t'+'\t'.join(strdata))
            fout.write('\n')
        
        #print('data',hmt,taxonomy,data)
            # if rowcount == 0:
#                 header = 'Taxonomy\tHMT\tNotes'
#             
#                 
#                 print('row',row)
#             
#                 new_row = update_site_abrv(row[0][2:])
#                 for key in new_row:
#                     items = key.split('-')
#                     if len(items) == 2:   # and items[1] in site_order:
#                         print(key)
#                         header += '\t'+key
#                 header += '\n'
#                 fout.write(header)
#             rowcount += 1
            #print(hmt)
#             data = []
#             hmt = row['HMT']
#             note = row['Notes']
#             print('row',row)
#             for key in row.keys():
#                 items = key.split('-')
#                 print('items',items)
#                 if len(items) == 2:  # and items[1] in site_order:
#                     # just get the hmts with data
#                     data.append(float(row[key]))
#             if mean(data) > 0:
#                 hmt_parts = hmt.split('-')
#                 if len(hmt_parts) == 2 and hmt_parts[0] == 'HMT':
#                     #print(hmt_parts[1])
#                     txt = get_taxonomy_from_db(hmt_parts[1])
#                     txt += '\t'+str(int(hmt_parts[1]))
#                     txt += '\t'+note
#                     for key in row:
#                         items = key.split('-')
#                         if len(items) == 2:  # and items[1] in site_order:
#                             txt += '\t'+str(row[key])
#                     txt += '\n'
#                     fout.write(txt)
#                     
#               
#     for hmt in lookup:
#         print(lookup[hmt])
#     
    fout.close()
    


if __name__ == "__main__":

    usage = """
    USAGE:
       
           
       ./7a-DewhirstERENabundance_hmt2taxonomy.py -i {source}_coalesce_{date}_homd.csv
       
       Makes taxonomy from DB and HMT
       Also gives new site name from old
       
       --source must be in ['eren2014_v1v3','eren2014_v3v5','dewhirst'] 
      
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=False,  action="store",   dest = "infile", default=False,
                                                    help="HOMD-endpoint1-wpcts.csv")
    
    parser.add_argument("-host", "--host", required = False, action = 'store', dest = "dbhost", default = 'localhost',
                                                   help="") 
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", default=False,
                                                    help="verbose print()") 
    parser.add_argument("-outfile", "--out_file", required = False, action = 'store', dest = "outfile", 
            default = 'taxonomyNpcts', help = "")
    parser.add_argument("-s", "--source", required = True, action = 'store', dest = "source", 
                         help = "['eren2014_v1v3','eren2014_v3v5','dewhirst']")
    args = parser.parse_args()
    
    if args.source not in ['dewhirst']:
        print(usage)
        sys.exit()
                            
    if args.dbhost == 'homd_v4':
        args.DATABASE = 'homd'
        dbhost= '192.168.1.46'
        args.prettyprint = False
    
    elif args.dbhost == 'homd_dev':
        args.DATABASE = 'homd'
        dbhost= '192.168.1.58'
        args.prettyprint = False

    elif args.dbhost == 'localhost':
        #args.json_file_path = '/Users/avoorhis/programming/homd-data/json'
        #args.TAX_DATABASE  = 'HOMD_taxonomy'
        args.DATABASE = 'homd'
        dbhost = 'localhost'
        #dbhost_old = 'localhost'
        
    else:
        sys.exit('dbhost - error')
    print('Using',args.dbhost,dbhost)
    args.outfile = args.source+'_'+args.outfile +'_'+today+'_homd.csv'
    myconn = MyConnection(host=dbhost, db=args.DATABASE,  read_default_file = "~/.my.cnf_node")
    if args.verbose:
        print()
    if not args.infile:
        print(usage)
        sys.exit()
        
    
    run(args)
