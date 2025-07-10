#!/usr/bin/env python

import os, sys, stat
import json
import argparse
import csv
sys.path.append('/Users/avoorhis/programming/')
sys.path.append('/home/ubuntu/homd-work/')
from connect import MyConnection
import datetime
ranks = ['domain','phylum','klass','order','family','genus','species','subspecies']
update_headers = ['Domain','Phylum','Class','Order','Family','Genus','Species']

today = str(datetime.date.today())


collector = {}

q_taxonomy = "SELECT  otid,domain,phylum,klass,`order`,"
q_taxonomy += " family,genus,species,subspecies from otid_prime"
q_taxonomy += " JOIN `taxonomy` using(taxonomy_id)"
q_taxonomy += " JOIN `domain` using(domain_id)"
q_taxonomy += " JOIN `phylum` using(phylum_id)"
q_taxonomy += " JOIN `klass` using(klass_id)"
q_taxonomy += " JOIN `order` using(order_id)"
q_taxonomy += " JOIN `family` using(family_id)"
q_taxonomy += " JOIN `genus` using(genus_id)"
q_taxonomy += " JOIN `species` using(species_id)"
q_taxonomy += " JOIN `subspecies` using(subspecies_id)"
q_taxonomy += " WHERE status !='DROPPED'"
"""
SELECT  otid,domain,phylum,klass,`order`,
 family,genus,species,subspecies from otid_prime
 JOIN `taxonomy` using(taxonomy_id)
 JOIN `domain` using(domain_id)
 JOIN `phylum` using(phylum_id)
 JOIN `klass` using(klass_id)
 JOIN `order` using(order_id)
 JOIN `family` using(family_id)
 JOIN `genus` using(genus_id)
 JOIN `species` using(species_id)
 JOIN `subspecies` using(subspecies_id)
 WHERE status !='DROPPED'
"""
errors = []
def get_current_taxonomy(args):
    
            
    result = myconn.execute_fetch_select_dict(q_taxonomy)
    if myconn.cursor.rowcount == 0:
        sys.exit('No Taxon found: '+row['HMT-ID'] +' -EXITING')
    for taxrow in result:
        #print(n)
        collector[taxrow['otid']] = taxrow
    return collector
                
def check_tax(name,id,parent,child):
    pass
    
def run_species():
    # find all species names and if dupes
    # there are many duplicate species names
    return
    sp_lookup = {}
    for otid in collector:
        species = collector[otid]['species']
        if species in sp_lookup:
            # error
            print('DUP Species',species,otid,sp_lookup[species])
            
        else:
            sp_lookup[species] = otid
        
        
    
def run_genera():
    lookup = {}
    problem_genera = []
    for otid in collector:
        genus = collector[otid]['genus']
        if genus in lookup:
            dup_otid = lookup[genus]
            # duplicate genus for otid and lookup[genus]
            # thats okay as long as phylum,klass,order,family all same
            if collector[otid]['phylum'] != collector[dup_otid]['phylum'] or \
                collector[otid]['klass'] != collector[dup_otid]['klass'] or \
                collector[otid]['order'] != collector[dup_otid]['order'] or \
                collector[otid]['family'] != collector[dup_otid]['family']:
                   
                   problem_genera.append('Duplicate Genus: '+genus+'\n\tHMT-'+str(otid)+':'+get_taxon_string(otid)+'\n\tHMT-'+str(dup_otid)+':'+get_taxon_string(dup_otid))
                   
        else:
            lookup[genus] = otid
    for problem in problem_genera:
        print(problem)
        
def run_families():
    lookup = {}
    problem_family = []
    for otid in collector:
        family = collector[otid]['family']
        if family in lookup:
            dup_otid = lookup[family]
            # duplicate genus for otid and lookup[genus]
            # thats okay as long as phylum,klass,order,family all same
            if collector[otid]['phylum'] != collector[dup_otid]['phylum'] or \
                collector[otid]['klass'] != collector[dup_otid]['klass'] or \
                collector[otid]['order'] != collector[dup_otid]['order']:
                   problem_family.append('Duplicate Family:'+family+'\n\tHMT-'+str(otid)+':'+get_taxon_string(otid)+'\n\tHMT-'+str(dup_otid)+':'+get_taxon_string(dup_otid))
                   
        else:
            lookup[family] = otid
    for problem in problem_family:
        print(problem)
        
def run_orders():
    lookup = {}
    problem_order = []
    for otid in collector:
        order = collector[otid]['order']
        if order in lookup:
            dup_otid = lookup[order]
            # duplicate genus for otid and lookup[genus]
            # thats okay as long as phylum,klass,order,family all same
            if collector[otid]['phylum'] != collector[dup_otid]['phylum'] or \
                collector[otid]['klass'] != collector[dup_otid]['klass']:
                   problem_order.append('Duplicate Order:'+order+'\n\tHMT-'+str(otid)+':'+get_taxon_string(otid)+'\n\tHMT-'+str(dup_otid)+':'+get_taxon_string(dup_otid))
                   
        else:
            lookup[order] = otid
    for problem in problem_order:
        print(problem)
        
def run_classes():
    lookup = {}
    problem_klass = []
    for otid in collector:
        klass = collector[otid]['klass']
        if klass in lookup:
            dup_otid = lookup[klass]
            # duplicate genus for otid and lookup[genus]
            # thats okay as long as phylum,klass,order,family all same
            if collector[otid]['phylum'] != collector[dup_otid]['phylum']:
                   problem_klass.append('DUP Class:'+klass+'\n'+get_taxon_string(otid)+'\n'+get_taxon_string(otid))
                   
        else:
            lookup[klass] = otid
    for problem in problem_klass:
        print(problem)

    
def get_taxon_string(otid):
    string = ''
    string += collector[otid]['domain']+';'
    string += collector[otid]['phylum']+';'
    string += collector[otid]['klass']+';'
    string += collector[otid]['order']+';'
    string += collector[otid]['family']+';'
    string += collector[otid]['genus']+';'
    string += collector[otid]['species']
    
    return string
    
if __name__ == "__main__":

    usage = """
    USAGE:
       
     check_db_for_mixed_ranks.py
     
     This script run will catch database taxonomy errors where
     parent taxa ranks are different for a certain child tax name.
     
     ie: for the Family(child) 'Peptoniphilaceae'  all the  Orders(parents) should be the same
     in the taxonomy table in the database. 
     
     This script will highlight those errors.
      
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
    
    
    args.outdir = './'                         
    if args.dbhost == 'homd_dev':
        #args.json_file_path = '/groups/vampsweb/vamps/nodejs/json'
        #args.TAX_DATABASE = 'HOMD_taxonomy'
        args.DATABASE = 'homd'
        #dbhost_old = '192.168.1.51'
        dbhost= '192.168.1.46'   #TESTING is 1.46  PRODUCTION is 1.42
        #dbhost= '192.168.1.42' 
        args.prettyprint = False
        #args.ncbi_dir = '/mnt/efs/bioinfo/projects/homd_add_genomes_V10.1/GCA_V10.1_all'
        #args.prokka_dir = '/mnt/efs/bioinfo/projects/homd_add_genomes_V10.1/prokka_V10.1_all'
    elif args.dbhost == 'homd_prod':  
        args.DATABASE = 'homd'
        #dbhost_old = '192.168.1.51'
        dbhost= '192.168.1.42' 
    elif args.dbhost == 'localhost':
        #args.json_file_path = '/Users/avoorhis/programming/homd-data/json'
        #args.TAX_DATABASE  = 'HOMD_taxonomy'
        args.DATABASE = 'homd'
        dbhost = 'localhost'
        
        #dbhost_old = 'localhost'
    else:
        sys.exit('dbhost - error')
    args.indent = None
    
    myconn = MyConnection(host=dbhost, db=args.DATABASE,  read_default_file = "~/.my.cnf_node")
    
    get_current_taxonomy(args)
    #print(ctax)
    run_species()
    run_genera()
    run_families()
    run_orders()
    run_classes()
    
    
        
    
    