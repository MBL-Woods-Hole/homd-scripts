#!/usr/bin/env python

## SEE https://docs.dhtmlx.com/suite/tree__api__refs__tree.html // new version 7 must load from json file
# this script creates a list of json objects that allows the dhtmlx javascript library
# to parse and show a taxonomy tree (Written for HOMD)
##
import os, sys
import gzip
import json
#from json import JSONEncoder
import argparse
import csv,re
import math
from Bio import SeqIO
sys.path.append('../homd-data/')
sys.path.append('../../homd-data/')
sys.path.append('../../../homd-data/')
#from connect import MyConnection,mysql
import datetime
import requests
global mysql_errors
mysql_errors = []
"""

"""
today = str(datetime.date.today())


#['_997', '995.2', '', '997', '1017', 'HOMD', 'HMT-997', 'Bacteria', 'Gracilibacteria_(GN02)', 'Gracilibacteria_(GN02)_[C-1]', 'Gracilibacteria_(GN02)_[O-1]', 'Gracilibacteria_(GN02)_[F-1]', 'Gracilibacteria_(GN02)_[G-4]', 'bacterium_HMT_997', 'NCBI', '363464', 'Bacteria', 'Candidatus Gracilibacteria', 'NA', 'NA', 'NA', 'NA', 'NA', '', '', 'NCBI', '363464', 'HMT-997', 'Bacteria', 'Candidatus Gracilibacteria (GN02)', 'Gracilibacteria_[C-1]', 'Gracilibacteria_[O-1]', 'Gracilibacteria_[F-1]', 'Gracilibacteria_[G-4]', 'bacterium_HMT_997', 'y']
ranks = ['domain','phylum','klass','order','family','genus','species']

skip_TM7 = True  # taxonomy only not for ncbi_taxon_id


def clean_hmt(s):
    
    #return str(int(s.split('-')[1]))  # strips zeros HMT-058 => 58
    pre = [str(int(x)) for x in s.split('-')[1:]]
    return '-'.join(pre)  # strips zeros HMT-275-283-284 => 275-283-284

def reform_hmt(s):
    return 'HMT-'+s.zfill(3)
    
    
def run():  
    ds_start_at = 3
    nfp = open(args.outfile,'w')
    mtx = open(args.mtx,'r')
    master = {}
    for line in mtx:
        line = line.strip()
        line_pts = line.split('\t')
        #print(line_pts)
        if line_pts[0] == 'HOT-ID':
            nfp.write(line + '\n')
            header = line_pts
            #print(header)
            datasets = header[ds_start_at:]
            #print(datasets)
            #ds_length = len(datasets)
        if line_pts[0].startswith('HMT') or line_pts[0].startswith('Unmatched'):
            counts_ary = line_pts[ds_start_at:]
            if line_pts[0].startswith('Unmatched'):
                master['Unmatched'] = [float(x) for x in counts_ary]
            else:
                # clean_hmt(line_pts[0]) ==== 675  or 564-893-543
                master[clean_hmt(line_pts[0])] = [float(x) for x in counts_ary]
    ordered_keys = list(master.keys())
    #ordered_keys.sort()
    #print(ordered_keys)
    singles = {}
    for hmt_plus in ordered_keys:
        hplus_pts = hmt_plus.split('-')
        if len(hplus_pts) == 1:
           singles[hmt_plus] = master[hmt_plus]
           
    for hmt_plus in ordered_keys:
        hplus_pts = hmt_plus.split('-')
        length = len(hplus_pts)
        if length > 1:
            #print()
            #print(hplus_pts)
            all_found = ''
            non_found = ''
            found_ct = []
            found = []
            for hmt in hplus_pts:
                
                if hmt in ordered_keys:
                    found_ct.append(hmt)
                    found.append(hmt)
                    pass
                else:
                    #print(hplus_pts)
                    #print('not found',hmt)
                    pass
            if len(found_ct) == length:
                #print('all found')
                all_found = True
                
            elif len(found_ct) == 0:
                #print('none Found')
                non_found = True
            else:
                #print('some found:',found_ct)
                #print(master[hmt_plus])
                pass
            #print('this is found list',found)
            if found:
                multiply_by = (100 / len(found) / 100)
                #print('multiply_by',multiply_by)
                
                for hmt in found:
                    
                    # to be split counts: master[hmt_plus]
                    # counts to be added to: singles[hmt]
                    #sum_list = 
                    #for i,ct in enumerate(master[hmt_plus]):
                    #print('sum cts',sum(master[hmt_plus]))
                    sum_add_to = sum(master[hmt_plus]) # skip if all zeros
                    if sum_add_to > 0:
                        for i in range(len(datasets)):
                            to_add = master[hmt_plus][i]  # should be ints
                            
                            if to_add:  # if not zero
                                add_to_each = to_add * multiply_by
                                #print('=>to_add * multiply_by:',to_add,'*',multiply_by)
                                #print('i type',type(singles[hmt][i]))
                                summed = math.ceil(singles[hmt][i] + add_to_each)  # rounds up
                                #print(hmt,'was',singles[hmt][i],'add_to_each',add_to_each,'after',summed)
                                
                                singles[hmt][i] = summed
                    #print(hmt,'skipping (no + counts)')
    for hmt in singles:
        str_row = [str(x) for x in singles[hmt]]
        if hmt != 'Unmatched':
            row = reform_hmt(hmt)+'\t1\t100\t'+'\t'.join(str_row)
        else:
            row = hmt+'\t1\t100\t'+'\t'.join(str_row)
        nfp.write(row+'\n')
    nfp.close()
        
    #print(singles)
    
    
    


     
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
          ALSO Removes zero rows
           ../../../scripts/3a-clean_big_file.py -i AKE_species_otu_table.PRELIM.gt1000ct.V1V3.sep.tsv -s ake -r v1v3
       split up multiple taxa:  line HMT-099-609-682-764
         Plan if all present 99,609,682,764 individually then devide count equally, but if some are absent
         then don't add it and divide
THIS SCRIPT  ==>       3b-separate_multiples.py -i AKE_species_otu_table.PRELIM.gt1000ct.V1V3.sep.tsv -s ake -r v1v3
           out: *split_counts*
       calc abundance :
         4-abundance_calculate_pctsNEW_add_species.py and add species 
           ../scripts/4-abundance_calculate_pctsNEW_add_species.py -i zeros_filled.tsv -r v3v5
       calc mean,max,sum and dscount:
         5-abundance_mean_max.py*  
           ./scripts/5-abundance_mean_max.py -i v3v5_NIH_ALL_samples_wpcts_2023-11-09_homd.csv -r v3v5
       --source must be in ['eren2014_v1v3','eren2014_v3v5','dewhirst_35x9']
           
         
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=True,  action="store",   dest = "mtx", 
                                                   help=" ")
    parser.add_argument("-outfile", "--out_file", required = False, action = 'store', dest = "outfile", 
                default = 'NIH_split_counts', help = "")
    parser.add_argument("-s", "--site",   required=True,  action="store",   dest = "site", 
                                                   help=" ")
    parser.add_argument("-r", "--region", required = True, action = 'store', dest = "region", 
                         help = "['eren2014_v1v3','eren2014_v3v5','dewhirst_35x9']")
    args = parser.parse_args()
    
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
    args.site = args.site.upper()
    if args.site not in site_names:
        sys.exit('site name not found',args.site)
    if args.region not in ['v1v3','v3v5']:
        print(usage)
        sys.exit()
    args.outfile = args.site+'_'+args.region+'_'+args.outfile +'_'+today+'.csv'
    
    run()
        
    
    # elif args.synonyms:
#         run_synonyms()
#     elif args.taxid:
#         run_taxon_id()
#     elif args.sspecies:
#         run_subspecies()
#     
    if not args:
       print('no def selected')
       print(usage)
    

    
