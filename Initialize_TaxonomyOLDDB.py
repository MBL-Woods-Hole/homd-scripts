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
taxon_tbl           = 'taxon_list'   # UNIQUE  - This is the defining table 
warning_tbl         = '1_warning'   # Unique
status_tbl          = '1_status'    # Unique
site_tbl            = 'taxonid_site'  # NOT Unique
synonyms_tbl        = '1_synonyms'    # OTID 0 UNIQUE  FIX
synonyms_tbl2       = '1_synonyms_correct'    # OTID 1 NOT UNIQUE  FIX

type_strain_tbl     = '1_type_strain'   # NOT UNIQUE FIX
ref_strain_tbl      = '1_reference_strain'   # NOT UNIQUE NOT USED 

ncbi_tax_tbl        = '1_ncbi_taxonomy'  # OTID 1 NOT UNIQUE  FIX

cult_info_tbl       = '1_cultivability'   # OTID 1 NOT UNIQUE  FIX
disease_info_tbl    = '1_disease_associations'  # OTID 1 NOT UNIQUE  FIX
general_info_tbl    = '1_general'               # OTID 1 NOT UNIQUE  FIX
pheno_info_tbl      = '1_phenotypic_characteristics' # OTID 1 NOT UNIQUE  FIX
prev_info_tbl       = '1_prevalence'                # OTID 1 NOT UNIQUE  FIX
original_tax_tbl    = 'original_taxontable'         # Unique
refs_tbl            = '1_references'    # NOT UNIQUE
refseqid            = 'taxonid_refseqid_seq'  # NOT UNIQUE
## Number of genomes-- NOT THE SAME database need another connection
otids_per_genomes   = 'HOMD_seqid_taxonid_index'

master_tax_lookup={}

query_refseqid = """
SELECT taxonid as otid, refseqid, seqname, strain, genbank, status,site,flag
from {tbl}
ORDER BY otid
""".format(tbl=refseqid)

query_gene_count ="""
SELECT oral_taxon_id as otid, seq_id
from {tbl}
ORDER BY oral_taxon_id
""".format(tbl=otids_per_genomes)

query_refs ="""
SELECT oral_taxon_id as otid, pubmed_id, journal, authors, title
from {tbl}
ORDER BY oral_taxon_id
""".format(tbl=refs_tbl)

query_taxa ="""
SELECT a.oral_taxon_id as otid, a.genus, a.species,
b.warning as `warning`,  
IFNULL(c.group,       'unknown') as `status`,  
IFNULL(d.site,        'unknown') as `site`,
e.synonyms as `synonyms`,  
f.type_strain as `type_strain`,
g.reference_strain as `ref_strain`,
h.NCBI_taxon_id as NCBI_taxid

FROM    {tbl0} a
LEFT JOIN {tbl1} b
    ON a.oral_taxon_id = b.oral_taxon_id
LEFT JOIN {tbl2} c
    ON a.oral_taxon_id = c.oral_taxon_id
LEFT JOIN {tbl3} d
    ON a.oral_taxon_id = d.oral_taxon_id
LEFT JOIN {tbl4} e
    ON a.oral_taxon_id = e.oral_taxon_id
LEFT JOIN {tbl5} f
    ON a.oral_taxon_id = f.oral_taxon_id
LEFT JOIN {tbl6} g
    ON a.oral_taxon_id = g.oral_taxon_id
LEFT JOIN {tbl7} h
    ON a.oral_taxon_id = h.oral_taxon_id
ORDER BY otid
""".format(tbl0=taxon_tbl,tbl1=warning_tbl,tbl2=status_tbl,tbl3=site_tbl,tbl4=synonyms_tbl2,tbl5=type_strain_tbl,tbl6=ref_strain_tbl,tbl7=ncbi_tax_tbl)

## These should all be unique to otid but the tables show non-unique
query_info ="""  
SELECT a.oral_taxon_id as otid, 
IFNULL(b.description, '') as `culta`, 
IFNULL(c.description, '') as `disease`,  
IFNULL(d.description, '') as `general`,  
IFNULL(e.description, '') as `pheno`,
IFNULL(f.description, '') as `prev`
FROM    {tbl0} a
LEFT JOIN    {tbl1} b
    ON a.oral_taxon_id = b.oral_taxon_id 
LEFT JOIN {tbl2} c
    ON a.oral_taxon_id = c.oral_taxon_id
LEFT JOIN {tbl3} d
    ON a.oral_taxon_id = d.oral_taxon_id
LEFT JOIN {tbl4} e
    ON a.oral_taxon_id = e.oral_taxon_id
LEFT JOIN {tbl5} f
    ON a.oral_taxon_id = f.oral_taxon_id    
ORDER BY otid
""".format(tbl0=taxon_tbl,tbl1=cult_info_tbl,tbl2=disease_info_tbl,tbl3=general_info_tbl,tbl4=pheno_info_tbl,tbl5=prev_info_tbl,)

# query_lineage ="""
# SELECT oral_taxon_id as otid,Domain as domain,Phylum as phylum,Class as klass,`Order` as `order`,Family as family,Genus as genus, Species as species 
# from {tbl}
# ORDER BY oral_taxon_id 
# """.format(tbl=original_tax_tbl)

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
    taxon['type_strain'] = []
    taxon['ref_strain'] = []
    taxon['synonyms'] = []
    taxon['site'] = []
    return taxon

def create_info(otid):
    """  alternative to a Class which seems to not play well with JSON """
    info = {}
    info['otid'] = otid
    info['culta'] = ''
    info['disease'] = ''
    info['general'] = ''
    info['pheno'] = ''
    info['prev'] = ''
    return info
    

    
       
            
            
def run_taxa(args):
    global master_lookup
    result = myconn_tax.execute_fetch_select_dict(query_taxa)
    #split_code = '&lt;BR&gt;'

    
    #print(result)
    for obj in result:
        #print(obj)
        if obj['otid'] not in master_lookup:
            # create ne taxon object with empty values
            taxonObj = create_taxon(obj['otid']) 
            
            for n in obj:
                #print('n',n)
                toadd = str(obj[n]).strip()
            
                if n =='type_strain':  #list
                    if toadd not in taxonObj['type_strain']:
                        taxonObj['type_strain'].append(toadd)
           
                elif n=='ref_strain':  #list  
                    if toadd not in taxonObj['ref_strain']:
                        taxonObj['ref_strain'].append(toadd)  
            
                elif n=='synonyms':  #list
                    if toadd not in taxonObj['synonyms']:
                        taxonObj['synonyms'].append(toadd)  
                
                elif n=='site':  #list
                    if toadd not in taxonObj['site']:
                        taxonObj['site'].append(toadd) 
                elif n=='genus':  #list
                        taxonObj['genus'] = toadd 
                elif n=='species':  #list
                        taxonObj['species'] = toadd
                elif n=='warning':  #list
                        taxonObj['warning'] = toadd 
                elif n=='status':  #list
                        taxonObj['status'] = toadd 
                elif n=='NCBI_taxid':  #list
                        taxonObj['NCBI_taxid'] = toadd    
                else:
                    #taxonObj[n] = toadd.replace('"','').replace("'","").replace(',','')
                    pass
            #master_lookup[obj['otid']] = ast.literal_eval(TaxonEncoder().encode(taxonObj))
            master_lookup[obj['otid']] = taxonObj
            


        else:
            # is already in master list
            pass
        #print(taxonObj.__dict__) 
        
           
def run_get_genome_count(args):  ## add this data to master_lookup
    global master_lookup
    result = myconn_gen.execute_fetch_select_dict(query_gene_count)
    
    
    for obj in result:
        #print(obj)
        if obj['otid'] not in master_lookup:
            print('Adding an Empty Taxon this needs attention! (otid='+str(obj['otid'])+')  -Continuing')
            taxonObj = create_taxon(obj['otid'])   # create an empty taxon object
            
            if obj['seq_id'] not in taxonObj['genomes']:
                taxonObj['genomes'].append(obj['seq_id'])
            #print(taxonObj)
            #print(TaxonEncoder().encode(taxonObj))
            #master_lookup[obj['otid']] = ast.literal_eval(TaxonEncoder().encode(taxonObj))
            master_lookup[obj['otid']] = taxonObj
            #continue
            #master_lookup[obj['otid']] = {}
        else:   
            #print(master_lookup[obj['otid']])
            #print()
            #print(master_lookup[obj['otid']].genomes)
            #print()
            master_lookup[obj['otid']]['genomes'].append(obj['seq_id']) 
    #print(taxonObj.__dict__)     
    file =  os.path.join(args.outdir,args.outfileprefix+'_taxalookup.json')   
    
    fix_object_before_print()
    
    with open(file, 'w') as outfile:
        json.dump(master_lookup, outfile, indent=args.indent)
    
    #print_dict(file, master_lookup) 





def run_info(args):  ## prev general,  On its own lookup
    global master_lookup
    result = myconn_tax.execute_fetch_select_dict(query_info)

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
            # remove any double quotes but single quotes are ok (to preserve links)
            lookup[obj['otid']][n] = str(obj[n]) \
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
    
    result = myconn_tax.execute_fetch_select_dict(query_refs)
    lookup = {}
    
    
    
    for obj in result:
        #print(obj)
        if obj['otid'] not in lookup:
            lookup[obj['otid']] = []
            
        lookup[obj['otid']].append(
            {'pubmed_id':obj['pubmed_id'],
              'journal': obj['journal'].replace('"',"'").replace('&quot;',"'").replace('&#039;',"'").replace('\r',"").replace('\n',""),
              'authors': obj['authors'],
              'title':   obj['title'].replace('"',"'").replace('&quot;',"'").replace('&#039;',"'").replace('\r',"").replace('\n',"")
            })
        
    file = os.path.join(args.outdir,args.outfileprefix+'_refslookup.json')
    print_dict(file, lookup)        
    
   




# def run_counts(args):
#     global counts
#     result = myconn_tax.execute_fetch_select_dict(query_lineage)
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


def run_refseq(args):
    result = myconn_tax.execute_fetch_select_dict(query_refseqid)
    lookup = {}
    for obj in result:
        #print(obj)
        if obj['otid'] not in lookup:
            lookup[obj['otid']] = []
             #'refseqid': '956_1687', 'seqname': 'cinerea', 'strain': 'Strain: ATCC 14685', 'genbank': 'GB: NR_121687'}
        newobj = {}
        newobj['refseqid'] =  obj['refseqid']
        newobj['seqname']  =  obj['seqname']
        newobj['strain']   =  obj['strain'] 
        newobj['genbank']  =  obj['genbank'] 
        newobj['status']   =  obj['status'] 
        newobj['site']     =  obj['site'] 
        newobj['flag']     =  obj['flag']    
        lookup[obj['otid']].append(newobj)
    file=os.path.join(args.outdir,args.outfileprefix+'_refseq.json')
    
    print_dict(file, lookup)
    
    
def print_dict(filename, dict):
    with open(filename, 'w') as outfile:
        json.dump(dict, outfile, indent=args.indent)
    
def fix_object_before_print():
    """
      lists: site,  type_strain, ref_strain
        genomes and synonyms leave empty (if already empty)
        Purpose is to prevent errors in filtering list
    """
    global master_lookup
    for n in master_lookup:
        #print(master_lookup[n])
        if len(master_lookup[n]['site']) == 0: 
            master_lookup[n]['site'] = [''] 
        if len(master_lookup[n]['ref_strain']) == 0:
            master_lookup[n]['ref_strain'] = [''] 
        if len(master_lookup[n]['type_strain']) == 0:
            master_lookup[n]['type_strain'] = ['']     

def run_lineage(args,table_selection):
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
        
    """
    if table_selection == 'oral':
        tables   = ['2_ItemLink_OralTaxonId_oral','2_ItemLink_Item_oral', '2_ClassifyTitle_oral']
        file1 = os.path.join(args.outdir,args.outfileprefix+'_oral_lineagelookup.json')
        file2 = os.path.join(args.outdir,args.outfileprefix+'_oral_hierarchy.json')
    else:
        tables = ['2_ItemLink_OralTaxonId',     '2_ItemLink_Item','2_ClassifyTitle']
        file1 = os.path.join(args.outdir,args.outfileprefix+'_nonoral_lineagelookup.json')
        file2 = os.path.join(args.outdir,args.outfileprefix+'_nonoral_hierarchy.json')
        
    q1 = "select item_id as species_id, oral_taxon_id as otid from {tbl}".format(tbl=tables[0])
    q2 = "select item1_id as id, taxonid_count as tax_cnt, seq_id_count as gne_cnt, sequenced_count as 16s_cnt \
           from {tbl} where item2_id={id}"
    first_result = myconn_tax.execute_fetch_select_dict(q1)
    obj_list = []
    obj_lookup = {}
    
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
            #print(int(level))
            #print(ranks[0])
            rank = ranks[int(level)]
            if rank == 'species':
                tax_name = parent_name+' '+tax_name
            this_obj[rank] = tax_name
            parent_name = tax_name
        if otid in obj_lookup:
            sys.exit('ERROR otid NOT unique')
        
        obj_lookup[otid] = this_obj
        obj_list.append(this_obj)
    
  
    
    
    print_dict(file1, obj_lookup)
    
    
    print_dict(file2, obj_list)

def run_counts(args,table_selection):
    """
   
   Counts doesn't tally up anything
   It just pulls count fields from the database that were tallied previosly
        
    """

    if table_selection == 'oral':
        tables   = ['2_ItemLink_OralTaxonId_oral','2_ItemLink_Item_oral', '2_ClassifyTitle_oral']
        file = os.path.join(args.outdir,args.outfileprefix+'_oral_taxcounts.json')
    else:
        tables = ['2_ItemLink_OralTaxonId',     '2_ItemLink_Item',      '2_ClassifyTitle']
        file = os.path.join(args.outdir,args.outfileprefix+'_nonoral_taxcounts.json')
    
    q1 = "select item_id as species_id, oral_taxon_id as otid from {tbl}".format(tbl=tables[0])  #  +2_ItemLink_OralTaxonId"
    
    
    # q2 = "select item1_id as id, item_title, taxonid_count as tax_cnt, seq_id_count as gne_cnt, \
#           sequenced_count as 16s_cnt from 2_ItemLink_Item AS a \
#            JOIN 2_ClassifyTitle AS b ON (a.item2_id = b.item_id) \
#            WHERE item2_id={}"
    q2 = "select item1_id as id, item_title, taxonid_count as tax_cnt, seq_id_count as gne_cnt, \
          sequenced_count as 16s_cnt from {tbl1} AS a \
           JOIN {tbl2} AS b ON (a.item2_id = b.item_id) \
           WHERE item2_id={id}"
           
    first_result = myconn_tax.execute_fetch_select_dict(q1)
    obj_list = []
    lineage_obj = {}
    
    for obj in first_result:
        # for each otid build up the taxonomy from species => domain
        this_obj = {}
        
        otid = obj['otid']
        this_obj['otid'] = otid
        species_id = str(obj['species_id'])
        #print('species_id',species_id)   # is item2
        
        species_result = myconn_tax.execute_fetch_select_dict(q2.format(tbl1=tables[1],tbl2=tables[2],id=str(species_id)))
        #print(species_id,genus_result)
        s_tax_cnt = str(species_result[0]['tax_cnt'])
        s_gne_cnt = str(species_result[0]['gne_cnt'])
        s_16s_cnt = str(species_result[0]['16s_cnt'])
        genus_id = str(species_result[0]['id'])
        species_name = str(species_result[0]['item_title'])
        
        genus_result = myconn_tax.execute_fetch_select_dict(q2.format(tbl1=tables[1],tbl2=tables[2],id=str(genus_id)))
        #print(species_id,genus_result)
        g_tax_cnt = str(genus_result[0]['tax_cnt'])
        g_gne_cnt = str(genus_result[0]['gne_cnt'])
        g_16s_cnt = str(genus_result[0]['16s_cnt'])
        family_id = str(genus_result[0]['id'])
        genus_name = str(genus_result[0]['item_title'])
        
        family_result = myconn_tax.execute_fetch_select_dict(q2.format(tbl1=tables[1],tbl2=tables[2],id=str(family_id)))
        f_tax_cnt = str(family_result[0]['tax_cnt'])
        f_gne_cnt = str(family_result[0]['gne_cnt'])
        f_16s_cnt = str(family_result[0]['16s_cnt'])
        order_id = str(family_result[0]['id'])
        family_name = str(family_result[0]['item_title'])
        
        order_result = myconn_tax.execute_fetch_select_dict(q2.format(tbl1=tables[1],tbl2=tables[2],id=str(order_id)))
        o_tax_cnt = str(order_result[0]['tax_cnt'])
        o_gne_cnt = str(order_result[0]['gne_cnt'])
        o_16s_cnt = str(order_result[0]['16s_cnt'])
        class_id = str(order_result[0]['id'])
        order_name = str(order_result[0]['item_title'])
        
        class_result = myconn_tax.execute_fetch_select_dict(q2.format(tbl1=tables[1],tbl2=tables[2],id=str(class_id)))
        c_tax_cnt = str(class_result[0]['tax_cnt'])
        c_gne_cnt = str(class_result[0]['gne_cnt'])
        c_16s_cnt = str(class_result[0]['16s_cnt'])
        phylum_id = str(class_result[0]['id'])
        class_name = str(class_result[0]['item_title'])
        
        phylum_result = myconn_tax.execute_fetch_select_dict(q2.format(tbl1=tables[1],tbl2=tables[2],id=str(phylum_id)))
        #print(class_id,phylum_result)
        p_tax_cnt = str(phylum_result[0]['tax_cnt'])
        p_gne_cnt = str(phylum_result[0]['gne_cnt'])
        p_16s_cnt = str(phylum_result[0]['16s_cnt'])
        domain_id = str(phylum_result[0]['id'])
        phylum_name = str(phylum_result[0]['item_title'])
        
        domain_result = myconn_tax.execute_fetch_select_dict(q2.format(tbl1=tables[1],tbl2=tables[2],id=str(domain_id)))
        d_tax_cnt = str(domain_result[0]['tax_cnt'])
        d_gne_cnt = str(domain_result[0]['gne_cnt'])
        d_16s_cnt = str(domain_result[0]['16s_cnt'])
        #domain_id = str(domain_result[0]['id'])
        domain_name = str(domain_result[0]['item_title'])
        
        if domain_name not in lineage_obj:
            lineage_obj[domain_name] = {'tax_cnt':d_tax_cnt,'gne_cnt':d_gne_cnt,'16s_cnt':d_16s_cnt}
        
        p = domain_name+';'+phylum_name
        if p not in lineage_obj:
            lineage_obj[p] = {'tax_cnt':p_tax_cnt,'gne_cnt':p_gne_cnt,'16s_cnt':p_16s_cnt}
        
        c = domain_name+';'+phylum_name+';'+class_name
        if c not in lineage_obj:
            lineage_obj[c] = {'tax_cnt':c_tax_cnt,'gne_cnt':c_gne_cnt,'16s_cnt':c_16s_cnt}
        
        o = domain_name+';'+phylum_name+';'+class_name+';'+order_name
        if o not in lineage_obj:
            lineage_obj[o] = {'tax_cnt':o_tax_cnt,'gne_cnt':o_gne_cnt,'16s_cnt':o_16s_cnt}
            
        f = domain_name+';'+phylum_name+';'+class_name+';'+order_name+';'+family_name
        if f not in lineage_obj:
            lineage_obj[f] = {'tax_cnt':f_tax_cnt,'gne_cnt':f_gne_cnt,'16s_cnt':f_16s_cnt}
            
        g = domain_name+';'+phylum_name+';'+class_name+';'+order_name+';'+family_name+';'+genus_name
        if g not in lineage_obj:
            lineage_obj[g] = {'tax_cnt':g_tax_cnt,'gne_cnt':g_gne_cnt,'16s_cnt':g_16s_cnt}
        
        s = domain_name+';'+phylum_name+';'+class_name+';'+order_name+';'+family_name+';'+genus_name+';'+species_name
        if s not in lineage_obj:
            lineage_obj[s] = {'tax_cnt':s_tax_cnt,'gne_cnt':s_gne_cnt,'16s_cnt':s_16s_cnt}
            
    
    
    #print(counts) 
    
    print_dict(file, lineage_obj)
    
   
    
               
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
        args.TAX_DATABASE  = 'HOMD_taxonomy'
        args.GENE_DATABASE = 'HOMD_genomes_new'
        dbhost = 'localhost'
    else:
        sys.exit('dbhost - error')
    args.indent = None
    if args.prettyprint:
        args.indent = 4
    myconn_tax = MyConnection(host=dbhost, db=args.TAX_DATABASE,   read_default_file = "~/.my.cnf_node")
    myconn_gen = MyConnection(host=dbhost, db=args.GENE_DATABASE,  read_default_file = "~/.my.cnf_node")

    print(args)
    print('running taxa')
    run_taxa(args)
    print('adding genome counts')
    run_get_genome_count(args)
    print('running info')
    run_info(args)
    print('running references')
    run_refs(args)
    print('running refseq')
    run_refseq(args)
    print('running lineage')
    run_lineage(args,'nonoral')
    run_lineage(args,'oral')
    print('running lineage counts')
    run_counts(args,'nonoral')
    run_counts(args,'oral')
    
    
    