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


collector = {}  

def get_current_taxonomy(args):
    with open(args.infile) as csv_file: 
        csv_reader = csv.DictReader(csv_file, delimiter='\t') # KK tab
        for row in csv_reader:
            #print(row['HMT'])
            collector[row['HMT']] = {}
            collector[row['HMT']]['new_taxonomy'] = {}
            collector[row['HMT']]['old_taxonomy'] = {}
            for i,rank in enumerate(ranks[:7]):   # headers from infile don't match field names
                name = update_headers[i]
                collector[row['HMT']]['new_taxonomy'][rank] = row[name]
            collector[row['HMT']]['new_taxonomy']['subspecies'] = ''
            # get old tax and tax_id
            q = q_taxonomy + " WHERE otid='"+row['HMT']+"'"
            
            result = myconn.execute_fetch_select_dict(q)
            if myconn.cursor.rowcount == 0:
                sys.exit('No Taxon found: '+row['HMT'] +' -EXITING')
            for taxrow in result:
                #print(n)
                collector[row['HMT']]['taxonomy_id'] = taxrow['taxonomy_id']
                
                for rank in ranks:
                    rank_id = taxrow[rank+'_id']
                    collector[row['HMT']]['old_taxonomy'][rank] = taxrow[rank]
                    collector[row['HMT']]['old_taxonomy'][rank+'_id'] = taxrow[rank+'_id']
                    
            
    #print(collector) 
    #sys.exit()       
def get_ids(args, update_ids, tax_list):
    # [{'rank': 'species', 'newname': 'sp._HMT_902', 'oldname': 'sp. HMT 902'}]
    for item in tax_list:
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
            result = myconn.execute_fetch_one(qsp)
            if myconn.cursor.rowcount == 0:
                qsp_insert = "INSERT into `species` (`species`) VALUES('%s')" % sp
                print("(w/-go)INSERTING New Species: "+sp)
                if args.go:
                    myconn.execute_no_fetch(qsp_insert)
                    species_id = myconn.cursor.lastrowid
                else:
                    species_id='000'
            else:
                species_id = result[0]
            
            qssp = "SELECT subspecies_id from `subspecies` WHERE `subspecies`='"+ssp+"'"
            #print(qssp)
            result = myconn.execute_fetch_one(qssp)
            if myconn.cursor.rowcount == 0:
                qssp_insert = "INSERT into `subspecies` (`subspecies`) VALUES('%s')" % ssp
                print("(w/-go)INSERTING New Subspecies: "+ssp)
                if args.go:
                    myconn.execute_no_fetch(qssp_insert)
                    subspecies_id = myconn.cursor.lastrowid
                else:
                    subspecies_id = '000'
            else:
                subspecies_id = result[0]   
            #print('sp & ssp',species_id,subspecies_id)
            update_ids['species_id'] = species_id
            update_ids['subspecies_id'] = subspecies_id
        elif rank !='subspecies':  # ignore rank = 'subspecies'
            q = "SELECT "+rank+'_id from `'+rank+'` WHERE `'+rank+"`='"+item['newname']+"'"
            #print(q)
            result = myconn.execute_fetch_one(q)
            if myconn.cursor.rowcount == 0:
                q_insert = "INSERT into `"+rank+"` (`"+rank+"`) VALUES('%s')" % item['newname']
                print("(w/-go)INSERTING New : "+rank+': '+item['newname'])
                if args.go:
                    myconn.execute_no_fetch(q_insert)
                    rank_id = myconn.cursor.lastrowid
                else:
                    rank_id = '000'
            else:
                rank_id = result[0]
        
            # Change update_ids
            update_ids[rank+'_id'] = rank_id
    return update_ids
    
def run_update(args):
    update_collector = {}
    for hmt in collector:
        print('HMT',hmt)
        oldtax = collector[hmt]['old_taxonomy']
        newtax = collector[hmt]['new_taxonomy']
        update_ids = {
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
        diff = compare(oldtax, newtax)
        print('diff',diff)
        if diff:
            if args.verbose:
                print()
                print(hmt)
            # update_collector[hmt] = {}
#             update_collector[hmt]['taxonomy_id'] = collector[hmt]['taxonomy_id']
#             update_collector[hmt]['update'] = res
            tax_id = collector[hmt]['taxonomy_id']
            
            
            update_ids = get_ids(args, update_ids, diff)  #{'rank': 'species', 'newname': 'sp._HMT_902', 'oldname': 'sp. HMT 902'}
            
            
            if args.verbose:
                print('after',update_ids)
            if args.go:
            
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
                    myconn.execute_no_fetch(q_update)
        else:
            #print('no update needed for HMT-'+hmt )
            pass
    

    
def compare(oldtax,newtax):
    result = []
    for rank in ranks:
        if oldtax[rank] != newtax[rank]:
            result.append({'rank':rank,'newname':newtax[rank],'oldname':oldtax[rank]})
    return result
    
def verify_id(table, field, id):
    q_check = "SELECT * FROM `"+table+"` WHERE `"+field+"`='"+id+"'"
    myconn.execute_fetch_one(q_check)
    if myconn.cursor.rowcount == 0:
        return False
    else:
        return True
        
def run_insert(args):
    update_ids = {
                'domain_id':    '1',
                'phylum_id':    '1',
                'klass_id':     '1',
                'order_id':     '1',
                'family_id':    '1',
                'genus_id':     '1',
                'species_id':   '1',
                'subspecies_id':'1'
    }
    with open(args.infile) as csv_file: 
        csv_reader = csv.DictReader(csv_file, delimiter='\t') # KK tab
        for row in csv_reader:
            print('\n\notid',row['HMT'].split('-')[1])
            otid = row['HMT'].split('-')[1]
            # verify that 'new' otid is not arleady in db
            verify = verify_id('otid_prime', 'otid', otid)
            if verify:
                sys.exit('otid:'+otid+' Exists -- Exiting')
            tax_list = row['Taxonomy'].split(';')
            status = row['status']
            #genome = row['genomes']
            print(tax_list)
            insert_list = []
            for i,taxname in enumerate(tax_list):
                insert_list.append({'rank':ranks[i],'newname':taxname})
            print(insert_list)
            # verify that 'new' otid is not arleady in db
            # split taxonomy and get/create IDs
            update_ids = get_ids(args, update_ids, insert_list)  #{'rank': 'species', 'newname': 'sp._HMT_902'
            print('after',update_ids)
            
            q_update1 = "INSERT into taxonomy (domain_id,phylum_id,klass_id,order_id,family_id,genus_id,species_id,subspecies_id)"
            q_update1 += " VALUES('%s','%s','%s','%s','%s','%s','%s','%s')"
            q_update1 = q_update1 % (str(update_ids['domain_id']),str(update_ids['phylum_id']),str(update_ids['klass_id']),
            str(update_ids['order_id']),str(update_ids['family_id']),str(update_ids['genus_id']),
            str(update_ids['species_id']),str(update_ids['subspecies_id']))
            q_select = "SELECT taxonomy_id from taxonomy WHERE domain_id='%s' and phylum_id='%s' and klass_id='%s'and order_id='%s' and family_id='%s'and genus_id='%s'and species_id='%s'and subspecies_id='%s'"
            q_select = q_select % (str(update_ids['domain_id']),str(update_ids['phylum_id']),str(update_ids['klass_id']),
            str(update_ids['order_id']),str(update_ids['family_id']),str(update_ids['genus_id']),
            str(update_ids['species_id']),str(update_ids['subspecies_id']))
            if args.verbose:
                print(q_update1)
            if args.go:
                try:
                    myconn.execute_no_fetch(q_update1)
                    tax_id = myconn.cursor.lastrowid
                except:
                    result = myconn.execute_fetch_one(q_select)
                    print('taxID',result[0])
                    tax_id = result[0]
                    
                print('tax_id',tax_id)
                q_otid = "INSERT into otid_prime (otid,otid_name,taxonomy_id,ncbi_taxon_id,status)"
                q_otid += " VALUES('%s','%s','%s','%s','%s')"
                q_otid = q_otid % (str(otid),str(row['HMT']),str(tax_id),'0',status)
                print(q_otid)
                myconn.execute_no_fetch(q_otid)
            
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
    parser.add_argument("-insert", "--insert",   required=False,  action="store_true",    dest = "insert", default=False,
                                                    help="")
    parser.add_argument("-update", "--update",   required=False,  action="store_true",    dest = "update", default=False,
                                                    help="")                                                 
    args = parser.parse_args()
    
    if not args.insert and not args.update:
        print(usage)
        sys.exit('Need to specify (-update or -insert) and --infile')
    
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
    if args.verbose:
        print()
    if not args.infile:
        print(usage)
        sys.exit()
        
    if args.update:
        get_current_taxonomy(args) 
        run_update(args)
        
    elif args.insert:
        run_insert(args)
    else:
        print(usage)
        sys.exit()
    if not args.go:
        print('\n *** Add "-g/--go" to the command line to update database ***\n')
    else:
        print('\nDone\n')
    