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
import requests
global mysql_errors
mysql_errors = []
"""

"""
today = str(datetime.date.today())

# should add these: 
# Missing: isolate origin, Sequencing status??, Combined length, GC percentage, ATCC stuff, num_contigs


    
def run(args):
    #for root, dirs, files in os.walk(args.indir):
    global genome_collector
    tab_file_to_check = 'CRISPR_Cas.tab'
    svg_file_to_check = 'plot.svg'
    # George:I think if there is no CRISPR_Cas.tab file, then there is no good prediction
    genome_list =[]
    genome_collector = {}
    q = "INSERT IGNORE INTO `homd`.`crispr_cas` (seq_id,contig,operon,operon_pos,prediction,crisprs,distances,prediction_cas,prediction_crisprs)"
    q += ' VALUES("%s","%s","%s","%s","%s","%s","%s","%s","%s")'
    
    q2 = "INSERT IGNORE INTO `homd`.`crispr_cas` (seq_id, operon)"
    q2 += ' VALUES("%s","%s")' 
    if args.write2db:
        for gid in os.listdir(args.ftp_base):
            if not gid.startswith('SEQF'+str(args.start_digit)):
                continue
            path_to_check = args.ftp_base+'/'+gid+'/'+tab_file_to_check
            svg_path_to_check = args.ftp_base+'/'+gid+'/'+svg_file_to_check
            if os.path.isfile(path_to_check):
                #print('found',path_to_check)
                fp = open(path_to_check,'r')
                print('running',path_to_check)
                for line in fp:
                    if line.startswith('Contig'):
                        continue
                    print(line)
                    
                    pts = line.split('\t') ## should be 8 parts
                    if len(pts) != 8:
                        sys.exit('row no == 8 error')
                    q_run = q % (gid,pts[0],pts[1],pts[2],pts[3],pts[4],pts[5],pts[6],pts[7])
                    print(q_run)
                    myconn.execute_no_fetch(q_run)   
                
            elif os.path.isfile(svg_path_to_check):  # capture ones with plot.svg and NOT CRISPR_Cas.tab
                q_run = q2 % (gid,'Ambiguous_'+gid)
                print(q_run)
                myconn.execute_no_fetch(q_run) 
            else:
                #print('XXXX',path_to_check)
                pass
    else:
        # file of counts only
        print('counts only')
        for gid in os.listdir(args.ftp_base):
            path_to_check = args.ftp_base+'/'+gid+'/'+tab_file_to_check
            svg_path_to_check = args.ftp_base+'/'+gid+'/'+svg_file_to_check
            if os.path.isfile(path_to_check):
                #print('found',path_to_check)
                fp = open(path_to_check,'r')
                #print('running',path_to_check)
                row_counter = 0
                for line in fp:
                    if line.startswith('Contig'):
                        continue
                    #print(line)
                    row_counter += 1
                    pts = line.split('\t') ## should be 8 parts
                    if len(pts) != 8:
                        sys.exit('row no == 8 error')
                     
                
                #genome_list.append(gid)
                genome_collector[gid] = row_counter
            elif os.path.isfile(svg_path_to_check):  # capture ones with plot.svg and NOT CRISPR_Cas.tab
                genome_collector[gid] = 'A'  # Ambiguous
            else:
                #print('XXXX',path_to_check)
                pass
    # counter = 0
#     for gid in genome_list:
#        #print(gid)
#        q = "update `"+args.DATABASE+"`.`genomes` set crispr_cas='1' where seq_id='"+gid+"'"
#        #print(q)
#        #res = myconn.execute_no_fetch(q)
#        counter += 1
#     print('count',counter)
        file =  os.path.join('CRISPRLookup.json')
        print('Done ')
        print_dict(file, genome_collector)

def print_dict(filename, dict):
    print('writing',filename)
    with open(filename, 'w') as outfile:
        json.dump(dict, outfile, indent=args.indent)

        
if __name__ == "__main__":

    usage = """
    USAGE:
        ./add_genomes_to_NCBI_METAV10_1.py 
        
        host and annotation will determine directory to search
        
        -host/--host [homd]  default:localhost
       
        

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
    parser.add_argument("-host", "--host",
                        required = False, action = 'store', dest = "dbhost", default = 'localhost',
                        help = "choices=['homd',  'localhost']")
    
    parser.add_argument("-s", "--start_digit",   required=False,  action="store",   dest = "start_digit", default='1',
                                                    help=" ")
    parser.add_argument("-o", "--outfile",   required=False,  action="store",    dest = "out", default='ncbi_meta_info.tsv',
                                                    help="verbose print()")
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
        sys.exit('localhost::Has to be run on an homd server')
        #dbhost_old = 'localhost'
       
        
    else:
        sys.exit('dbhost - error')
    
    
    myconn = MyConnection(host=dbhost,   read_default_file = "~/.my.cnf_node")
    #myconn_new = MyConnection(host=dbhost_new, db=args.NEW_DATABASE,  read_default_file = "~/.my.cnf_node")
#     if args.source not in ['segata','dewhirst','eren']:
#         sys.exit('no valid source')
#     if args.source.lower() not in args.infile.lower():
#         sys.exit('file/source mismatch')
    args.indent = 4
    args.url_base = 'https://www.homd.org/'
    args.ftp_base = '/mnt/efs/lv1_dev/homd_ftp/genomes/CRISPR_Cas/CCTyper/'
    
    run(args)
    

    
