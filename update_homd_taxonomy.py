#!/usr/bin/env python

import os, sys, stat
import json
import argparse
import csv
from connect import MyConnection
import datetime
ranks = ['domain','phylum','klass','order','family','genus','species']
today = str(datetime.date.today())

"""

"""
queries = [
"SELECT domain_id FROM `domain` WHERE `domain`='%s'",
"SELECT phylum_id FROM `phylum` WHERE `phylum`='%s'",
 "SELECT klass_id FROM `klass` WHERE `klass`='%s'",
 "SELECT order_id FROM `order` WHERE `order`='%s'",
 "SELECT family_id FROM `family` WHERE `family`='%s'",
 "SELECT genus_id FROM `genus` WHERE `genus`='%s'",
 "SELECT species_id FROM `species` WHERE `species`='%s'"
]
q_domain = "SELECT domain_id FROM `domain` WHERE `domain`='%s'"
q_phylum = "SELECT phylum_id FROM `phylum` WHERE `phylum`='%s'"
q_class = "SELECT klass_id FROM `klass` WHERE `klass`='%s'"
q_order = "SELECT order_id FROM `order` WHERE `order`='%s'"
q_family = "SELECT family_id FROM `family` WHERE `family`='%s'"
q_genus = "SELECT genus_id FROM `genus` WHERE `genus`='%s'"
q_species = "SELECT species_id FROM `species` WHERE `species`='%s'"
    

def run(args):
    lookup = {}
    with open(args.infile) as csv_file: 
        csv_reader = csv.DictReader(csv_file, delimiter='\t') # 
        for row in csv_reader:
            print(row)
            
            lookup[row['HMT']] = row
            
            
    taxonomy_collector = {}
    for hmt in lookup:
        taxonomy_collector = {}
        #print(hmt,'domain',lookup[hmt]['domain'])
        otid = str(int(hmt[-3:]))
        print('otid',otid)
        qtax = "SELECT taxonomy_id from otid_prime where otid ='"+otid+"'"
        result = myconn_new.execute_fetch_one(qtax)
        taxonomy_id = result[0]
        taxonomy_collector['taxonomy_id'] = taxonomy_id
        # Domain
        
       #  q = q_domain % lookup[hmt]['domain']
#         result = myconn_new.execute_fetch_one(q)
#         if myconn_new.cursor.rowcount == 0:
#             q_insert = "INSERT into `domain` (domain) VALUES('%s')" % lookup[hmt]['domain']
#             myconn_new.execute_no_fetch(q_insert)
#             print('lastrowid',myconn_new.cursor.lastrowid)
#             domain_id = myconn_new.cursor.lastrowid
#         else:
#             domain_id = result[0]
#         taxonomy_collector['domain_id'] = domain_id
        
        for i,rank in enumerate(ranks):
            #if rank == 'klass':rank = 'class'
            q = queries[i] % lookup[hmt][rank]
            result = myconn_new.execute_fetch_one(q)
            if myconn_new.cursor.rowcount == 0:
                q_insert = "INSERT into `"+rank+"` ("+rank+") VALUES('%s')" % lookup[hmt][rank]
                myconn_new.execute_no_fetch(q_insert)
                rank_id = myconn_new.cursor.lastrowid
            else:
                rank_id = result[0]
            
            taxonomy_collector[rank+'_id'] = rank_id
        print(taxonomy_collector)
        # next step is to write query to update
        print() 
        print('HMT:',hmt) 
        q = "UPDATE taxonomy set"
        q += " domain_id='"+str(taxonomy_collector['domain_id'])+"', "
        q += " phylum_id='"+str(taxonomy_collector['phylum_id'])+"', "
        q += " klass_id='"+str(taxonomy_collector['klass_id'])+"',"
        q += " order_id='"+str(taxonomy_collector['order_id'])+"', "
        q += " family_id='"+str(taxonomy_collector['family_id'])+"', "
        q += " genus_id='"+str(taxonomy_collector['genus_id'])+"', "
        q += " species_id='"+str(taxonomy_collector['species_id'])+"'"
        q += " WHERE taxonomy_id='"+str(taxonomy_collector['taxonomy_id'])+"'"
        print(q)
        if args.go:
            myconn_new.execute_no_fetch(q)
        
    print('\nTo actually run the update commands add -g/--go to the command line.\n')
        

if __name__ == "__main__":

    usage = """
    USAGE:
       
           
       ./update_homd_taxonomy.py -i HOMD-new-taxonomy.csv
       currently the column class must be spelled 'klass'
       and the HMT column must be the full 'HMT-038'
      
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=False,  action="store",   dest = "infile", default=False,
                                                    help="HOMD-endpoint1-wpcts.csv")
    parser.add_argument("-g", "--go",   required=False,  action="store_true",    dest = "go", default=False,
                                                    help="Alter Database") 
    parser.add_argument("-host", "--host", required = False, action = 'store', dest = "dbhost", default = 'localhost',
                                                   help="") 
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", default=False,
                                                    help="verbose print()") 
    
    args = parser.parse_args()
    
    #parser.print_help(usage)
    
    args.outdir = './'                         
    if args.dbhost == 'homd':
        args.NEW_DATABASE = 'homd'
        dbhost_new= '192.168.1.40'

    elif args.dbhost == 'localhost':
        args.NEW_DATABASE = 'homd'
        dbhost_new = 'localhost'
        
    else:
        sys.exit('dbhost - error')
    args.indent = None
    
    myconn_new = MyConnection(host=dbhost_new, db=args.NEW_DATABASE,  read_default_file = "~/.my.cnf_node")
    if args.verbose:
        print()
    if not args.infile:
        print(usage)
        sys.exit()
        
    run(args)
