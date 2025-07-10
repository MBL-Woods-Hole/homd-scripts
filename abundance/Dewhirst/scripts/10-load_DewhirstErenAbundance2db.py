#!/usr/bin/env python

## SEE https://docs.dhtmlx.com/suite/tree__api__refs__tree.html // new version 7 must load from json file
# this script creates a list of json objects that allows the dhtmlx javascript library
# to parse and show a taxonomy tree (Written for HOMD)
##
import os, sys
import json
#from json import JSONEncoder
import argparse
import csv
sys.path.append('/home/ubuntu/homd-work/')
sys.path.append('/Users/avoorhis/programming/')
from connect import MyConnection
import datetime
ranks = ['domain','phylum','klass','order','family','genus','species','subspecies']
rankid_list = ['domain_id','phylum_id','klass_id','order_id','family_id','genus_id','species_id','subspecies_id']
today = str(datetime.date.today())
# nih_headers = [  # want to make them
# 'AKE_mean','AKE_90p','AKE_10p','AKE_sd','AKE_prev',
# 'ANA_mean','ANA_90p','ANA_10p','ANA_sd','ANA_prev',
# 'BMU_mean','BMU_90p','BMU_10p','BMU_sd','BMU_prev',
# 'HPA_mean','HPA_90p','HPA_10p','HPA_sd','HPA_prev',
# 'LAF_mean','LAF_90p','LAF_10p','LAF_sd','LAF_prev',
# 'LRC_mean','LRC_90p','LRC_10p','LRC_sd','LRC_prev',
# 'MVA_mean','MVA_90p','MVA_10p','MVA_sd','MVA_prev',
# 'PFO_mean','PFO_90p','PFO_10p','PFO_sd','PFO_prev',
# 'PTO_mean','PTO_90p','PTO_10p','PTO_sd','PTO_prev',
# 'RAF_mean','RAF_90p','RAF_10p','RAF_sd','RAF_prev',
# 'RRC_mean','RRC_90p','RRC_10p','RRC_sd','RRC_prev',
# 'SAL_mean','SAL_90p','SAL_10p','SAL_sd','SAL_prev',
# 'STO_mean','STO_90p','STO_10p','STO_sd','STO_prev',
# 'SUBP_mean','SUBP_90p','SUBP_10p','SUBP_sd','SUBP_prev',
# 'SUPP_mean','SUPP_90p','SUPP_10p','SUPP_sd','SUPP_prev',
# 'THR_mean','THR_90p','THR_10p','THR_sd','THR_prev',
# 'TDO_mean','TDO_90p','TDO_10p','TDO_sd','TDO_prev',
# 'VIN_mean','VIN_90p','VIN_10p','VIN_sd','VIN_prev'
# ]
# 	ANA	Old:NS
# 	AKE	Old:KG
# 	BMU	Old:BM
# 	HPA	Old:HP
# 	PTO	Old:PT
# 	SAL	Old:SV
# 	STO	Old:ST
# 	SUBPOld:SubP
# 	SUPPOld:SupP
# 	THR	Old:TH
# 	TDO	Old:TD
def get_otid_from_hmt(hmt):
    if hmt.startswith('HMT'):
        return str(int(hmt.split('-')[1]))  # strips zeros HMT-058 => 58
    else:
        return ''
def run_abundance_csv(args): 
    print(args.source)
    if args.source == 'eren_v1v3':
        check = 'Max'
        reference = 'Eren2014_v1v3'
        tmp = 'BMU-mean,BMU-10p,BMU-90p,BMU-sd,BMU-prev,AKE-mean,AKE-10p,AKE-90p,AKE-sd,AKE-prev,HPA-mean,HPA-10p,HPA-90p,HPA-sd,HPA-prev,TDO-mean,TDO-10p,TDO-90p,TDO-sd,TDO-prev,PTO-mean,PTO-10p,PTO-90p,PTO-sd,PTO-prev,THR-mean,THR-10p,THR-90p,THR-sd,THR-prev,SAL-mean,SAL-10p,SAL-90p,SAL-sd,SAL-prev,SUPP-mean,SUPP-10p,SUPP-90p,SUPP-sd,SUPP-prev,SUBP-mean,SUBP-10p,SUBP-90p,SUBP-sd,SUBP-prev,STO-mean,STO-10p,STO-90p,STO-sd,STO-prev'
    elif args.source == 'eren_v3v5':
        check = 'Max'
        reference = 'Eren2014_v3v5'
        tmp = 'BMU-mean,BMU-10p,BMU-90p,BMU-sd,BMU-prev,AKE-mean,AKE-10p,AKE-90p,AKE-sd,AKE-prev,HPA-mean,HPA-10p,HPA-90p,HPA-sd,HPA-prev,TDO-mean,TDO-10p,TDO-90p,TDO-sd,TDO-prev,PTO-mean,PTO-10p,PTO-90p,PTO-sd,PTO-prev,THR-mean,THR-10p,THR-90p,THR-sd,THR-prev,SAL-mean,SAL-10p,SAL-90p,SAL-sd,SAL-prev,SUPP-mean,SUPP-10p,SUPP-90p,SUPP-sd,SUPP-prev,SUBP-mean,SUBP-10p,SUBP-90p,SUBP-sd,SUBP-prev,STO-mean,STO-10p,STO-90p,STO-sd,STO-prev'
    elif args.source == 'dewhirst':
        #check = 'max Dewhirst oral site'
        check = 'Max'
        reference = 'Dewhirst35x9'
        tmp = 'BMU-mean,BMU-10p,BMU-90p,BMU-sd,BMU-prev,AKE-mean,AKE-10p,AKE-90p,AKE-sd,AKE-prev,HPA-mean,HPA-10p,HPA-90p,HPA-sd,HPA-prev,TDO-mean,TDO-10p,TDO-90p,TDO-sd,TDO-prev,PTO-mean,PTO-10p,PTO-90p,PTO-sd,PTO-prev,THR-mean,THR-10p,THR-90p,THR-sd,THR-prev,SAL-mean,SAL-10p,SAL-90p,SAL-sd,SAL-prev,SUPP-mean,SUPP-10p,SUPP-90p,SUPP-sd,SUPP-prev,SUBP-mean,SUBP-10p,SUBP-90p,SUBP-sd,SUBP-prev,ANA-mean,ANA-10p,ANA-90p,ANA-sd,ANA-prev'
    elif args.source in ['NIH_v1v3','NIH_v3v5']:
        # calulate max mead
        # new set of acronyms
        check = 'Max'
        l = [args.site+'-mean',args.site+'-10p',args.site+'-90p',args.site+'-sd',args.site+'-prev']
        tmp = ','.join(l)
        reference = args.source
        rank = 'species'
    
    else:
        sys.exit('no source found')
    
    rankid_list = ['domain_id','phylum_id','klass_id','order_id','family_id','genus_id','species_id','subspecies_id']
    active = tmp.split(',')
    #active = [n.replace('-','_') for n in active]
    
    print(active)
    
    with open(args.infile) as csv_file: 
        
        csv_reader = csv.DictReader(csv_file, delimiter='\t') # KK tab
        active_clean = [x.replace('-','_') for x in active]
        for row in csv_reader:
            values = []
            print(row)
            q = "INSERT IGNORE INTO `"+args.sqltable+"` (reference,otid,"+','.join(rankid_list)+",notes,`level`,`max`,`"+'`,`'.join(active_clean)+"`) VALUES "
            if not row[check]:
               continue
            
            for item in active:
                values.append(row[item])
            notes = ''
            try:  # segata has no notes
                if row['Notes']:
                    notes = row['Notes']
            except:
                pass
            print(row['Taxonomy'])
            id_list = get_id_list(row['Taxonomy'])
            print('id_list',id_list)
            #id_list = []
            calcmax = str(calculate_max(row,active))
            if id_list[-1] != '1':
                rank = 'subspecies'
                #print(id_list)
                #print('rank',row['Rank'],row)
            else:
                rank = row['Rank'].lower()
            otid = get_otid_from_hmt(row['HMT'])
            
            q = q + "('"+reference+"','"+otid+"','"+"','".join(id_list)+"','"+notes+"','"+rank+"','"+calcmax+"','"+"','".join(values)+"')"

            print(q)
            
    
            myconn.execute_no_fetch(q) 
            
def get_id_list(taxonomy):
    
    tax_items = taxonomy.split(';')
    id_list = []
    species = tax_items[-1]
    if 'subsp' in species or 'clade' in species:
        ## exception: species:  [Eubacterium] yurii subsp. schtitka
        last = species.split()
        if '[Eubacterium] yurii' in species:
            tax_items[-1] = last[0]+' '+last[1]
            tax_items.append(' '.join(last[2:]))
        else:
            
            tax_items[-1] = last[0]
            tax_items.append(' '.join(last[1:]))
        
    for i,name in enumerate(tax_items):
        rank = ranks[i]
        q = "SELECT "+rank+'_id FROM `'+rank+'` WHERE `'+rank+"`='"+name+"'"
        
        row = myconn.execute_fetch_one(q) 
        if myconn.cursor.rowcount == 0:
            print('ERROR-', q)
            print(taxonomy)
            sys.exit('\nExiting: no name found\n')
        else:
            id_list.append(str(row[0]))
    for i in range(8 - len(id_list)):
        id_list.append('1')   
    
    return id_list
        
def calculate_max(row, active):
    max = 0
    
    #sys.exit()
    for item in active:
        if item.endswith('mean') and float(row[item]) > max:
            max = float(row[item])
    #print('max',max)
    return max
    
    
    
        
if __name__ == "__main__":

    usage = """
    USAGE:
        takes the abundance data from 3 csv files to the database.
        HOMD-abundance-Segata.csv   => segata_edit2021-12-24.csv
        HOMD-abundance-Dewhirst.csv => dewhirst_edit2021-12-27.csv
        HOMD-abundance-Segata.csv   =>  eren2014_v1v3_MeanStdevPrev_byRankFINAL_2021-12-26_homd.csv
        
        No-No NIH EDIT: see notes.txt
        
        -s/--source ['eren_v1v3','eren_v3v5','dewhirst']
        
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=True,  action="store",   dest = "infile", default='none',
                                                    help=" ")
    parser.add_argument("-src", "--source",   required=True,  action="store",   dest = "source", 
                                    help="eren2014_v1v3 eren2014_v3v5 dewhirst segata ")
    parser.add_argument("-site", "--site",   required=False,  action="store",   dest = "site", default='NONE',
                                                   help=" ")
    parser.add_argument("-host", "--host",
                        required = False, action = 'store', dest = "dbhost", default = 'localhost',
                        help = "choices=['homd',  'localhost']")
    parser.add_argument("-pp", "--prettyprint",
                        required = False, action = 'store_true', dest = "prettyprint", default = False,
                        help = "output file is human friendly")
    parser.add_argument("-d", "--delimiter", required = False, action = 'store', dest = "delimiter", default = 'tab',
                         help = "Delimiter: commaAV[Default]: 'comma' or tabKK: 'tab'")
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", default=False,
                                                    help="verbose print()") 
    parser.add_argument("-t", "--sqltable",   required=False,  action="store",    dest = "sqltable", default='abundance_new',
                                                    help="verbose print()")
    args = parser.parse_args()
    if args.source not in ['eren_v1v3','eren_v3v5','dewhirst']:
        print(usage)
        sys.exit()
    
    #parser.print_help(usage)
    if args.dbhost == 'homd_v4':
        args.DATABASE = 'homd'
        dbhost= '192.168.1.46'
        args.prettyprint = False
    
    elif args.dbhost == 'homd_dev':
        args.DATABASE = 'homd'
        dbhost= '192.168.1.58'
        args.prettyprint = False

    elif args.dbhost == 'localhost':
        #args.json_file_path = '/Users/avoorhis/programming/homd-data/json'
        #args.TAX_DATABASE  = 'HOMD_taxonomy'
        args.DATABASE = 'homd'
        dbhost = 'localhost'
        #dbhost_old = 'localhost'
        
    else:
        sys.exit('dbhost - error')
    print('Using',args.dbhost,dbhost)
        
    
    #myconn_tax = MyConnection(host=dbhost_old, db=args.TAX_DATABASE,   read_default_file = "~/.my.cnf_node")
    myconn = MyConnection(host=dbhost, db=args.DATABASE,  read_default_file = "~/.my.cnf_node")
    
    
    run_abundance_csv(args)
   
    