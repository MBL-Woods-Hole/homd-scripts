#!/usr/bin/env python

import os, sys, stat
import json
import argparse
import csv
sys.path.append('../../homd-data/')
from connect import MyConnection
import datetime
ranks = ['domain','phylum','klass','order','family','genus','species','subspecies']
update_headers = ['Domain','Phylum','Class','Order','Family','Genus','Species']

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
q_domain = "SELECT domain_id FROM `domain`"
q_phylum = "SELECT phylum,phylum_id FROM `phylum`"
q_class = "SELECT klass,klass_id FROM `klass`"
q_order = "SELECT `order`,order_id FROM `order`"
q_family = "SELECT family,family_id FROM `family`"
q_genus = "SELECT genus,genus_id FROM `genus`"
q_species = "SELECT species,species_id FROM `species`"

q_taxonomy = "SELECT taxonomy_id, domain,domain_id,phylum,phylum_id,klass,klass_id,`order`,order_id,"
q_taxonomy += " family,family_id,genus,genus_id,species,species_id,subspecies,subspecies_id from otid_prime"
q_taxonomy += " JOIN `taxonomy` using(taxonomy_id)"
q_taxonomy += " JOIN `domain` using(domain_id)"
q_taxonomy += " JOIN `phylum` using(phylum_id)"
q_taxonomy += " JOIN `klass` using(klass_id)"
q_taxonomy += " JOIN `order` using(order_id)"
q_taxonomy += " JOIN `family` using(family_id)"
q_taxonomy += " JOIN `genus` using(genus_id)"
q_taxonomy += " JOIN `species` using(species_id)"
q_taxonomy += " JOIN `subspecies` using(subspecies_id)"

errors = []
def check_tax(name,id,parent,child):
    parent_array = []
    qtax = "SELECT taxonomy_id,"+parent+"_id from taxonomy WHERE "+child+"_id='%s'" % (id)
    res_tax = myconn.execute_fetch_select_dict(qtax)
    if res_tax:
        #print()
        #print(child,name,res_tax)
        pass
    for result in res_tax:
       #print('taxonomy result',result)
       resid = result[parent+'_id']
       if len(parent_array) == 0:
           parent_array.append(resid)
       else:
           if resid not in parent_array:
              err = '  A second "'+parent+'_id Found For '+child+' ('+name+','+str(id)+')"!!!!'
              err += '\n     run: '+qtax
              print(err)
              #sys.exit('Second "'+parent+'_id Found For '+child+' ('+name+')"!!!!')
              errors.append(err)
def run(args):
    # dont check species
    #genus
    print('Checking Genera')
    res_genera = myconn.execute_fetch_select(q_genus)
    genus_ids = []
    for i in res_genera:
        genus_ids.append([i[0],i[1]])
    for (genus,gid) in genus_ids:
        check_tax(genus,gid,'family','genus')
    
    print('Checking Families')
    result = myconn.execute_fetch_select(q_family)
    rank_ids = []
    for i in result:
        rank_ids.append([i[0],i[1]])
    for (family,fid) in rank_ids:
        check_tax(family,fid,'order','family')
# taxonomy result {'taxonomy_id': 2385, 'order_id': 2991}
# taxonomy result {'taxonomy_id': 2386, 'order_id': 3022}
# select * from otid_prime where taxonomy_id in (2385,2386)
# 96 Bacteria;Bacillota;Clostridia;Eubacteriales;Lachnospiraceae;Lachnospiraceae [G2];Lachnospiraceae [G2] bacterium HMT-096
# 97 Bacteria;Bacillota;Clostridia;Lachnospirales;Lachnospiraceae;Moryella;Moryella sp. HMT-097
# plan to change 'Eubacteriales' to 'Lachnospirales' for HMT-96

    print('Checking Orders')
    result = myconn.execute_fetch_select(q_order)
    rank_ids = []
    for i in result:
        rank_ids.append([i[0],i[1]])
    for (order,oid) in rank_ids:
        check_tax(order,oid,'klass','order')

    print('Checking Classes')
    result = myconn.execute_fetch_select(q_class)
    rank_ids = []
    for i in result:
        rank_ids.append([i[0],i[1]])
    for (klass,kid) in rank_ids:
        check_tax(klass,kid,'phylum','klass')
        
    print('Checking Phyla')
    result = myconn.execute_fetch_select(q_phylum)
    rank_ids = []
    for i in result:
        rank_ids.append([i[0],i[1]])
    for (phylum,pid) in rank_ids:
        check_tax(phylum,pid,'domain','phylum')
    print()
    if len(errors) == 0:
        print('ALL GOOD!')
    else:
        for e in errors:
            print(e)
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
    
    
    run(args)
        
    
    