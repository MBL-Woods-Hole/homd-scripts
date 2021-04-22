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
    
       
            
            
def run_taxa(args):
    global tt_lookup
    result = myconn_tax.execute_fetch_select_dict(query_taxa)
    #split_code = '&lt;BR&gt;'

    
    #print(result)
    for obj in result:
        #print(obj)
        if obj['otid'] not in tt_lookup:
            # create ne taxon object with empty values
            taxonObj = create_taxon(obj['otid']) 
            taxonObj['genus'] = obj['genusTT']
            taxonObj['species'] = obj['speciesTT']
            #master_lookup[obj['otid']] = ast.literal_eval(TaxonEncoder().encode(taxonObj))
            tt_lookup[obj['otid']] = taxonObj
        else:
            sys.exit('Problem with taxon_table unique')
            
        #print(taxonObj.__dict__) 
    #print(tt_lookup)       
           


    
def print_dict(filename, dict):
    with open(filename, 'w') as outfile:
        json.dump(dict, outfile, indent=args.indent)
    


def run_lineage(args):
    """
   
        
    """
    global full_tax_lookup
    tables = ['2_ItemLink_OralTaxonId',     '2_ItemLink_Item','2_ClassifyTitle']
    file1 = os.path.join(args.outdir,args.outfileprefix+'_NEW_lineagelookup.json')
    file2 = os.path.join(args.outdir,args.outfileprefix+'_NEW_hierarchy.json')
        
    q1 = "select item_id as species_id, oral_taxon_id as otid from {tbl}".format(tbl=tables[0])
    q2 = "select item1_id as id, taxonid_count as tax_cnt, seq_id_count as gne_cnt, sequenced_count as 16s_cnt \
           from {tbl} where item2_id={id}"
    first_result = myconn_tax.execute_fetch_select_dict(q1)
    full_tax_list = []
    full_tax_lookup = {}
    
    for obj in first_result:
        # for each otid build up the taxonomy from species => domain
        this_obj = {}
        
        otid = obj['otid']
        this_obj['otid'] = otid
        species_id = str(obj['species_id'])
        
        genus_result = myconn_tax.execute_fetch_select_dict(q2.format(tbl=tables[1],id=str(species_id)))
        genus_id = str(genus_result[0]['id'])
        
        family_result = myconn_tax.execute_fetch_select_dict(q2.format(tbl=tables[1],id=str(genus_id)))
        family_id = str(family_result[0]['id'])
        
        order_result = myconn_tax.execute_fetch_select_dict(q2.format(tbl=tables[1],id=str(family_id)))
        order_id = str(order_result[0]['id'])
        
        class_result = myconn_tax.execute_fetch_select_dict(q2.format(tbl=tables[1],id=str(order_id)))
        class_id = str(class_result[0]['id'])
        
        phylum_result = myconn_tax.execute_fetch_select_dict(q2.format(tbl=tables[1],id=str(class_id)))
        phylum_id = str(phylum_result[0]['id'])
        
        domain_result = myconn_tax.execute_fetch_select_dict(q2.format(tbl=tables[1],id=str(phylum_id)))
        domain_id = str(domain_result[0]['id'])
        
        id_list = [domain_id,phylum_id,class_id,order_id,family_id,genus_id,species_id]
        
        q3= "select item_title as tax_name, level from {tbl}".format(tbl=tables[2])
        q3 += " WHERE item_id in (\""+'\",\"'.join(id_list)+"\") ORDER BY level"
        #print('q3',q3)
        final_result = myconn_tax.execute_fetch_select_dict(q3)
        lineage = []
        parent_name = 0
        for obj2 in final_result:
            #print(obj2)
            level = obj2['level']  # 0 for domain
            tax_name = obj2['tax_name']
            lineage.append(tax_name)
            
            rank = ranks[int(level)]
            this_obj[rank] = tax_name
            parent_name = tax_name
        if otid in full_tax_lookup:
            sys.exit('ERROR otid NOT unique')
        
        full_tax_lookup[otid] = this_obj
        full_tax_list.append(this_obj)
    
  
    
    
    print_dict(file1, full_tax_lookup)
    print_dict(file2, full_tax_list)
    check_genus(args)
    transfer(args)

def check_genus(args):
    
    global full_tax_lookup, tt_lookup
    meta_collection = []
    for otid in full_tax_lookup:
    #for otid in [1,2,3,500]:
        print(otid)
        collection = [str(otid)]
#         print(otid)
#         print(full_tax_lookup[otid]['genus'],tt_lookup[otid]['genus'])
#         print(full_tax_lookup[otid]['species'],tt_lookup[otid]['species'])
        if full_tax_lookup[otid]['genus'] != tt_lookup[otid]['genus']:
            print(otid,'genus no match')
            print('Classify:',full_tax_lookup[otid]['genus'],' != taxonTable:',tt_lookup[otid]['genus'])
            
        if full_tax_lookup[otid]['species'] != tt_lookup[otid]['species']:
            print(otid,'species no match')
            print(full_tax_lookup[otid]['species'],tt_lookup[otid]['species'])

def transfer(args): 
     """
    select domain,phylum,klass,`order`,family,genus,species from taxonomy
	JOIN domain using(domain_id)
	JOIN phylum using(phylum_id)
	JOIN klass using (klass_id)
	JOIN `order` using(order_id)
	JOIN family using(family_id)
	JOIN genus using (genus_id)
	JOIN species using (species_id)
	WHERE otid = '500'
    """
    global full_tax_lookup, tt_lookup
    meta_collection = []
    for otid in full_tax_lookup:       
        # domain
        for rank in ranks:
            
            q1 = "INSERT IGNORE INTO `"+rank+"` (`"+rank+"`) VALUES ('"+full_tax_lookup[otid][rank]+"')"
            print(q1)
            myconn_new.execute_no_fetch(q1)
            q2 = "SELECT LAST_INSERT_ID()"
            last_id = myconn_new.execute_fetch_one(q2)
            print('last_id1',last_id)
            print('last_id2',last_id[0])
            if last_id[0] == 0:   # Already exists: Must select again to get the id
                q3 = "SELECT "+rank+"_id from `"+rank+"` WHERE `"+rank+"` = '"+full_tax_lookup[otid][rank]+"'"
                print(q3)
                result = myconn_new.execute_fetch_one(q3)
                rank_id = result[0]
                print('id',rank_id)
                
            else:
                rank_id = last_id[0]
            collection.append(str(rank_id))
            print()
        print(collection) 
        meta_collection.append(collection)
    q5 = "INSERT INTO taxonomy (oral_taxon_id,domain_id,phylum_id,klass_id,order_id,family_id,genus_id,species_id)"
    q5 +=     " VALUES "
    for col in meta_collection:
        q5 += "\n('"+"','".join(col)+"'),"
    q5 = q5[:-1]
    print(q5)
    myconn_new.execute_no_fetch(q5)
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
        args.TAX_DATABASE = 'HOMD_taxonomy'
        args.NEW_DATABASE = 'homdAV'
        dbhost = '192.168.1.51'
        args.outdir = '../homd-startup-data/'
        args.prettyprint = False

    elif args.dbhost == 'localhost':
        #args.json_file_path = '/Users/avoorhis/programming/homd-data/json'
        args.TAX_DATABASE  = 'HOMD_taxonomy'
        args.NEW_DATABASE = 'homdAV'
        dbhost = 'localhost'
    else:
        sys.exit('dbhost - error')
    args.indent = None
    if args.prettyprint:
        args.indent = 4
    myconn_tax = MyConnection(host=dbhost, db=args.TAX_DATABASE,   read_default_file = "~/.my.cnf_node")
    myconn_new = MyConnection(host=dbhost, db=args.NEW_DATABASE,  read_default_file = "~/.my.cnf_node")

    print(args)
    print('run_taxa(args)')
    run_taxa(args)
    print('running lineage')
    run_lineage(args)
    # run_lineage(args,'oral')
#     print('running lineage counts')
#     run_counts(args,'nonoral')
#     run_counts(args,'oral')
    
    
    