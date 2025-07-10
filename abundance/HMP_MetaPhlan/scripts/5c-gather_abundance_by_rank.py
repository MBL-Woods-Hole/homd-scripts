#!/usr/bin/env python

import os, sys, stat
import json
import argparse
import csv
sys.path.append('/home/ubuntu/homd-work')
sys.path.append('/Users/avoorhis/programming/')
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
#     row = myconn.execute_fetch_one(taxquery % hmt)
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
    
def get_otid_from_hmt(hmt):
    if hmt.startswith('HMT'):
        return str(int(hmt.split('-')[1]))  # strips zeros HMT-058 => 58
    else:
        return 0
        
def get_taxonomy_from_db(otid):
    sql = "select domain,phylum,klass,`order`,family,genus,species,subspecies from otid_prime"
    #sql = "select domain,phylum,klass,`order`,family,genus,species from otid_prime"
    sql += " join taxonomy using(taxonomy_id)"
    sql += " join domain using(domain_id)"
    sql += " join phylum using(phylum_id)"
    sql += " join klass using(klass_id)"
    sql += " join `order` using(order_id)"
    sql += " join family using(family_id)"
    sql += " join genus using(genus_id)"
    sql += " join species using(species_id)"
    sql += " join subspecies using(subspecies_id)"
    sql += " WHERE"
    sql += " otid='%s'"
    q1 = sql % (otid)
    #print(q1)
    result = myconn.execute_fetch_select(q1)
    #print('result',result[0])
    lst = list(result[0])
    if lst[-1] != '':
        # join sp and subsp
        lst[-2] = lst[-2] +'$$$'+lst[-1]
        del lst[-1]
    taxstr = ';'.join(lst)
    #print('taxstr',taxstr)
    #print('taxstr',taxstr.rstrip(';'))
    return taxstr.rstrip(';')
def add_row_by_cell(list1, list2):
    new_list = []
    if len(list1) != len(list2):
        sys.exit('list length difference')
    for i in range(0, len(list1)): 
        new_list.append(float(list1[i]) + float(list2[i])) 
    return new_list
    
def run(args):
    
    taxlookup = {}
    otidlookup = {}
    # INFILE: taxonomyNcounts
    mtx = open(args.infile,'r')
    rowcount = 0
    for line in mtx:
    #with open(args.infile) as csv_file: 
        line = line.strip()
        row = line.split('\t')
        #csv_reader = csv.DictReader(csv_file, delimiter='\t') # 
        if rowcount==0:
            samples_list = row[5:]
        else:
            taxonomy = row.pop(0)
            taxon = row.pop(0)
            otid = row.pop(0)
            level = row.pop(0)
            note = row.pop(0)
            #print('row',row)
            if taxonomy.startswith('NonHOMD'):
                    non_homd_row  = row
            elif taxonomy.startswith('LowAbund'):
                    low_abund_row = row
            else:
                if taxonomy in taxlookup:
                    taxlookup[taxonomy] = add_row_by_cell(taxlookup[taxonomy], row)
                else:
                    taxlookup[taxonomy] = row
                otidlookup[taxonomy] = otid
        rowcount+=1
    
    #print('samples_list',len(samples_list),samples_list)
    
    domain_lookup = {}
    phylum_lookup = {}
    class_lookup = {}
    order_lookup = {}
    family_lookup = {}
    genus_lookup = {}
    species_lookup = {}
    subspecies_lookup = {}
    count = 0
    for fulltax in taxlookup:
        # if count == 0:
#             print('fulltax',fulltax)
#             print('G_ST_SRS011061_v1_hmp2-STO',taxlookup[fulltax]['G_ST_SRS011061_v1_hmp2-STO'])
        count +=1
        tax_list = fulltax.split(';')
        #print(tax_list)
        #sys.exit()
        
        #for i in range(0,8):  # 7 for species 8-for subsp
        for i,tax in enumerate(tax_list):
            
        #for i,name in enumerate(tax_list):
            longname = get_longname(i, fulltax)
            if not longname:
                 #print('no lN',fulltax)
                 pass
            #print('fulltax',fulltax,'longname',longname)
            if i == 0:  #domain
                
                #print('0-longname',longname)
                if longname not in domain_lookup:
                    domain_lookup[longname] = {}
                #print('G_ST_SRS011061_v1_hmp2-STO',float(taxlookup[fulltax]['G_ST_SRS011061_v1_hmp2-STO']))
                for i,value in enumerate(taxlookup[fulltax]):
                    samplesite = samples_list[i]
                    #if samplesite == 'G_ST_SRS011061_v1_hmp2-STO':
                    if samplesite not in domain_lookup[longname]:
                        domain_lookup[longname][samplesite] = float(value) #+ float(noclosematch[samplesite])
                    else:
                        domain_lookup[longname][samplesite] += float(value)
            elif i == 1:  #phylum
                
                if longname not in phylum_lookup:
                    phylum_lookup[longname] = {}
                for i,value in enumerate(taxlookup[fulltax]):
                    samplesite = samples_list[i]
                    if samplesite not in phylum_lookup[longname]:
                        phylum_lookup[longname][samplesite] = float(value) #+ float(noclosematch[samplesite])
                    else:
                        phylum_lookup[longname][samplesite] += float(value)
            elif i == 2:  #class
                
                if longname not in class_lookup:
                    class_lookup[longname] = {}
                for i,value in enumerate(taxlookup[fulltax]):
                    samplesite = samples_list[i]
                    if samplesite not in class_lookup[longname]:
                        class_lookup[longname][samplesite] = float(value) #+ float(noclosematch[samplesite])
                    else:
                        class_lookup[longname][samplesite] += float(value)
            elif i == 3:  #order
                
                if longname not in order_lookup:
                    order_lookup[longname] = {}
                for i,value in enumerate(taxlookup[fulltax]):
                    samplesite = samples_list[i]
                    if samplesite not in order_lookup[longname]:
                        order_lookup[longname][samplesite] = float(value) #+ float(noclosematch[samplesite])
                    else:
                        order_lookup[longname][samplesite] += float(value)
            elif i == 4:  #family
                
                if longname not in family_lookup:
                    family_lookup[longname] = {}
                for i,value in enumerate(taxlookup[fulltax]):
                    samplesite = samples_list[i]
                    if samplesite not in family_lookup[longname]:
                        family_lookup[longname][samplesite] = float(value) #+ float(noclosematch[samplesite])
                    else:
                        family_lookup[longname][samplesite] += float(value)
            elif i == 5:  #genus
                
                if longname not in genus_lookup:
                    genus_lookup[longname] = {}
                for i,value in enumerate(taxlookup[fulltax]):
                    samplesite = samples_list[i]
                    if samplesite not in genus_lookup[longname]:
                        genus_lookup[longname][samplesite] = float(value) #+ float(noclosematch[samplesite])
                    else:
                        genus_lookup[longname][samplesite] += float(value)
            elif i == 6:  #species and subsp
                
                if longname not in species_lookup:
                    species_lookup[longname] = {}
                for i,value in enumerate(taxlookup[fulltax]):
                    samplesite = samples_list[i]
                    if samplesite not in species_lookup[longname]:
                        species_lookup[longname][samplesite] = float(value)
                    else:
                        species_lookup[longname][samplesite] += float(value)

            else:
                sys.exit('i === 8?')
    
    
    #print('subspecies_lookup',subspecies_lookup)
    #sys.exit()
    header = 'Taxonomy\tRank\tHMT\tNotes'
    for samplesite in samples_list:
        header += '\t'+samplesite
    header += '\n'
    fout = open(args.outfile,'w')
    fout.write(header)
    #for oligotype in file1_newlookup:
    #print('domainLU',domain_lookup.keys())
    for name in domain_lookup:
        txt =  name+'\tdomain\t\t'  # no HMT
        for samplesite in samples_list:
            txt += '\t'+str(round(domain_lookup[name][samplesite],3))
        txt += '\n'
        fout.write(txt)
    for name in phylum_lookup:
        txt =  name+'\tphylum\t\t'  # no HMT
        for samplesite in samples_list:
            txt += '\t'+str(round(phylum_lookup[name][samplesite],3))
        txt += '\n'
        fout.write(txt)
    for name in class_lookup:
        txt =  name+'\tclass\t\t'  # no HMT
        for samplesite in samples_list:
            txt += '\t'+str(round(class_lookup[name][samplesite],3))
        txt += '\n'
        fout.write(txt)
    for name in order_lookup:
        txt =  name+'\torder\t\t'  # no HMT
        for samplesite in samples_list:
            txt += '\t'+str(round(order_lookup[name][samplesite],3))
        txt += '\n'
        fout.write(txt)
    for name in family_lookup:
        txt =  name+'\tfamily\t\t'  # no HMT
        for samplesite in samples_list:
            txt += '\t'+str(round(family_lookup[name][samplesite],3))
        txt += '\n'
        fout.write(txt)
    for name in genus_lookup:
        txt =  name+'\tgenus\t\t'  # no HMT
        for samplesite in samples_list:
            txt += '\t'+str(round(genus_lookup[name][samplesite],3))
        txt += '\n'
        fout.write(txt)
    for name in species_lookup:
        txt =  name+'\tspecies'
        note = ''
        if not otidlookup[name]:
            note = 'has subspecies'
        txt += '\t'+otidlookup[name]
        txt += '\t'+note
        for samplesite in samples_list:
            txt += '\t'+str(round(species_lookup[name][samplesite],3))
        txt += '\n'
        fout.write(txt)
    for name in subspecies_lookup:
        print('ssp name',name)
        if name not in otidlookup:
            print('MISSING tax-subsp: '+name)
        name_clean = name.replace('$$$',';')
        txt =  name_clean+'\tsubspecies'
        txt += '\t'+otidlookup[name]
        txt += '\t'
        for samplesite in samples_list:
            txt += '\t'+str(round(subspecies_lookup[name][samplesite],3))
        txt += '\n'
        fout.write(txt)
    # nonHOMD
    txt = "NonHOMD\tNonHOMD"
    txt += '\t'
    txt += '\t'
    for item in non_homd_row:
        txt += '\t'+str(round(float(item),3))
    txt += '\n'
    fout.write(txt)
    
    # LowAbund
    txt = "LowAbund\tLowAbund"
    txt += '\t'
    txt += '\t'
    for item in low_abund_row:
        #print('item',unmatched[item])
        txt += '\t'+str(round(float(item),3))
    txt += '\n'
    fout.write(txt)
    
    fout.close()
    


if __name__ == "__main__":

    usage = """
    USAGE:
       
           
       ../8-NEWgather_abundance_by_rank.py -i AKE_v3v5_NIH_pct_matrix_2023-11-20_homd.csv
       --source must be in ['NIH_v1v3','NIH_v3v5']
      
       ** need to grab the "NoCloseMatch" numbers for each sample-site and add that to the
        sum (will make the results lower). But only for ranks domain...genus Not Species.
        "NoCloseMatch" counts are in the coalesce file
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=True,  action="store",   dest = "infile", default=False,
                                                    help="HOMD-endpoint1-wpcts.csv")
    #parser.add_argument("-site", "--site",   required=True,  action="store",   dest = "site", 
     #                                              help=" ")
    parser.add_argument("-host", "--host", required = False, action = 'store', dest = "dbhost", default = 'localhost',
                                                   help="") 
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", default=False,
                                                    help="verbose print()") 
    parser.add_argument("-o", "--out_file", required = False, action = 'store', dest = "outfile", 
            default = 'NEWrank_abundance_sums', help = "")
    
    args = parser.parse_args()
    
    # if args.source not in ['NIH_v1v3','NIH_v3v5']:
#         print(usage)
#         sys.exit()
    
                            
    if args.dbhost == 'homd_dev':
        args.DATABASE = 'homd'
        dbhost = '192.168.1.46'
        args.prettyprint = False
    
    elif args.dbhost == 'homd_prod':
        args.DATABASE = 'homd'
        dbhost = '192.168.1.42'
        args.prettyprint = False

    elif args.dbhost == 'localhost':
        #args.json_file_path = '/Users/avoorhis/programming/homd-data/json'
        #args.TAX_DATABASE  = 'HOMD_taxonomy'
        args.DATABASE = 'homd'
        dbhost = 'localhost'
        #dbhost_old = 'localhost'
        
    else:
        sys.exit('dbhost - error')
        
    site_names = [
    'AKE',  #Attached_Keratinized_gingiva
    'ANA',  #Anterior_nares
    'BMU',  #Buccal_mucosa
    'HPA',  #Hard_palate
    'LAF',  #L_Antecubital_fossa
    'LRC',  #L_Retroauricular_crease
    'MVA',  #Mid_vagina
    'PFO',  #Posterior_fornix
    'PTO',  #Palatine_Tonsils
    'RAF',  #R_Antecubital_fossa
    'RRC',  #R_Retroauricular_crease
    'SAL',  #Saliva
    'STO',  #Stool
    'SUBP', #Subgingival_plaque
    'SUPP', #Supragingival_plaque
    'THR',  #Throat
    'TDO',  #Tongue_dorsum
    'VIN'   #Vaginal_introitus
    ]
    
    if args.dbhost == 'homd_v4':
        args.DATABASE = 'homd'
        dbhost= '192.168.1.46'
        args.prettyprint = False
    elif args.dbhost == 'homd_dev':
        args.DATABASE = 'homd'
        dbhost= '192.168.1.58'
        args.prettyprint = False
    elif args.dbhost == 'localhost':
        args.DATABASE = 'homd'
        dbhost = 'localhost'
    else:
        sys.exit('dbhost - error')
    print('Using',args.dbhost,dbhost)
    myconn = MyConnection(host=dbhost, db=args.DATABASE,  read_default_file = "~/.my.cnf_node")
    
    args.outfile = 'HMP_'+args.outfile +'_'+today+'_homd.csv'
    if args.verbose:
        print()
    if not args.infile:
        print(usage)
        sys.exit()
        
    
    # noclosematch = get_no_close_match(args)    
#     run(args, noclosematch)
    run(args)
