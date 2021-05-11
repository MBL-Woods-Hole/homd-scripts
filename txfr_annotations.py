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

q_gc_count = "INSERT IGNORE INTO annotation.gc_count (annotation,genome,contig,`stop`,`start`,gc_percentage) \
             SELECT '{annotation}','{seqid}',contig,`stop`,`start`,GC_percentage FROM {db}.GC_count;"

q_genome_seq = "INSERT IGNORE INTO annotation.genome_seq (annotation,genome,molecule_id,`mol_order`,`seq`) \
                SELECT '{annotation}','{seqid}',molecule_id,`mol_order`,`seq` FROM {db}.genome_seq;"

q_gff = "INSERT IGNORE INTO annotation.gff (annotation,genome,seqid,`source`,`type`,`start`,`end`,score,strand,`phase`,attributes) \
         SELECT '{annotation}','{seqid}',seqid,`source`,`type`,`start`,`end`,score,strand,`phase`,attributes FROM {db}.gff;"
         
q_orf_seq = "INSERT IGNORE INTO annotation.orf_sequence (annotation,genome,  mol_id,length,gene,synonym,PID,`code`,COD,product,`start`,`stop`,seq_na,seq_aa) \
          SELECT '{annotation}','{seqid}',  mol_id,length,gene,synonym,PID,`code`,COD,product,`start`,`stop`,seq_na,seq_aa FROM {db}.ORF_seq;"         

"""
ANNOTATIONS
CREATE TABLE `gc_count` (
  `gc_count_id` int(6) NOT NULL AUTO_INCREMENT,
  `genome` varchar(10) NOT NULL,
  `annotation` varchar(10) NOT NULL,
  `contig` int(6) NOT NULL DEFAULT '0',
  `start` int(11) NOT NULL DEFAULT '0',
  `stop` int(11) NOT NULL DEFAULT '0',
  `gc_percentage` float NOT NULL DEFAULT '0',
  PRIMARY KEY (`gc_count_id`),
  KEY `contig` (`contig`),
  KEY `start` (`start`),
  KEY `stop` (`stop`)
) ENGINE=InnoDB AUTO_INCREMENT=8191 DEFAULT CHARSET=latin1;
INSERT INTO annotation.gc_count (annotation,genome,contig,`stop`,`start`,gc_percentage) 
SELECT 'PROKKA','SEQF1595',contig,`stop`,`start`,GC_percentage FROM PROKKA_SEQF1595.GC_count;

CREATE TABLE `genome_seq` (
  `genome_seq_id` int(11) NOT NULL AUTO_INCREMENT,
  `genome` varchar(10) NOT NULL,
  `annotation` varchar(10) NOT NULL,
  `molecule_id` int(11) NOT NULL DEFAULT '0',
  `mol_order` int(11) NOT NULL DEFAULT '0',
  `seq` text NOT NULL,
  PRIMARY KEY (`genome_seq_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4095 DEFAULT CHARSET=latin1;
INSERT INTO annotation.genome_seq (annotation,genome,molecule_id,`mol_order`,`seq`) 
SELECT 'NCBI','SEQF1595',molecule_id,`mol_order`,`seq` FROM NCBI_SEQF1595.genome_seq;

CREATE TABLE `gff` (
  `gff_id` int(11) NOT NULL AUTO_INCREMENT,
  `genome` varchar(10) NOT NULL,
  `annotation` varchar(10) NOT NULL,
  `seqid` text NOT NULL,
  `source` text NOT NULL,
  `type` tinytext NOT NULL,
  `start` int(11) NOT NULL,
  `end` int(11) NOT NULL,
  `score` float NOT NULL,
  `strand` varchar(2) NOT NULL,
  `phase` tinyint(4) NOT NULL,
  `attributes` text NOT NULL,
  PRIMARY KEY (`gff_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6143 DEFAULT CHARSET=latin1;
INSERT INTO annotation.gff (annotation,genome,seqid,`source`,`type`,`start`,`end`,score,strand,`phase`,attributes) 
SELECT 'PROKKA','SEQF1595',seqid,`source`,`type`,`start`,`end`,score,strand,`phase`,attributes FROM PROKKA_SEQF1595.gff;

CREATE TABLE `orf_sequence` (
  `orf_seq_id` int(11) NOT NULL AUTO_INCREMENT,
  `genome` varchar(10) NOT NULL,
  `annotation` varchar(10) NOT NULL,
  `mol_id` int(11) NOT NULL DEFAULT '0',
  `length` int(11) NOT NULL DEFAULT '0',
  `gene` varchar(20) DEFAULT '0',
  `synonym` varchar(20) DEFAULT NULL,
  `PID` varchar(20) DEFAULT NULL,
  `code` varchar(20) DEFAULT NULL,
  `COD` varchar(20) DEFAULT NULL,
  `product` tinytext,
  `start` int(11) NOT NULL DEFAULT '0',
  `stop` int(11) NOT NULL DEFAULT '0',
  `seq_na` text,
  `seq_aa` text,
  PRIMARY KEY (`orf_seq_id`),
  KEY `PID` (`PID`),
  KEY `start` (`start`),
  KEY `stop` (`stop`)
) ENGINE=InnoDB AUTO_INCREMENT=4095 DEFAULT CHARSET=latin1;
INSERT INTO annotation.orf_sequence (annotation,genome,  mol_id,length,gene,synonym,PID,`code`,COD,product,`start`,`stop`,seq_na,seq_aa) 
SELECT 'PROKKA','SEQF1595',  mol_id,length,gene,synonym,PID,`code`,COD,product,`start`,`stop`,seq_na,seq_aa FROM PROKKA_SEQF1595.ORF_seq;

CREATE TABLE `molecules_seq` (
  `molecules_id` int(11) NOT NULL AUTO_INCREMENT,
  `genome` varchar(10) NOT NULL,
  `annotation` varchar(10) NOT NULL,
  `accession` varchar(50) NOT NULL DEFAULT '',
  `name` tinytext NOT NULL,
  `bps` int(11) NOT NULL DEFAULT '0',
  `GC` float NOT NULL,
  `date` date NOT NULL DEFAULT '0000-00-00',
  PRIMARY KEY (`molecules_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
others
molecules(4rows) , prokka, ncbi

"""



q_index = "SELECT seq_id, otid FROM seqid_otid_index"             
            
def get_seqs(args):
    q1 = "SELECT seq_id from seq_genomes"
    result = myconn_homd.execute_fetch_select(q1)
    seqid_list = []
    for n in result:
        print(n[0])
        seqid_list.append(n[0])
    #myconn_homd = MyConnection(host=args.dbhost, db=args.HOMD_DATABASE,  read_default_file = "~/.my.cnf_node")
    for seqid in seqid_list:
        ncbi_db_name = 'NCBI_'+seqid
        prokka_db_name = 'PROKKA_'+seqid
        # first ncbi
        anno = 'NCBI'
        annot_conn = MyConnection(host=args.dbhost,  read_default_file = "~/.my.cnf_node")
        query = q_gc_count.format(annotation=anno,seqid=seqid,db=ncbi_db_name.upper())
        print(query)
        myconn_homd.execute_no_fetch(query)
    

    
    
if __name__ == "__main__":

    usage = """
    USAGE:
        takes the annotations  from the old homd to the new db:annotation
        
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
        args.dbhost = '192.168.1.51'
        args.outdir = '../homd-startup-data/'
        args.prettyprint = False

    elif args.dbhost == 'localhost':
        #args.json_file_path = '/Users/avoorhis/programming/homd-data/json'
        args.ANNOT_DATABASE  = 'annotation'
        args.HOMD_DATABASE = 'homdAV'
        args.dbhost = 'localhost'
        print('TESTING')
    else:
        sys.exit('dbhost - error')
    args.indent = None
    if args.prettyprint:
        args.indent = 4
    myconn_annotation = MyConnection(host=args.dbhost, db=args.ANNOT_DATABASE,   read_default_file = "~/.my.cnf_node")
    myconn_homd = MyConnection(host=args.dbhost, db=args.HOMD_DATABASE,  read_default_file = "~/.my.cnf_node")

    print(args)
    
    list_of_seqs = get_seqs(args)
    print(list_of_seqs)
   #transfer_per_seq(args)
    
    
    