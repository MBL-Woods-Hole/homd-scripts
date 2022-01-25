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


collector = {}  
def run(args):
    with open(args.infile) as csv_file: 
        csv_reader = csv.DictReader(csv_file, delimiter='\t') # KK tab
        for row in csv_reader:
            #print(row['HMT-old'],row['HMT-new'])
            if row['HMT-old'] != row['HMT-new']:
                sys.exit('hmts dont match')
            hmt = row['HMT-old']
            collector[hmt] = {}
            collector[hmt]['new_taxonomy'] = {}
            collector[hmt]['old_taxonomy'] = {}
            news=[]
            olds=[]
            for name in headers:
                news.append(row[name+'-new'])
                olds.append(row[name+'-old'])
            new_tax = ';'.join(news)
            old_tax = ';'.join(olds)
            if new_tax == old_tax:
                print('SAME',hmt)
                print(new_tax)
                print(old_tax)
                
            collector[hmt]['new_taxonomy'] = new_tax
            collector[hmt]['old_taxonomy'] = old_tax
            
            
            
            
                    
            
    print(collector['910']) 
    #sys.exit()       
        
def runX(args):
    update_collector = {}
    for hmt in collector:
        oldtax = collector[hmt]['old_taxonomy']
        newtax = collector[hmt]['new_taxonomy']
        
        res = compare(oldtax,newtax)
        if res:
            if args.verbose:
                print()
                print(hmt)
            # update_collector[hmt] = {}
#             update_collector[hmt]['taxonomy_id'] = collector[hmt]['taxonomy_id']
#             update_collector[hmt]['update'] = res
            tax_id = collector[hmt]['taxonomy_id']
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
            for item in res:
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
    
    
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", default=False,
                                                    help="verbose print()") 
    
    args = parser.parse_args()
    
    #parser.print_help(usage)
    
    args.outdir = './'                         
    
    
    #myconn_new = MyConnection(host=dbhost_new, db=args.NEW_DATABASE,  read_default_file = "~/.my.cnf_node")
    if args.verbose:
        print()
    if not args.infile:
        print(usage)
        sys.exit()
        
      
    run(args)
    