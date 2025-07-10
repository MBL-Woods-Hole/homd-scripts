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
new_fi = {
   "hmt":27,  # AB
   "nd": 28,  # AC
   "np": 29,
   "nk": 30,
   "no": 31,
   "nf": 32,
   "ng": 33,
   "ns": 34,
   "taxid":26 #AA
}

old_fi = {  #orange
    "nd": 7,  # H
   "np": 8,
   "nk": 9,
   "no": 10,
   "nf": 11,
   "ng": 12,
   "ns": 13
}
hmts_with_ssp =[  # 19 of them
'411','431',
'578',
'638',
'721',
'818',
'886',
'938',
'58','398','707','106','70','71','377',
'420','698','202','200'   # 4Fusobacterium
]
skip_TM7 = True  # taxonomy only not for ncbi_taxon_id
new_phyla = {
'Proteobacteria':'Pseudomonadota',
'Firmicutes':'Bacillota',
'Actinobacteria':'Actinomycetota',
'Spirochaetes':'Spirochaetota',
'Fusobacteria':'Fusobacteriota',
'Bacteroidetes':'Bacteroidota',
'Cyanobacteria':'Cyanobacteriota',
'Absconditabacteria_(SR1)':'Candidatus_Absconditabacteria',
'Saccharibacteria_(TM7)':'Candidatus_Saccharibacteria',
'Synergistetes':'Synergistota',
'Chloroflexi':'Chloroflexota',
'Chlamydiae':'Chlamydiota',
'Euryarchaeota':'Euryarchaeota',
'Gracilibacteria_(GN02)':'Candidatus_Gracilibacteria',
'Chlorobi':'Chlorobiota',
'WPS-2':'Candidatus_Eremiobacterota',
'Tenericutes':'Mycoplasmatota',
'Ignavibacteriae':'Ignavibacteriota',
'Lentisphaerae':'Lentisphaerae'
}

def clean_hmt(s):
    
    return str(int(s.split('-')[1]))  # strips zeros HMT-058 => 58
    
def clean_up_taxonomy(tax):
    #print('tax',tax)
    pts = tax.split(';')
    clean_tax = [x.split('__')[1] for x in pts]
    if len(clean_tax) != 7:
        sys.exit('bad clean '+';'.join(clean_tax))
    #clean_tax[-1] = clean_tax[-1].split(' ')[0]
    return clean_tax
    
def run():  
    
    mtx = open(args.mtx,'r')
    # check for zero sum datasets
    master_ds_collector = {}
    master_tax_collector = {}
    for line in mtx:
        line = line.strip()
        line_pts = line.split('\t')
        if line_pts[0] == '#OTU ID':
            header = line_pts[1:]
            for ds in header:
                master_ds_collector[ds] = 0  
        if line_pts[0].startswith('k__Bacteria') or line_pts[0].startswith('k__Archaea'):
            counts_ary = line_pts[1:]
            # wait til after split v1v3 from v3v5 to remove zero sum rows
            #sumcounts = sum([float(x) for x in counts_ary])
            #print('sum',sum([float(x) for x in counts_ary]))
            
            #print(line_pts[0])
            clean_tax_ary = clean_up_taxonomy(line_pts[0])
            #print(clean_tax_ary)
            
            #if sumcounts > 0:
            master_tax_collector[';'.join(clean_tax_ary)] = counts_ary
            #print('goodtax',mtx_old_tax_pts)
            for i,ds in enumerate(header):
                master_ds_collector[ds] += float(counts_ary[i])
            
    
    ds_no_low_counts = []
    indecies = []
    num_low_ds_removed = 0
    for i,ds in enumerate(master_ds_collector):
        index = i
        if int(master_ds_collector[ds]) >= int(args.min_count_threshold):
            ds_no_low_counts.append({"ds":ds,"index":i})
            indecies.append(i)
        else:
            num_low_ds_removed += 1
    print('ds count',len(ds_no_low_counts))
    print('ds removed ',num_low_ds_removed)
    #mtx.close()
    fname_base = '.'.join(args.mtx.split('.')[:-1])  #remove '.mtx'
    fname_base = fname_base.split('/')[-1]  #remove 'path'
    outfile = fname_base+'.PRELIM.gt'+str(args.min_count_threshold)+'ct.tsv'
    fout = open(outfile,'w')
    statsfile = 'stats.'+args.site+'.txt'
    foutstats = open(statsfile,'w')
    foutstats.write('Datasets removed for low counts: '+str(num_low_ds_removed)+'\n')
    #txt =  "# Excludes 'multi' and '_nov_' in taxa\n# Also checks for zero sum datasets and taxa\n"
    fout.write('# Created by remove_small_datasets.py :: '+" ".join(sys.argv)+'\n')
    
    #fout.write(txt)
    fout.write('#OTU ID')
    for obj in ds_no_low_counts:
        ds = obj["ds"]
        fout.write('\t'+ds)
    fout.write('\n')
    for tax in master_tax_collector: # all rows
        full_counts = master_tax_collector[tax]
        fout.write(tax)
        for idx in indecies:
            fout.write('\t'+str(float(full_counts[idx])))
        fout.write('\n')
    print('Write File:',outfile)


     
if __name__ == "__main__":

    usage = """
    USAGE:
        In each site directory:
THIS SCRIPT  ==>         ./1-clean_data_step1.py -i AKE_species_count_table.tsv
          
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
    parser.add_argument("-d", "--delete",   required=False,  action="store",   dest = "min_count_threshold", default=1000,
                                                    help=" ")
    parser.add_argument("-s", "--site",   required=True,  action="store",   dest = "site", 
                                                   help=" ")
    args = parser.parse_args()
    
    #parser.print_help(usage)
                        
   
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
    

    
