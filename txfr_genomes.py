#!/usr/bin/env python

## SEE https://docs.dhtmlx.com/suite/tree__api__refs__tree.html // new version 7 must load from json file
# this script creates a list of json objects that allows the dhtmlx javascript library
# to parse and show a taxonomy tree (Written for HOMD)
##
import os, sys
import json
#from json import JSONEncoder
import argparse
#import ast
from connect import MyConnection
import datetime
ranks = ['domain','phylum','klass','order','family','genus','species']
today = str(datetime.date.today())

# TABLES
taxon_tbl           = 'taxon_list'   # UNIQUE  - This is the defining table 



master_tax_lookup={}



query_taxa ="""
SELECT a.oral_taxon_id as otid, a.genus as genusTT, a.species as speciesTT
from {tbl} as a

ORDER BY otid
""".format(tbl=taxon_tbl)


counts = {}
tt_lookup = {}

def create_taxon(otid):
    """   """
    taxon = {}
    taxon['otid'] = otid
    taxon['genus'] = ''
    taxon['species'] = ''
    return taxon
    
q_tax = "SELECT \
   `otid_prime`.`otid` AS `otid`, \
   `genus`.`genus` AS `genus`,genus.genus_id, \
   `species`.`species` AS `species`,species.species_id \
FROM ((((((((`taxonomy` join `otid_prime` on((`taxonomy`.`taxonomy_id` = `otid_prime`.`taxonomy_id`))) join `domain` on((`taxonomy`.`domain_id` = `domain`.`domain_id`))) join `phylum` on((`taxonomy`.`phylum_id` = `phylum`.`phylum_id`))) join `klass` on((`taxonomy`.`klass_id` = `klass`.`klass_id`))) join `order` on((`taxonomy`.`order_id` = `order`.`order_id`))) join `family` on((`taxonomy`.`family_id` = `family`.`family_id`))) join `genus` on((`taxonomy`.`genus_id` = `genus`.`genus_id`))) join `species` on((`taxonomy`.`species_id` = `species`.`species_id`))) order by `otid_prime`.`otid`;"

q_gene = "SELECT seq_id, genus, species, flag,culture_collection,status, \
IFNULL(sequence_center, '') as sequence_center, \
IFNULL(number_contig, '') as number_contig, \
IFNULL(combined_length, '') as combined_length, \
IFNULL(oral_pathogen, '') as oral_pathogen \
FROM seq_genomes"       




q_index = "SELECT seq_id, otid FROM seqid_otid_index"             
            
def get_flags(args):
    q1 = "SELECT seqid_flag_id,seqid_flag from seqid_flag"
    flag_result = myconn_new.execute_fetch_select(q1)
    #print(flag_result)
    
def get_genus_species(args):
    tax_result = myconn_new.execute_fetch_select_dict(q_tax)
    tax_genus_sp_lookup = {}
    index_lookup = {}
    for n in tax_result:
        if str(n['otid']) in tax_genus_sp_lookup:
            sys.exit('tax error')
        tax_genus_sp_lookup[str(n['otid'])] = {'genus':n['genus'],'genus_id':n['genus_id'],'species_id':n['species_id'], 'species':n['species']}
    
    #for n in tax_genus_sp_lookup:
        #print(n,tax_genus_sp_lookup[n] )       
    # now get genome genus sp
    idx_result = myconn_new.execute_fetch_select_dict(q_index)
    for n in idx_result:
        if n['seq_id'] in index_lookup:
            sys.exit('tax error')
        index_lookup[n['seq_id']] = str(n['otid'])
    #print(index_lookup)
    for n in index_lookup:
        #print(n,index_lookup[n])
        pass
    gen_result = myconn_gene.execute_fetch_select_dict(q_gene)
    missing_seqs = []
    missing_otid = []
    for n in gen_result:
        print(n)
        seq_id = n['seq_id']
        flag_id = n['flag']
        oralpath  = n['oral_pathogen']
        clength = n['combined_length']
        ncontigs = n['number_contig']
        seq_center = n['sequence_center'].replace('\r','').replace('\n','')
        status = n['status']
        ccolct = n['culture_collection']
        
        
        if seq_id in index_lookup:
            
            otid = str(index_lookup[seq_id])
            print('madeit-1',otid)
            if otid in tax_genus_sp_lookup:
                print('madeit-2')
                
                new_genus = tax_genus_sp_lookup[otid]['genus']
                new_species = tax_genus_sp_lookup[otid]['species']
                gid = tax_genus_sp_lookup[otid]['genus_id']
                sid = tax_genus_sp_lookup[otid]['species_id']
                gen_genus = n['genus']
                gen_species= n['species']
                if new_genus != gen_genus:
                    print (new_genus,gen_genus)
                if new_species != gen_species:
                    print (new_species,gen_species)
               #print('seqid',seqid,'otid',otid,'new genus',new_genus,'new species',new_species)
                q_insert = "INSERT IGNORE into seq_genomes (seq_id,genus_id,species_id,flag_id,oral_pathogen,"
                q_insert += "combined_length,number_contig,sequence_center,status,culture_collection) "
                q_insert += "VALUES ('"+seq_id+"','"+str(gid)+"','"+str(sid)+"','"+str(flag_id)+"','"+oralpath+"','"+str(clength)+"','"+str(ncontigs)+"','"+seq_center+"','"+status+"','"+ccolct+"')"
                print(q_insert)
                myconn_new.execute_no_fetch(q_insert)
            else:
                if otid not in missing_otid:
                   missing_otid.append(otid)
                
        else:
            if seq_id not in missing_seqs:
                missing_seqs.append(seq_id)
    #print('missing otids',missing_otid)
    #print('missing seqs',missing_seqs)
    
    
    
if __name__ == "__main__":

    usage = """
    USAGE:
        takes the taxonomy from the old homd to the new
        
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=False,  action="store",   dest = "infile", default='none',
                                                    help=" ")
    parser.add_argument("-o", "--outfileprefix",   required=False,  action="store",   dest = "outfileprefix", default='homd_data',
                                                    help=" ")
    parser.add_argument("-outdir", "--out_directory", required = False, action = 'store', dest = "outdir", default = './',
                         help = "Not usually needed if -host is accurate")
    parser.add_argument("-host", "--host",
                        required = False, action = 'store', dest = "dbhost", default = 'localhost',
                        help = "choices=['homd',  'localhost']")
    parser.add_argument("-pp", "--prettyprint",
                        required = False, action = 'store_true', dest = "prettyprint", default = False,
                        help = "output file is human friendly")
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", default=False,
                                                    help="verbose print()") 
    args = parser.parse_args()
    #parser.print_help(usage)
    if not os.path.exists(args.outdir):
        print("\nThe out put directory doesn't exist:: using the current dir instead\n")
        args.outdir = './'                         
    if args.dbhost == 'homd':
        #args.json_file_path = '/groups/vampsweb/vamps/nodejs/json'
        args.GEN_DATABASE = 'HOMD_genomes_new'
        args.NEW_DATABASE = 'homdAV'
        dbhost = '192.168.1.51'
        args.outdir = '../homd-startup-data/'
        args.prettyprint = False

    elif args.dbhost == 'localhost':
        #args.json_file_path = '/Users/avoorhis/programming/homd-data/json'
        args.GEN_DATABASE  = 'HOMD_genomes_new'
        args.NEW_DATABASE = 'homdAV'
        dbhost = 'localhost'
    else:
        sys.exit('dbhost - error')
    args.indent = None
    if args.prettyprint:
        args.indent = 4
    myconn_gene = MyConnection(host=dbhost, db=args.GEN_DATABASE,   read_default_file = "~/.my.cnf_node")
    myconn_new = MyConnection(host=dbhost, db=args.NEW_DATABASE,  read_default_file = "~/.my.cnf_node")

    print(args)
    print('get_flags')
    get_flags(args)
    get_genus_species(args)
    
    