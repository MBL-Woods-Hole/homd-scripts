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



q_taxonomy = "select otid,taxonomy_id,domain,domain_id,phylum,phylum_id,klass,klass_id,`order`,order_id,"
q_taxonomy += " family,family_id,genus,genus_id,species,species_id,subspecies,subspecies_id,naming_status,cultivation_status"
q_taxonomy += " from otid_prime"
q_taxonomy += " join taxonomy using(taxonomy_id)"
q_taxonomy += " join domain using(domain_id)"
q_taxonomy += " join phylum using (phylum_id)"
q_taxonomy += " join klass using (klass_id)"
q_taxonomy += " join `order` using (order_id)"
q_taxonomy += " join family using (family_id)"
q_taxonomy += " join genus using(genus_id)"
q_taxonomy += " join species using (species_id)"
q_taxonomy += " join subspecies using (subspecies_id)"

"""
SELECT taxonomy_id, domain,domain_id,phylum,phylum_id,klass,klass_id,`order`,order_id,
family,family_id,genus,genus_id,species,species_id,subspecies,subspecies_id,naming_status,cultivation_status 
from otid_prime
JOIN `taxonomy` using(taxonomy_id)
JOIN `domain` using(domain_id)
JOIN `phylum` using(phylum_id)
JOIN `klass` using(klass_id)
JOIN `order` using(order_id)
JOIN `family` using(family_id)
JOIN `genus` using(genus_id)
JOIN `species` using(species_id)
JOIN `subspecies` using(subspecies_id)
WHERE otid=''
"""

 
 

def get_current_taxonomy(args):
    collector = {} 
    with open(args.infile) as csv_file: 
        csv_reader = csv.DictReader(csv_file, delimiter='\t') # KK tab
        for row in csv_reader:
            #print('row',row)
            if not row['HMT-ID']:
                continue
            #hmt = str(int(row['HMT-ID'].split('-')[1]))
            hmt = row['HMT-ID']
            if '-' in hmt:
                hmt = hmt.split('-')[1]
            collector[hmt] = {}
            collector[hmt]['new_taxonomy'] = {}
            collector[hmt]['old_taxonomy'] = {}
            collector[hmt]['naming_status'] = {}
            collector[hmt]['cultivation_status'] = {}
            for i,rank in enumerate(ranks[:7]):   # headers from infile don't match field names
                name = update_headers[i]
                collector[hmt]['new_taxonomy'][rank] = row[name]
            collector[hmt]['new_taxonomy']['subspecies'] = ''
            # get old tax and tax_id 
            q = q_taxonomy + " WHERE otid='"+hmt+"'"
            #print(q)
            result = myconn.execute_fetch_select_dict(q)
            if myconn.cursor.rowcount == 0:
                sys.exit('No Taxon found: '+row['HMT-ID'] +' -EXITING')
            for taxrow in result:
                #print(n)
                collector[hmt]['taxonomy_id'] = taxrow['taxonomy_id']
                collector[hmt]['naming_status'] = taxrow['naming_status']
                collector[hmt]['cultivation_status'] = taxrow['cultivation_status']
                for rank in ranks:
                    rank_id = taxrow[rank+'_id']
                    collector[hmt]['old_taxonomy'][rank] = taxrow[rank]
                    collector[hmt]['old_taxonomy'][rank+'_id'] = taxrow[rank+'_id']
                    
            
    #print(collector['255'])
    #sys.exit('sysexit')  
    return collector
    #      
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
                    species_id='TBD'
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
                    subspecies_id = 'TBD'
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
                    rank_id = 'TBD'
            else:
                rank_id = result[0]
        
            # Change update_ids
            update_ids[rank+'_id'] = rank_id
    return update_ids
    
def run_update(args):
    print('in update')
    collector = get_current_taxonomy(args) 
    #print('collector',collector)
    update_collector = {}
    for hmt in collector:
        #if collector[hmt]['status'] == 'Dropped':
        #    continue
        #print()
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
        
        diff = compare(oldtax, newtax)
        #print('diff',diff)
        if diff:
                
                
            # update_collector[hmt] = {}
#             update_collector[hmt]['taxonomy_id'] = collector[hmt]['taxonomy_id']
#             update_collector[hmt]['update'] = res
            tax_id = collector[hmt]['taxonomy_id']
            
            if args.verbose:
                print()
                print(hmt,oldtax['genus'],oldtax['species'])
                print('before',update_ids)
            update_ids = get_ids(args, update_ids, diff)  #{'rank': 'species', 'newname': 'sp._HMT_902', 'oldname': 'sp. HMT 902'}
            
            
            if args.verbose:
                print('after ',update_ids)
            
            
            q_update = "UPDATE taxonomy set"
            q_update += " domain_id='%s',"
            q_update += " phylum_id='%s',"
            q_update += " klass_id='%s',"
            q_update += " order_id='%s',"
            q_update += " family_id='%s',"
            q_update += " genus_id='%s',"
            q_update += " species_id='%s'"
            #q_update += " subspecies_id='%s'"
            q_update += " WHERE taxonomy_id='%s'"
            q_update = q_update % (
              str(update_ids['domain_id']),
              str(update_ids['phylum_id']),
              str(update_ids['klass_id']),
              str(update_ids['order_id']),
              str(update_ids['family_id']),
              str(update_ids['genus_id']),
              str(update_ids['species_id']),
              #str(update_ids['subspecies_id']),
              str(tax_id)
            )
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
            print('\n\notid',row['HMT-ID'])
            #print(row)
            #otid = row['HMT-ID'].split('-')[1]
            otid = row['HMT-ID']
            if '-' in otid:
                otid = otid.split('-')[1]
            # verify that 'new' otid is not already in db
            verify = verify_id('otid_prime', 'otid', otid)
            if verify:
                sys.exit('otid:'+otid+' Exists -- Exiting')
            #tax_list = row['Taxonomy'].split(';')
            tax_list = [row['Domain'],row['Phylum'],row['Class'],row['Order'],row['Family'],row['Genus'],row['Species']]
            
            
            naming_status = row['naming_status']
            cultivation_status = row['cultivation_status']
            body_site = row['site']
            #genome = row['genomes']
            print('taxlist:',tax_list)
            insert_list = []
            for i,taxname in enumerate(tax_list):
                insert_list.append({'rank':ranks[i],'newname':taxname})
            print(insert_list)
            
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
                q_otid = "INSERT into otid_prime (otid,otid_name,taxonomy_id,ncbi_taxon_id,naming_status,cultivation_status,primary_body_site)"
                q_otid += " VALUES('%s','%s','%s','%s','%s','%s','%s')"
                q_otid = q_otid % (str(otid),str(row['HMT-ID']),str(tax_id),'0',naming_status,cultivation_status,body_site)
                print(q_otid)
                myconn.execute_no_fetch(q_otid)


def run_accession(args):
    with open(args.infile) as csv_file: 
        csv_reader = csv.DictReader(csv_file, delimiter='\t') # KK tab
        for row in csv_reader:
            otid = row['HMT-ID'].split('_')[1]
            
            acc = row['GTDB']
            q = "UPDATE ignore otid_prime set GTDB_accession='%s' WHERE otid ='%s'"
            q = q % (acc, otid)
            
            print(q)
            if args.go:
                myconn.execute_no_fetch(q)
            
            
if __name__ == "__main__":

    usage = """
    USAGE:
       
     -update  Change Taxon(s) taxonomy
            Tax format: columns
            ./update_homd_taxonomy_lpsn.py -update -i HOMD-new-taxonomy.csv
       
            KISS infile cols:
       
            HMT, Domain...Species 
       
            
       
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
    parser.add_argument("-acc", "--acc",   required=False,  action="store_true",    dest = "accession", default=False,
                                                    help="") 
    args = parser.parse_args()
    
    if not args.insert and not args.update and not args.accession:
        print(usage)
        sys.exit('Need to specify (-update or -insert or -accession) and --infile')
    
    args.outdir = './'                         
    if args.dbhost == 'homd_dev':
        args.NEW_DATABASE = 'homd'
        dbhost = '192.168.1.46'
    elif args.dbhost == 'homd_prod':
        args.NEW_DATABASE = 'homd'
        dbhost = '192.168.1.42'
    elif args.dbhost == 'localhost':
        args.NEW_DATABASE = 'homd'
        dbhost = 'localhost'
        
    else:
        sys.exit('dbhost - error')
    args.indent = None
    
    myconn = MyConnection(host=dbhost, db=args.NEW_DATABASE,  read_default_file = "~/.my.cnf_node")
    if args.verbose:
        print()
    if not args.infile:
        print(usage)
        sys.exit()
        
    if args.update:
        
        run_update(args)
        
    elif args.insert:
        #sys.exit('insert turned off')
        run_insert(args)
    elif args.accession:
        #sys.exit('insert turned off')
        run_accession(args)
    else:
        print(usage)
        sys.exit()
    if not args.go:
        print('\n *** Add "-g/--go" to the command line to update database ***\n')
    else:
        print('\nDone\n')
    