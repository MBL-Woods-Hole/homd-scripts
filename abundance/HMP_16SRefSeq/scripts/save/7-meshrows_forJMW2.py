#!/usr/bin/env python

## SEE https://docs.dhtmlx.com/suite/tree__api__refs__tree.html // new version 7 must load from json file
# this script creates a list of json objects that allows the dhtmlx javascript library
# to parse and show a taxonomy tree (Written for HOMD)
##
import os, sys
import gzip
import json
import glob
#from json import JSONEncoder
import argparse
import csv,re
from Bio import SeqIO
sys.path.append('../homd-data/')
sys.path.append('../../homd-data/')
sys.path.append('/Users/avoorhis/programming/homd-data/')
sys.path.append('/Users/avoorhis/programming/')
#from connect import MyConnection,mysql
import datetime
import requests
#import pandas as pd

global mysql_errors
mysql_errors = []
"""

"""
today = str(datetime.date.today())


#['_997', '995.2', '', '997', '1017', 'HOMD', 'HMT-997', 'Bacteria', 'Gracilibacteria_(GN02)', 'Gracilibacteria_(GN02)_[C-1]', 'Gracilibacteria_(GN02)_[O-1]', 'Gracilibacteria_(GN02)_[F-1]', 'Gracilibacteria_(GN02)_[G-4]', 'bacterium_HMT_997', 'NCBI', '363464', 'Bacteria', 'Candidatus Gracilibacteria', 'NA', 'NA', 'NA', 'NA', 'NA', '', '', 'NCBI', '363464', 'HMT-997', 'Bacteria', 'Candidatus Gracilibacteria (GN02)', 'Gracilibacteria_[C-1]', 'Gracilibacteria_[O-1]', 'Gracilibacteria_[F-1]', 'Gracilibacteria_[G-4]', 'bacterium_HMT_997', 'y']
ranks = ['domain','phylum','klass','order','family','genus','species']



    
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

def run():  
    collector = {}
    rank_collector = {}
    hmt_collector = {}
    datacols = {}
    hmts={}
    notes={}
    true_site_names = []
    mx = 0.0
    data_starts_at = 5
    for site in site_names:
        #fn = site+'_species_otu_table.PRELIM.gt1000ct.'+args.region+'.clean_wcounts.tsv'
        path = site+'_v1v3_rank_abundance_sums_2024-04-19.csv'  # site+'_brief*'
        
        for fn in glob.glob(path):  # must only be one per site
            
            if os.path.isfile(fn):
                #print('Reading:',fn)
                
                print('site',site)
                fp = open(fn,'r')
                for line in fp:
               
                    line = line.strip()
                    line_pts = line.split('\t')
                    
                    if line_pts[0]=='Taxonomy':
                        #header = line
                        datacols[site] = line_pts[data_starts_at:]
                        datalen = len(datacols[site])
                        #ds_count = len(dataset_order)
                        #non_ds_order = line_pts[:3]
                    else:
                        taxonomy = line_pts[0]
                        rank = line_pts[1]
                        hmt = line_pts[2]
                        taxid = line_pts[3]
                        notes = line_pts[4]
                        #print(line_pts[data_starts_at:])
                        data = [round(float(x),5) for x in line_pts[data_starts_at:]]
                        
                        if taxonomy not in collector:
                            collector[taxonomy] = {}
                            collector[taxonomy][site] = {}
                        # if site not in collector[taxonomy]:
#                             zerodata = 
#                             collector[taxonomy][site] = {"data":data,"level":rank,"HMT":hmt}
                        collector[taxonomy][site] = data
                        rank_collector[taxonomy] = rank
                        hmt_collector[taxonomy] = hmt
                        #print(hmts,site)
                        #note_collector[taxonomy][site] = note
                        
                        
    #print('note_collector',note_collector)
    
        
    outfp = open(args.outfile,'w')
    #Taxonomy	Rank	HMT	Taxonomy_ID	Notes
    outfp.write('Taxonomy\tRank\tHMT')
    
        
    for site in site_names:
        print('site',site)
        for colname in datacols[site]:
            outfp.write('\t'+colname)
    outfp.write('\n')
    
    for taxonomy in collector:
        #tax_pts = tax.split(';')
        
        #print('hp',hot_pts)
        #rank = ranks[len(tax_pts)-1]
        #print(site,collector[taxonomy])
        #print(site,collector[taxonomy])
        outfp.write(taxonomy+'\t'+rank_collector[taxonomy]+'\t'+hmt_collector[taxonomy])
        
        
        for site in site_names:  # to keep order
            for i,n in enumerate(datacols[site]):
                if site in collector[taxonomy]:
                    outfp.write('\t'+str(collector[taxonomy][site][i]))
                else:
                    outfp.write('\t0.0')
        outfp.write('\n')
        
    outfp.close()
    
if __name__ == "__main__":

    usage = """
     USAGE:
         mesh matricies
         
         6-NEWmeshrows.py* -r v1v3
         run with all files in a directory to merge them 
         AKE_NIH_v3v5_MeanStdevPrev_byRankFINAL_2023-12-15_homd.csv
         ANA_NIH_v3v5_MeanStdevPrev_byRankFINAL_2023-12-15_homd.csv
 
 
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-r", "--region",   required=True,  action="store",   dest = "region", 
                                                   help=" ")
    
    args = parser.parse_args()
    
    #parser.print_help(usage)
                        
    args.region = args.region.lower()
    
    dbhost = 'localhost'
    args.DATABASE = 'homd'
    #myconn = MyConnection(host=dbhost, db=args.DATABASE,  read_default_file = "~/.my.cnf_node")
    args.notaxcolumn = True
    args.outfile = 'HMP_Refseq_Sites_v1v3_rank_abundance_sums_2024-04-19.csv'
    run()
        
    
    
    
    if not args:
       print('no def selected')
       print(usage)
    

    
