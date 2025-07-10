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
sys.path.append('/Users/avoorhis/programming/')
sys.path.append('/Users/avoorhis/programming/homd-data/')
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


def get_hots(hot_filename):
    hot_collector = {}
    fp = open(hot_filename,'r')
    for line in fp:
        line = line.strip().strip(';')
        
        pts = line.split('\t')
        hot = str(int(line[:3]))
        tax = pts[1]
        tax_pts = tax.split(';')
        
        if hot in hot_collector and tax != hot_collector[hot]["fulltax"]:
            print('Bad dupe',line,hot_collector[hot])
            sys.exit()
        #species
        hot_collector[tax] = {"hmt":hot}
        if len(tax_pts) != 7:
            print('ERROR XX',tax) 
        hot_collector[tax]["genus"]=tax_pts[-2]
        
        if ' ' in tax_pts[-1]:
            hot_collector[tax]["species"]=tax_pts[-1].split(' ')[1]
        else:
            hot_collector[tax]["species"]=tax_pts[-1]
    
    return hot_collector
    
def run():  
    
    mtx = open(args.mtx,'r')
    
    
    foutClean = open(args.outfile,'w')
    
    # check for zero sum datasets
    
    master = {}
    nov_collector = {}
    multi_tax_collector = {}
    for line in mtx:
        line = line.strip()
        line_pts = line.split('\t')
        
        if line_pts[0] == '#OTU ID':
            header = line_pts[1:]
            foutClean.write('Tax\tHOT-ID\tSPPid\tNum\tNote\t'+'\t'.join(header)+'\n')
            for ds in header:
                nov_collector[ds] = 0.0
        if 'Bacteria' in line_pts[0] or line_pts[0].startswith('Archaea'):
            mtx_old_tax_pts = line_pts[0].split(';')
            counts_ary = line_pts[1:]
            
            if '_nov_' in mtx_old_tax_pts[6]:  # or mtx_old_tax_pts[6] == 'sp._genotype_4':#  LAF
                for i,ds in enumerate(header):
                    nov_collector[ds] += float(counts_ary[i])
            elif mtx_old_tax_pts[6].startswith('multispecies'):
                
                sp_pts = mtx_old_tax_pts[-1].split(' ')
                mtx_old_tax_pts[-1] = sp_pts[0]
                msid = sp_pts[1].strip('(').strip(')')
                if msid in multi_tax_collector:
                    sys.exit('msid error')
                multi_tax_collector[msid] = {}
                #print('mtx_old_tax_pts',mtx_old_tax_pts,msid)
                if msid in multi_file_collector:
                   #print('multi_file_collector',multi_file_collector[msid],msid)
                   split_by = len(multi_file_collector[msid]['taxa'])
                   cts = []
                   for i,ds in enumerate(header):
                       cts.append(str(float(counts_ary[i])/split_by))
                   for tax in multi_file_collector[msid]['taxa']:
                       if tax not in args.hot_conversion:
                          sys.exit('hot_conversion Error1')
                       hmt = args.hot_conversion[tax]['hmt']
                       #multi_tax_collector[msid][tax] = {'cts':cts,'hmt':hmt,'msid':msid,'num',split_by,'note':note}
                       note='Split evenly: group of '+str(split_by)
                       foutClean.write(tax+'\t'+hmt+'\t'+msid+'\t'+str(split_by)+'\t'+note+'\t'+'\t'.join(cts)+'\n')
                else:
                   sys.exit('no msid in multifile')
                
            else:
                mtx_old_tax_pts[-1] = mtx_old_tax_pts[-1].split(' ')[0]
                #print(mtx_old_tax_pts)
                tax = ';'.join(mtx_old_tax_pts)
                if tax not in args.hot_conversion:
                    print('HMT not found',tax)
                    hmt = 'Unknown'
                else:
                    hmt = args.hot_conversion[tax]['hmt']
                #for hmt in 
                note = ''
                foutClean.write(tax+'\t'+hmt+'\t1\t100\t'+note+'\t'+'\t'.join(counts_ary)+'\n')
   
    
    foutClean.write('Unmatched\tUnmatched\tUnmatched\tUnmatched\t\t')
    nov_counts = []
    for ds in header:
        nov_counts.append(str(nov_collector[ds]))
    
    foutClean.write('\t'.join(nov_counts)+'\n')
    

    
if __name__ == "__main__":

    usage = """
    USAGE:
        
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=True,  action="store",   dest = "mtx", 
                                                   help=" ")
    #parser.add_argument("-s", "--site",   required=True,  action="store",   dest = "site", 
    #                                               help=" ")
    parser.add_argument("-host", "--host",
                        required = False, action = 'store', dest = "dbhost", default = 'localhost',
                        help = "choices=['homd',  'localhost']")
    args = parser.parse_args()
    if args.dbhost == 'homd_dev':
        args.DATABASE = 'homd'
        dbhost = '192.168.1.46'
        args.prettyprint = False
    
    elif args.dbhost == 'homd_prod':
        args.DATABASE = 'homd'
        dbhost = '192.168.1.42'
        args.prettyprint = False

    elif args.dbhost == 'localhost':
        #args.json_file_path = '/Users/avoorhis/programming/homd-data/json'
        #args.TAX_DATABASE  = 'HOMD_taxonomy'
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
    
    ifpts = args.mtx.split('_')
    args.site = ifpts[0]
    args.site = args.site.upper()
    args.region = ifpts[1]
    args.outfile = '_'.join([args.site,args.region,'sep_multiples',today+'.csv'])
    
    
    if args.site not in site_names:
        sys.exit('site name not found',args.site)
                        
    multi_file = args.site+'_spp_spids_all_tax.txt'
    args.hot_conversion = get_hots('../ref.taxonomy')
    mfp = open(multi_file,'r')
    multi_file_collector = {}
    for line in mfp:
        line = line.strip()
        line_pts = line.split('\t')
        ct = len(line_pts[1].split(';'))
        msid = line_pts[0].strip()
        
        multi_file_collector[msid] = {'ct':ct,'ids':line_pts[1],'taxa':line_pts[2:]}
    #singles_file = '../spid_taxonomy_single.txt'
    mfp.close()
    # sfp = open(singles_file,'r')
#     single_file_collector = {}
#     for line in sfp:
#         line = line.strip()
#         line_pts = line.split('\t')
#         single_file_collector[line_pts[0]] = {'taxa':line_pts[1]}
#     sfp.close()
    
    #myconn = MyConnection(host=dbhost, db=args.DATABASE,  read_default_file = "~/.my.cnf_node")
    
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
    

    
