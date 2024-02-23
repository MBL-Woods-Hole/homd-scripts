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
sys.path.append('../../homd-data/')
from connect import MyConnection
import datetime
ranks = ['domain','phylum','klass','order','family','genus','species','subspecies']
today = str(datetime.date.today())



def run_abundance_csv(args): 
    print(args.source)
    if args.source == 'eren2014_v1v3':
        check = 'Max'
        reference = 'Eren2014_v1v3'
        tmp = 'BM-mean,BM-10p,BM-90p,BM-sd,BM-prev,KG-mean,KG-10p,KG-90p,KG-sd,KG-prev,HP-mean,HP-10p,HP-90p,HP-sd,HP-prev,TD-mean,TD-10p,TD-90p,TD-sd,TD-prev,PT-mean,PT-10p,PT-90p,PT-sd,PT-prev,TH-mean,TH-10p,TH-90p,TH-sd,TH-prev,SV-mean,SV-10p,SV-90p,SV-sd,SV-prev,SUPP-mean,SUPP-10p,SUPP-90p,SUPP-sd,SUPP-prev,SUBP-mean,SUBP-10p,SUBP-90p,SUBP-sd,SUBP-prev,ST-mean,ST-10p,ST-90p,ST-sd,ST-prev'
    elif args.source == 'eren2014_v3v5':
        check = 'Max'
        reference = 'Eren2014_v3v5'
        tmp = 'BM-mean,BM-10p,BM-90p,BM-sd,BM-prev,KG-mean,KG-10p,KG-90p,KG-sd,KG-prev,HP-mean,HP-10p,HP-90p,HP-sd,HP-prev,TD-mean,TD-10p,TD-90p,TD-sd,TD-prev,PT-mean,PT-10p,PT-90p,PT-sd,PT-prev,TH-mean,TH-10p,TH-90p,TH-sd,TH-prev,SV-mean,SV-10p,SV-90p,SV-sd,SV-prev,SUPP-mean,SUPP-10p,SUPP-90p,SUPP-sd,SUPP-prev,SUBP-mean,SUBP-10p,SUBP-90p,SUBP-sd,SUBP-prev,ST-mean,ST-10p,ST-90p,ST-sd,ST-prev'
    elif args.source == 'segata':
        check = 'Max'
        reference = 'Segata2012'
        tmp = 'BM-mean,BM-sd,KG-mean,KG-sd,HP-mean,HP-sd,TH-mean,TH-sd,PT-mean,PT-sd,TD-mean,TD-sd,SV-mean,SV-sd,SUPP-mean,SUPP-sd,SUBP-mean,SUBP-sd,ST-mean,ST-sd'
    elif args.source == 'dewhirst':
        #check = 'max Dewhirst oral site'
        check = 'Max'
        reference = 'Dewhirst35x9'
        tmp = 'BM-mean,BM-10p,BM-90p,BM-sd,BM-prev,KG-mean,KG-10p,KG-90p,KG-sd,KG-prev,HP-mean,HP-10p,HP-90p,HP-sd,HP-prev,TD-mean,TD-10p,TD-90p,TD-sd,TD-prev,PT-mean,PT-10p,PT-90p,PT-sd,PT-prev,TH-mean,TH-10p,TH-90p,TH-sd,TH-prev,SV-mean,SV-10p,SV-90p,SV-sd,SV-prev,SUPP-mean,SUPP-10p,SUPP-90p,SUPP-sd,SUPP-prev,SUBP-mean,SUBP-10p,SUBP-90p,SUBP-sd,SUBP-prev,NS-mean,NS-10p,NS-90p,NS-sd,NS-prev'
    else:
        sys.exit('no source found')
    rankid_list = ['domain_id','phylum_id','klass_id','order_id','family_id','genus_id','species_id','subspecies_id']
    active = tmp.split(',')
    active = [n.replace('-','_') for n in active]
    print(active)
    
    with open(args.infile) as csv_file: 
        
        csv_reader = csv.DictReader(csv_file, delimiter='\t') # KK tab
        
        for row in csv_reader:
            values = []
            q = "INSERT IGNORE INTO `abundance_tax_ranked` (reference,otid,UPDATEDTaxonomy,tax_rank_id,"+','.join(rankid_list)+",notes,`rank`,`max`,`"+'`,`'.join(active)+"`) VALUES "
            if not row[check]:
               continue
            
            for item in active:
                values.append(row[item.replace('_','-')])
            notes = ''
            try:  # segata has no notes
                if row['Notes']:
                    notes = row['Notes']
            except:
                pass
            id_list = get_id_list(row['Taxonomy'])
            #id_list = []
            calcmax = str(calculate_max(row,active))
            if id_list[-1] != '1':
                rank = 'subspecies'
                #print(id_list)
                #print('rank',row['Rank'],row)
            else:
                rank = row['Rank'].lower()
            #ranked_id = get_ranked_id(rank, id_list)
            ranked_id=''
            taxonomy = row['Taxonomy']
            if taxonomy in args.tax_ids:
                ranked_id = args.tax_ids[row['Taxonomy']]
            q = q + "('"+reference+"','"+row['HMT']+"','"+taxonomy+"','"+ranked_id+"','"+"','".join(id_list)+"','"+notes+"','"+rank+"','"+calcmax+"','"+"','".join(values)+"')"

            print(q)
            
    
            myconn.execute_no_fetch(q) 
            
def get_ranked_id(rank, lst):
    print(rank,lst)
    follow=[]
    for n,id in enumerate(lst):
        follow.append(ranks[n]+"_id='"+str(id)+"'")
    q = "SELECT tax_rank_id from `taxonomy_ranked_clean` WHERE "+ ' and '.join(follow)
    print(q)
    row = myconn.execute_fetch_select(q) 
    print('row',row)
    
    return row[0][0]
    
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
    for item in active:
        if item.endswith('mean') and float(row[item.replace('_','-')]) > max:
            max = float(row[item.replace('_','-')])
    return max
    
def get_taxid_obj():
    collect = {}
    q = "SELECT tax_rank_id,tax_string from taxonomy_ranked_clean"
    result = myconn.execute_fetch_select(q)
    for row in result:
        
        collect[str(row[1])] = str(row[0])
    return collect
        
if __name__ == "__main__":

    usage = """
    USAGE:
        ./10a-load_abundance_ranked.py -i ../abundance-erenv1v3/eren2014_v1v3_MeanStdevPrev_byRankFINAL_2023-08-11_homd.csv -s eren2014_v1v3
        INSERT IGNORE INTO `abundance_tax_ranked`
        
        takes the abundance data from 3 csv files to the database.
        BROKEN:: HOMD-abundance-Segata.csv   => segata_edit2021-12-24.csv
        HOMD-abundance-Dewhirst.csv => dewhirst_edit2021-12-27.csv
        HOMD-abundance-Segata.csv   =>  eren2014_v1v3_MeanStdevPrev_byRankFINAL_2021-12-26_homd.csv
        
        --source must be in ['eren2014_v1v3','eren2014_v3v5','dewhirst', 'segata']
        
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=True,  action="store",   dest = "infile", default='none',
                                                    help=" ")
    parser.add_argument("-s", "--source",   required=True,  action="store",   dest = "source", 
                                    help="eren2014_v1v3 eren2014_v3v5 dewhirst segata ")
    
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
    args = parser.parse_args()
    if args.source not in ['eren2014_v1v3','eren2014_v3v5','dewhirst','segata']:
        print(usage)
        sys.exit()
    #parser.print_help(usage)
    if args.dbhost == 'homd_dev':
        args.DATABASE = 'homd'
        dbhost_new= '192.168.1.46'
        args.prettyprint = False
    
    elif args.dbhost == 'homd_prod':
        args.DATABASE = 'homd'
        dbhost_new= '192.168.1.42'
        args.prettyprint = False

    elif args.dbhost == 'localhost':
        #args.json_file_path = '/Users/avoorhis/programming/homd-data/json'
        #args.TAX_DATABASE  = 'HOMD_taxonomy'
        args.DATABASE = 'homd'
        dbhost_new = 'localhost'
        #dbhost_old = 'localhost'
        
    else:
        sys.exit('dbhost - error')
    
    #myconn_tax = MyConnection(host=dbhost_old, db=args.TAX_DATABASE,   read_default_file = "~/.my.cnf_node")
    myconn = MyConnection(host=dbhost_new, db=args.DATABASE,  read_default_file = "~/.my.cnf_node")
    
    args.tax_ids = get_taxid_obj()
    
    run_abundance_csv(args)
   
    