#!/usr/bin/env python

import os, sys, stat
import json
import argparse
import csv

import datetime
ranks = ['domain','phylum','klass','order','family','genus','species']
today = str(datetime.date.today())
from statistics import mean,stdev
"""

"""
directory_to_search = './'

#header = 'OLIGOTYPE\tPHYLUM\tNUM_BEST_HITS\tBEST_HIT_%ID\tBEST_HIT_%COV\tOVERALL_%IDENT\tHMTs\tHOMD_SPECIES\tSTRAIN_CLONE\tHOMD_REFSEQ_ID\tGB_NCBI_ID\tHOMD_STATUS\n'
#header = 'OLIGOTYPE\tPHYLUM\tNUM_BEST_HITS\tBEST_PCT_ID\tBEST_FULL_PCT_ID\tHMTs\tHOMD_SPECIES\tSTRAIN_CLONE\tHOMD_REFSEQ_ID\tGB_NCBI_ID\tHOMD_STATUS\n'
#site_order = ['BM','HP','KG','PT','ST','SUBP','SUPP','SV','TD','TH']
HMTs = {}
hmt_notes = {}
sample_site_list = []
def writeFile(name, data):
    f = open(name, "w")
    f.write(data)
    f.close()
# taxquery = """
#     SELECT
#    
#    `domain`.`domain` AS `domain`,
#    `phylum`.`phylum` AS `phylum`,
#    `klass`.`klass` AS `klass`,
#    `order`.`order` AS `order`,
#    `family`.`family` AS `family`,
#    `genus`.`genus` AS `genus`,
#    `species`.`species` AS `species`,
#    `subspecies`.`subspecies` AS `subspecies`
# FROM (((((((((`otid_prime` join `taxonomy` on((`otid_prime`.`taxonomy_id` = `taxonomy`.`taxonomy_id`))) join `domain` on((`taxonomy`.`domain_id` = `domain`.`domain_id`))) join `phylum` on((`taxonomy`.`phylum_id` = `phylum`.`phylum_id`))) join `klass` on((`taxonomy`.`klass_id` = `klass`.`klass_id`))) join `order` on((`taxonomy`.`order_id` = `order`.`order_id`))) join `family` on((`taxonomy`.`family_id` = `family`.`family_id`))) join `genus` on((`taxonomy`.`genus_id` = `genus`.`genus_id`))) join `species` on((`taxonomy`.`species_id` = `species`.`species_id`))) join `subspecies` on((`taxonomy`.`subspecies_id` = `subspecies`.`subspecies_id`)))
# where otid='%s'
# """
    
# def get_taxonomy_from_db(hmt):
#     
#     row = myconn_new.execute_fetch_one(taxquery % hmt)
#     tmp = list(row)
#     # combine sp and subsp
#     if tmp[7]:
#         tmp[6] = tmp[6]+' '+tmp[7]
#     tmp = tmp[:7]
#     print(tmp)    
#     return ';'.join(tmp)
        
def get_longname(i, tax_string):
    tax_list = tax_string.split(';')
    return ';'.join(tax_list[0:i+1])
    
# def get_no_close_match(args):
#     lookup = {}
#     with open(args.coalesceFile) as csv_file: 
#         csv_reader = csv.DictReader(csv_file, delimiter='\t')
#         for row in csv_reader:
#             #print(row)
#             if row['HMT'] == 'no_98.5pct_match_in_HOMD':
#                 for key in row:
#                     items = key.split('-')
#                     if len(items) == 2 and items[1] in site_order:
#                         lookup[key] = row[key]
#     #print(lookup)
#     return lookup      
#def run(args, noclosematch):
def run(args):
    
    taxlookup = {}
    otidlookup = {}
    # INFILE: taxonomyNcounts
    with open(args.infile) as csv_file: 
        
        csv_reader = csv.DictReader(csv_file, delimiter='\t') # 
        for row in csv_reader:
            #taxonomy = row['Taxonomy']
            #hmt = row['HMT']
            taxonomy = row.pop('Taxonomy', None)
            hmt = row.pop('HMT', None)
            note = row.pop('Notes', None)
            taxlookup[taxonomy] = row
            otidlookup[taxonomy] = {'HMT':hmt,'Note':note}
    samplesite_order = list(row.keys())
            
    domain_lookup = {}
    phylum_lookup = {}
    class_lookup = {}
    order_lookup = {}
    family_lookup = {}
    genus_lookup = {}
    species_lookup = {}
    for fulltax in taxlookup:
        
        tax_list = fulltax.split(';')
        for i in range(0,7):
        #for i,name in enumerate(tax_list):
            longname = get_longname(i, fulltax)
            #print('fulltax',fulltax,'longname',longname)
            if i == 0:  #domain
                
                #print('longname',longname)
                if longname not in domain_lookup:
                    domain_lookup[longname] = {}
                for samplesite in taxlookup[fulltax]:
                    #if samplesite == '158013734-TD':
                    if samplesite not in domain_lookup[longname]:
                        domain_lookup[longname][samplesite] = float(taxlookup[fulltax][samplesite]) #+ float(noclosematch[samplesite])
                    else:
                        domain_lookup[longname][samplesite] += float(taxlookup[fulltax][samplesite])
            elif i == 1:  #phylum
                
                if longname not in phylum_lookup:
                    phylum_lookup[longname] = {}
                for samplesite in taxlookup[fulltax]:
                    if samplesite not in phylum_lookup[longname]:
                        phylum_lookup[longname][samplesite] = float(taxlookup[fulltax][samplesite]) #+ float(noclosematch[samplesite])
                    else:
                        phylum_lookup[longname][samplesite] += float(taxlookup[fulltax][samplesite])
            elif i == 2:  #class
                
                if longname not in class_lookup:
                    class_lookup[longname] = {}
                for samplesite in taxlookup[fulltax]:
                    if samplesite not in class_lookup[longname]:
                        class_lookup[longname][samplesite] = float(taxlookup[fulltax][samplesite]) #+ float(noclosematch[samplesite])
                    else:
                        class_lookup[longname][samplesite] += float(taxlookup[fulltax][samplesite])
            elif i == 3:  #order
                
                if longname not in order_lookup:
                    order_lookup[longname] = {}
                for samplesite in taxlookup[fulltax]:
                    if samplesite not in order_lookup[longname]:
                        order_lookup[longname][samplesite] = float(taxlookup[fulltax][samplesite]) #+ float(noclosematch[samplesite])
                    else:
                        order_lookup[longname][samplesite] += float(taxlookup[fulltax][samplesite])
            elif i == 4:  #family
                
                if longname not in family_lookup:
                    family_lookup[longname] = {}
                for samplesite in taxlookup[fulltax]:
                    if samplesite not in family_lookup[longname]:
                        family_lookup[longname][samplesite] = float(taxlookup[fulltax][samplesite]) #+ float(noclosematch[samplesite])
                    else:
                        family_lookup[longname][samplesite] += float(taxlookup[fulltax][samplesite])
            elif i == 5:  #genus
                
                if longname not in genus_lookup:
                    genus_lookup[longname] = {}
                for samplesite in taxlookup[fulltax]:
                    if samplesite not in genus_lookup[longname]:
                        genus_lookup[longname][samplesite] = float(taxlookup[fulltax][samplesite]) #+ float(noclosematch[samplesite])
                    else:
                        genus_lookup[longname][samplesite] += float(taxlookup[fulltax][samplesite])
            elif i == 6:  #species
                
                if longname not in species_lookup:
                    species_lookup[longname] = {}
                for samplesite in taxlookup[fulltax]:
                    if samplesite not in species_lookup[longname]:
                        species_lookup[longname][samplesite] = float(taxlookup[fulltax][samplesite])
                    else:
                        species_lookup[longname][samplesite] += float(taxlookup[fulltax][samplesite])
            else:
                sys.exit('i === 7?')
    
    
    #print('domain_lookup',domain_lookup)     
    header = 'Taxonomy\tRank\tHMT\tNotes'
    for samplesite in samplesite_order:
        header += '\t'+samplesite
    header += '\n'
    fout = open(args.outfile,'w')
    fout.write(header)
    #for oligotype in file1_newlookup:
    
    for name in domain_lookup:
        txt =  name+'\tdomain\t\t'  # no HMT
        for samplesite in samplesite_order:
            txt += '\t'+str(round(domain_lookup[name][samplesite],3))
        txt += '\n'
        fout.write(txt)
    for name in phylum_lookup:
        txt =  name+'\tphylum\t\t'  # no HMT
        for samplesite in samplesite_order:
            txt += '\t'+str(round(phylum_lookup[name][samplesite],3))
        txt += '\n'
        fout.write(txt)
    for name in class_lookup:
        txt =  name+'\tclass\t\t'  # no HMT
        for samplesite in samplesite_order:
            txt += '\t'+str(round(class_lookup[name][samplesite],3))
        txt += '\n'
        fout.write(txt)
    for name in order_lookup:
        txt =  name+'\torder\t\t'  # no HMT
        for samplesite in samplesite_order:
            txt += '\t'+str(round(order_lookup[name][samplesite],3))
        txt += '\n'
        fout.write(txt)
    for name in family_lookup:
        txt =  name+'\tfamily\t\t'  # no HMT
        for samplesite in samplesite_order:
            txt += '\t'+str(round(family_lookup[name][samplesite],3))
        txt += '\n'
        fout.write(txt)
    for name in genus_lookup:
        txt =  name+'\tgenus\t\t'  # no HMT
        for samplesite in samplesite_order:
            txt += '\t'+str(round(genus_lookup[name][samplesite],3))
        txt += '\n'
        fout.write(txt)
    for name in species_lookup:
        txt =  name+'\tspecies'
        if name not in otidlookup:
            sys.exit('MISSING tax',name)
        txt += '\t'+otidlookup[name]['HMT']
        txt += '\t'+otidlookup[name]['Note']
        for samplesite in samplesite_order:
            txt += '\t'+str(round(species_lookup[name][samplesite],3))
        txt += '\n'
        fout.write(txt)
    fout.close()
    


if __name__ == "__main__":

    usage = """
    USAGE:
       
           
       ../8-gather_abundance_by_rank.py -i {source}_taxonomyNpcts_{date}.csv
       --source must be in ['eren2014_v1v3','eren2014_v3v5','dewhirst_35x9']
      
       ** need to grab the "NoCloseMatch" numbers for each sample-site and add that to the
        sum (will make the results lower). But only for ranks domain...genus Not Species.
        "NoCloseMatch" counts are in the coalesce file
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=False,  action="store",   dest = "infile", default=False,
                                                    help="")
    

    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", default=False,
                                                    help="verbose print()") 
    parser.add_argument("-outfile", "--out_file", required = False, action = 'store', dest = "outfile", 
            default = 'rank_abundance_sums', help = "")
    parser.add_argument("-r", "--region", required = True, action = 'store', dest = "region", 
                         help = "['v1v3','eren2014_v3v5','dewhirst']")
    # parser.add_argument("-ic", "--icoalesce", required = True, action = 'store', dest = "coalesceFile", 
#                          help = "")
    args = parser.parse_args()
    
    if args.region not in ['v1v3','v3v5']:
        print(usage)
        sys.exit()
    
                            

    
    args.outfile = args.region+'_'+args.outfile +'_'+today+'_homd.csv'
    #myconn = MyConnection(host=dbhost, db=args.DATABASE,  read_default_file = "~/.my.cnf_node")
    if args.verbose:
        print()
    if not args.infile:
        print(usage)
        sys.exit()
        
    
    # noclosematch = get_no_close_match(args)    
#     run(args, noclosematch)
    run(args)
