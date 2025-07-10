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

"""

"""
# queries = [
# "SELECT domain_id FROM `domain` WHERE `domain`='%s'",
# "SELECT phylum_id FROM `phylum` WHERE `phylum`='%s'",
#  "SELECT klass_id FROM `klass` WHERE `klass`='%s'",
#  "SELECT order_id FROM `order` WHERE `order`='%s'",
#  "SELECT family_id FROM `family` WHERE `family`='%s'",
#  "SELECT genus_id FROM `genus` WHERE `genus`='%s'",
#  "SELECT species_id FROM `species` WHERE `species`='%s'"
# ]
# q_domain = "SELECT domain_id FROM `domain` WHERE `domain`='%s'"
# q_phylum = "SELECT phylum_id FROM `phylum` WHERE `phylum`='%s'"
# q_class = "SELECT klass_id FROM `klass` WHERE `klass`='%s'"
# q_order = "SELECT order_id FROM `order` WHERE `order`='%s'"
# q_family = "SELECT family_id FROM `family` WHERE `family`='%s'"
# q_genus = "SELECT genus_id FROM `genus` WHERE `genus`='%s'"
# q_species = "SELECT species_id FROM `species` WHERE `species`='%s'"

q_taxonomy = "SELECT otid, status,domain,phylum,klass,`order`,"
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
q_taxonomy += " ORDER BY otid"



def get_taxonomy(conn):
    collector = {}  
    # get old tax and tax_id
    q = q_taxonomy
        
    result = conn.execute_fetch_select_dict(q)
    for taxrow in result:
        #print(n)
        collector['HMT-'+str(taxrow['otid']).zfill(3)] = taxrow
            
    return collector
                    
            
    
    #sys.exit()       

    


def run():
    # get all taxa
    taxonid_list = list(old_taxV3.keys())
    
    for otid in new_taxV4:
        if otid not in taxonid_list:
            taxonid_list.append(otid)
    
    #sorted_list = [str(x).zfill(3) for x in taxonid_list]
    outfile = 'outfile.csv'
    fh = open(outfile,'w')
    taxonid_list.sort()
    text = 'Taxon-ID\tStatus-V4.0\tDomain-V4.0\tPhylum-V4.0\tClass-V4.0\tOrder-V4.0\tFamily-V4.0\tGenus-V4.0\tSpecies-V4.0\tSubspecies-V4.0'
    text += '\tStatus-V3.1\tDomain-V3.1\tPhylum-V3.1\tClass-V3.1\tOrder-V3.1\tFamily-V3.1\tGenus-V3.1\tSpecies-V3.1\tSubspecies-V3.1\n'
    fh.write(text)
    for hmt in taxonid_list:
        txt = hmt+'\t'
        statusv3 = ''
        statusv4 = ''
        if hmt in new_taxV4 and hmt in old_taxV3:
            if new_taxV4[hmt]['status'].lower() == 'dropped':
                statusv4 = 'Dropped'
            if old_taxV3[hmt]['status'].lower() == 'dropped':
                statusv3 = 'Dropped'
            txt += statusv4+'\t'+new_taxV4[hmt]['domain']+'\t'+new_taxV4[hmt]['phylum']+'\t'+new_taxV4[hmt]['klass']+'\t'+new_taxV4[hmt]['order']+'\t'+new_taxV4[hmt]['family']+'\t'+new_taxV4[hmt]['genus']+'\t'+new_taxV4[hmt]['species']+'\t'+new_taxV4[hmt]['subspecies']
            txt += '\t'+statusv3+'\t'+old_taxV3[hmt]['domain']+'\t'+old_taxV3[hmt]['phylum']+'\t'+old_taxV3[hmt]['klass']+'\t'+old_taxV3[hmt]['order']+'\t'+old_taxV3[hmt]['family']+'\t'+old_taxV3[hmt]['genus']+'\t'+old_taxV3[hmt]['species']+'\t'+old_taxV3[hmt]['subspecies']
            txt += '\n'
        elif hmt in new_taxV4:
            if new_taxV4[hmt]['status'].lower() == 'dropped':
                statusv4 = 'Dropped'
            txt += statusv4+'\t'+new_taxV4[hmt]['domain']+'\t'+new_taxV4[hmt]['phylum']+'\t'+new_taxV4[hmt]['klass']+'\t'+new_taxV4[hmt]['order']+'\t'+new_taxV4[hmt]['family']+'\t'+new_taxV4[hmt]['genus']+'\t'+new_taxV4[hmt]['species']+'\t'+new_taxV4[hmt]['subspecies']
            txt += '\t\t\t\t\t\t\t\t\t'
            txt += '\n'
        elif hmt in old_taxV3:
            if old_taxV3[hmt]['status'].lower() == 'dropped':
                statusv3 = 'Dropped'
            txt += '\t\t\t\t\t\t\t\t\t'
            txt += '\t'+statusv3+'\t'+old_taxV3[hmt]['domain']+'\t'+old_taxV3[hmt]['phylum']+'\t'+old_taxV3[hmt]['klass']+'\t'+old_taxV3[hmt]['order']+'\t'+old_taxV3[hmt]['family']+'\t'+old_taxV3[hmt]['genus']+'\t'+old_taxV3[hmt]['species']+'\t'+old_taxV3[hmt]['subspecies']
            txt += '\n'
        else:
           sys.exit('neither')
        fh.write(txt)
        
            
        
if __name__ == "__main__":

    usage = """
    USAGE:
       
     -update  Change Taxon(s) taxonomy
            Tax format: columns
            ./update_homd_taxonomy_byFile.py.py -update -i HOMD-new-taxonomy.csv
       
            KISS infile cols:
       
            HMT, Domain...Species 
       
            Run taxonomy (-t homd) first then genomes(-t genomes)
       
     -insert  NEW Taxons
            Tax format: Bacteria;Actinobacteria;Actinomycetia;Micrococcales;Promicromonosporaceae;Cellulosimicrobium;cellulans
            ./update_homd_taxonomy_byFile.py.py -insert -i HOMD-new-taxonomy.csv
      
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
    if args.dbhost == 'homd':
        #args.json_file_path = '/groups/vampsweb/vamps/nodejs/json'
        #args.TAX_DATABASE = 'HOMD_taxonomy'
        args.DATABASE = 'homd'
        #dbhost_old = '192.168.1.51'
        dbhostV4= '192.168.1.46'   #TESTING is 1.46  PRODUCTION is 1.42
        dbhostV3= '192.168.1.42' 
        
    
    elif args.dbhost == 'localhost':
        #args.json_file_path = '/Users/avoorhis/programming/homd-data/json'
        #args.TAX_DATABASE  = 'HOMD_taxonomy'
        args.DATABASE = 'homd'
        dbhostV4 = 'localhost'
        dbhostV3 = 'localhost'
        
        #dbhost_old = 'localhost'
    else:
        sys.exit('dbhost - error')
        
    args.indent = None
    
    myconnV4 = MyConnection(host=dbhostV4, db=args.DATABASE,  read_default_file = "~/.my.cnf_node")
    myconnV3 = MyConnection(host=dbhostV3, db=args.DATABASE,  read_default_file = "~/.my.cnf_node")
    
    old_taxV3 = get_taxonomy(myconnV3)
    new_taxV4 = get_taxonomy(myconnV4)
    
    #print('old',old_taxV10)
    #print('new',new_taxV11)
    
    run()
        
    