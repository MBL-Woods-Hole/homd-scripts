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
    

    
def run():  
    
    mtx = open(args.mtx,'r')
    # check for zero sum datasets
    master = {}
    for line in mtx:
        line = line.strip()
        line_pts = line.split('\t')
        if line_pts[0] == '#OTU ID':
            header = line_pts[1:]
            for ds in header:
                master[ds] = 0  
        if 'Bacteria' in line_pts[0] or line_pts[0].startswith('Archaea'):
            mtx_old_tax_pts = line_pts[0].split(';')
            
            counts_ary = line_pts[1:]
            
            #print('goodtax',mtx_old_tax_pts)
            for i,ds in enumerate(header):
                master[ds] = master[ds] + float(counts_ary[i])
            
 
    
    mtx = open(args.mtx,'r')
    count = 0
    # content_collector1 = {}
#     content_collector2 = {}
#     content_collector3 = {}
#     content_collector4 = {}
#     content_collector5 = []
    fname_base = '.'.join(args.mtx.split('.')[:-1])  #remove '.mtx'
    fname_base = fname_base.split('/')[-1]  #remove 'path'
    outfilev1_v3 = args.site+'_v1v3_'+fname_base+'.tsv'
    outfilev3_v5 = args.site+'_v3v5_'+fname_base+'.tsv'
    outfileother = args.site+'_Vother_'+fname_base+'.tsv'
    statsfile = 'stats.'+args.site+'.txt'
    foutv1_v3 = open(outfilev1_v3,'w')
    foutv3_v5 = open(outfilev3_v5,'w')
    foutother = open(outfileother,'w')
    foutstats = open(statsfile,'a')
    headerv1_v3 = []
    countsv1_v3 = []
    
    headerv3_v5 = []
    countsv3_v5 = []
    
    headerother =[]
    countsother = []
    for line in mtx:
        line = line.strip()
        line_pts = line.split('\t')
        if line_pts[0] == '#OTU ID':
            header = line_pts[1:]
        
            for i,ds in enumerate(header):
                if ds[-5:] == 'V1-V3':
                     # remove V1-V3 and add args.site
                     headerv1_v3.append(ds[:-5]+'-'+args.site)
                elif  ds[-5:] == 'V3-V5':
                    headerv3_v5.append(ds[:-5]+'-'+args.site)
                else:
                    headerother.append(ds[:-5]+'-'+args.site)
            foutv1_v3.write("#OTU ID"+'\t'+'\t'.join(headerv1_v3)+'\n')
            foutv3_v5.write("#OTU ID"+'\t'+'\t'.join(headerv3_v5)+'\n')
            foutother.write("#OTU ID"+'\t'+'\t'.join(headerother)+'\n')
        line = line.strip()
        line_pts = line.split('\t')
        if line_pts[0] == '#OTU ID':
            header = line_pts[1:]
        #print(line_pts[0])
        if 'Bacteria' in line_pts[0] or line_pts[0].startswith('Archaea'):
            
            counts_ary = line_pts[1:]
            clean_tax = line_pts[0]
            
           
            count += 1
            
            countsv1_v3 = []
            countsv3_v5 = []
            countsother = []
            for i,ds in enumerate(header):
                if ds[-5:] == 'V1-V3':
                    countsv1_v3.append(counts_ary[i])
                    
                elif ds[-5:] == 'V3-V5':
                    countsv3_v5.append(counts_ary[i])
                else:
                    countsother.append(counts_ary[i])
            foutv1_v3.write(clean_tax+'\t'+'\t'.join(countsv1_v3)+'\n')
            foutv3_v5.write(clean_tax+'\t'+'\t'.join(countsv3_v5)+'\n')
            foutother.write(clean_tax+'\t'+'\t'.join(countsother)+'\n')
    
    foutstats.write('v1v3 dataset count: '+str(len(countsv1_v3))+'\n')
    foutstats.write('v3v5 dataset count: '+str(len(countsv3_v5))+'\n')
    foutstats.write('v6v9 dataset count: '+str(len(countsother))+'\n')
    foutv1_v3.close()
    foutv3_v5.close()
    foutother.close()


     
if __name__ == "__main__":

    usage = """
    USAGE:   HMP 16S RefSeq
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
          
THIS SCRIPT  ==>        1a-separate_v1v3_v3v5.py
       2-separate_multispecies_taxa.py
       Next:
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
       --source must be in ['eren2014_v1v3','eren2014_v3v5','dewhirst_35x
         
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=True,  action="store",   dest = "mtx", 
                                                   help=" ")
    #parser.add_argument("-s", "--site",   required=True,  action="store",   dest = "site", 
    #                                               help=" ")
    parser.add_argument("-d", "--delete",   required=False,  action="store",   dest = "min_count_threshold", default=1000,
                                                    help=" ")
    args = parser.parse_args()
    
    #parser.print_help(usage)
                        
   
    
    
   # myconn = MyConnection(host=dbhost, db=args.DATABASE,  read_default_file = "~/.my.cnf_node")
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
    'SUBP',  #Subgingival_plaque
    'SUPP',  #Supragingival_plaque
    'THR',  #Throat
    'TDO',  #Tongue_dorsum
    'VIN'  #Vaginal_introitus
    ]
    ifpts = args.mtx.split('_')
    args.site = ifpts[0]
    args.site = args.site.upper()
    #args.outfile = '_'.join([args.site,args.region,'sep_multiples',today+'.csv'])
    
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
    

    
