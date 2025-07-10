#!/usr/bin/env python

import os, sys, stat
import json
import argparse
import csv
sys.path.append('/home/ubuntu/homd-work')
sys.path.append('/Users/avoorhis/programming/')
from connect import MyConnection
import datetime
ranks = ['domain','phylum','klass','order','family','genus','species','subspecies']
today = str(datetime.date.today())
from statistics import mean,stdev
"""

"""
directory_to_search = './'

#header = 'OLIGOTYPE\tPHYLUM\tNUM_BEST_HITS\tBEST_HIT_%ID\tBEST_HIT_%COV\tOVERALL_%IDENT\tHMTs\tHOMD_SPECIES\tSTRAIN_CLONE\tHOMD_REFSEQ_ID\tGB_NCBI_ID\tHOMD_STATUS\n'
#header = 'OLIGOTYPE\tPHYLUM\tNUM_BEST_HITS\tBEST_PCT_ID\tBEST_FULL_PCT_ID\tHMTs\tHOMD_SPECIES\tSTRAIN_CLONE\tHOMD_REFSEQ_ID\tGB_NCBI_ID\tHOMD_STATUS\n'
#site_order = ['BMU','HPA','AKE','PTO','STO','SUBP','SUPP','SAL','TDO','THR']
#site_order_dewhirst = ['BMU','HPA','AKE','PTO','SUBP','SUPP','SAL','TDO','THR','ANA']
#site_order_nih = ['ANA','AKE','BMU','HPA','LAF','LRC','MVA','PTO','PFO','RAF','RRC','SAL','STO','SUBP','SUPP','THR','TDO','VIN']


def get_otids_w_subspecies():
    otid_list = []
    q = "SELECT otid, genus, species, subspecies from otid_prime"
    q += " JOIN taxonomy using(taxonomy_id)"
#     q += " JOIN domain using(domain_id)"
#     q += " JOIN phylum using (phylum_id)"
#     q += " JOIN klass using (klass_id)"
#     q += " JOIN `order` using (order_id)"
#     q += " JOIN family using (family_id)"
    q += " JOIN genus using(genus_id)"
    q += " JOIN species using (species_id)"
    q += " JOIN subspecies using(subspecies_id)"
    q += " WHERE subspecies_id != '1'"
    #print(q)
    result = myconn.execute_fetch_select_dict(q)
    for row in result:
        otid_list.append(str(row['otid']))
    
    #print('otid_list',otid_list)
    #sys.exit()
    return otid_list
    
# species_w_subspecies = {
# 
#    'Actinomyces;oris':['clade-169','clade-893','clade-043','clade-079','clade-144','clade-171'],
#   'Campylobacter;concisus':['clade-575','clade-433'],
#   'Corynebacterium;aurimucosum':['clade-034','clade-445'],
#   'Corynebacterium;jeikeium':['clade-047'],
#   'Gemella;haemolysans':['clade-434','clade-626'],
#   'Limosilactobacillus;reuteri':['clade-938'],
#   
#   'Peptoanaerobacter;yurii': ['subsps. yurii&margaretiae','subsp. schtitka'],
#   'Rothia;mucilaginosa':['clade-681','clade-147'],
#   
#   'Streptococcus;parasanguinis': ['clade-721'],
#     'Streptococcus;infantis': ['clade-638','clade-444','clade-061','clade-431'],
#     'Streptococcus;cristatus': ['clade-886'],
#     'Streptococcus;oralis': ['subsp. oralis', 'subsp. dentisani', 'subsp. tigurinus'],
#     'Treponema;socranskii': ['subsp. paredis','subsp. socranskii','subsp. buccale'],
#     'Treponema;vincentii': ['clade-029','clade-432']
#     
# }
#hmts_w_subspecies = ['106','71','377','398','707']
#hmts_w_subspecies = ['169','893','43','79','144','938','106','377','681','147','71','398','707','721','886']
#hmts_w_subspecies = [144,169,43,79,893,433,575,445,450,34,454,47,626,434,938,106,377,147,681,886,638,398,707,71,721,444,438,440,29,769,432]
def calc(row, site, fxn):
    import numpy as np
    data = []
    #print()
    for key in row.keys():
        items = key.split('-')
        #G_ST_SRS055982_v2_hmp2-STO
        if  site == items[-1]:
            #print(key,site,row[key])
            data.append(float(row[key]))
            #print('row[key]',row[key])
    #print(site,data)
    if fxn == '90p':
        if len(data)==1:
            return data[0]
        else:
            return np.percentile(data,90)
    if fxn == '10p':
        if len(data)==1:
            return data[0]
        else:
            return np.percentile(data,10)
    if fxn == 'mean':
        if len(data)==1:
            return data[0]
        else:
            return mean(data)
    if fxn == 'sd':
        if len(data)==1:
            return 0
        else:
            return stdev(data)
    if fxn == 'prev':
        # of individuals in which this HMT is non-zero at this site)
        # /(total number of individuals for whom we have samples at this site) = 77
        return 100*(float(len([x for x in data if x > 0])) / float(len(data)))
           
      

def run(args):
    
    sites =  site_names  # PERIO ???
    otids_w_subspecies = get_otids_w_subspecies()
    lookup = {}
    subsp_rows = []
    with open(args.infile) as csv_file: 
        
        csv_reader = csv.DictReader(csv_file, delimiter='\t')
        #file1.append( {rows[0]:rows[1] for rows in reader} )
        gut_count = 0
        nomatch_count = 0
        row_count = 1
        
        for row in csv_reader:
            
            hmt = row['HMT']  # format HMT-955
            otid = ''
            if '-' in hmt:
                otid = hmt.split('-')[1]
            if otid in otids_w_subspecies:
                print('metaphlan appending',otid)
                subsp_rows.append(row)
            
            lookup[row['Taxonomy']] = {}
            lookup[row['Taxonomy']]['Rank']= 'XX' # gets set elsewhere
            lookup[row['Taxonomy']]['HMT']= hmt
            lookup[row['Taxonomy']]['Note']= row['Notes']
            
            
            
            rowmax = 0
            for site in sites:
                #print('site,row',site,row)
                mean = calc(row, site.upper(), 'mean')
                
                if mean > rowmax:
                    rowmax = mean
                lookup[row['Taxonomy']][site+'-mean'] = mean
                lookup[row['Taxonomy']][site+'-sd']   = calc(row, site.upper(), 'sd')
                lookup[row['Taxonomy']][site+'-10p']   = calc(row, site.upper(), '10p')
                lookup[row['Taxonomy']][site+'-90p']   = calc(row, site.upper(), '90p')
                
                lookup[row['Taxonomy']][site+'-prev'] = calc(row, site.upper(), 'prev')
            lookup[row['Taxonomy']]['Max'] = rowmax
            
            row_count += 1
    
    # for rows with subspecies
    sp_collector = {}
    for row in subsp_rows:
        #print('tax',row['Taxonomy'])
        tparts = row['Taxonomy'].split(';')
        del tparts[-1]
        species = ';'.join(tparts)
        #print('sp',species)
        if species not in sp_collector:
            sp_collector[species] = []
        sp_collector[species].append(row)

    for species in sp_collector:
        if species in lookup:
            #sys.exit('ERROR -already in lookup')
            print('ERROR -species already in lookup',species)
        lookup[species] = {}
        lookup[species]['Rank'] = 'species'
        lookup[species]['HMT'] = ''
        lookup[species]['Note'] = 'combined from subspecies'  
        #bm,hp,kg,pt,subp,supp,sv,td,th=0,0,0,0,0,0,0,0,0
        psite_collector ={}
        for row in sp_collector[species]:
            #print(row)
            for key in row.keys():
                items = key.split('-') 
                if items[-1] in site_names:
                    if key not in psite_collector:
                        psite_collector[key] = float(row[key])
                    else:
                        psite_collector[key] += float(row[key])
        rowmax = 0
        for site in sites:
            mean = calc(psite_collector, site.upper(), 'mean')
            if mean > rowmax:
                rowmax = mean
            lookup[species][site+'-mean'] = mean
            lookup[species][site+'-sd']   = calc(psite_collector, site.upper(), 'sd')
            #if args.source in ['dewhirst_35x9','eren2014_v1v3','eren2014_v3v5']:
            lookup[species][site+'-10p']   = calc(psite_collector, site.upper(), '10p')
            lookup[species][site+'-90p']   = calc(psite_collector, site.upper(), '90p')
            lookup[species][site+'-prev'] = calc(psite_collector, site.upper(), 'prev')
        lookup[species]['Max'] = rowmax
    header = ''
    header += 'Taxonomy\tRank\tHMT\tNotes\tMax'
    for site in sites:
        header += '\t'+site.upper()+'-mean'
        header += '\t'+site.upper()+'-10p'
        header += '\t'+site.upper()+'-90p'
        header += '\t'+site.upper()+'-sd'
        header += '\t'+site.upper()+'-prev'

    header += '\n'
    
    
  
    fout = open(args.outfile,'w')
    fout.write(header)
    #for oligotype in file1_newlookup:
    
    for tax in lookup:
        if tax == 'UNMATCHED':
            rank = ''
        else:
            rank = ranks[len(tax.split(';'))-1]
        txt =  tax
        txt += '\t'+rank  #lookup[tax]['Rank']
        txt += '\t'+lookup[tax]['HMT']
        txt += '\t'+lookup[tax]['Note']
        txt += '\t'+str(round(lookup[tax]['Max'],3))
        for site in sites:
            txt += '\t'+str(round(lookup[tax][site+'-mean'],3))
            txt += '\t'+str(round(lookup[tax][site+'-10p'],3))
            txt += '\t'+str(round(lookup[tax][site+'-90p'],3))
            txt += '\t'+str(round(lookup[tax][site+'-sd'],3))
            txt += '\t'+str(round(lookup[tax][site+'-prev'],3))
            #if args.source == 'dewhirst_35x9':
            #    txt += '\t'+str(round(lookup[tax][site+'-prev2'],3))
        txt += '\n'
   
        fout.write(txt)
    fout.close()
            
    
    


if __name__ == "__main__":

    usage = """
    USAGE:
       
           
       ../9-abunance_ranks_calc_means.py -i AKE_NIH_v3v5_NEWrank_abundance_sums_2023-12-14_homd.csv -src NIH_v3v5 -site ake
       -src/--source must be in ['NIH_v1v3','NIH_v3v5']
       -site/--site ake, ana, bmu...
     
       Must amend species with subspecies: need to sum pcts into species
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=True,  action="store",   dest = "infile", 
            default=False, help="HOMD_NEWcoalesce01.csv")
    #parser.add_argument("-site", "--site",   required=True,  action="store",   dest = "site", default='NONE',
    #                                               help=" ")
    parser.add_argument("-host", "--host", required = False, action = 'store', dest = "dbhost", 
            default = 'localhost',help="") 
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", 
            default=False, help="verbose print()") 
    parser.add_argument("-outfile", "--out_file", required = False, action = 'store', dest = "outfile", 
            default = 'HMPMeanStdevPrev_byRankFINAL', help = "")
    # parser.add_argument("-src", "--source", required = True, action = 'store', dest = "source", 
#                          help = "['NIH_v1v3','NIH_v3v5']")
    
    
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
 #   'LAF',  #L_Antecubital_fossa  # not in HMP
    'PERIO',  # ONLY in HMP
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
    
        
    args.outfile = args.outfile +'_'+today+'_homd.csv'
    
    
        
    myconn = MyConnection(host=dbhost, db=args.DATABASE,  read_default_file = "~/.my.cnf_node")
    if args.verbose:
        print()
    if not args.infile:
        print(usage)
        sys.exit()
     
    run(args)
