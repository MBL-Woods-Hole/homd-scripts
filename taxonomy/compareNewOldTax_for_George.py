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

# q_taxonomy = "SELECT taxonomy_id, domain,domain_id,phylum,phylum_id,klass,klass_id,`order`,order_id,"
# q_taxonomy += " family,family_id,genus,genus_id,species,species_id,subspecies,subspecies_id from otid_prime"
q_taxonomy = "SELECT otid,taxonomy_id, "
q_taxonomy += " genus,genus_id,species,species_id,subspecies,subspecies_id,status from otid_prime"

q_taxonomy += " JOIN `taxonomy` using(taxonomy_id)"
# q_taxonomy += " JOIN `domain` using(domain_id)"
# q_taxonomy += " JOIN `phylum` using(phylum_id)"
# q_taxonomy += " JOIN `klass` using(klass_id)"
# q_taxonomy += " JOIN `order` using(order_id)"
# q_taxonomy += " JOIN `family` using(family_id)"
q_taxonomy += " JOIN `genus` using(genus_id)"
q_taxonomy += " JOIN `species` using(species_id)"
q_taxonomy += " JOIN `subspecies` using(subspecies_id)"
q_taxonomy += " ORDER BY otid"



def get_current_taxonomy(args):
    collector = {}  
    # get old tax and tax_id
    q = q_taxonomy
        
    result = myconn.execute_fetch_select_dict(q)
    if myconn.cursor.rowcount == 0:
        sys.exit('No Taxon found: '+row['otid'] +' -EXITING')
    for taxrow in result:
        #print(n)
        collector[str(taxrow['otid'])] = taxrow
            
    return collector
                    
            
    
    #sys.exit()       

    
def run_development(args):
    dev_collector = get_current_taxonomy(args) 
    fp = open(args.dev_tax_fn,'w')
    fp.write('HMT-ID\totid\tNew-Genus\tNew-Species\tNew-SubSpecies\tNew-Status\n')
    for otid in dev_collector:
        hmt='HMT-'+str(otid).zfill(3)
        #print(hmt,dev_collector[otid])
        genus = dev_collector[otid]['genus']
        species = dev_collector[otid]['species']
        
        subsp  = dev_collector[otid]['subspecies']
         
        status  = dev_collector[otid]['status']
        if status != 'Dropped':
            status =''
        fp.write(hmt+'\t'+str(otid)+'\t'+genus+'\t'+species+'\t'+subsp+'\t'+status+ '\n')
    # plan print out csv into file
    # then on public site open/read that file and get data from mysql
    
    
    
    


def run_public(args):
    master_collector = {}
    with open(args.dev_tax_fn) as csv_file: 
        csv_reader = csv.DictReader(csv_file, delimiter='\t')
        for row in csv_reader:
            otid = str(row['otid'])
            print('otid from file',otid)
            master_collector[otid] = {'new_tax':{},'old_tax':{}}
            master_collector[otid]['new_tax']['New-Genus'] = row['New-Genus']
            master_collector[otid]['new_tax']['New-Species'] = row['New-Species']
            master_collector[otid]['new_tax']['New-SubSpecies'] = row['New-SubSpecies']
            master_collector[otid]['new_tax']['New-Status'] = row['New-Status']
            master_collector[otid]['old_tax']['Old-Genus'] = ''
            master_collector[otid]['old_tax']['Old-Species'] = ''
            master_collector[otid]['old_tax']['Old-SubSpecies'] = ''
            master_collector[otid]['old_tax']['Old-Status'] = ''
    public_collector = get_current_taxonomy(args) 
    fp = open(args.full_tax_fn,'w')
    fp.write('HMT-ID\tNew-Genus\tNew-Species\tNew-SubSpecies\tNew-Status')
    fp.write('\tOld-Genus\tOld-Species\tOld-SubSpecies\tOld-Status\n')
    for otid in public_collector:
        otid = str(otid)
        hmt='HMT-'+str(otid).zfill(3)
        #print(hmt,dev_collector[otid])
        old_genus = public_collector[otid]['genus']
        old_species = public_collector[otid]['species']
        
        old_subsp  = public_collector[otid]['subspecies']
         
        old_status  = public_collector[otid]['status']
        if old_status != 'Dropped':
            old_status =''
        
        new_genus   = ''
        new_species = ''
        new_subsp   = ''
        new_status  = ''
        if otid not in master_collector:
            master_collector[otid] = {'new_tax':{},'old_tax':{}}
            master_collector[otid]['new_tax']['New-Genus'] = ''
            master_collector[otid]['new_tax']['New-Species'] = ''
            master_collector[otid]['new_tax']['New-SubSpecies'] = ''
            master_collector[otid]['new_tax']['New-Status'] = ''
            
        master_collector[otid]['old_tax']['Old-Genus'] = old_genus
        master_collector[otid]['old_tax']['Old-Species'] = old_species
        master_collector[otid]['old_tax']['Old-SubSpecies'] = old_subsp
        master_collector[otid]['old_tax']['Old-Status'] = old_status
        
    ordered_otid_list = [int(x) for x in list(master_collector.keys())]
    
    ordered_otid_list.sort()
    
    
    for otid in ordered_otid_list:
        otid = str(otid)
        hmt='HMT-'+str(otid).zfill(3)
        new_genus   =master_collector[otid]['new_tax']['New-Genus']
        new_species =master_collector[otid]['new_tax']['New-Species']
        new_subsp   =master_collector[otid]['new_tax']['New-SubSpecies']
        new_status  =master_collector[otid]['new_tax']['New-Status']
        old_genus   =master_collector[otid]['old_tax']['Old-Genus']
        old_species =master_collector[otid]['old_tax']['Old-Species']
        old_subsp   =master_collector[otid]['old_tax']['Old-SubSpecies']
        old_status  =master_collector[otid]['old_tax']['Old-Status']
        fp.write(hmt+'\t'+new_genus+'\t'+new_species+'\t'+new_subsp+'\t'+new_status)
        fp.write('\t'+old_genus+'\t'+old_species+'\t'+old_subsp+'\t'+old_status+ '\n')
            
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
    
    args.dev_tax_fn = 'HOMD_Development_Taxonomy.csv'
    args.full_tax_fn = 'HOMD_Full_Taxonomy.csv'
    if args.dbhost =='homd_prod':
        # open dev file first
        
        run_public(args)
    else:
        # print out file
        run_development(args)
    
        
    