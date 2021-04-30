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
try:
    import mysqlclient as mysql
except ImportError:
    try:
        import pymysql as mysql
    except ImportError:
        import MySQLdb as mysql
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




    
# def print_dict(filename, dict):
#     with open(filename, 'w') as outfile:
#         json.dump(dict, outfile, indent=args.indent)
    

def run_prime(args):
    q1 = "select Oral_taxon_id as otid from  taxonid_site"
    otid_result = myconn_tax.execute_fetch_select_dict(q1)
    for obj in otid_result:
        # for each otid build up the taxonomy from species => domain
        print(obj)
        #lst = [str(obj['otid']),str(site_lookup[obj['site']])]
        q3 = "INSERT IGNORE into `otid_prime` (otid) VALUES"
        q3 += "('"+str(obj['otid'])+"')"  
        
        myconn_new.execute_no_fetch(q3) 
        q4 = "SELECT LAST_INSERT_ID()"
        last_id = myconn_new.execute_fetch_one(q4) 
        if last_id[0] == 0:
            # failed to insert: 
            print(obj['otid']) 


def run_site(args):
    """
   CREATE TABLE `site` (
	  `site_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
	  `otid` int(11) unsigned NOT NULL,
	  `site` varchar(20) DEFAULT '',
	  PRIMARY KEY (`site_id`),
	  UNIQUE KEY `otid` (`otid`,`site`),
	  CONSTRAINT `otid_fk3` FOREIGN KEY (`otid`) REFERENCES `otid_prime` (`otid`)
	) ENGINE=InnoDB AUTO_INCREMENT=825 DEFAULT CHARSET=latin1;
        
    """
    global full_tax_lookup
    
    q1 = "select Oral_taxon_id as otid, site from  taxonid_site"
    
    full_tax_list = []
    full_tax_lookup = {}
    collector = []
    for obj in otid_result:
        # for each otid build up the taxonomy from species => domain
        print(obj)
        otid = str(obj['otid'])
        #lst = [str(obj['otid']),str(site_lookup[obj['site']])]
        q3 = "INSERT IGNORE into `site` (otid, site) VALUES"
        q3 += "('"+otid+"',"+"'"+obj['site']+"')"  
        print(q3)
        myconn_new.execute_no_fetch(q3) 
        
     
    
def run_type_strain(args):
    """
   CREATE TABLE `type_strain` (
	  `type_strain_id` int(8) unsigned NOT NULL AUTO_INCREMENT,
	  `otid` int(11) unsigned NOT NULL,
	  `type_strain` varchar(30) NOT NULL DEFAULT '',
	  PRIMARY KEY (`type_strain_id`),
	  UNIQUE KEY `otid` (`otid`,`type_strain`),
	  CONSTRAINT `type_strain_ibfk_1` FOREIGN KEY (`otid`) REFERENCES `otid_prime` (`otid`) ON UPDATE CASCADE
	) ENGINE=InnoDB AUTO_INCREMENT=167 DEFAULT CHARSET=latin1;
    """
    q1 = "select Oral_taxon_id as otid, type_strain from  1_type_strain"
    
        
    otid_result = myconn_tax.execute_fetch_select_dict(q1)
    full_tax_list = []
    full_tax_lookup = {}
    collector = []
    for obj in otid_result:
        # for each otid build up the taxonomy from species => domain
        print(obj)
        otid = str(obj['otid'])
        #lst = [str(obj['otid']),str(site_lookup[obj['site']])]
        q2 = "INSERT IGNORE into type_strain (otid,type_strain) VALUES ('"+otid+"','"+obj['type_strain']+"')"
        print(q2)
        myconn_new.execute_no_fetch(q2) 
        # q3 = "SELECT LAST_INSERT_ID()"
#         last_id = myconn_new.execute_fetch_one(q3) 
#         if last_id[0] == 0: ## already in table
#             q4 = "SELECT type_strain_id from type_strain where type_strain ='"+obj['type_strain']+"'"
#             print(q4)
#             result = myconn_new.execute_fetch_one(q4)
#             ts_id = result[0]
#         else:
#             ts_id = last_id[0] 
#         q5 = "INSERT IGNORE into `otid_type_strain` (otid, type_strain_id) VALUES"
#         q5 += "('"+str(obj['otid'])+"',"+"'"+str(ts_id)+"')"  
#         print(q5)
#         myconn_new.execute_no_fetch(q5) 
def run_ref_strain(args):
    """
    CREATE TABLE `ref_strain` (
	  `reference_strain_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
	  `otid` int(11) unsigned NOT NULL,
	  `reference_strain` varchar(100) NOT NULL,
	  PRIMARY KEY (`reference_strain_id`),
	  UNIQUE KEY `otid` (`otid`,`reference_strain`),
	  CONSTRAINT `otid_ref_strain_fk3` FOREIGN KEY (`otid`) REFERENCES `otid_prime` (`otid`)
	) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

    """
    
    
    q1 = "select Oral_taxon_id as otid, reference_strain from  1_reference_strain"
    
    otid_result = myconn_tax.execute_fetch_select_dict(q1)
    
    for obj in otid_result:
        # for each otid build up the taxonomy from species => domain
        print(obj)
        otid = str(obj['otid'])
        #lst = [str(obj['otid']),str(site_lookup[obj['site']])]
        q2 = "INSERT IGNORE into ref_strain (otid,reference_strain) VALUES ('"+otid+"','"+obj['reference_strain']+"')"
        print(q2)
        myconn_new.execute_no_fetch(q2) 
                
def ncbi_taxid(args):
    q1 = "select Oral_taxon_id as otid, NCBI_taxon_id from  1_ncbi_taxonomy"
     
    otid_result = myconn_tax.execute_fetch_select_dict(q1)
    full_tax_list = []
    full_tax_lookup = {}
    collector = []
    for obj in otid_result:
        # for each otid build up the taxonomy from species => domain
        print(obj)
        #lst = [str(obj['otid']),str(site_lookup[obj['site']])]
        q2 = "UPDATE otid_prime set NCBI_taxon_id='"+str(obj['NCBI_taxon_id'])+"' WHERE otid ='"+str(obj['otid'])+"'"
        print(q2)
        myconn_new.execute_no_fetch(q2) 

def run_status(args):
    q1 = "select Oral_taxon_id as otid, `group` from  1_status"
    
    otid_result = myconn_tax.execute_fetch_select_dict(q1)
    full_tax_list = []
    full_tax_lookup = {}
    collector = []
    for obj in otid_result:
        # for each otid build up the taxonomy from species => domain
        print(obj)
        #lst = [str(obj['otid']),str(site_lookup[obj['site']])]
        q2 = "UPDATE otid_prime set status='"+str(obj['group'])+"' WHERE otid ='"+str(obj['otid'])+"'"
        print(q2)
        myconn_new.execute_no_fetch(q2) 
                
def run_16s_rRNA_seqs(args):
    """
    CREATE TABLE `rRNA_sequence` (
	  `rRNA_sequence_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
	  `otid` int(11) unsigned NOT NULL,
	  `rRNA_sequence` varchar(100) NOT NULL,
	  PRIMARY KEY (`rRNA_sequence_id`),
	  UNIQUE KEY `otid` (`otid`,`rRNA_sequence`),
	  CONSTRAINT `otid_rRNA_sequence_fk3` FOREIGN KEY (`otid`) REFERENCES `otid_prime` (`otid`)
	) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
    """
    q1 = "select Oral_taxon_id as otid, 16S_rRNA_sequence as seqref from  1_16S_rRNA_sequence"
    
        
    otid_result = myconn_tax.execute_fetch_select_dict(q1)
    full_tax_list = []
    full_tax_lookup = {}
    collector = []
    for obj in otid_result:
        # for each otid build up the taxonomy from species => domain
        print(obj)
        otid = str(obj['otid'])
        #lst = [str(obj['otid']),str(site_lookup[obj['site']])]
        q2 = "INSERT IGNORE into rRNA_sequence (otid, rRNA_sequence) VALUES ('"+otid+"','"+obj['seqref']+"')"
        print(q2)
        myconn_new.execute_no_fetch(q2) 
        #q3 = "SELECT LAST_INSERT_ID()"
        #last_id = myconn_new.execute_fetch_one(q3) 
        
        
        
# def run_index(args):
#     """
#         CREATE TABLE `seqid_otid_index` (
#       `seq_id` varchar(9) NOT NULL,
#       `otid` int(5) unsigned DEFAULT NULL,
#       PRIMARY KEY (`seq_id`),
#       KEY `otid` (`otid`),
#       CONSTRAINT `genome_ibfk_4` FOREIGN KEY (`otid`) REFERENCES `otid_prime` (`otid`) ON UPDATE CASCADE,
#       CONSTRAINT `genome_ibfk_5` FOREIGN KEY (`seq_id`) REFERENCES `seq_genomes` (`seq_id`) ON UPDATE CASCADE
#     ) ENGINE=InnoDB DEFAULT CHARSET=latin1;
# """
#     
#     q1 = "select Oral_taxon_id as otid, seq_id  from  HOMD_seqid_taxonid_index"
#     result = myconn_gene.execute_fetch_select_dict(q1)
#     #print(result)
#     
#     for n in result:
#         print(n)
#         q2_insert = "INSERT into seqid_otid_index (seq_id,otid) "
#         q2_insert += "VALUES('"+n['seq_id']+"','"+str(n['otid'])+"')" 
#         print(q2_insert)
#         myconn_new.execute_no_fetch(q2_insert)

def run_synonyms(args):
    """
	   CREATE TABLE `synonym` (
		  `synonym_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
		  `otid` int(11) unsigned DEFAULT NULL,
		  `synonym` varchar(100) NOT NULL DEFAULT '',
		  PRIMARY KEY (`synonym_id`),
		  UNIQUE KEY `otid` (`otid`,`synonym`),
		  CONSTRAINT `synonyms_ibfk_1` FOREIGN KEY (`otid`) REFERENCES `otid_prime` (`otid`) ON UPDATE CASCADE
		) ENGINE=InnoDB AUTO_INCREMENT=1006 DEFAULT CHARSET=latin1;
        
    """
    global full_tax_lookup
    
        
    q1 = "select Oral_taxon_id as otid, synonyms as synonym from  1_synonyms_correct"
    #q2 = "SELECT site,site_id from site"
    
    #site_result = myconn_new.execute_fetch_select_dict(q2)
    #print(site_result)
    #site_lookup = {}
    #for obj in site_result:
    #    site_lookup[obj['site']] = obj['site_id']
    otid_result = myconn_tax.execute_fetch_select_dict(q1)
    full_tax_list = []
    full_tax_lookup = {}
    collector = []
    for obj in otid_result:
        # for each otid build up the taxonomy from species => domain
        print(obj)
        otid = str(obj['otid'])
        #lst = [str(obj['otid']),str(site_lookup[obj['site']])]
        q2 = "INSERT IGNORE into `synonym` (otid,synonym) VALUES ('"+otid+"','"+obj['synonym']+"')"
        myconn_new.execute_no_fetch(q2) 


def run_refseq(args):
    """
	CREATE TABLE `otid_refseqid` (
	  `otid_refseq_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
	  `otid` int(11) unsigned NOT NULL,
	  `refseqid` varchar(20) NOT NULL,
	  `seqname` varchar(50) NOT NULL,
	  `strain` varchar(128) NOT NULL,
	  `genbank` varchar(30) NOT NULL,
	  `seq_trim9` text NOT NULL,
	  `seq_trim28` text NOT NULL,
	  `seq_aligned` text NOT NULL,
	  `seq_trim28_end` text NOT NULL,
	  `status` varchar(20) NOT NULL,
	  `site` varchar(100) NOT NULL,
	  `order` int(11) NOT NULL,
	  `flag` varchar(100) NOT NULL,
	  PRIMARY KEY (`otid_refseq_id`),
	  UNIQUE KEY `otid` (`otid`,`refseqid`),
	  CONSTRAINT `otid_refseq_fk3` FOREIGN KEY (`otid`) REFERENCES `otid_prime` (`otid`)
	) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
    """
    q1 = "select taxonid as otid, refseqid,seqname,strain,genbank,seq_trim9,seq_trim28,seq_aligned,seq_trim28_end,status,site,`order`,flag from  taxonid_refseqid_seq"
    
    result = myconn_tax.execute_fetch_select_dict(q1)
    for obj in result:
        # for each otid build up the taxonomy from species => domain
        print(obj)
        otid = str(obj['otid'])
        #lst = [str(obj['otid']),str(site_lookup[obj['site']])]
        q2 = "INSERT IGNORE into `otid_refseqid` (otid,refseqid,seqname,strain,genbank,seq_trim9,seq_trim28,seq_aligned,seq_trim28_end,status,site,`order`,flag ) "
        q2 += "VALUES ('"+otid+"','"+obj['refseqid']+"','"+obj['seqname']+"','"+obj['strain']+"','"+obj['genbank']+"','"+obj['seq_trim9']+"','"+obj['seq_trim28']+"','"+obj['seq_aligned']+"','"+obj['seq_trim28_end']+"','"+obj['status']+"','"+obj['site']+"','"+str(obj['order'])+"','"+obj['flag']+"')"
        print(q2)
        myconn_new.execute_no_fetch(q2) 
    
if __name__ == "__main__":

    usage = """
    USAGE:
        takes the 
        sites, 
        type_strain, 
        ncbi_taxid - unique in otid_prime 
        16S_rRNA_seq
        status (field was group)
        from old tables into the new format
        
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
        args.GEN_DATABASE  = 'HOMD_genomes_new'
        args.TAX_DATABASE = 'HOMD_taxonomy'
        args.NEW_DATABASE = 'homdAV'
        dbhost = '192.168.1.51'
        args.outdir = '../homd-startup-data/'
        args.prettyprint = False

    elif args.dbhost == 'localhost':
        #args.json_file_path = '/Users/avoorhis/programming/homd-data/json'
        args.GEN_DATABASE  = 'HOMD_genomes_new'
        args.TAX_DATABASE  = 'HOMD_taxonomy'
        args.NEW_DATABASE = 'homdAV'
        dbhost = 'localhost'
    else:
        sys.exit('dbhost - error')
    args.indent = None
    if args.prettyprint:
        args.indent = 4
    myconn_gene = MyConnection(host=dbhost, db=args.GEN_DATABASE,   read_default_file = "~/.my.cnf_node")
    myconn_tax = MyConnection(host=dbhost, db=args.TAX_DATABASE,   read_default_file = "~/.my.cnf_node")
    myconn_new = MyConnection(host=dbhost, db=args.NEW_DATABASE,  read_default_file = "~/.my.cnf_node")

    print(args)
    print('edit and uncomment defs to run')
    #print('run_taxa(args)')
    #run_prime(args)
    #run_site(args)
    #run_type_strain(args)
    #run_ref_strain(args)
    #ncbi_taxid(args)  # in otid_prime
    
    # warnings are put into otid_prime  by hand
    #run_status(args)   # in otid_prime
    #run_index(args)    UNUSED
    #run_synonyms(args)
    #run_16s_rRNA_seqs(args)
    run_refseq(args)
    
    
    