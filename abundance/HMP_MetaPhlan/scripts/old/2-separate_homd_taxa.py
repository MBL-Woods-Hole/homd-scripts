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

sys.path.append('/Users/avoorhis/programming')
from connect import MyConnection,mysql
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

def get_otid_from_db(genus,species):
    #sql = "select domain,phylum,klass,`order`,family,genus,species,subspecies from otid_prime"
    sql = "select otid from otid_prime"
    #sql = "select domain,phylum,klass,`order`,family,genus,species from otid_prime"
    sql += " join taxonomy using(taxonomy_id)"
    # sql += " join domain using(domain_id)"
#     sql += " join phylum using(phylum_id)"
#     sql += " join klass using(klass_id)"
#     sql += " join `order` using(order_id)"
#     sql += " join family using(family_id)"
    sql += " join genus using(genus_id)"
    sql += " join species using(species_id)"
    sql += " join subspecies using(subspecies_id)"
    sql += " WHERE"
    sql += " genus='%s' and species='%s'" 
    q1 = sql % (genus, species)
    #print(q1)
    result = myconn.execute_fetch_select(q1)
    if result:
        #print('result',genus,species,result[0][0])
        return result[0][0]
    else:
        #print('NOresult',genus,species)
        return ''
    
def clean_hmt(s):
    
    #return str(int(s.split('-')[1]))  # strips zeros HMT-058 => 58
    pre = [str(int(x)) for x in s.split('-')[1:]]
    return '-'.join(pre)  # strips zeros HMT-275-283-284 => 275-283-284

def reform_hmt(s):
    return 'HMT-'+s.zfill(3)
    
def find_hmt(name):
    pts = name.split('_')
    
    if len(pts) == 2:
        otid = get_otid_from_db(pts[0],pts[1])
        return otid
    else:
        return ''
        
# def convert_ds_names(ds_list):
#     new_names = []
#     old_prefixes = site_conversion.keys()
#     for ds in ds_list:
#         for prefix in old_prefixes:
#             if prefix in ds:
#                 #new_name = ds.replace(prefix,site_conversion[prefix])
#                 new_name = ds+'-'+site_conversion[prefix]
#                 new_names.append(new_name)
#     print('oldname len',len(ds_list))
#     print('newname len',len(new_names))
#     return new_names
        
def run():  
    ds_start_at = 2  # first DS is G_ST_SRS011061_v1_hmp2
    #open 18 files
    
    fn1 = args.infile.split('.')[0]+'hmt_taxa.csv'
    fn2 = args.infile.split('.')[0]+'other_taxa.csv'
    out1 = open(fn1,'w')
    out2 = open(fn2,'w')
    mtx = open(args.infile,'r')
    master = {}
    taxa_hmts = {}
    for line in mtx:
        line = line.strip()
        line_pts = line.split('\t')
        #print(line_pts)
        if line_pts[0] == 'Taxon':
            
            header = line_pts
            #print(header)
            new_ds_names = header[ds_start_at:]
            
        else:  # data rows
            taxon = line_pts[0]
            hmt = line_pts[1]
            taxa_hmts[taxon] = hmt
            master[taxon] = line_pts[ds_start_at:]
            if taxon == 'z__Low_abundance':
                low_abund_row = line_pts[ds_start_at:]
    
    
    
    out1.write('Taxon\tHMT')
    out2.write('Taxon\tHMT')
    # row1 => write the sample name into the correct file
    for sample in new_ds_names:
        out1.write('\t'+sample)
        out2.write('\t'+sample)
    out1.write('\n')
    out2.write('\n')
    # other rows
    for taxon in master:
        #print(name)
        
        if taxa_hmts[taxon]:
            out1.write(taxon+'\t'+str(taxa_hmts[taxon]))
            for i,sample in enumerate(new_ds_names):
                out1.write('\t'+master[taxon][i])
            out1.write('\n')
        else:
            out2.write(taxon+'\t')
            for i,sample in enumerate(new_ds_names):
                out2.write('\t'+master[taxon][i])
            out2.write('\n')
        
    
        
                
    sys.exit()

if __name__ == "__main__":

    usage = """
    
         USAGE:
   Attached is the abundance matrix for the HMP data that Julian prepared from metagenomes using MetaPhlan.
It is already a percent matrix and there is already a category for low abundance, named 
z__Low_abundance for taxa that did not reach 0.01% in any sample.

      We can have a more relaxed criterion for low abundance, and add those additional low-abundance 
      taxa to the z__Low_abundance category.

The trick will be matching up the MetaPhlan taxonomy to the HOMD taxonomy.  

For a first pass, I think we can just match species names and have a category for "other taxa" 
into which we put everything that doesn't match.  

That works for species.  For genus, when we add up the abundance values for each genus, ideally 
we'd include the species names that matched to that genus, and also include the "[Genus name]_SGBxxxxx" 
(the "species genome bin".)

Ultimately, we will want to dig in to which genomes went into the bins, and see if we can match 
up taxa with weird names to their HOMD taxonomy.

There are variable numbers of samples available, ranging from 550 (stool) to 1 (hard palate).  
Actually ranging to zero, there are no samples from the left antecubital fossa.

Also there is data from 24 samples from periodontitis patients from a study by Califf et al.

The naming convention is:  in order, Stool, buccal mucosa, hard palate, keratinized gingiva, 
periodontitis, palatine tonsils, subgingival plaque, supragingival plaque, saliva, tongue dorsum, 
throat, anterior fossa right, anterior nares, retroauricular crease left, retroauricular crease right, 
mid-vagina, posterior fornix, vaginal introitus:
G_ST_SRS…
O_BM_SRS…
O_HP_SRS…
O_KG_SRS…
O_PERIO_Califf_...
O_PT_SRS…
O_SUBP_SRS…
O_SUPP_SRS..
O_SV_SRS…
O_TD_SRS…
O_TH_SRS…
S_AFR_SRS…
S_AN_SRS…
S_RCL_SRS…
S_RCR_SRS…
V_MV_SRS…
V_PF_SRS…
V_VI_SRS…    
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=True,  action="store",   dest = "infile", 
                                                   help=" ")
    #parser.add_argument("-outfile", "--out_file", required = False, action = 'store', dest = "outfile", 
    #            default = 'HMP_Meta_with_taxa', help = "")
    parser.add_argument("-low", "--low_abundance", required = False, action = 'store', dest = "low_abund", 
                default = '0.01', help = "")
    #parser.add_argument("-s", "--site",   required=True,  action="store",   dest = "site", 
    #                                               help=" ")
    #parser.add_argument("-r", "--region", required = True, action = 'store', dest = "region", 
    #                     help = "['eren2014_v1v3','eren2014_v3v5','dewhirst_35x9']")
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
    """
    The naming convention is:  in order, Stool, buccal mucosa, hard palate, keratinized gingiva, 
periodontitis, palatine tonsils, subgingival plaque, supragingival plaque, saliva, tongue dorsum, 
throat, anterior fossa right, anterior nares, retroauricular crease left, retroauricular crease right, 
mid-vagina, posterior fornix, vaginal introitus:
"""
    site_conversion = {
        'G_ST_SRS':'STO',
        'O_BM_SRS':'BMU',
        'O_HP_SRS':'HPA',
        'O_KG_SRS':'AKE',
        'O_PERIO_Califf_':'PERIO',
        'O_PT_SRS':'PTO',
        'O_SUBP_SRS':'SUBP',
        'O_SUPP_SRS':'SUPP',
        'O_SV_SRS':'SAL',
        'O_TD_SRS':'TDO',
        'O_TH_SRS':'THR',
        'S_AFR_SRS':'RAF',
        'S_AN_SRS':'ANA',
        'S_RCL_SRS':'LRC',
        'S_RCR_SRS':'RRC',
        'V_MV_SRS':'MVA',
        'V_PF_SRS':'PFO',
        'V_VI_SRS':'VIN'
    }
    dbhost = 'localhost'
    DATABASE = 'homd'
    myconn = MyConnection(host=dbhost, db=DATABASE,  read_default_file = "~/.my.cnf_node")
    #args.outfile = args.outfile +'_'+today+'.csv'
    
    run()
          
    
    

    
