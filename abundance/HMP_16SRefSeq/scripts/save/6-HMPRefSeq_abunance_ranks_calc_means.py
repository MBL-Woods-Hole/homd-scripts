#!/usr/bin/env python

import os, sys, stat
import json
import argparse
import csv
sys.path.append('../../homd-data/')
sys.path.append('/Users/avoorhis/programming/')
#from connect import MyConnection
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



species_w_subspecies = {
    'Streptococcus;parasanguinis': ['clade_411','clade_721'],
    'Streptococcus;infantis': ['clade_431','clade_638'],
    'Streptococcus;cristatus': ['clade_578','clade_886'],
    'Streptococcus;oralis': ['subsp._oralis', 'subsp._dentisani_clade_058', 'subsp._dentisani_clade_398', 'subsp._tigurinus_clade_070', 'subsp._tigurinus_clade_071'],
    'Fusobacterium;nucleatum': ['subsp._animalis', 'subsp._nucleatum', 'subsp._polymorphum', 'subsp._vincentii'],
    #'Limosilactobacillus;reuteri': ['clade_818','clade_938'],  # no abundance data
    'Peptostreptococcaceae_[G-7];[Eubacterium]_yurii': ['subsps._yurii_&_margaretiae','subsp._schtitka']
}
hmts_w_subspecies = ['411','431','578','638','721','818','886','938','398','707','106','71','377']
        


def calc(row, site, fxn):
    import numpy as np
    data = []
    for key in row.keys():
        items = key.split('-')
        #UC06-SUBP1  UC06-SUBP2 UC06-SUBP
        if len(items) == 2 and site in items[1]:
            #print(key,site,row[key])
            data.append(float(row[key]))
    if fxn == '90p':
        return np.percentile(data,90)
    if fxn == '10p':
        return np.percentile(data,10)
    if fxn == 'mean':
        return mean(data)
    if fxn == 'sd':
        return stdev(data)
    if fxn == 'prev':
        
        # of individuals in which this HMT is non-zero at this site)
        # /(total number of individuals for whom we have samples at this site) = 77
        return 100*(float(len([x for x in data if x > 0])) / float(len(data)))
           
      

def run(args):
    
    sites =  [args.site]
    
    lookup = {}
    subsp_rows = []
    with open(args.infile) as csv_file: 
        
        csv_reader = csv.DictReader(csv_file, delimiter='\t')
        #file1.append( {rows[0]:rows[1] for rows in reader} )
        gut_count = 0
        nomatch_count = 0
        row_count = 1
        
        for row in csv_reader:
            # subsps = species_w_subspecies.keys()
#             for subsp in subsps:
#                 if subsp in row['Taxonomy']:
#                     subsp_rows.append(row)
            hmt = row['HMT']
            lookup[row['Taxonomy']] = {}
            #print(row['Taxonomy'])
            lookup[row['Taxonomy']]['Rank']= 'XX' # gets set elsewhere
            lookup[row['Taxonomy']]['HMT']= hmt
            lookup[row['Taxonomy']]['Note']= row['Notes']
            if hmt in hmts_w_subspecies:
                subsp_rows.append(row) 
            rowmax = 0
            for site in sites:
                #print(site,row)
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
                if len(items) == 2:
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
        print('tax',tax)
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
            default = 'MeanStdevPrev_byRankFINAL', help = "")
    #parser.add_argument("-r", "--region", required = True, action = 'store', dest = "region", 
    #                     help = "['v1v3','v3v5']")
    
    
    args = parser.parse_args()
    
    
    if args.dbhost == 'homd':
        args.DATABASE = 'homd'
        dbhost = '192.168.1.40'

    elif args.dbhost == 'localhost':
        args.DATABASE = 'homd'
        dbhost = 'localhost'
        
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
    ifpts = args.infile.split('_')
    args.site = ifpts[0]
    args.site = args.site.upper()
    args.region = ifpts[1]
    args.outfile = '_'.join([args.site,args.region,args.outfile,today+'.csv'])
    args.site = args.site.upper()
    if args.site != 'NONE' and args.site not in site_names:
        sys.exit('site name not found '+args.site)
    
        
    #myconn_new = MyConnection(host=dbhost, db=args.DATABASE,  read_default_file = "~/.my.cnf_node")
    if args.verbose:
        print()
    if not args.infile:
        print(usage)
        sys.exit()
     
    run(args)
