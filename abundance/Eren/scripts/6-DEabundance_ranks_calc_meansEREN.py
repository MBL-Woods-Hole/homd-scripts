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
site_order_eren =     ['BMU','HPA','AKE','PTO','STO','SUBP','SUPP','SAL','TDO','THR']
site_order_dewhirst = ['BMU','HPA','AKE','PTO','SUBP','SUPP','SAL','TDO','THR','ANA']
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

def calcPrevByPerson(row, site):
    #data = []
    #print(site)
    personsiteavg = {}
    #personsiteavg2 = []
    personsitecollector = {}
    for key in row.keys():
        items = key.split('-')
        if len(items) == 2:
            person = items[0]
            for site_fd in site_order_dewhirst:
                personsite = person+'-'+site_fd
                personsitecollector[personsite] = []
    for key in row.keys():
        items = key.split('-')
        if len(items) == 2:
            for personsite in personsitecollector:
                if personsite in key:
                    personsitecollector[personsite].append(float(row[key]))

    for personsite in personsitecollector:
        if len(personsitecollector[personsite]) > 0:
            personsiteavg[personsite] = mean(personsitecollector[personsite])
            #personsiteavg2.append([personsite,mean(personsitecollector[personsite])])
    #print('\npersonsiteavg-row',personsiteavg)
    prev = calc(personsiteavg, site, 'prev')
    
    #print('prev2',site, prev)
    return prev
        
        # of individuals in which this HMT is non-zero at this site)
        # /(total number of individuals for whom we have samples at this site) = 77
    #return 100*(float(len([x for x in data if x > 0])) / float(len(data)))
        
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
    
    sites = site_order_eren
    
    lookup = {}
    with open(args.infile) as csv_file: 
        
        csv_reader = csv.DictReader(csv_file, delimiter='\t')
        #file1.append( {rows[0]:rows[1] for rows in reader} )
        gut_count = 0
        nomatch_count = 0
        row_count = 1
        subsp_rows = []
        for row in csv_reader:
            subsps = species_w_subspecies.keys()
            for subsp in subsps:
                if subsp in row['Taxonomy']:
                    subsp_rows.append(row)
            lookup[row['Taxonomy']] = {}
            lookup[row['Taxonomy']]['Rank']= 'XX' # gets set elsewhere
            lookup[row['Taxonomy']]['HMT']= row['HMT']
            lookup[row['Taxonomy']]['Note']= row['Notes']
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
    sp_collector = {}
    for row in subsp_rows:
        
        species = row['Taxonomy'].split()[0]
        if species not in sp_collector:
            sp_collector[species] = []
        sp_collector[species].append(row)
# site_order =          ['BM','HP','KG','PT','SUBP','SUPP','SV','TD','TH', 'ST']
# site_order_dewhirst = ['BM','HP','KG','PT','SUBP','SUPP','SV','TD','TH', 'NS']
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
       
           
       ../9-abunance_ranks_calc_means.py -i AKE_NIH_v3v5_NEWrank_abundance_sums_2023-12-14_homd.csv -src dewhirst
       -src/--source must be in ['eren_v1v3','eren_v3v5','dewhirst']
       -site/--site ake, ana, bmu...
     
       Must amend species with subspecies: need to sum pcts into species
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=True,  action="store",   dest = "infile", 
            default=False, help="2-HOMD_NEWcoalesce01.csv")
    

    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", 
            default=False, help="verbose print()") 
    parser.add_argument("-outfile", "--out_file", required = False, action = 'store', dest = "outfile", 
            default = 'MeanStdevPrev_byRankFINAL', help = "")
    parser.add_argument("-r", "--region", required = True, action = 'store', dest = "region", 
                         help = "['eren_v1v3','eren_v3v5','dewhirst']")
    
    
    args = parser.parse_args()
    
    
    if args.region not in ['v1v3','v3v5']:
        print(usage)
        sys.exit()
    
    
    
        
    args.outfile = args.region+'_'+args.outfile +'_'+today+'.csv'
    
    
    
        
    #myconn_new = MyConnection(host=dbhost, db=args.NEW_DATABASE,  read_default_file = "~/.my.cnf_node")
    if args.verbose:
        print()
    if not args.infile:
        print(usage)
        sys.exit()
     
    run(args)
