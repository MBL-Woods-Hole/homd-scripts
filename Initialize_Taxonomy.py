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

import datetime
ranks = ['domain','phylum','klass','order','family','genus','species']
today = str(datetime.date.today())

from connect import MyConnection

# TABLES
taxon_tbl           = 'otid_prime'   # UNIQUE  - This is the defining table 


master_tax_lookup={}


query_taxa ="""
SELECT otid, taxonomy_id, genus, species,
`warning`,  
`status`,  
NCBI_taxon_id
from otid_prime
join taxonomy using(taxonomy_id)
join genus using(genus_id)
join species using(species_id)
"""
query_gene_count ="""
SELECT otid, seq_id
from seq_genomes
ORDER BY otid
"""

counts = {}
master_lookup = {}

def create_taxon(otid):
    """  alternative to a Class which seems to not play well with JSON """
    taxon = {}
    taxon['otid'] = otid
    taxon['genus'] = ''
    taxon['species'] = ''
    taxon['warning'] = ''
    taxon['status'] = ''
    taxon['NCBI_taxid'] = ''
    taxon['genomes'] = []
    taxon['type_strains'] = []
    taxon['ref_strains'] = []
    taxon['synonyms'] = []
    taxon['sites'] = []
    taxon['ref_seqs'] = []
    
    return taxon


    
       
            
            
def run_taxa(args):
    global master_lookup
    #print(query_taxa)
    result = myconn.execute_fetch_select_dict(query_taxa)
    #split_code = '&lt;BR&gt;'

    
    #print(result)
    for obj in result:
        #print(obj)
        otid = str(obj['otid'])
        if otid not in master_lookup:
            # create ne taxon object with empty values
            taxonObj = create_taxon(otid) 
            
            for n in obj:
                #print('n',n)
                toadd = str(obj[n]).strip()
            
                if n=='genus':  #list
                        taxonObj['genus'] = toadd 
                elif n=='species':  #list
                        taxonObj['species'] = toadd
                elif n=='warning':  #list
                        taxonObj['warning'] = toadd 
                elif n=='status':  #list
                        taxonObj['status'] = toadd 
                elif n=='NCBI_taxid':  #list
                        taxonObj['NCBI_taxon_id'] = toadd    
                else:
                    #taxonObj[n] = toadd.replace('"','').replace("'","").replace(',','')
                    pass
            #master_lookup[obj['otid']] = ast.literal_eval(TaxonEncoder().encode(taxonObj))
            master_lookup[otid] = taxonObj
            


        else:
            # is already in master list
            pass
        #print(master_lookup) 
        
           
def run_get_genomes(args):  ## add this data to master_lookup
    global master_lookup
    result = myconn.execute_fetch_select_dict(query_gene_count)
    
    
    for obj in result:
        #print(obj)
        otid = str(obj['otid'])
        if otid in master_lookup:
            master_lookup[otid]['genomes'].append(obj['seq_id'])
        else:
            sys.exit('problem with genome exiting') 
    #print(taxonObj.__dict__)     
     
    
    #fix_object_before_print()
    
    #with open(file, 'w') as outfile:
    #    json.dump(master_lookup, outfile, indent=args.indent)
    
    


def run_synonyms(args):
    global master_lookup
    q = """
    select otid, synonym from synonym
    """
    result = myconn.execute_fetch_select_dict(q)
    for obj in result:
        otid = str(obj['otid'])
        if otid in master_lookup:
            master_lookup[otid]['synonyms'].append(obj['synonym'])
        else:
            sys.exit('problem with synonym exiting') 
    
    
    
def run_type_strain(args):
    global master_lookup
    q = """
    select otid, type_strain from type_strain
    """
    result = myconn.execute_fetch_select_dict(q)
    for obj in result:
        otid = str(obj['otid'])
        if otid in master_lookup:
            master_lookup[otid]['type_strains'].append(obj['type_strain'])
        else:
            sys.exit('problem with type_strain exiting') 
    
    

def run_sites(args):
    global master_lookup
    q = """
    select otid, site from site
    """
    result = myconn.execute_fetch_select_dict(q)
    for obj in result:
        otid = str(obj['otid'])
        if otid in master_lookup:
            master_lookup[otid]['sites'].append(obj['site'])
        else:
            sys.exit('problem with site exiting') 
    
    
   
def run_ref_strain(args):
    pass


def run_refseq(args):
    global master_lookup
    query_refseqid = "SELECT otid,refseqid, seqname, strain, genbank FROM otid_refseqid"
    result = myconn.execute_fetch_select_dict(query_refseqid)
    lookup = {}
    for obj in result:
        #print(obj)
        otid = str(obj['otid'])
        if otid in master_lookup:
            master_lookup[otid]["ref_seqs"].append(obj['refseqid'])
        else:
            sys.exit('problem with refseqid exiting') 
        if otid not in lookup:
            lookup[otid] = []
             #'refseqid': '956_1687', 'seqname': 'cinerea', 'strain': 'Strain: ATCC 14685', 'genbank': 'GB: NR_121687'}
        newobj = {}
        newobj['refseqid'] =  obj['refseqid']
        newobj['seqname']  =  obj['seqname']
        newobj['strain']   =  obj['strain'] 
        newobj['genbank']  =  obj['genbank'] 
        #newobj['status']   =  obj['status'] 
        #newobj['site']     =  obj['site'] 
        #newobj['flag']     =  obj['flag']    
        lookup[otid].append(newobj)
    file=os.path.join(args.outdir,args.outfileprefix+'_refseq.json')
    print_dict(file, lookup)

    file =  os.path.join(args.outdir,args.outfileprefix+'_taxalookup.json')  
    print_dict(file, master_lookup) 

#############################
def run_info(args):  ## prev general,  On its own lookup
    global master_lookup
    result = myconn.execute_fetch_select_dict(query_info)

    lookup = {}
    #for obj in result:
    for otid in master_lookup:
        #print(otid)
        if otid not in lookup:
            infoObj = create_info(otid)
            lookup[otid] = infoObj
    for obj in result:
        
        for n in obj:
            #print(n)
            otid = str(obj['otid'])
            # remove any double quotes but single quotes are ok (to preserve links)
            lookup[otid][n] = str(obj[n]) \
                .strip() \
                .replace('"',"'") \
                .replace('&amp;#39;',"'") \
                .replace(',','') \
                .replace('&lt;','<') \
                .replace('&gt;','>') \
                .replace('&amp;nbsp;',' ') \
                .replace('&nbsp;',' ') \
                .replace('&quot;',"'") \
                .replace('\r',"").replace('\n',"")
    file = os.path.join(args.outdir,args.outfileprefix+'_infolookup.json')
    print_dict(file, lookup) 
    

    

def run_refs(args):   ## REFERENCE Citations
    
    result = myconn.execute_fetch_select_dict(query_refs)
    lookup = {}
    
    
    
    for obj in result:
        #print(obj)
        otid = str(obj['otid'])
        if otid not in lookup:
            lookup[otid] = []
            
        lookup[otid].append(
            {'pubmed_id':obj['pubmed_id'],
              'journal': obj['journal'].replace('"',"'").replace('&quot;',"'").replace('&#039;',"'").replace('\r',"").replace('\n',""),
              'authors': obj['authors'],
              'title':   obj['title'].replace('"',"'").replace('&quot;',"'").replace('&#039;',"'").replace('\r',"").replace('\n',"")
            })
        
    file = os.path.join(args.outdir,args.outfileprefix+'_refslookup.json')
    print_dict(file, lookup)        
    
   




# def run_counts(args):
#     global counts
#     result = myconn.execute_fetch_select_dict(query_lineage)
#     for obj in result:
#         #print(obj)
#         taxlist = []
#         taxlist.append(obj['domain'])
#         taxlist.append(obj['phylum'])
#         taxlist.append(obj['klass'])
#         taxlist.append(obj['order'])
#         taxlist.append(obj['family'])
#         taxlist.append(obj['genus'])
#         taxlist.append(obj['species'])
#         counts = get_counts(taxlist)
#     
#     file=os.path.join(args.outdir,args.outfileprefix+'_taxcounts.json')
#     
#     print_dict(file, counts)
#     



    
    

    
def fix_object_before_print():
    global master_lookup
    """
      lists: site,  type_strain, ref_strain
        genomes and synonyms leave empty (if already empty)
        Purpose is to prevent errors in filtering list
    """
    
    for n in master_lookup:
        #print(master_lookup[n])
        if len(master_lookup[n]['site']) == 0: 
            master_lookup[n]['site'] = [''] 
        if len(master_lookup[n]['ref_strain']) == 0:
            master_lookup[n]['ref_strain'] = [''] 
        if len(master_lookup[n]['type_strain']) == 0:
            master_lookup[n]['type_strain'] = ['']     

def run_lineage(args):
    global counts
    global master_lookup
    """
    we need both a list and a lookup 
    lookup:
    {
    "1": {
        "otid": 1,
        "domain": "Bacteria",
        "phylum": "Proteobacteria",
        "klass": "Alphaproteobacteria",
        ......
        
    list:
    [
    {
        "otid": 1,
        "domain": "Bacteria",
        "phylum": "Proteobacteria",
        "klass": "Alphaproteobacteria",
        ......
    
    
    select otid,domain,phylum,klass,`order`,family,genus,species
from otid_prime
JOIN taxonomy using(taxonomy_id)
JOIN domain using(domain_id)
JOIN phylum using(phylum_id)
JOIN klass using(klass_id)
JOIN `order` using(order_id)
JOIN family  using(family_id)
JOIN genus using(genus_id)
JOIN species  using(species_id)
    
    """
    
    qtax = """select otid,domain,phylum,klass,`order`,family,genus,species
        from otid_prime
        JOIN taxonomy using(taxonomy_id)
        JOIN domain using(domain_id)
        JOIN phylum using(phylum_id)
        JOIN klass using(klass_id)
        JOIN `order` using(order_id)
        JOIN family  using(family_id)
        JOIN genus using(genus_id)
        JOIN species  using(species_id)
      """
    
    result = myconn.execute_fetch_select_dict(qtax)
    
        
    obj_list = []
    obj_lookup = {}
    for obj in result:
        #print(obj)
        # for each otid build up the taxonomy from species => domain
        this_obj = {}
        
        otid = str(obj['otid'])
        # how many seqs??
        # Number of 16S rRNA RefSeqs ??
        num_genomes = len(master_lookup[otid]['genomes'])
        num_refseqs = len(master_lookup[otid]['ref_seqs'])
        # if otid in master_lookup and otid=='550':
#             print('otid',otid,' num genomes:',num_genomes)
        obj_lookup[otid] = {}
        if obj['domain']:
            this_obj['otid'] = otid
            this_obj['domain'] = obj['domain']
            this_obj['phylum'] =  obj['phylum']
            this_obj['klass'] =  obj['klass']
            this_obj['order'] =  obj['order']
            this_obj['family'] =  obj['family']
            this_obj['genus'] =  obj['genus']
            this_obj['species'] =  obj['species']
            obj_list.append(this_obj)
            obj_lookup[otid] = this_obj
            tax_list = [obj['domain'],obj['phylum'],obj['klass'],obj['order'],obj['family'],obj['genus'],obj['species']]
            
            run_counts2(tax_list, num_genomes, num_refseqs)
    
    file1 = os.path.join(args.outdir,args.outfileprefix+'_lineagelookup.json')
    file2 = os.path.join(args.outdir,args.outfileprefix+'_hierarchy.json')
    
    print_dict(file1, obj_lookup)
    print_dict(file2, obj_list)
    
    file = os.path.join(args.outdir,args.outfileprefix+'_NEWtaxcounts.json')
    
    print_dict(file, counts)
    
def run_counts2(taxlist,gcnt, rfcnt):
    global counts
    #print(taxlist)
    
        
    for m in range(len(ranks)): # 7
        tax_name = taxlist[m]
                    
        sumdtaxname = []
        for d in range(m+1):
            sumdtaxname.append(taxlist[d])
        long_tax_name = ';'.join(sumdtaxname)
            #print('long_tax_name ',long_tax_name)
        if long_tax_name in counts:
            counts[long_tax_name]["tax_cnt"] += 1
            counts[long_tax_name]['gcnt']    += gcnt
            counts[long_tax_name]['refcnt']  += rfcnt
        else:
            
            counts[long_tax_name] = { "tax_cnt": 1, "gcnt": gcnt, "refcnt": rfcnt}
            
    return counts        
            
# def run_counts(args,table_selection):
#     """
#    
#    Counts doesn't tally up anything
#    It just pulls count fields from the database that were tallied previosly
#         
#     """
# 
#     if table_selection == 'oral':
#         tables   = ['2_ItemLink_OralTaxonId_oral','2_ItemLink_Item_oral', '2_ClassifyTitle_oral']
#         file = os.path.join(args.outdir,args.outfileprefix+'_oral_taxcounts.json')
#     else:
#         tables = ['2_ItemLink_OralTaxonId',     '2_ItemLink_Item',      '2_ClassifyTitle']
#         file = os.path.join(args.outdir,args.outfileprefix+'_nonoral_taxcounts.json')
#     
#     q1 = "select item_id as species_id, oral_taxon_id as otid from {tbl}".format(tbl=tables[0])  #  +2_ItemLink_OralTaxonId"
#     
#     
#     # q2 = "select item1_id as id, item_title, taxonid_count as tax_cnt, seq_id_count as gne_cnt, \
# #           sequenced_count as 16s_cnt from 2_ItemLink_Item AS a \
# #            JOIN 2_ClassifyTitle AS b ON (a.item2_id = b.item_id) \
# #            WHERE item2_id={}"
#     q2 = "select item1_id as id, item_title, taxonid_count as tax_cnt, seq_id_count as gne_cnt, \
#           sequenced_count as 16s_cnt from {tbl1} AS a \
#            JOIN {tbl2} AS b ON (a.item2_id = b.item_id) \
#            WHERE item2_id={id}"
#            
#     first_result = myconn.execute_fetch_select_dict(q1)
#     obj_list = []
#     lineage_obj = {}
#     
#     for obj in first_result:
#         # for each otid build up the taxonomy from species => domain
#         this_obj = {}
#         
#         otid = obj['otid']
#         this_obj['otid'] = otid
#         species_id = str(obj['species_id'])
#         #print('species_id',species_id)   # is item2
#         
#         species_result = myconn.execute_fetch_select_dict(q2.format(tbl1=tables[1],tbl2=tables[2],id=str(species_id)))
#         #print(species_id,genus_result)
#         s_tax_cnt = str(species_result[0]['tax_cnt'])
#         s_gne_cnt = str(species_result[0]['gne_cnt'])
#         s_16s_cnt = str(species_result[0]['16s_cnt'])
#         genus_id = str(species_result[0]['id'])
#         species_name = str(species_result[0]['item_title'])
#         
#         genus_result = myconn.execute_fetch_select_dict(q2.format(tbl1=tables[1],tbl2=tables[2],id=str(genus_id)))
#         #print(species_id,genus_result)
#         g_tax_cnt = str(genus_result[0]['tax_cnt'])
#         g_gne_cnt = str(genus_result[0]['gne_cnt'])
#         g_16s_cnt = str(genus_result[0]['16s_cnt'])
#         family_id = str(genus_result[0]['id'])
#         genus_name = str(genus_result[0]['item_title'])
#         
#         family_result = myconn.execute_fetch_select_dict(q2.format(tbl1=tables[1],tbl2=tables[2],id=str(family_id)))
#         f_tax_cnt = str(family_result[0]['tax_cnt'])
#         f_gne_cnt = str(family_result[0]['gne_cnt'])
#         f_16s_cnt = str(family_result[0]['16s_cnt'])
#         order_id = str(family_result[0]['id'])
#         family_name = str(family_result[0]['item_title'])
#         
#         order_result = myconn.execute_fetch_select_dict(q2.format(tbl1=tables[1],tbl2=tables[2],id=str(order_id)))
#         o_tax_cnt = str(order_result[0]['tax_cnt'])
#         o_gne_cnt = str(order_result[0]['gne_cnt'])
#         o_16s_cnt = str(order_result[0]['16s_cnt'])
#         class_id = str(order_result[0]['id'])
#         order_name = str(order_result[0]['item_title'])
#         
#         class_result = myconn.execute_fetch_select_dict(q2.format(tbl1=tables[1],tbl2=tables[2],id=str(class_id)))
#         c_tax_cnt = str(class_result[0]['tax_cnt'])
#         c_gne_cnt = str(class_result[0]['gne_cnt'])
#         c_16s_cnt = str(class_result[0]['16s_cnt'])
#         phylum_id = str(class_result[0]['id'])
#         class_name = str(class_result[0]['item_title'])
#         
#         phylum_result = myconn.execute_fetch_select_dict(q2.format(tbl1=tables[1],tbl2=tables[2],id=str(phylum_id)))
#         #print(class_id,phylum_result)
#         p_tax_cnt = str(phylum_result[0]['tax_cnt'])
#         p_gne_cnt = str(phylum_result[0]['gne_cnt'])
#         p_16s_cnt = str(phylum_result[0]['16s_cnt'])
#         domain_id = str(phylum_result[0]['id'])
#         phylum_name = str(phylum_result[0]['item_title'])
#         
#         domain_result = myconn.execute_fetch_select_dict(q2.format(tbl1=tables[1],tbl2=tables[2],id=str(domain_id)))
#         d_tax_cnt = str(domain_result[0]['tax_cnt'])
#         d_gne_cnt = str(domain_result[0]['gne_cnt'])
#         d_16s_cnt = str(domain_result[0]['16s_cnt'])
#         #domain_id = str(domain_result[0]['id'])
#         domain_name = str(domain_result[0]['item_title'])
#         
#         if domain_name not in lineage_obj:
#             lineage_obj[domain_name] = {'tax_cnt':d_tax_cnt,'gne_cnt':d_gne_cnt,'16s_cnt':d_16s_cnt}
#         
#         p = domain_name+';'+phylum_name
#         if p not in lineage_obj:
#             lineage_obj[p] = {'tax_cnt':p_tax_cnt,'gne_cnt':p_gne_cnt,'16s_cnt':p_16s_cnt}
#         
#         c = domain_name+';'+phylum_name+';'+class_name
#         if c not in lineage_obj:
#             lineage_obj[c] = {'tax_cnt':c_tax_cnt,'gne_cnt':c_gne_cnt,'16s_cnt':c_16s_cnt}
#         
#         o = domain_name+';'+phylum_name+';'+class_name+';'+order_name
#         if o not in lineage_obj:
#             lineage_obj[o] = {'tax_cnt':o_tax_cnt,'gne_cnt':o_gne_cnt,'16s_cnt':o_16s_cnt}
#             
#         f = domain_name+';'+phylum_name+';'+class_name+';'+order_name+';'+family_name
#         if f not in lineage_obj:
#             lineage_obj[f] = {'tax_cnt':f_tax_cnt,'gne_cnt':f_gne_cnt,'16s_cnt':f_16s_cnt}
#             
#         g = domain_name+';'+phylum_name+';'+class_name+';'+order_name+';'+family_name+';'+genus_name
#         if g not in lineage_obj:
#             lineage_obj[g] = {'tax_cnt':g_tax_cnt,'gne_cnt':g_gne_cnt,'16s_cnt':g_16s_cnt}
#         
#         s = domain_name+';'+phylum_name+';'+class_name+';'+order_name+';'+family_name+';'+genus_name+';'+species_name
#         if s not in lineage_obj:
#             lineage_obj[s] = {'tax_cnt':s_tax_cnt,'gne_cnt':s_gne_cnt,'16s_cnt':s_16s_cnt}
#             
#     
#     
#     #print(counts) 
#     
#     print_dict(file, lineage_obj)
    
   
def print_dict(filename, dict):
    with open(filename, 'w') as outfile:
        json.dump(dict, outfile, indent=args.indent)    
               
if __name__ == "__main__":

    usage = """
    USAGE:
        homd_init_data.py
        
        will print out the need initialization files for homd
        Needs MySQL: tries to read your ~/.my.cnf_node
        
           -outdir Output directory [default]
        for homd site
           -host homd
           
        for debugging
          -pp  pretty print
          -o <outfile>  Change outfile name from 'taxonomy'*
        
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
        args.GENE_DATABASE = 'HOMD_genomes_new'
        dbhost = '192.168.1.51'
        args.outdir = '../homd-startup-data/'
        args.prettyprint = False

    elif args.dbhost == 'localhost':
        #args.json_file_path = '/Users/avoorhis/programming/homd-data/json'
        args.DATABASE  = 'homdAV'
        dbhost='localhost'
        
    else:
        sys.exit('dbhost - error')
    args.indent = None
    if args.prettyprint:
        args.indent = 4
    myconn = MyConnection(host=dbhost, db=args.DATABASE,   read_default_file = "~/.my.cnf_node")
   

    print(args)
    print('running taxa (run in order)')
    run_taxa(args)
   
    run_get_genomes(args)
    run_synonyms(args)
    run_type_strain(args)
    run_sites(args)
    run_refseq(args)
#     run_ref_strain(args)

#     print('running info')
#     run_info(args)
#     print('running references')
#     run_refs(args)
#     print('running refseq')
    
     # run lineage AFTER to get counts
    run_lineage(args)

#     print('running lineage counts')
#     run_counts(args,'nonoral')
#     run_counts(args,'oral')
    
    
    