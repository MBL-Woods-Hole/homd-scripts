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
#from connect import MyConnection,mysql
import datetime
import requests
global mysql_errors
mysql_errors = []
"""

"""
today = str(datetime.date.today())


ranks = ['domain','phylum','klass','order','family','genus','species']


def get_otid_from_db(genus,species):
    sql = "select otid,domain,phylum,klass,`order`,family,genus,species,subspecies from otid_prime"
    #sql = "select otid from otid_prime"
    #sql = "select domain,phylum,klass,`order`,family,genus,species from otid_prime"
    sql += " join taxonomy using(taxonomy_id)"
    sql += " join domain using(domain_id)"
    sql += " join phylum using(phylum_id)"
    sql += " join klass using(klass_id)"
    sql += " join `order` using(order_id)"
    sql += " join family using(family_id)"
    sql += " join genus using(genus_id)"
    sql += " join species using(species_id)"
    sql += " join subspecies using(subspecies_id)"
    sql += " WHERE"
    sql += " genus='%s' and species='%s'" 
    sql += " and status !='dropped'"
    q1 = sql % (genus, species)
    #print(q1)
    result = myconn.execute_fetch_select(q1)
    if result:
        #print('result',genus,species,result[0][0])
        return result
    else:
        #print('NOresult',genus,species)
        return ''

def find_genus_in_homd(genus):
    sql = "select domain,phylum,klass,`order`,family,genus from otid_prime"
    #sql = "select genus from otid_prime"
    #sql = "select domain,phylum,klass,`order`,family,genus,species from otid_prime"
    sql += " join taxonomy using(taxonomy_id)"
    sql += " join domain using(domain_id)"
    sql += " join phylum using(phylum_id)"
    sql += " join klass using(klass_id)"
    sql += " join `order` using(order_id)"
    sql += " join family using(family_id)"
    sql += " join genus using(genus_id)"
    #sql += " join species using(species_id)"
    #sql += " join subspecies using(subspecies_id)"
    sql += " WHERE"
    sql += " genus='%s'" 
    sql += " and status !='dropped'" 
    q1 = sql % (genus)
    #print(q1)
    result = myconn.execute_fetch_select(q1)
    if result:
        #print('result',genus,species,result[0][0])
        return result[0]
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
        ## if subsp may result in 2 rows
        result = get_otid_from_db(pts[0],pts[1])
        #print('get_otid_from_db',result)
        return result  # (882, 'Bacteria', 'Bacillota', 'Bacilli', 'Lactobacillales', 'Lactobacillaceae', 'Limosilactobacillus', 'panis', '')
    else:
        return ''
        
def convert_ds_names(ds_list):
    new_names = []
    old_prefixes = site_conversion.keys()
    for ds in ds_list:
        for prefix in old_prefixes:
            if prefix in ds:
                #new_name = ds.replace(prefix,site_conversion[prefix])
                new_name = ds+'-'+site_conversion[prefix]
                new_names.append(new_name)
    print('oldname sample len',len(ds_list))
    print('newname sample len',len(new_names))
    return new_names
    
def add_row_by_cell(list1, list2):
    new_list = []
    if len(list1) != len(list2):
        sys.exit('list length difference')
    for i in range(0, len(list1)): 
        new_list.append(float(list1[i]) + float(list2[i])) 
    return new_list
            
def run():  
    outfiles = {
    'rows_wHOTs': 'HMProws_wHOTs_'+today+'.csv',
    'rows_wGenus_in_homd' : 'HMProws_wGenus_in_homd_'+today+'.csv',
    'rows_wGenus_not_in_homd' : 'HMProws_wGenus_not_in_homd_'+today+'.csv',
    'rows_other_low_abund' : 'HMProws_other_'+today+'.csv'   # low 
    }
    ds_start_at = 6  # first DS is S700014982-AKE
    taxlookup = {}
    otidlookup = {}
    #open 18 files
    # file_pointers = {}
#     for item in outfiles:
#         
#         fnp = open(outfiles[item],'w')
#         file_pointers[item] = fnp
    print('args.outfile',args.outfile)
    print('args.infile',args.infile)
    outfilep = open(args.outfile,'w')
    mtx = open(args.infile,'r')
    rowcount = 0
    for line in mtx:
        master = {}
        line = line.strip()
        row = line.split('\t')
        #csv_reader = csv.DictReader(csv_file, delimiter='\t') # 
        if rowcount==0:
            samples_list = row[5:]
        else:
            taxonomy = row.pop(0)
            otid = row.pop(0)
            msid = row.pop(0)
            divby = row.pop(0)
            note = row.pop(0)
            #print('row',row)
            #Tax	HOT-ID	SPPid	Num	Note
            if taxonomy in taxlookup:
                    taxlookup[taxonomy] = add_row_by_cell(taxlookup[taxonomy], row)
            else:
                    taxlookup[taxonomy] = row
            otidlookup[taxonomy] = otid
            
        rowcount+=1
    outfilep.write('HOMDTaxString\tHMT\tlevel\tNotes')
    for sample in samples_list:
        outfilep.write('\t'+sample)
    outfilep.write('\n')
    
    for tax in taxlookup:
        level = ''
        if not tax.startswith('Unmatched'):
            level = ranks[len(tax.split(';'))-1]
        
        outfilep.write(tax+'\t'+otidlookup[tax]+'\t'+level+'\t')
        for i,sample in enumerate(samples_list):
            outfilep.write('\t'+str(taxlookup[tax][i]))
        outfilep.write('\n')
       
    
    

if __name__ == "__main__":

    usage = """
    
         USAGE:
  


    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=True,  action="store",   dest = "infile", 
                                                   help=" ")
    parser.add_argument("-outfile", "--out_file", required = False, action = 'store', dest = "outfile", 
                default = 'hmpRefSeq_Unique_taxstrings', help = "")
    #parser.add_argument("-low", "--low_abundance", required = False, action = 'store', dest = "low_abund", 
    #            default = '0.01', help = "")  
    #parser.add_argument("-t", "--taxa_only", required = False, action = 'store_true', dest = "taxa_only", 
    #            default = False, help = "")
    #parser.add_argument("-s", "--site",   required=True,  action="store",   dest = "site",  help=" ")
    #parser.add_argument("-r", "--region", required = True, action = 'store', dest = "region",  help = "")
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
    ifpts = args.infile.split('_')
    args.site = ifpts[0]
    args.site = args.site.upper()
    args.region = ifpts[1]
    args.outfile = '_'.join([args.site,args.region,args.outfile,today+'.csv'])
    
    
    args.site = args.site.upper()
    if args.site not in site_names:
        sys.exit('site name not found',args.site)
   
    
    #dbhost = 'localhost'
    #DATABASE = 'homd'
    #myconn = MyConnection(host=dbhost, db=DATABASE,  read_default_file = "~/.my.cnf_node")
    
    
    run()
          
    
    

    
