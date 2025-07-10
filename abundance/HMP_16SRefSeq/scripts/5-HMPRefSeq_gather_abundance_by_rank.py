#!/usr/bin/env python

import os, sys, stat
import json
import argparse
import csv

sys.path.append('/Users/avoorhis/programming/')
sys.path.append('/home/ubuntu/homd-work')
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
    sql = "select taxonomy_id,domain,phylum,klass,`order`,family,genus,species,subspecies from otid_prime"
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
    tax_id = str(lst.pop(0))  # returns AND removes taxonomy_id
    #print('lst',lst)
    if lst[-1] != '':
        
        
        # join sp and subsp
        lst[-2] = lst[-2] +'$$$'+lst[-1]
        del lst[-1]
    taxstr = ';'.join(lst)
    #print('taxstr',taxstr)
    #print('taxstr',taxstr.rstrip(';'))
    return (tax_id, taxstr.rstrip(';'))
    
def run(args):
    
    taxlookup = {}
    otidlookup = {}
    notes_lookup = {}
    # INFILE: taxonomyNcounts
    with open(args.infile) as csv_file: 
        
        csv_reader = csv.DictReader(csv_file, delimiter='\t') # 
        for row in csv_reader:
            #taxonomy = row['Taxonomy']
            
            #print(row)
            hmt = row.pop('HOT-ID', None)
            notes = row.pop('Notes', None)
            #print('hmt',hmt)
            ## Important to get taxonomy from database
            ## because it may be different than in table
            if 'Unknown' in hmt:
                continue
            if hmt == 'Unmatched':
                unmatched = row
            else:
                otid = hmt.split('-')[1]
                #print('otid',otid)
                notes_lookup[otid] = notes
                (tax_id, taxonomy) = get_taxonomy_from_db(otid)
                taxlookup[taxonomy] = row
                otidlookup[taxonomy] = {'HMT':otid,"Taxonomy_id":tax_id}
                
    samplesite_order = list(row.keys())
    #print('unmatched',unmatched)
    domain_lookup = {}
    phylum_lookup = {}
    class_lookup = {}
    order_lookup = {}
    family_lookup = {}
    genus_lookup = {}
    species_lookup = {}
    subspecies_lookup = {}
    for fulltax in taxlookup:
        
        tax_list = fulltax.split(';')
        #print(tax_list)
        #sys.exit()
        #for i in range(0,8):  # 7 for species 8-for subsp
        for i,tax in enumerate(tax_list):
            
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
            elif i == 6:  #species and subsp
                if '$$$' in tax_list[-1]:  #subsp
                    
                    if longname not in subspecies_lookup:
                        subspecies_lookup[longname] = {}
                    for samplesite in taxlookup[fulltax]:
                        if samplesite not in subspecies_lookup[longname]:
                            subspecies_lookup[longname][samplesite] = float(taxlookup[fulltax][samplesite])
                        else:
                            subspecies_lookup[longname][samplesite] += float(taxlookup[fulltax][samplesite])
                else:
                    if longname not in species_lookup:
                        species_lookup[longname] = {}
                    for samplesite in taxlookup[fulltax]:
                        if samplesite not in species_lookup[longname]:
                            species_lookup[longname][samplesite] = float(taxlookup[fulltax][samplesite])
                        else:
                            species_lookup[longname][samplesite] += float(taxlookup[fulltax][samplesite])

            else:
                sys.exit('i === 8?')
    
    
    #print('subspecies_lookup',subspecies_lookup)
    #sys.exit()
    header = 'Taxonomy\tRank\tHMT\tTaxonomy_ID\tNotes'
    for samplesite in samplesite_order:
        header += '\t'+samplesite
    header += '\n'
    fout = open(args.outfile,'w')
    fout.write(header)
    #for oligotype in file1_newlookup:
    
    for name in domain_lookup:
        txt =  name+'\tdomain\t\t\t'  # no HMT
        for samplesite in samplesite_order:
            txt += '\t'+str(round(domain_lookup[name][samplesite],3))
        txt += '\n'
        fout.write(txt)
    for name in phylum_lookup:
        txt =  name+'\tphylum\t\t\t'  # no HMT
        for samplesite in samplesite_order:
            txt += '\t'+str(round(phylum_lookup[name][samplesite],3))
        txt += '\n'
        fout.write(txt)
    for name in class_lookup:
        txt =  name+'\tclass\t\t\t'  # no HMT
        for samplesite in samplesite_order:
            txt += '\t'+str(round(class_lookup[name][samplesite],3))
        txt += '\n'
        fout.write(txt)
    for name in order_lookup:
        txt =  name+'\torder\t\t\t'  # no HMT
        for samplesite in samplesite_order:
            txt += '\t'+str(round(order_lookup[name][samplesite],3))
        txt += '\n'
        fout.write(txt)
    for name in family_lookup:
        txt =  name+'\tfamily\t\t\t'  # no HMT
        for samplesite in samplesite_order:
            txt += '\t'+str(round(family_lookup[name][samplesite],3))
        txt += '\n'
        fout.write(txt)
    for name in genus_lookup:
        txt =  name+'\tgenus\t\t\t'  # no HMT
        for samplesite in samplesite_order:
            txt += '\t'+str(round(genus_lookup[name][samplesite],3))
        txt += '\n'
        fout.write(txt)
    for name in species_lookup:
        txt =  name+'\tspecies'
        
        if name not in otidlookup:
            print('MISSING tax-sp: '+name)
        txt += '\t'+otidlookup[name]['HMT']
        txt += '\t'+otidlookup[name]['Taxonomy_id']
        txt += '\t'+notes_lookup[otidlookup[name]['HMT']]
        for samplesite in samplesite_order:
            txt += '\t'+str(round(species_lookup[name][samplesite],3))
        txt += '\n'
        fout.write(txt)
    for name in subspecies_lookup:
        #print('ssp name',name)
        if name not in otidlookup:
            print('MISSING tax-subsp: '+name)
        name_clean = name.replace('$$$',';')
        txt =  name_clean+'\tsubspecies'
        txt += '\t'+otidlookup[name]['HMT']
        txt += '\t'+otidlookup[name]['Taxonomy_id']
        txt += '\t'+notes_lookup[otidlookup[name]['HMT']]
        for samplesite in samplesite_order:
            txt += '\t'+str(round(subspecies_lookup[name][samplesite],3))
        txt += '\n'
        fout.write(txt)
    # unmatched
    txt = "UNMATCHED\tUNMATCHED"
    txt += '\t\t\t'
    for item in unmatched:
        #print('item',unmatched[item])
        txt += '\t'+str(round(float(unmatched[item]),3))
    txt += '\n'
    fout.write(txt)
    
    
    fout.close()
    


if __name__ == "__main__":

    usage = """
    USAGE:
       
           
       ../8-NEWgather_abundance_by_rank.py -i AKE_v3v5_NIH_pct_matrix_2023-11-20_homd.csv
       --region must be in ['v1v3','v3v5']
      
       ** need to grab the "NoCloseMatch" numbers for each sample-site and add that to the
        sum (will make the results lower). But only for ranks domain...genus Not Species.
        "NoCloseMatch" counts are in the coalesce file
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=True,  action="store",   dest = "infile", default=False,
                                                    help="HOMD-endpoint1-wpcts.csv")
    #parser.add_argument("-site", "--site",   required=True,  action="store",   dest = "site", 
    #                                               help=" ")
    parser.add_argument("-host", "--host", required = False, action = 'store', dest = "dbhost", default = 'localhost',
                                                   help="") 
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", default=False,
                                                    help="verbose print()") 
    parser.add_argument("-o", "--out_file", required = False, action = 'store', dest = "outfile", 
            default = 'rank_abundance_sums', help = "")
    #parser.add_argument("-r", "--region", required = True, action = 'store', dest = "region", 
     #                    help = "['v1v3','v3v5']")
    # parser.add_argument("-ic", "--icoalesce", required = True, action = 'store', dest = "coalesceFile", 
#                          help = "")
    args = parser.parse_args()
    
    
    
                            
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
    ifpts = args.infile.split('_')
    args.site = ifpts[0]
    args.site = args.site.upper()
    args.region = ifpts[1]
    args.outfile = '_'.join([args.site,args.region,args.outfile,today+'.csv'])
    args.site = args.site.upper()
    if args.site not in site_names:
        sys.exit('site name not found',args.site)
    if args.region not in ['v1v3','v3v5']:
        print(usage)
        sys.exit()
    
    
    myconn = MyConnection(host=dbhost, db=args.DATABASE,  read_default_file = "~/.my.cnf_node")
    if args.verbose:
        print()
    if not args.infile:
        print(usage)
        sys.exit()
        
    
    # noclosematch = get_no_close_match(args)    
#     run(args, noclosematch)
    run(args)
