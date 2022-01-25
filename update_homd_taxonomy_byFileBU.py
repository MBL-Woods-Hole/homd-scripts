#!/usr/bin/env python

import os, sys, stat
import json
import argparse
import csv
from connect import MyConnection
import datetime
ranks = ['domain','phylum','klass','order','family','genus','species','subspecies']
headers = ['Domain','Phylum','Class','Order','Family','Genus','Species']
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

q_genomes = "SELECT otid as HMT,genus,genus_id,species,species_id from genomes"
q_genomes += " JOIN `genus` using(genus_id)"
q_genomes += " JOIN `species` using(species_id)" 

collector = {} 
def get_current_genome_taxonomy(args): 
    result = myconn_new.execute_fetch_select_dict(q_genomes)
    for taxrow in result:
        if taxrow['HMT'] not in collector:   
            collector[taxrow['HMT']] = {}
        collector[taxrow['HMT']]['old_genome_tax'] = {'genus':taxrow['genus'],'genus_id':taxrow['genus_id'],'species':taxrow['species'],'species_id':taxrow['species_id']}

def get_current_taxonomy(args):
    with open(args.infile) as csv_file: 
        csv_reader = csv.DictReader(csv_file, delimiter='\t') # KK tab
        for row in csv_reader:
            #print(row['HMT'])
            if row['HMT'] not in collector: 
                collector[row['HMT']] = {}
                collector[row['HMT']]['new_taxonomy'] = {}
                collector[row['HMT']]['old_taxonomy'] = {}
            for i,rank in enumerate(ranks[:7]):   # headers from infile don't match field names
                name = headers[i]
                collector[row['HMT']]['new_taxonomy'][rank] = row[name]
            collector[row['HMT']]['new_taxonomy']['subspecies'] = ''
            # get old tax and tax_id
            q = q_taxonomy + " WHERE otid='"+row['HMT']+"'"
            
            result = myconn_new.execute_fetch_select_dict(q)
            for taxrow in result:
                #print(n)
                collector[row['HMT']]['taxonomy_id'] = taxrow['taxonomy_id']
                
                for rank in ranks:
                    rank_id = taxrow[rank+'_id']
                    collector[row['HMT']]['old_taxonomy'][rank] = taxrow[rank]
                    collector[row['HMT']]['old_taxonomy'][rank+'_id'] = taxrow[rank+'_id']
                    
            
    #print(collector) 
    #sys.exit()       
def run_genomes(args): 
    if 'old_genome_tax' in collector[hmt] and newtax['species_id'] != collector[hmt]['old_genome_tax']['species_id']:
                print('SPECIES NE ',hmt)
            #if new['genus_id'] != old['genus_id']:
            #    print('GENUS NE ', hmt)
               
            q_genome = "UPDATE genomes set genus_id ='%s',"
            q_genome += " species_id='%s'"
            q_genome += " WHERE otid='%s'"
            q_genome = q_genome % (str(update_ids['genus_id']),str(update_ids['species_id']),str(hmt))
            q2 = "SELECT * from genomes where genus_id='%s'" % str(oldtax['genus_id'])
            res_genome = myconn_new.execute_fetch_one(q2)
            if myconn_new.cursor.rowcount > 0:
                pass
                #print('FOUND',hmt,oldtax['genus_id'],update_ids['genus_id'])
                
def run_homd(args):
    
    for hmt in collector:
        oldtax = collector[hmt]['old_taxonomy']
        newtax = collector[hmt]['new_taxonomy']
        
        res_taxonomy = compare(oldtax, newtax)
        if res_taxonomy:
            if args.verbose:
                print()
                print(hmt)

            tax_id = collector[hmt]['taxonomy_id']
            update_ids = {  # initialize with old tax ids
                'domain_id':    oldtax['domain_id'],
                'phylum_id':    oldtax['phylum_id'],
                'klass_id':     oldtax['klass_id'],
                'order_id':     oldtax['order_id'],
                'family_id':    oldtax['family_id'],
                'genus_id':     oldtax['genus_id'],
                'species_id':   oldtax['species_id'],
                'subspecies_id':oldtax['subspecies_id']
            }
            if args.verbose:
                print('before',update_ids)
            for item in res_taxonomy:
                #{'rank': 'species', 'newname': 'sp._HMT_902', 'oldname': 'sp. HMT 902'}
                
                # get new id
                rank = item['rank']
                if args.verbose:
                    print('rank',item)
                if rank == 'species' and ('subsp' in item['newname'] or 'clade' in item['newname']):
                    if 'Eubacterium' in item['newname']:
                        ssitems = item['newname'].split('_') 
                        sp = ssitems[0]+'_'+ssitems[1]
                        ssp = '_'.join(ssitems[2:])
                    else:
                        ssitems = item['newname'].split('_',1) # split on first occurance
                        sp = ssitems[0]
                        ssp = ssitems[1]
                    #print(hmt,'got subspecies in sp',sp,ssp)
                    qsp = "SELECT species_id from `species` WHERE `species`='"+sp+"'"
                    #print(qsp)
                    result = myconn_new.execute_fetch_one(qsp)
                    if myconn_new.cursor.rowcount == 0:
                        qsp_insert = "INSERT into `species` (`species`) VALUES('%s')" % sp
                        #print(qsp_insert)
                        myconn_new.execute_no_fetch(qsp_insert)
                        species_id = myconn_new.cursor.lastrowid
                    else:
                        species_id = result[0]
                    #collector[hmt]['new_taxonomy']['species_id'] = species_id
                    qssp = "SELECT subspecies_id from `subspecies` WHERE `subspecies`='"+ssp+"'"
                    #print(qssp)
                    result = myconn_new.execute_fetch_one(qssp)
                    if myconn_new.cursor.rowcount == 0:
                        qssp_insert = "INSERT into `subspecies` (`subspecies`) VALUES('%s')" % ssp
                        #print(qssp_insert)
                        myconn_new.execute_no_fetch(qssp_insert)
                        subspecies_id = myconn_new.cursor.lastrowid
                    else:
                        subspecies_id = result[0]   
                    #print('sp & ssp',species_id,subspecies_id)
                    update_ids['species_id'] = species_id
                    update_ids['subspecies_id'] = subspecies_id
                elif rank !='subspecies':  # ignore rank = 'subspecies'
                    q = "SELECT "+rank+'_id from `'+rank+'` WHERE `'+rank+"`='"+item['newname']+"'"
                    #print(q)
                    result = myconn_new.execute_fetch_one(q)
                    if myconn_new.cursor.rowcount == 0:
                        q_insert = "INSERT into `"+rank+"` (`"+rank+"`) VALUES('%s')" % item['newname']
                        #print(q_insert)
                        myconn_new.execute_no_fetch(q_insert)
                        rank_id = myconn_new.cursor.lastrowid
                    else:
                        rank_id = result[0]
                
                    # Change update_ids
                    update_ids[rank+'_id'] = rank_id
            if args.verbose:
                print('after',update_ids)
            
            
            #print('new',newtax)
            #print('old',oldtax)
            #if hmt == 3:
            
            
            q_update = "UPDATE taxonomy set domain_id='%s',"
            q_update += " phylum_id='%s',"
            q_update += " klass_id='%s',"
            q_update += " order_id='%s',"
            q_update += " family_id='%s',"
            q_update += " genus_id='%s',"
            q_update += " species_id='%s',"
            q_update += " subspecies_id='%s'"
            q_update += " WHERE taxonomy_id='%s'"
            q_update = q_update % (str(update_ids['domain_id']),str(update_ids['phylum_id']),str(update_ids['klass_id']),
            str(update_ids['order_id']),str(update_ids['family_id']),str(update_ids['genus_id']),
            str(update_ids['species_id']),str(update_ids['subspecies_id']),str(tax_id))
            if args.verbose:
                print(q_update)
        
            if args.go:
                myconn_new.execute_no_fetch(q_update)
                
        else:
            #print('no update needed for HMT-'+hmt )
            pass
    

def compare(oldtax,newtax):
    result = []
    for rank in ranks:
        if oldtax[rank] != newtax[rank]:
            result.append({'rank':rank,'newname':newtax[rank],'oldname':oldtax[rank]})
    return result

if __name__ == "__main__":

    usage = """
    USAGE:
       
           
       ./update_homd_taxonomy_byFile.py.py -i HOMD-new-taxonomy.csv
       
       KISS infile cols:
       
       HMT, Domain...Species 
       
       
       
      
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
    parser.add_argument("-t", "--table",   required=False,  action="store_true",    dest = "table", default='homd',
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
        
    
    
    if args.table == 'genome':
        get_current_genome_taxonomy(args)  
        run_genome(arg)
    else:
        get_current_taxonomy(args) 
        run_homd(args)
    if not args.go:
        print('\n *** Add "-g/--go" to the command line to update database ***\n')
    else:
        print('\nDone\n')
        print('Remember to run both -t homd and -t genome')