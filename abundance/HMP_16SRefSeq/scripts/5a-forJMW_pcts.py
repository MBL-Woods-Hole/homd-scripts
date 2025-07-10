#!/usr/bin/env python

import os, sys, stat
import json
import argparse
import csv
sys.path.append('../../homd-data/')
sys.path.append('/Users/avoorhis/programming/homd-data/')
sys.path.append('/Users/avoorhis/programming/')
from connect import MyConnection
import datetime
ranks = ['domain','phylum','klass','order','family','genus','species']
today = str(datetime.date.today())

"""

"""

ds_start_at = 1

def get_ds_totals(args):

    fp = open(args.infile,'r')
    dsets = {}
    for line in fp:
        
        line = line.strip()
        line_pts = line.split('\t')
        #print(line_pts[:3],line_pts[3:] )
        # ['HOT-ID', 'num', 'pct'] ['S700014982-AKE',....
        if line_pts[0] == 'HOT-ID':
            header = line
            dataset_order = line_pts[ds_start_at:]
            #print('dataset_order',dataset_order)
            non_ds_order = line_pts[:ds_start_at]
            for ds in dataset_order:
                dsets[ds]=0
        else:
            cells = line_pts[ds_start_at:]
            
            for i,ds in enumerate(dataset_order):
                dsets[ds] += float(cells[i])
    fp.close()
    
    return(dsets)
    
def run(args):  # NOT dewhirst new data
    file1 = []
    file_lookup = {}
    species_lookup = {}
    subject_summer = {}
    site_subject_summer = {}
    collector = {}
    fp = open(args.infile,'r')
    outfp = open(args.outfile,'w')
    outfp.write('HOT-ID')
    #print(args.infile)
    for line in fp:
        # first S700014982V1-V3 S700014982V3-V5
        line = line.strip()
        line_pts = line.split('\t')
        #print(line_pts[:3],line_pts[3:] )
        # ['HOT-ID', 'num', 'pct'] ['S700014982-AKE',....
        if line_pts[0] == 'HOT-ID':
            header = line
            dataset_order = line_pts[ds_start_at:]
            for ds in dataset_order:
                outfp.write('\t'+ds)
            outfp.write('\n')
            non_ds_order = line_pts[:ds_start_at]
        else:
            # ['HOT-ID', 'Species', 'num_of_taxa', 'assign_reads_to', 'notes']
            hotid = line_pts[0]
            taxa = line_pts[1]
            
            cells = line_pts[ds_start_at:]
            row_sum = sum([float(x) for x in cells])
            
            
            outfp.write(hotid)
            for i,ct in enumerate(cells):
                abund = 100 * (float(ct) / float(args.dsets[dataset_order[i]]))
                outfp.write('\t'+str(abund))
            outfp.write('\n')
  
    outfp.close()
    
    
def get_qlength(seqfilename):
    with open(seqfilename) as f:
        seq = ''
        for line in f:
            if line.startswith('>'):
                continue
            seq += line.strip().replace('-','')
    return len(seq)
    
    


if __name__ == "__main__":

    usage = """
    USAGE:
    In each site directory:
    ./1-clean_data_step1.py -i AKE_species_count_table.tsv   
          
          -d/--delete xxx  (integer min ds count to retain default:1000)
          -s/--site   Required AKE,ANA...
           MUST use the original file: XXX_species_count_table.tsv
           
        This script is the first step:
          -- counts: creates integer from float
          -- cleans the taxa name to remove 'k__','p__', 'c__' .... 
          
          -- removes datasets that sum less than XX counts (Default: keep all data)
        Does Not:
          -- Split into v1v3 and v3v5 
          -- Remove 'multi' and '_nov_' taxa
          
    
       1a-separate_v1v3_v3v5.py   
       2-separate_multispecies_taxa.py 
    
       copy all the individual site files to a common dir ~/programming/homd-work/NIH-VAMPS/v1v3
       Get file example_[date].tsv from 3-combine_sites.py
       ***Clean out num-[site] and pct-[site]  columns  BY HAND
       ***Also change col 2& 3 to num and pct NOT num-AKE
       run 
         3a-clean big file to add zeros and fill in num and pct column
           ../scripts/3a-clean_big_file.py -i example-v3v5.tsv   ==> zero filled
       NO calc abundance :
       NO  4-abundance_calculate_pctsNEW_add_species.py and add species
       NO     ../scripts/4-abundance_calculate_pctsNEW_add_species.py -i zeros_filled.tsv -r v3v5
       calc mean,max,sum and dscount:
 THIS SCRIPT  ==>      5a-percent_matrix.py* -i AKE_v1v3_NIH_sites_wcounts_2023-11-13_homd.csv -r v1v3 -s ake
           ./scripts/5a-percent_matrix.py -i v3v5_NIH_ALL_samples_wcounts_2023-11-09_homd.csv -r v3v5 -s AKE
           Removes zero sum rows
           
           ./scripts/5b-mean_relative_abundance.py -i AKE_v1v3_NIH_pct_matrix_2023-11-15_homd.csv -r v1v3 -s AKE
           
      
       
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=True,  action="store",   dest = "infile", default=False,
                                                    help="")
    
    # parser.add_argument("-host", "--host", required = False, action = 'store', dest = "dbhost", default = 'localhost',
#                                                    help="") 
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", default=False,
                                                    help="verbose print()") 
    parser.add_argument("-outfile", "--out_file", required = False, action = 'store', dest = "outfile", 
                default = 'pcts_for_JMW', help = "")
    
    parser.add_argument("-r", "--region", required = True, action = 'store', dest = "region", 
                         help = "['eren2014_v1v3','eren2014_v3v5','dewhirst_35x9']")
    parser.add_argument("-s", "--site", required = True, action = 'store', dest = "site", 
                         help = "")
    args = parser.parse_args()
    args.site = args.site.upper()
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
    
    if args.site not in site_names:
        sys.exit('site name not found '+args.site)
    if args.region not in ['v1v3','v3v5']:
        print(usage)
        sys.exit()
                            
   #  if args.dbhost == 'homd_dev':
#         args.DATABASE = 'homd'
#         dbhost= '192.168.1.46'
#         args.prettyprint = False
#     
#     elif args.dbhost == 'homd_prod':
#         args.DATABASE = 'homd'
#         dbhost= '192.168.1.42'
#         args.prettyprint = False
# 
#     elif args.dbhost == 'localhost':
#         #args.json_file_path = '/Users/avoorhis/programming/homd-data/json'
#         #args.TAX_DATABASE  = 'HOMD_taxonomy'
#         args.DATABASE = 'homd'
#         dbhost = 'localhost'
#         #dbhost_old = 'localhost'
#         
#     else:
#         sys.exit('dbhost - error')
    
    
#     myconn = MyConnection(host=dbhost, db=args.NEW_DATABASE,  read_default_file = "~/.my.cnf_node")
    if args.verbose:
        print()
    if not args.infile:
        print(usage)
        sys.exit()
    
    args.outfile = args.site+'_'+args.region+'_'+args.outfile +'_'+today+'_homd.csv'
    args.dsets = get_ds_totals(args)
    
    run(args)
