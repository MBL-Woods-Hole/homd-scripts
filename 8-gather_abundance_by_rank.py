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
        
def get_longname(i, tax_string):
    tax_list = tax_string.split(';')
    return ';'.join(tax_list[0:i+1])
    
def run(args):
    
    taxlookup = {}
    
    with open(args.infile) as csv_file: 
        
        csv_reader = csv.DictReader(csv_file, delimiter='\t') # 
        for row in csv_reader:
            taxonomy = row['Taxonomy']
            row.pop('Taxonomy', None)
            taxlookup[taxonomy] = row        
    samplesite_order = list(row.keys())
            
    domain_lookup = {}
    phylum_lookup = {}
    class_lookup = {}
    order_lookup = {}
    family_lookup = {}
    genus_lookup = {}
    species_lookup = {}
    for tax in taxlookup:
        tax_list = tax.split(';')
        for i,name in enumerate(tax_list):
            if i == 0:  #domain
                longname = get_longname(i, tax)
                #print('longname',longname)
                if longname not in domain_lookup:
                    domain_lookup[longname] = {}
                for samplesite in taxlookup[tax]:
                    if samplesite not in domain_lookup[longname]:
                        domain_lookup[longname][samplesite] = float(taxlookup[tax][samplesite])
                    else:
                        domain_lookup[longname][samplesite] += float(taxlookup[tax][samplesite])
            if i == 1:  #phylum
                longname = get_longname(i, tax)
                
                if longname not in phylum_lookup:
                    phylum_lookup[longname] = {}
                for samplesite in taxlookup[tax]:
                    if samplesite not in phylum_lookup[longname]:
                        phylum_lookup[longname][samplesite] = float(taxlookup[tax][samplesite])
                    else:
                        phylum_lookup[longname][samplesite] += float(taxlookup[tax][samplesite])
            if i == 2:  #class
                longname = get_longname(i, tax)
                if longname not in class_lookup:
                    class_lookup[longname] = {}
                for samplesite in taxlookup[tax]:
                    if samplesite not in class_lookup[longname]:
                        class_lookup[longname][samplesite] = float(taxlookup[tax][samplesite])
                    else:
                        class_lookup[longname][samplesite] += float(taxlookup[tax][samplesite])
            if i == 3:  #order
                longname = get_longname(i, tax)
                if longname not in order_lookup:
                    order_lookup[longname] = {}
                for samplesite in taxlookup[tax]:
                    if samplesite not in order_lookup[longname]:
                        order_lookup[longname][samplesite] = float(taxlookup[tax][samplesite])
                    else:
                        order_lookup[longname][samplesite] += float(taxlookup[tax][samplesite])
            if i == 4:  #family
                longname = get_longname(i, tax)
                if longname not in family_lookup:
                    family_lookup[longname] = {}
                for samplesite in taxlookup[tax]:
                    if samplesite not in family_lookup[longname]:
                        family_lookup[longname][samplesite] = float(taxlookup[tax][samplesite])
                    else:
                        family_lookup[longname][samplesite] += float(taxlookup[tax][samplesite])
            if i == 5:  #genus
                longname = get_longname(i, tax)
                
                if longname not in genus_lookup:
                    genus_lookup[longname] = {}
                for samplesite in taxlookup[tax]:
                    if samplesite not in genus_lookup[longname]:
                        genus_lookup[longname][samplesite] = float(taxlookup[tax][samplesite])
                    else:
                        genus_lookup[longname][samplesite] += float(taxlookup[tax][samplesite])
#             if i == 6:  #species
#                 if longname not in species_lookup:
#                     species_lookup[longname] = {}
#                 for samplesite in taxlookup[tax]:
#                     if samplesite not in species_lookup[longname]:
#                         species_lookup[longname][samplesite] = float(taxlookup[tax][samplesite])
#                     else:
#                         species_lookup[longname][samplesite] += float(taxlookup[tax][samplesite])
    
           
    header = 'Taxonomy\tRank'
    for samplesite in samplesite_order:
        header += '\t'+samplesite
    header += '\n'
    fout = open(args.outfile,'w')
    fout.write(header)
    #for oligotype in file1_newlookup:
    
    for name in domain_lookup:
        txt =  name+'\tdomain'
        for samplesite in samplesite_order:
            txt += '\t'+str(round(domain_lookup[name][samplesite],3))
        txt += '\n'
        fout.write(txt)
    for name in phylum_lookup:
        txt =  name+'\tphylum'
        for samplesite in samplesite_order:
            txt += '\t'+str(round(phylum_lookup[name][samplesite],3))
        txt += '\n'
        fout.write(txt)
    for name in class_lookup:
        txt =  name+'\tclass'
        for samplesite in samplesite_order:
            txt += '\t'+str(round(class_lookup[name][samplesite],3))
        txt += '\n'
        fout.write(txt)
    for name in order_lookup:
        txt =  name+'\torder'
        for samplesite in samplesite_order:
            txt += '\t'+str(round(order_lookup[name][samplesite],3))
        txt += '\n'
        fout.write(txt)
    for name in family_lookup:
        txt =  name+'\tfamily'
        for samplesite in samplesite_order:
            txt += '\t'+str(round(family_lookup[name][samplesite],3))
        txt += '\n'
        fout.write(txt)
    for name in genus_lookup:
        txt =  name+'\tgenus'
        for samplesite in samplesite_order:
            txt += '\t'+str(round(genus_lookup[name][samplesite],3))
        txt += '\n'
        fout.write(txt)
#     for name in species_lookup:
#         txt =  name+'\tspecies'
#         for samplesite in samplesite_order:
#             txt += '\t'+str(round(species_lookup[name][samplesite],3))
#         txt += '\n'
#         fout.write(txt)
    fout.close()
    


if __name__ == "__main__":

    usage = """
    USAGE:
       
           
       ../8-gather_abundance_by_rank.py -i HOMD_NEW_taxonomyNcounts_2021-12-22.csv
       --source must be in ['eren2014_v1v3','eren2014_v3v5','dewhirst_35x9']
      
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=False,  action="store",   dest = "infile", default=False,
                                                    help="HOMD-endpoint1-wpcts.csv")
    
    parser.add_argument("-host", "--host", required = False, action = 'store', dest = "dbhost", default = 'localhost',
                                                   help="") 
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", default=False,
                                                    help="verbose print()") 
    parser.add_argument("-outfile", "--out_file", required = False, action = 'store', dest = "outfile", 
            default = 'rank_abundance_sums', help = "")
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
        
    
    run(args)
