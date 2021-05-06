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
genome_tbl = 'seq_genomes'

master_tax_lookup={}
acceptable_genome_flags = ('11','12','21','91')

query_taxa ="""
SELECT otid, taxonomy_id, genus, species,
`warning`,  
`status`,  
ncbi_taxon_id as ncbi_taxid
from otid_prime
join taxonomy using(taxonomy_id)
join genus using(genus_id)
join species using(species_id)
"""
query_gene_count ="""
SELECT otid, seq_id
from {tbl}
WHERE flag_id in {flags}
ORDER BY otid
""".format(tbl=genome_tbl,flags=acceptable_genome_flags)

counts = {}
master_lookup = {}

def create_taxon(otid):
    """  alternative to a Class which seems to not play well with JSON """
    taxon = {}
    taxon['otid'] = otid
    taxon['status'] = ''
    taxon['genus'] = ''
    taxon['species'] = ''
    taxon['warning'] = ''
    
    taxon['ncbi_taxid'] = ''
    taxon['genomes'] = []
    taxon['type_strains'] = []
    taxon['ref_strains'] = []
    taxon['synonyms'] = []
    taxon['sites'] = []
    
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
                #print(n,toadd)
                if n=='status' and toadd == 'Dropped':
                   pass
                else:
                    if n=='status':
                        taxonObj['status'] = toadd 
                    if n=='genus':  #list
                        taxonObj['genus'] = toadd 
                    elif n=='species':  #list
                        taxonObj['species'] = toadd
                    elif n=='warning':  #list
                        taxonObj['warning'] = toadd 
            
                    elif n=='ncbi_taxid':  #list
                        taxonObj['ncbi_taxid'] = toadd    
                    else:
                        #taxonObj[n] = toadd.replace('"','').replace("'","").replace(',','')
                        pass
            #master_lookup[obj['otid']] = ast.literal_eval(TaxonEncoder().encode(taxonObj))
            #print(taxonObj)
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
            if master_lookup[otid]['status'] != 'Dropped':
                master_lookup[otid]['genomes'].append(obj['seq_id'])
        else:
            sys.exit('problem with genome exiting') 
    


def run_synonyms(args):
    global master_lookup
    q = """
    select otid, synonym from synonym
    """
    result = myconn.execute_fetch_select_dict(q)
    for obj in result:
        otid = str(obj['otid'])
        if otid in master_lookup:
            if master_lookup[otid]['status'] != 'Dropped':
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
            if master_lookup[otid]['status'] != 'Dropped':
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
            if master_lookup[otid]['status'] != 'Dropped':
                master_lookup[otid]['sites'].append(obj['site'])
        else:
            sys.exit('problem with site exiting') 
    
    
   
def run_ref_strain(args):
    global master_lookup
    q = """
    select otid, reference_strain from ref_strain
    """
    result = myconn.execute_fetch_select_dict(q)
    for obj in result:
        otid = str(obj['otid'])
        if otid in master_lookup:
            if master_lookup[otid]['status'] != 'Dropped':
                master_lookup[otid]['ref_strains'].append(obj['reference_strain'])
        else:
            sys.exit('problem with reference_strain exiting') 


def run_refseq(args):
    global refseq_lookup
    global master_lookup
    query_refseqid = "SELECT otid,refseqid, seqname, strain, genbank FROM taxon_refseqid"
    result = myconn.execute_fetch_select_dict(query_refseqid)
    refseq_lookup = {}
    for obj in result:
        #print(obj)
        otid = str(obj['otid'])
        
        if otid not in refseq_lookup:
            refseq_lookup[otid] = []
             #'refseqid': '956_1687', 'seqname': 'cinerea', 'strain': 'Strain: ATCC 14685', 'genbank': 'GB: NR_121687'}
        newobj = {}
        newobj['refseqid'] =  obj['refseqid']
        newobj['seqname']  =  obj['seqname']
        newobj['strain']   =  obj['strain'] 
        newobj['genbank']  =  obj['genbank'] 
        #newobj['status']   =  obj['status'] 
        #newobj['site']     =  obj['site'] 
        #newobj['flag']     =  obj['flag']    
        refseq_lookup[otid].append(newobj)
    file=os.path.join(args.outdir,args.outfileprefix+'RefSeqLookup.json')
    print_dict(file, refseq_lookup)

    

#############################

def run_info(args):  ## prev general,  On its own lookup
    global master_lookup
    q = "SELECT otid, general, prevalence, cultivability, disease_associations, phenotypic_characteristics FROM taxon_info"
    result = myconn.execute_fetch_select_dict(q)

    lookup = {}

    for obj in result:
        #print(obj)
       
        #print(n)
        otid = str(obj['otid'])
        # remove any double quotes but single quotes are ok (to preserve links)
        lookup[otid] = {}
        lookup[otid]['otid']    = otid
        lookup[otid]['culta']   = obj['cultivability']
        lookup[otid]['disease'] = obj['disease_associations']
        lookup[otid]['general'] = obj['general']
        lookup[otid]['pheno']   = obj['phenotypic_characteristics']
        lookup[otid]['prev']    = obj['prevalence']
            
    file = os.path.join(args.outdir,args.outfileprefix+'InfoLookup.json')
    print_dict(file, lookup) 
    

    

def run_references(args):   ## REFERENCE Citations
    
    lookup = {}
    q =  "SELECT otid,pubmed_id,journal,authors,`title` from reference"
    result = myconn.execute_fetch_select_dict(q)
    
    for obj in result:
        #print(obj)
        otid = str(obj['otid'])
        
        #if otid not in lookup:
        lookup[otid] = []
            
        lookup[otid].append(
            {'pubmed_id':obj['pubmed_id'],
              'journal': obj['journal'].replace('"',"'").replace('&quot;',"'").replace('&#039;',"'").replace('\r',"").replace('\n',""),
              'authors': obj['authors'],
              'title':   obj['title'].replace('"',"'").replace('&quot;',"'").replace('&#039;',"'").replace('\r',"").replace('\n',"")
            })
        
    file = os.path.join(args.outdir,args.outfileprefix+'ReferencesLookup.json')
    print_dict(file, lookup)        
    
   




def run_lineage(args):
    global counts
    global refseq_lookup
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
        num_refseqs = 0
        if otid in refseq_lookup:
            num_refseqs = len(refseq_lookup[otid])
        
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
            this_obj['species'] =  obj['genus']+' '+obj['species']
            obj_list.append(this_obj)
            obj_lookup[otid] = this_obj
            tax_list = [obj['domain'],obj['phylum'],obj['klass'],obj['order'],obj['family'],obj['genus'],obj['species']]
           
            run_counts(tax_list, num_genomes, num_refseqs)
    
    file1 = os.path.join(args.outdir,args.outfileprefix+'Lineagelookup.json')
    file2 = os.path.join(args.outdir,args.outfileprefix+'Hierarchy.json')
    
    print_dict(file1, obj_lookup)
    print_dict(file2, obj_list)
    
    file = os.path.join(args.outdir,args.outfileprefix+'Counts.json')
    print_dict(file, counts)
    
    file =  os.path.join(args.outdir,args.outfileprefix+'Lookup.json')  
    print_dict(file, master_lookup) 
    
def run_counts(taxlist,gcnt, rfcnt):
    global counts
    #print(taxlist)
    
        
    for m in range(len(ranks)): # 7
        tax_name = taxlist[m]
                    
        sumdtaxname = []
        for d in range(m+1):
            sumdtaxname.append(taxlist[d])
        if len(sumdtaxname) == 7:   # species only
            #print(sumdtaxname)
            sumdtaxname[-1] = sumdtaxname[-2]+' '+sumdtaxname[-1]
            #print(sumdtaxname)
        long_tax_name = ';'.join(sumdtaxname)
            #print('long_tax_name ',long_tax_name)
        if long_tax_name in counts:
            counts[long_tax_name]["tax_cnt"] += 1
            counts[long_tax_name]['gcnt']    += gcnt
            counts[long_tax_name]['refcnt']  += rfcnt
        else:
            # this will always be species
            counts[long_tax_name] = { "tax_cnt": 1, "gcnt": gcnt, "refcnt": rfcnt}
            
    return counts        
            

   
def print_dict(filename, dict):
    print('writing',filename)
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
    parser.add_argument("-o", "--outfileprefix",   required=False,  action="store",   dest = "outfileprefix", default='homdData-Taxon',
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
        args.DATABASE  = 'homdAV'
        dbhost = '192.168.1.40'
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
    print('running taxa (run defs in order)')
    
    run_taxa(args)   # RUN FIRST in master_lookup => homd_data_taxalookup.json
   
    run_get_genomes(args)  # in master_lookup => homd_data_taxalookup.json
    run_synonyms(args)     # in master_lookup
    run_type_strain(args)  # in master_lookup
    run_sites(args)        # in master_lookup
    run_ref_strain(args)   # in master_lookup
    run_refseq(args)       # in master_lookup
    

#     print('running info')
    run_info(args)
#     print('running references')
    run_references(args)

    
     # run lineage AFTER to get counts
    run_lineage(args)


    