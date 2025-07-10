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


def get_species(hot_pts):
    sql = "select genus,species from otid_prime"
    sql += " join taxonomy using(taxonomy_id)"
    sql += " join genus using(genus_id)"
    sql += " join species using(species_id)"
    sql += " WHERE"
    sql += " otid='%s'"
    lst = []
    for hot in hot_pts[1:]:
        q1 = sql % (hot)
        #print(q1)
        result = myconn.execute_fetch_select(q1)
        if myconn.cursor.rowcount == 0:
            sys.exit('ERROR',sql)
        lst.append(result[0][0]+' '+result[0][1])
    #print(';'.join(lst))
    return ';'.join(lst)
def clean_hmt(s):
    
    return str(int(s.split('-')[1]))  # strips zeros HMT-058 => 58
    
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
    note_collector = {}
    datacols = {}
    hmts={}
    notes={}
    true_site_names = []
    mx = 0.0
    for site in site_names:
        #fn = site+'_species_otu_table.PRELIM.gt1000ct.'+args.region+'.clean_wcounts.tsv'
        path = site+'_'+args.region+'_MeanStdevPrev_byRankFINAL*'  # site+'_brief*'
        
        for fn in glob.glob(path):  # must only be one per site
            
            if os.path.isfile(fn):
                print('Reading:',fn)
                true_site_names.append(site)
                
                fp = open(fn,'r')
                for line in fp:
               
                    line = line.strip()
                    line_pts = line.split('\t')
                    if line_pts[0] == 'UNMATCHED':
                        continue
                    if line_pts[0] == 'Taxonomy':
                        #header = line
                        datacols[site] = line_pts[5:]
                        
                        #ds_count = len(dataset_order)
                        #non_ds_order = line_pts[:3]
                    else:
                        tax = line_pts[0]
                        note = line_pts[3]
                        
                        if tax not in collector:
                            collector[tax] = {}
                        if tax not in note_collector:
                            note_collector[tax] = []
                        if note:
                            note_collector[tax].append(note)
                        data = [round(float(x),5) for x in line_pts[5:]]
                        collector[tax][site] = data
                        collector[tax]["rank"] =line_pts[1]
                        
                        collector[tax]["hmt"] = line_pts[2]
                        #print('hmt',line_pts[2])
                        #collector[tax]["note"] = line_pts[3]
                        # collector[tax]["linemax"] = line_pts[4]
#                         if float(line_pts[4]) > mx:
#                             collector[tax]["max"] = float(line_pts[4])
#                             mx = float(line_pts[4])
                        
    if len(true_site_names) == 0:
        sys.exit('no files found')
        
    outfp = open(args.outfile,'w')
    outfp.write('Taxonomy\tRank\tHMT\tNotes\tMax')
    for site in true_site_names:
        for colname in datacols[site]:
            outfp.write('\t'+colname)
    outfp.write('\n')
    
    for tax in collector:
        tax_pts = tax.split(';')
        #print('hp',hot_pts)
        #rank = ranks[len(tax_pts)-1]
        mx = 0.0
        for site in true_site_names:  # to keep order
            for i,n in enumerate(datacols[site]):
                if site in collector[tax] and "mean" in n:
                    #print('need max',n, collector[tax][site][i])
                    if collector[tax][site][i] > mx:
                        mx = collector[tax][site][i]
        #print(tax,mx)
        
        notes = ';'.join(note_collector[tax])
        hmt =  collector[tax]["hmt"]  #.zfill(3)
        #print('hmt2',tax+'\t'+collector[tax]["rank"]+'\t'+hmt)
        outfp.write(tax+'\t'+collector[tax]["rank"]+'\t'+hmt+'\t'+notes+'\t'+str(mx))
        for site in true_site_names:  # to keep order
            for i,n in enumerate(datacols[site]):
                if site in collector[tax]:
                    outfp.write('\t'+str(collector[tax][site][i]))
                else:
                    outfp.write('\t0.0')
        outfp.write('\n')
        
        
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
    
    args.outfile = 'NEWAll_Sites_'+args.region+'_RelAbund_'+today+'_homd.csv'
    run()
        
    

    if not args:
       print('no def selected')
       print(usage)
    

    
