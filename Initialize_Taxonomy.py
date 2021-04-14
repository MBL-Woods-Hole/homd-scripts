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
try:
    import mysqlclient as mysql
except ImportError:
    try:
        import pymysql as mysql
    except ImportError:
        import MySQLdb as mysql
import datetime
ranks = ['domain','phylum','klass','order','family','genus','species']
today = str(datetime.date.today())

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

## These should all be unique to otid but the tables shoe non-unique
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
class MyConnection:
    """
    Takes parameters from ~/.my.cnf, default host = "localhost", db="test"
    if different use my_conn = MyConnection(host, db)
    """

    def __init__(self, host = "localhost", db="test", read_default_file = ""):
        # , read_default_file=os.path.expanduser("~/.my.cnf"), port = 3306

        self.conn = None
        self.cursor = None
        self.cursorD = None
        self.rows = 0
        self.new_id = None
        self.lastrowid = None

        port_env = 3306
        try:
            print("host = " + str(host) + ", db = "+str(db))
            print("=" * 40)
            read_default_file = os.path.expanduser("~/.my.cnf_node")

            if is_local():
                host = "127.0.0.1"
                read_default_file = "~/.my.cnf_node"
            self.conn = mysql.connect(host = host, db = db, read_default_file = read_default_file, port = port_env)
            self.cursor = self.conn.cursor()
            self.cursorD = self.conn.cursor(mysql.cursors.DictCursor)

        except (AttributeError, mysql.OperationalError):
            self.conn = mysql.connect(host = host, db = db, read_default_file = read_default_file, port = port_env)
            self.cursor = self.conn.cursor()
        except mysql.Error:
            e = sys.exc_info()[1]
            print("Error %d: %s" % (e.args[0], e.args[1]))
            raise
        except:  # catch everything
            print("Unexpected:")
            print(sys.exc_info()[0])
            raise  # re-throw caught exception

    @staticmethod
    def connect(host, db, read_default_file, port_env):
        print('host ',host,' db ',db)
        return mysql.connect(host = host, db = db, read_default_file = read_default_file, port = port_env)

    def execute_fetch_select(self, sql):
        if self.cursor:
            try:
                self.cursor.execute(sql)
                return self.cursor.fetchall()
            except:
                print("ERROR: query = %s" % sql)
                raise

    def execute_no_fetch(self, sql):
        if self.cursor:
            self.cursor.execute(sql)
            self.conn.commit()
            try:
                return self.cursor._result.message
            except:
                return self.cursor._info

    def execute_fetch_select_dict(self, sql):
        if self.cursorD:
            try:
                self.cursorD.execute(sql)
                return self.cursorD.fetchall()
            except:
                print("ERROR: query = %s" % sql)
                raise
def is_local():
    print(os.uname()[1])
    dev_comps = ['avoorhis.mbl.edu', "Joannes-MacBook-Air.local"]
    if os.uname()[1] in dev_comps:
        return True
    else:
        return False


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
    

    
       
def create_lineage(otid):
    """  alternative to a Class which seems to not play well with JSON """
    lineage = {}
    lineage['otid'] = otid
    lineage['domain'] = ''
    lineage['phylum'] = ''
    lineage['class'] = ''
    lineage['order'] = ''
    lineage['family'] = ''
    lineage['genus'] = ''
    lineage['strain'] = ''
    
    return lineage
            
            
            
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
    
# def run_lineage(args):   ##Domain,Phylum,Class,Order, Family,Genus,Species
#     global master_lookup
#     result = myconn_tax.execute_fetch_select_dict(query_lineage)
#     lookup = {}
#     for otid in master_lookup:
#         #print(otid)
#         if otid not in lookup:
#             infoObj = create_lineage(otid)
#             lookup[otid] = infoObj
#     
#     for obj in result:
#         #print(obj)
#         lookup[obj['otid']] = obj
#         
#     file1 = os.path.join(args.outdir,args.outfileprefix+'_lineagelookup.json')
#     print_dict(file1, lookup)
#     file2 = os.path.join(args.outdir,args.outfileprefix+'_hierarchy.json')
#     
#     print_dict(file2, result)
    

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

def run_new_lineage(args):
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
    global counts
    q1 = "select item_id as species_id, oral_taxon_id as otid from 2_ItemLink_OralTaxonId"
    q2 = "select item1_id as id from 2_ItemLink_Item where item2_id={}"
    first_result = myconn_tax.execute_fetch_select_dict(q1)
    obj_list = []
    obj_lookup = {}
    
    for obj in first_result:
        # for each otid build up the taxonomy from species => domain
        this_obj = {}
        
        otid = obj['otid']
        this_obj['otid'] = otid
        species_id = str(obj['species_id'])
        
        genus_result = myconn_tax.execute_fetch_select_dict(q2.format(str(species_id)))
        genus_id = str(genus_result[0]['id'])
        
        family_result = myconn_tax.execute_fetch_select_dict(q2.format(str(genus_id)))
        family_id = str(family_result[0]['id'])
        
        order_result = myconn_tax.execute_fetch_select_dict(q2.format(str(family_id)))
        order_id = str(order_result[0]['id'])
        
        class_result = myconn_tax.execute_fetch_select_dict(q2.format(str(order_id)))
        class_id = str(class_result[0]['id'])
        
        phylum_result = myconn_tax.execute_fetch_select_dict(q2.format(str(class_id)))
        phylum_id = str(phylum_result[0]['id'])
        
        domain_result = myconn_tax.execute_fetch_select_dict(q2.format(str(phylum_id)))
        domain_id = str(domain_result[0]['id'])
        
        id_list = [domain_id,phylum_id,class_id,order_id,family_id,genus_id,species_id]
        
        q3= "select item_title as tax_name, level from 2_ClassifyTitle where item_id in (\""+'\",\"'.join(id_list)+"\") ORDER BY level"
        #print(q3)
        final_result = myconn_tax.execute_fetch_select_dict(q3)
        lineage = []
        for obj2 in final_result:
            #print(obj2)
            level = obj2['level']  # 0 for domain
            tax_name = obj2['tax_name']
            lineage.append(tax_name)
            #print(int(level))
            #print(ranks[0])
            this_obj[ranks[int(level)]] = tax_name
        counts = get_counts(lineage) 
        if otid in obj_lookup:
            sys.exit('ERROR otid NOT unique')
        
        obj_lookup[otid] = this_obj
        obj_list.append(this_obj)
    
    #print(counts) 
    file=os.path.join(args.outdir,args.outfileprefix+'_taxcounts.json')
    
    print_dict(file, counts)
    
    file1 = os.path.join(args.outdir,args.outfileprefix+'_lineagelookup.json')
    print_dict(file1, obj_lookup)
    
    file2 = os.path.join(args.outdir,args.outfileprefix+'_hierarchy.json')
    print_dict(file2, obj_list)

def get_counts(gline):
    global counts

    if args.verbose:
        print('\ncounts::parsing ',gline)
    for m in range(len(ranks)): # 7
        tax_name = gline[m]
        
        #counts = get_counts(counts,  m, lst[n])

        sumdtaxname = []
        for d in range(m+1):
            sumdtaxname.append(gline[d])
        long_tax_name = ';'.join(sumdtaxname)
        #print('long_tax_name ',long_tax_name)
        if  long_tax_name in counts:
            counts[long_tax_name] +=1
        else:
            counts[long_tax_name] = 1
    if args.verbose:
        print('returning: ',counts)
    return counts
    
               
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
    run_taxa(args)
    run_get_genome_count(args)
    run_info(args)
##    run_lineage(args)
    run_refs(args)
 ##   run_counts(args)
    run_refseq(args)
    
    run_new_lineage(args)
    
    
    
    