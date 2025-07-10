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
sys.path.append('../homd-data/')
sys.path.append('../../homd-data/')
from connect import MyConnection,mysql
import datetime
"""
 LOAD DATA LOCAL INFILE 'ncbi_faa_data.txt' INTO TABLE protein_seq (id,seq_id,mol_id,protein_id,@col4) SET seq_compressed=COMPRESS(@col4);
"""
today = str(datetime.date.today())
ncbi_orf_table_fields = [
  'accession','length','gene','PID','product','start','stop'
]

skip = ['SEQF3713', 'SEQF3714', 'SEQF2736']
# should add these: 
# Missing: isolate origin, Sequencing status??, Combined length, GC percentage, ATCC stuff, num_contigs
query = """SELECT `otid_prime`.`otid` AS `otid`
   FROM `otid_prime` 
   join `taxonomy` on(`otid_prime`.`taxonomy_id` = `taxonomy`.`taxonomy_id`)
   join `genus` on(`taxonomy`.`genus_id` = `genus`.`genus_id`)
   join `species` on(`taxonomy`.`species_id` = `species`.`species_id`)
"""

global dup_count
dup_count = 0
def get_seqid_ver_gcaid(file):
    gid_list = {}
    with open(file, 'r') as handle:
        for line in handle:
            line = line.strip().split('\t')
            gid_list[line[0]] = {}
            gid_list[line[0]]['n'] = line[1]
            gid_list[line[0]]['gca'] = line[2]
    return gid_list

def get_seqids_from_new_genomes_file(file):
    file_list = []
    with open(file, 'r') as handle:
        first_line = handle.readline()
        for line in handle:
            line = line.strip().split('\t')
            if line[1].startswith('SEQF'):
                if '.' in line[1]:
                    file_list.append(line[1].split('.')[0])
                else:
                    file_list.append(line[1])
    
    #print(file_list,len(file_list))
    return file_list
    


    
def make_info_dict(info):
    return_dict = {}
    info_pts = info.split(';')
    #print(info_pts)
    for item in info_pts:
        i = item.split('=')
        return_dict[i[0]] = i[1]
    return  return_dict
    

    
def run_ncbi(args): 
    #for root, dirs, files in os.walk(args.indir):
    global genome_collector
    global mysql_errors
    global dup_count
    mysql_errors = []
    dup_count = 0
    line_collector = {}
    seq_count = 1
    
    for seqid in args.seqids_from_file:
        #print(seq_count,'SEQ From File',seqid)
        seqidplus = seqid+'.'+args.seqid_ver_gcaid[seqid]['n']
        q = "UPDATE `"+args.db+"`.`"+args.table+"` set seq_id='%s' WHERE seq_id = '%s'" % (seqidplus, seqid)
        if args.verbose:
            print()
            print(q)
        if args.write2db:
            run_insert_sql(q)
            
# mysql -h localhost -u root -p  NCBI_faa  --execute="LOAD DATA LOCAL INFILE 'ncbi_faa_data.txt' INTO TABLE table_name(col1, col2, col3, @col4_comp_data) SET col4=COMPRESS(@col4_comp_data) FIELDS TERMINATED BY '\\t' LINES TERMINATED BY '\\n' IGNORE 1 LINES; SHOW WARNINGS"
def run_insert_sql(q):
    global dup_count
    global mysql_errors
    
    #print(q)
    
    try:
        myconn.execute_no_fetch(q)
        count +=1
    except mysql.Error as e:
        #print()
        
        #print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
        #print()
        
        #err_count +=1
        if 'Duplicate entry' in str(e):
            dup_count += 1
        else:
            mysql_errors.append((q,e))
        #sys.exit(e)
    except:
        #print('\nERROR\n',q)
        pass            
def write2file(line,fh):
    #print('writing')
    fh.write(line+'\n')
    

        
if __name__ == "__main__":

    usage = """
    USAGE:
        ./add_genomes_to_NCBI_dbV10_1.py 
        
        host and annotation will determine directory to search
        
        -host/--host [vamps]  default:localhost
       
        

    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    #parser.add_argument("-i", "--infile",   required=True,  action="store",   dest = "infile", default='none',
    #                                                help=" ")
    parser.add_argument("-a", "--anno",   required=False,  action="store",   dest = "anno",  default='ncbi',
                                                    help="")
    parser.add_argument("-w", "--write",   required=False,  action="store_true",   dest = "write2db", default=False,
                                                    help=" ")
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",   dest = "verbose", default=False,
                                                    help=" ")
    parser.add_argument("-t", "--table",   required=True,  action="store",   dest = "table",
                                                    help=" ")
    parser.add_argument("-db", "--database",   required=True,  action="store",   dest = "db",
                                                    help=" ")
    parser.add_argument("-host", "--host",
                        required = False, action = 'store', dest = "dbhost", default = 'localhost',
                        help = "choices=['homd',  'localhost']")
    
    parser.add_argument("-o", "--outfile",   required=False,  action="store",    dest = "out", default='ncbi_faa_data.tsv',
                                                    help="verbose print()")
    args = parser.parse_args()
    
    #parser.print_help(usage)
                        
    if args.dbhost == 'homd':
        #args.json_file_path = '/groups/vampsweb/vamps/nodejs/json'
        #args.TAX_DATABASE = 'HOMD_taxonomy'
        args.DATABASE = 'homd'
        #dbhost_old = '192.168.1.51'
        dbhost= '192.168.1.42'   #TESTING is 1.42  PRODUCTION is 1.40
        args.prettyprint = False
        #args.ncbi_dir = '/mnt/efs/bioinfo/projects/homd_add_genomes_V10.1/GCA_V10.1_all'
        #args.prokka_dir = '/mnt/efs/bioinfo/projects/homd_add_genomes_V10.1/prokka_V10.1_all'
        if args.anno == 'prokka':
            args.indir = '/mnt/efs/bioinfo/projects/homd_add_genomes_V10.1/prokka_V10.1_all'
        else:
            args.indir = '/mnt/efs/bioinfo/projects/homd_add_genomes_V10.1/GCA_V10.1_all'

    elif args.dbhost == 'localhost':
        #args.json_file_path = '/Users/avoorhis/programming/homd-data/json'
        #args.TAX_DATABASE  = 'HOMD_taxonomy'
        args.DATABASE = 'homd'
        dbhost = 'localhost'
        #dbhost_old = 'localhost'
        if args.anno == 'prokka':
            args.indir = '/Users/avoorhis/programming/homd-work/new_genomesV10.1/prokka_V10.1_all/'
        else:
            args.indir = '/Users/avoorhis/programming/homd-work/new_genomesV10.1/GCA_V10.1_all/'
        
    else:
        sys.exit('dbhost - error')
    
    print('Searching Directory:',args.indir)
    myconn = MyConnection(host=dbhost,   read_default_file = "~/.my.cnf_node")
    #myconn_new = MyConnection(host=dbhost_new, db=args.NEW_DATABASE,  read_default_file = "~/.my.cnf_node")
#     if args.source not in ['segata','dewhirst','eren']:
#         sys.exit('no valid source')
#     if args.source.lower() not in args.infile.lower():
#         sys.exit('file/source mismatch')

    seqid_file = 'new_gca_selected_8148_seqID.csv'
    print('getting seqids from file')
    args.seqids_from_file = get_seqids_from_new_genomes_file(seqid_file)
    args.seqid_ver_gcaid = get_seqid_ver_gcaid('seqid_ver_gcaid.txt')
    #args.seqids_to_skip = get_seqids_in_db(args)
    if args.anno =='ncbi':
        run_ncbi(args)
        
    else:
        pass
        # args.DATABASE = 'PROKKA_genomes'
#         args.table = 'ORF_seq'
#         run_prokka(args)
        
        
    print('Run on Tables:')
    print('Done  Write?', args.write2db)
    