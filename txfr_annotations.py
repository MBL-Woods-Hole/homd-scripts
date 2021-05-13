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

q_gc_count2 = "INSERT IGNORE INTO annotation.gc_count (annotation,seq_id,contig,`stop`,`start`,gc_percentage) VALUES"
q_gc_count1 = "SELECT '{annotation}','{seqid}',contig,`stop`,`start`,GC_percentage FROM {db}.GC_count;"

q_genome_seq2 = "INSERT IGNORE INTO annotation.genome (annotation,seq_id,molecule_id,`mol_order`,`seq`) VALUES"
q_genome_seq1 = "SELECT '{annotation}','{seqid}',molecule_id,`mol_order`,`seq` FROM {db}.genome_seq;"

q_gff2 = "INSERT IGNORE INTO annotation.gff (annotation,seq_id,seqid,`source`,`type`,`start`,`end`,score,strand,`phase`,attributes) VALUES"
q_gff1 = "SELECT '{annotation}','{seqid}',seqid,`source`,`type`,`start`,`end`,score,strand,`phase`,attributes FROM {db}.gff;"
         
q_orf_seq2 = "INSERT IGNORE INTO annotation.orf_sequence (annotation,seq_id,  mol_id,length,gene,synonym,PID,`code`,COD,product,`start`,`stop`,seq_na,seq_aa) VALUES"
q_orf_seq1 = """SELECT '{annotation}','{seqid}', mol_id,length, \
IFNULL(gene, '') as gene, \
IFNULL(synonym, '') as synonym, \
IFNULL(PID, '') as PID, \
IFNULL(code, '') as code, \
IFNULL(COD, '') as COD, \
IFNULL(product, '') as product, \
`start`,`stop`,seq_na,seq_aa FROM {db}.ORF_seq;"""

q_molecule2 = "INSERT IGNORE INTO annotation.molecule (annotation,seq_id,accession,`name`,`bps`,GC,`date`) VALUES"
q_molecule1 = "SELECT '{annotation}','{seqid}',accession,`name`,`bps`,GC,DATE_FORMAT(`date`, '%Y-%m-%d') as date FROM {db}.molecules;"




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
  UNIQUE KEY `genome` (`genome`,`annotation`,`contig`,`start`,`stop`,`gc_percentage`),
  KEY `contig` (`contig`),
  KEY `start` (`start`),
  KEY `stop` (`stop`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
    q = "SELECT seq_id from homd.genomes"
    result = myconn_new.execute_fetch_select(q)
    seqid_list = []
    available_dbs = []
    for n in result:
        #print(n[0])
        #db = args.anno+'_'+n[0]
        seqid_list.append(n[0])
        
    
    q = "SHOW DATABASES LIKE '"+args.anno+"_%'"
    #print(q)
    result = myconn_old.execute_fetch_select(q)
    for n in result:
        available_dbs.append(n[0])
    #print(available_dbs)
    return(seqid_list,  available_dbs )    
        
def go_gc_count(args,seqlst,dbs):
    
    for seqid in seqlst:
        db_name = args.anno+'_'+seqid
        if db_name in dbs:
            print('Processing',db_name,args.table)
            query1 = q_gc_count1.format(annotation=args.anno,seqid=seqid,db=db_name)
               
            result = myconn_old.execute_fetch_select(query1)
            for n in result:
                #('NCBI', 'SEQF1595', 4, 160500, 160001, 43.0)
                #print(n)
                query2 = q_gc_count2+str(n)
                #print(query2)
                myconn_new.execute_no_fetch(query2)
        
def go_genome_seq(args,seqlst,dbs):
    for seqid in seqlst:
        db_name = args.anno+'_'+seqid
        if db_name in dbs:
            print('Processing',db_name,args.table)
            query1 = q_genome_seq1.format(annotation=args.anno,seqid=seqid,db=db_name)
               
            result = myconn_old.execute_fetch_select(query1)
            for n in result:
                
                #print(n)
                query2 = q_genome_seq2+str(n)
                #print(query2)
                myconn_new.execute_no_fetch(query2)
def go_gff(args,seqlst,dbs):
    for seqid in seqlst:
        db_name = args.anno+'_'+seqid
        if db_name in dbs:
            print('Processing',db_name,args.table)
            query1 = q_gff1.format(annotation=args.anno,seqid=seqid,db=db_name)
               
            result = myconn_old.execute_fetch_select(query1)
            for n in result:
                
                #print(n)
                query2 = q_gff2+str(n)
                #print(query2)
                myconn_new.execute_no_fetch(query2)
def go_orf_sequence(args,seqlst,dbs):
    for seqid in seqlst:
        db_name = args.anno+'_'+seqid
        if db_name in dbs:
            print('Processing',db_name,args.table)
            query1 = q_orf_seq1.format(annotation=args.anno,seqid=seqid,db=db_name)
               
            result = myconn_old.execute_fetch_select(query1)
            for n in result:
                
                query2 = q_orf_seq2+str(n)
                #print(query2)
                myconn_new.execute_no_fetch(query2)

def go_molecule(args,seqlst,dbs):
    for seqid in seqlst:
        db_name = args.anno+'_'+seqid
        if db_name in dbs:
            print('Processing',db_name,args.table)
            query1 = q_molecule1.format(annotation=args.anno,seqid=seqid,db=db_name)
            #print(query1)   
            result = myconn_old.execute_fetch_select(query1)
            for n in result:
                #print(n)
                query2 = q_molecule2+str(n)
                #print(query2)
                myconn_new.execute_no_fetch(query2)
                
def go_info(args, seqlst, dbs):
    # prokka and ncbi are vvvveerrry different
    for seqid in seqlst:
        db_name = args.anno+'_'+seqid
        if db_name in dbs:
            print('Processing',db_name,args.table)
            
            if args.anno == 'PROKKA':
                q="SELECT * from "+db_name+".prokka"
                #print(q)
                result = myconn_old.execute_fetch_select(q)
                
                q2 = "INSERT IGNORE into annotation.prokka_info (seq_id,organism,contigs,bases,CDS,rRNA,repeat_region,tmRNA,tRNA,misc_RNA) VALUES "
                for n in result:
                    lst = list(n)
                    lst2 = [str(n).strip() for n in lst]
                    print(lst2)
                    q2  = q2 +"('" +seqid +"','"+ "','".join(lst2) + "')"
                    #print(q2)
                    myconn_new.execute_no_fetch(q2)
            else:
                q="SELECT * from "+db_name+".assembly_stats"
                result = myconn_old.execute_fetch_select_dict(q)
                # diff 1595 and 2325 fields
                 
                
                q2X="""INSERT IGNORE into annotation.ncbi_info (seq_id,
                    assembly_name,
                    organism,
                    infraspecific_name,
                    taxid,
                    biosample,
                    bioproject,
                    submitter,
                    date,
                    assembly_type,
                    release_type,
                    assembly_level,
                    genome_representation,
                    wgs_project,
                    assembly_method,
                    genome_coverage,
                    sequencing_technology,
                    relation_to_type_material,
                    refseq_category,
                    genbank_assembly_accession,refseq_assembly_accession,
                    refseq_assembly_and_genbank_assemblies_identical) VALUES 
                    """
                #print('21 items')
                q2="""INSERT IGNORE into annotation.ncbi_info (seq_id,    """
                input_fields = ['assembly_name',
                    'organism',
                    'infraspecific_name',
                    'taxid',
                    'biosample',
                    'bioproject',
                    'submitter',
                    'date',
                    'assembly_type',
                    'release_type',
                    'assembly_level',
                    'genome_representation',
                    'wgs_project',
                    'assembly_method',
                    'genome_coverage',
                    'sequencing_technology',
                    'relation_to_type_material',
                    'refseq_category',
                    'genbank_assembly_accession',
                    'refseq_assembly_accession',
                    'refseq_assembly_and_genbank_assemblies_identical']               
                
                
                
                #print(len(result),'items')
                input = ''
                for n in result:
                    #print(n)
                    fn = n['field_name'].lower().replace(' ','_')
                    # for ncbi if n['field_name'] == 'organism_name' then use 'organism'
                    if fn == 'organism_name':
                        print('found org')
                        fn = 'organism'
                    else:
                        pass
                    
                    if fn in input_fields:
                        input += "'"+n['field_value'].strip().replace("'","")+"',"
                        q2 += fn+','
                    else:
                        pass
                    #print(fn)
                    
                    #input += "'"+n[1].strip()+"',"
                
                q2 = q2[:-1] + ") VALUES ('"+seqid+"',"+input[:-1]+')'
                
                #print(q2)
                myconn_new.execute_no_fetch(q2)
                
                
if __name__ == "__main__":

    usage = """
    USAGE:
        takes the annotations  from the old homd to the new db:annotation
        REQUIRES -anno   either NCBI or PROKKA
              -table   ['gc', 'genome', 'gff', 'mole', 'orf', 'info']
        
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=False,  action="store",   dest = "infile", default='none',
                                                    help=" ")
    parser.add_argument("-o", "--outfileprefix",   required=False,  action="store",   dest = "outfileprefix", default='homd_data',
                                                    help=" ")
    parser.add_argument("-anno", "--annotation", required = True, action = 'store', dest = "anno",
                         help = "PROKKA or NCBI")
    parser.add_argument("-t", "--table", required = True, action = 'store', dest = "table",
                         help = "gc, genome, gff, mole, orf, info")
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
                      
    if args.dbhost == 'homd':
        #args.json_file_path = '/groups/vampsweb/vamps/nodejs/json'
       # args.GEN_DATABASE = 'HOMD_genomes_new'
        #args.NEW_DATABASE = 'homd'
        args.olddbhost = '192.168.1.51'
        args.newdbhost = '192.168.1.40'
        args.outdir = '../homd-startup-data/'
        args.prettyprint = False

    elif args.dbhost == 'localhost':
        #args.json_file_path = '/Users/avoorhis/programming/homd-data/json'
        #args.ANNOT_DATABASE  = 'annotation'
        
        args.olddbhost = 'localhost'
        args.newdbhost = 'localhost'
        
        print('localhost')
    else:
        sys.exit('dbhost - error')
    args.indent = None
    if args.prettyprint:
        args.indent = 4
    myconn_old = MyConnection(host=args.olddbhost,  read_default_file = "~/.my.cnf_node")
    myconn_new = MyConnection(host=args.newdbhost,  read_default_file = "~/.my.cnf_node")
    acceptable_annos = ['PROKKA','NCBI']
    if args.anno not in acceptable_annos:
        sys.exit('Wrong annotation: NEED either PROKKA or NCBI')
    acceptable_tables  = ['gc', 'genome', 'gff', 'mole', 'orf', 'info']
    if args.table not in acceptable_tables:
        sys.exit('Wrong table: NEED one of','gc', 'genome', 'gff', 'mole', 'orf', 'info')
    #print(args)
    #args.anno = 'NCBI'
    #args.anno = 'PROKKA'
    (list_of_seqs,dbs) = get_seqs(args)
    if args.table == 'gc':
        go_gc_count(args,list_of_seqs, dbs)
    if args.table == 'genome':
        go_genome_seq(args,list_of_seqs, dbs)
    if args.table == 'gff':
        go_gff(args,list_of_seqs, dbs)
    if args.table == 'orf':
        go_orf_sequence(args,list_of_seqs, dbs)
    if args.table == 'info':
        go_info(args,list_of_seqs, dbs)
    if args.table == 'mole':
        go_molecule(args,list_of_seqs, dbs)
    #print(list_of_seqs)
   #transfer_per_seq(args)
    
    
    