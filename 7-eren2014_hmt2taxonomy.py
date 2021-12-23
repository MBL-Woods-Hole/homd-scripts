#!/usr/bin/env python

import os, sys, stat
import json
import argparse
import csv
from connect import MyConnection
import datetime
ranks = ['domain','phylum','klass','order','family','genus','species']
today = str(datetime.date.today())
from statistics import mean,stdev
"""

"""
directory_to_search = './'

#header = 'OLIGOTYPE\tPHYLUM\tNUM_BEST_HITS\tBEST_HIT_%ID\tBEST_HIT_%COV\tOVERALL_%IDENT\tHMTs\tHOMD_SPECIES\tSTRAIN_CLONE\tHOMD_REFSEQ_ID\tGB_NCBI_ID\tHOMD_STATUS\n'
#header = 'OLIGOTYPE\tPHYLUM\tNUM_BEST_HITS\tBEST_PCT_ID\tBEST_FULL_PCT_ID\tHMTs\tHOMD_SPECIES\tSTRAIN_CLONE\tHOMD_REFSEQ_ID\tGB_NCBI_ID\tHOMD_STATUS\n'
site_order = ['BM','HP','KG','PT','ST','SUBP','SUPP','SV','TD','TH']
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
    
def get_taxonomy_from_db(hmt):
    
    row = myconn_new.execute_fetch_one(taxquery % hmt)
    return ';'.join(row)
        

def run(args):
    file1 = []
    lookup = {}
    problem_list =[]
    subject_summer = {}
    site_subject_summer = {}
    hmts_w_data = {}
    with open(args.infile) as csv_file: 
        
        csv_reader = csv.DictReader(csv_file, delimiter='\t') # 
        #file1.append( {rows[0]:rows[1] for rows in reader} )
        count = 0
        nomatch_count = 0
        fout = open(args.outfile,'w')
        for row in csv_reader:
            if count == 0:
                header = 'Taxonomy'
                for key in row:
                    items = key.split('-')
                    if len(items) == 2 and items[1] in site_order:
                        header += '\t'+key
                header += '\n'
                fout.write(header)
            hmt = row['HMT']
            #print(hmt)
            data = []
            for key in row.keys():
                items = key.split('-')
                if len(items) == 2 and items[1] in site_order:
                    # just get the hmts with data
                    data.append(float(row[key]))
            if mean(data) > 0:
                hmt_parts = hmt.split('-')
                if len(hmt_parts) == 2 and hmt_parts[0] == 'HMT':
                    #print(hmt_parts[1])
                    txt = get_taxonomy_from_db(hmt_parts[1])
                    for key in row:
                        items = key.split('-')
                        if len(items) == 2 and items[1] in site_order:
                            txt += '\t'+str(row[key])
                    txt += '\n'
                    fout.write(txt)
                    
            count += 1    
    for hmt in lookup:
        print(lookup[hmt])
    
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
    parser.add_argument("-outfile", "--out_file", required = False, action = 'store', dest = "outfile", default = 'HOMD_NEW_taxonomyNcounts',
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
    
    args.outfile = args.outfile +'_'+today+'.csv'
    myconn_new = MyConnection(host=dbhost_new, db=args.NEW_DATABASE,  read_default_file = "~/.my.cnf_node")
    if args.verbose:
        print()
    if not args.infile:
        print(usage)
        sys.exit()
        
    
    run(args)
