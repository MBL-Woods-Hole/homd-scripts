#!/usr/bin/env python

## SEE https://docs.dhtmlx.com/suite/tree__api__refs__tree.html // new version 7 must load from json file
# this script creates a list of json objects that allows the dhtmlx javascript library
# to parse and show a taxonomy tree (Written for HOMD)
##
import os, sys
import gzip
import json
#from json import JSONEncoder
import argparse
import csv,re
from Bio import SeqIO
sys.path.append('../')
sys.path.append('../homd-data/')
sys.path.append('../../homd-data/')

from connect import MyConnection,mysql
import datetime
import requests
global mysql_errors
mysql_errors = []
"""
CREATE TABLE `taxonomy_ranked_clean` (
  `taxonomy_ranked_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `rank` varchar(12) NOT NULL DEFAULT '',
  `fixed_id` varchar(10) NOT NULL DEFAULT '',
  `HMT` varchar(12) DEFAULT '',
  `tax_string` varchar(200) DEFAULT NULL,
  `domain_id` int(11) unsigned DEFAULT '1',
  `phylum_id` int(11) unsigned DEFAULT '1',
  `klass_id` int(11) unsigned DEFAULT '1',
  `order_id` int(11) unsigned DEFAULT '1',
  `family_id` int(11) unsigned DEFAULT '1',
  `genus_id` int(11) unsigned DEFAULT '1',
  `species_id` int(11) unsigned DEFAULT '1',
  `subspecies_id` int(11) unsigned DEFAULT '1',
  PRIMARY KEY (`taxonomy_ranked_id`),
  UNIQUE KEY `fixed_id` (`fixed_id`),
  UNIQUE KEY `rank_ids` (`domain_id`,`phylum_id`,`klass_id`,`order_id`,`family_id`,`genus_id`,`species_id`,`subspecies_id`),
  KEY `taxonomy_rank_ibfk_2` (`phylum_id`),
  KEY `taxonomy_rank_ibfk_3` (`klass_id`),
  KEY `taxonomy_rank_ibfk_4` (`order_id`),
  KEY `taxonomy_rank_ibfk_5` (`family_id`),
  KEY `taxonomy_rank_ibfk_6` (`genus_id`),
  KEY `taxonomy_rank_ibfk_7` (`species_id`),
  KEY `taxonomy_rank_ibfk_8` (`subspecies_id`),
  CONSTRAINT `taxonomy_ranked_clean_ibfk_1` FOREIGN KEY (`domain_id`) REFERENCES `domain` (`domain_id`) ON UPDATE CASCADE,
  CONSTRAINT `taxonomy_ranked_clean_ibfk_2` FOREIGN KEY (`phylum_id`) REFERENCES `phylum` (`phylum_id`) ON UPDATE CASCADE,
  CONSTRAINT `taxonomy_ranked_clean_ibfk_3` FOREIGN KEY (`klass_id`) REFERENCES `klass` (`klass_id`) ON UPDATE CASCADE,
  CONSTRAINT `taxonomy_ranked_clean_ibfk_4` FOREIGN KEY (`order_id`) REFERENCES `order` (`order_id`) ON UPDATE CASCADE,
  CONSTRAINT `taxonomy_ranked_clean_ibfk_5` FOREIGN KEY (`family_id`) REFERENCES `family` (`family_id`) ON UPDATE CASCADE,
  CONSTRAINT `taxonomy_ranked_clean_ibfk_6` FOREIGN KEY (`genus_id`) REFERENCES `genus` (`genus_id`) ON UPDATE CASCADE,
  CONSTRAINT `taxonomy_ranked_clean_ibfk_7` FOREIGN KEY (`species_id`) REFERENCES `species` (`species_id`) ON UPDATE CASCADE,
  CONSTRAINT `taxonomy_ranked_clean_ibfk_8` FOREIGN KEY (`subspecies_id`) REFERENCES `subspecies` (`subspecies_id`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
"""
today = str(datetime.date.today())
ranks = ['domain','phylum','klass','order','family','genus','species','subspecies']

def clean_hmt(s):
    
    return str(int(s.split('-')[1]))  # strips zeros HMT-058 => 58
    
def get_tax_db_ids(tax):
    
    id_obj={}
    for i,name in enumerate(tax):
        rank = ranks[i]
        q = "SELECT %s FROM `%s` WHERE `%s`='%s'" % (rank+'_id',rank,rank,name)
        #print(q)
        row = myconn.execute_fetch_select(q)
        if row[0][0]:
            id_obj[rank] = row[0][0]
        else:
            sys.exit('NO id found: '+rank,'-',name)
    
    return id_obj
    
def run_taxonomy():
    fp = open(args.infile,'r')
    
    for line in fp:
        line = line.strip()
        pts = line.split('\t')
        #print(pts)
        rank_id = pts[0]
        rank = pts[1]
        hmt = pts[2]
        taxonomy = pts[3].split(';')
        print(rank)
        qbase = "INSERT into taxonomy_ranked_clean (`rank`,`fixed_id`,`tax_string`,"
        tax_db_ids = get_tax_db_ids(taxonomy)
        for n in range(ranks.index(rank)+1):
            qbase += ranks[n]+'_id,'
        qbase = qbase[:-1]+") VALUES('"
        
        vals = [rank,rank_id,pts[3]]
        for n in range(ranks.index(rank)+1):
            vals.append(str(tax_db_ids[ranks[n]]))
        q = qbase + "','".join(vals) + "')"
        print(q)
        run_sql(rank,q)
        # qphylum2 += " VALUES('phylum','%s','%s','%s','%s')"
#         q2 = qphylum2  % (rankid,  tax_str, 
#                                 str(row['domain_id']),  
#                                 str(row['phylum_id']) 
#                        )
    
    
    
    sys.exit()
    fout_filename = 'ranked_taxonomy_w_fixed_ids'+today+'.csv'
    fout = open(fout_filename,'w')
    test_hmts = ('1','2','3','4','5','6','297','282','815','377')  # both acenitobacter   815 = Archaea  377=subsp
    sql = len(test_hmts)*'%s,'
    q = "SELECT otid,domain_id,domain,phylum_id,phylum,klass_id,klass,order_id,`order`,family_id,family,genus_id,genus,species_id,species,subspecies_id,subspecies"
    q += " FROM otid_prime"
    q += " JOIN taxonomy using(taxonomy_id)"
    q += " JOIN domain using(domain_id)"
    q += " JOIN phylum using(phylum_id)"
    q += " JOIN klass using(klass_id)"
    q += " JOIN `order` using(order_id)"
    q += " JOIN family using(family_id)"
    q += " JOIN genus using(genus_id)"
    q += " JOIN species using(species_id)"
    q += " JOIN subspecies using(subspecies_id)"
    #q += " WHERE otid in ("+sql[:-1]+")"
    q += " WHERE status != 'Dropped'"
    #q = q % test_hmts
    print(q)
    result = myconn.execute_fetch_select_dict(q)
    print(result)
    text_collector = {}
    for i,row in enumerate(result):
        #DOMAIN
        rankid = 'D'+str(i+101)
        
        tax_str = make_tax_string('domain',row)
        qdomain = "INSERT into taxonomy_ranked (rank,fixed_id,tax_string,domain,domain_id)"
        qdomain += " VALUES('domain','%s','%s','%s','%s')"
        q = qdomain  % (rankid, tax_str, row['domain'], str(row['domain_id']))
        
        qdomain2 = "INSERT into taxonomy_ranked_clean (rank,fixed_id,tax_string,domain_id)"
        qdomain2 += " VALUES('domain','%s','%s','%s')"
        q2 = qdomain2  % (rankid, tax_str, str(row['domain_id']))
        
        print(q)
        run_sql('domain',q)
        run_sql('domain',q2)
        text_collector[tax_str] = {"id":rankid,"rank":"domain", "HMT":''}
        
        #PHYLUM
        rankid = 'P'+str(i+101)
        tax_str = make_tax_string('phylum',row)
        qphylum = "INSERT into taxonomy_ranked (rank,fixed_id,tax_string,domain,domain_id,phylum,phylum_id)"
        qphylum += " VALUES('phylum','%s','%s','%s','%s','%s','%s')"
        q = qphylum  % (rankid,  tax_str,
                                row['domain'], 
                                str(row['domain_id']),
                                row['phylum'],  
                                str(row['phylum_id']) 
                       )
        qphylum2 = "INSERT into taxonomy_ranked_clean (rank,fixed_id,tax_string,domain_id,phylum_id)"
        qphylum2 += " VALUES('phylum','%s','%s','%s','%s')"
        q2 = qphylum2  % (rankid,  tax_str, 
                                str(row['domain_id']),  
                                str(row['phylum_id']) 
                       )
        print(q)
        run_sql('phylum',q)
        run_sql('phylum',q2)
        text_collector[tax_str] = {"id":rankid,"rank":"phylum", "HMT":''}
        
        #CLASS
        rankid = 'C'+str(i+101)
        tax_str = make_tax_string('klass',row)
        qklass = "INSERT into taxonomy_ranked (rank,fixed_id,tax_string,domain,domain_id,phylum,phylum_id,klass,klass_id)"
        qklass += " VALUES('class','%s','%s','%s','%s','%s','%s','%s','%s')"
        q = qklass  % (rankid,  tax_str,
                                row['domain'], 
                                str(row['domain_id']),
                                row['phylum'],  
                                str(row['phylum_id']) ,
                                row['klass'],  
                                str(row['klass_id'])
                       )
        qklass2 = "INSERT into taxonomy_ranked_clean (rank,fixed_id,tax_string,domain_id,phylum_id,klass_id)"
        qklass2 += " VALUES('class','%s','%s','%s','%s','%s')"
        q2 = qklass2  % (rankid,  tax_str, 
                                str(row['domain_id']),
                                str(row['phylum_id']),
                                str(row['klass_id'])
                       )
        print(q)
        run_sql('klass',q)
        run_sql('klass',q2)
        text_collector[tax_str] = {"id":rankid,"rank":"klass", "HMT":''}
        
        #ORDER
        rankid = 'O'+str(i+101)
        tax_str = make_tax_string('order',row)
        qorder = "INSERT into taxonomy_ranked (rank,fixed_id,tax_string,domain,domain_id,phylum,phylum_id,klass,klass_id,`order`,order_id)"
        qorder += " VALUES('order','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
        q = qorder  % (rankid,  tax_str,
                                row['domain'], 
                                str(row['domain_id']),
                                row['phylum'],  
                                str(row['phylum_id']) ,
                                row['klass'],  
                                str(row['klass_id']),
                                row['order'],  
                                str(row['order_id'])
                       )
        qorder2 = "INSERT into taxonomy_ranked_clean (rank,fixed_id,tax_string,domain_id,phylum_id,klass_id,order_id)"
        qorder2 += " VALUES('order','%s','%s','%s','%s','%s','%s')"
        q2 = qorder2  % (rankid,  tax_str,
                                str(row['domain_id']),
                                str(row['phylum_id']),
                                str(row['klass_id']),
                                str(row['order_id'])
                       )
        print(q)
        run_sql('order',q)
        run_sql('order',q2)
        text_collector[tax_str] = {"id":rankid,"rank":"order", "HMT":''}
        
        #FAMILY
        rankid = 'F'+str(i+101)
        tax_str = make_tax_string('family',row)
        qfamily = "INSERT into taxonomy_ranked (rank,fixed_id,tax_string,domain,domain_id,phylum,phylum_id,klass,klass_id,`order`,order_id,family,family_id)"
        qfamily += " VALUES('family','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
        q = qfamily  % (rankid,  tax_str,
                                row['domain'], 
                                str(row['domain_id']),
                                row['phylum'],  
                                str(row['phylum_id']) ,
                                row['klass'],  
                                str(row['klass_id']),
                                row['order'],  
                                str(row['order_id']),
                                row['family'],  
                                str(row['family_id'])
                       )
        qfamily2 = "INSERT into taxonomy_ranked_clean (rank,fixed_id,tax_string,domain_id,phylum_id,klass_id,order_id,family_id)"
        qfamily2 += " VALUES('family','%s','%s','%s','%s','%s','%s','%s')"
        q2 = qfamily2  % (rankid,  tax_str,
                                str(row['domain_id']),
                                str(row['phylum_id']) ,
                                str(row['klass_id']),
                                str(row['order_id']),
                                str(row['family_id'])
                       )
        print(q)
        run_sql('family',q)
        run_sql('family',q2)
        text_collector[tax_str] = {"id":rankid,"rank":"family", "HMT":''}
        
         #GENUS
        rankid = 'G'+str(i+101)
        tax_str = make_tax_string('genus',row)
        qgenus = "INSERT into taxonomy_ranked (rank,fixed_id,tax_string,domain,domain_id,phylum,phylum_id,klass,klass_id,`order`,order_id,family,family_id,genus,genus_id)"
        qgenus += " VALUES('genus','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
        q = qgenus  % (rankid,  tax_str,
                                row['domain'], 
                                str(row['domain_id']),
                                row['phylum'],  
                                str(row['phylum_id']) ,
                                row['klass'],  
                                str(row['klass_id']),
                                row['order'],  
                                str(row['order_id']),
                                row['family'],  
                                str(row['family_id']),
                                row['genus'],  
                                str(row['genus_id'])
                       )
        qgenus2 = "INSERT into taxonomy_ranked_clean (rank,fixed_id,tax_string,domain_id,phylum_id,klass_id,order_id,family_id,genus_id)"
        qgenus2 += " VALUES('genus','%s','%s','%s','%s','%s','%s','%s','%s')"
        q = qgenus2  % (rankid,  tax_str,
                                str(row['domain_id']),
                                str(row['phylum_id']) ,
                                str(row['klass_id']),
                                str(row['order_id']),
                                str(row['family_id']),
                                str(row['genus_id'])
                       )
        print(q)
        run_sql('genus',q)
        run_sql('genus',q2)
        text_collector[tax_str] = {"id":rankid,"rank":"genus", "HMT":''}
                
        #SPECIES
        rankid = 'S'+str(i+101)
        tax_str = make_tax_string('species',row)
        hmt = ''
        if str(row['subspecies_id']) == '1':
            hmt = format_hmt(row['otid'])
        qspecies = "INSERT into taxonomy_ranked (rank,fixed_id,HMT,tax_string,domain,domain_id,phylum,phylum_id,klass,klass_id,`order`,order_id,family,family_id,genus,genus_id,species,species_id)"
        qspecies += " VALUES('species','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
        q = qspecies  % (rankid,  hmt, tax_str,
                                row['domain'], 
                                str(row['domain_id']),
                                row['phylum'],  
                                str(row['phylum_id']) ,
                                row['klass'],  
                                str(row['klass_id']),
                                row['order'],  
                                str(row['order_id']),
                                row['family'],  
                                str(row['family_id']),
                                row['genus'],  
                                str(row['genus_id']),
                                row['species'],  
                                str(row['species_id'])
                       )
        qspecies2 = "INSERT into taxonomy_ranked_clean (rank,fixed_id,HMT,tax_string,domain_id,phylum_id,klass_id,order_id,family_id,genus_id,species_id)"
        qspecies2 += " VALUES('species','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
        q2 = qspecies2  % (rankid,  hmt, tax_str,
                                str(row['domain_id']),
                                str(row['phylum_id']) ,
                                str(row['klass_id']),
                                str(row['order_id']),
                                str(row['family_id']),
                                str(row['genus_id']),
                                str(row['species_id'])
                       )
        print(q)
        run_sql('species',q)
        run_sql('species',q2)
        text_collector[tax_str] = {"id":rankid,"rank":"species", "HMT":hmt}
                
        #SUBSPECIES
        rankid = 'SSP'+str(i+101)
        tax_str = make_tax_string('subspecies',row)
        hmt = ''
        if str(row['subspecies_id']) != '1':
            hmt = format_hmt(row['otid'])
        qsspecies = "INSERT into taxonomy_ranked (rank,fixed_id,HMT,tax_string,domain,domain_id,phylum,phylum_id,klass,klass_id,`order`,order_id,family,family_id,genus,genus_id,species,species_id,subspecies,subspecies_id)"
        qsspecies += " VALUES('subspecies','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
        q = qsspecies  % (rankid,  hmt, tax_str,
                                row['domain'], 
                                str(row['domain_id']),
                                row['phylum'],  
                                str(row['phylum_id']) ,
                                row['klass'],  
                                str(row['klass_id']),
                                row['order'],  
                                str(row['order_id']),
                                row['family'],  
                                str(row['family_id']),
                                row['genus'],  
                                str(row['genus_id']),
                                row['species'],  
                                str(row['species_id']),
                                row['subspecies'],  
                                str(row['subspecies_id'])
                       )
        qsspecies2 = "INSERT into taxonomy_ranked_clean (rank,fixed_id,HMT,tax_string,domain_id,phylum_id,klass_id,order_id,family_id,genus_id,species_id,subspecies_id)"
        qsspecies2 += " VALUES('subspecies','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
        q2 = qsspecies2  % (rankid,  hmt, tax_str,
                                str(row['domain_id']),
                                str(row['phylum_id']) ,
                                str(row['klass_id']),
                                str(row['order_id']),
                                str(row['family_id']),
                                str(row['genus_id']),
                                str(row['species_id']),
                                str(row['subspecies_id'])
                       )
        print(q)
        run_sql('subspecies',q)
        run_sql('subspecies',q2)
        if row['subspecies']:
            text_collector[tax_str] = {"id":rankid,"rank":"subspecies", "HMT":hmt}
    for ts in text_collector:
        fout.write(text_collector[ts]["id"]+'\t'+text_collector[ts]["rank"]+'\t'+text_collector[ts]["HMT"]+'\t'+ts+'\n')
    
    fout.close()
    
def make_tax_string(r, row):
    string = row['domain']
    if r != 'domain':
        for i,rank in enumerate(ranks[1:]):
            string += ';'+row[rank]
            if rank == r:
                break
        
    return string
    
def format_hmt(n):
    return 'HMT-'+str(n).zfill(3)
        
def run_sql(rank, q):
    
    try:
        myconn.execute_no_fetch(q)
    except mysql.err.IntegrityError as e:
        # mysql.err.IntegrityError: (1062, "Duplicate entry '2201-2201-1-1-1-1-1-1' for key 'rank_ids'")
        # mysql.err.IntegrityError: (1062, "Duplicate entry 'D103' for key 'fixed_id'")
        if 'rank_ids' in e.args[1]:
            print(rank,'Duplicate entry (rank_ids):',e)
        elif 'fixed_ids' in e.args[1]:
            print('Duplicate entry (fixed_id):',e)
            # give another fixed_id and ty\ry again
            sys.exit()
        else:
            print('Other mysql.err.IntegrityError:',e)
if __name__ == "__main__":

    usage = """
    USAGE:
        ./ranked_taxonomy_table.py 
         
        Creates a ranked taxonomy sql table with a fixed_id (from file)
         The table has all ranks domain => subspecies
         from the HOMD database
         
         The fixed ID should be static when the table is re-created across databases.
        -i/--infile  ranked_taxonomy_w_fixed_ids2023-08-17.csv
        -host/--host [homd]  default:localhost
       
        

    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=True,  action="store",   dest = "infile", default='none',
                                                   help=" ")
    # parser.add_argument("-a", "--anno",   required=False,  action="store",   dest = "anno",  default='ncbi',
#                                                     help="")
    parser.add_argument("-w", "--write",   required=False,  action="store_true",   dest = "write2db", default=False,
                                                help=" ")
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",   dest = "verbose", default=False,
                                                    help=" ")
    parser.add_argument("-host", "--host",
                        required = False, action = 'store', dest = "dbhost", default = 'localhost',
                        help = "choices=['homd',  'localhost']")
    
    
    args = parser.parse_args()
    
    #parser.print_help(usage)
                        
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
    
    
    myconn = MyConnection(host=dbhost, db=args.DATABASE,  read_default_file = "~/.my.cnf_node")

    args.indent = 4
    #args.taxonomy_obj = get_taxonomy_obj()
    
    
    run_taxonomy()
    

    
