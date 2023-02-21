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

"""
today = str(datetime.date.today())
orf_table_fields = [
  'accession','length_na','gene','PID','product','start','stop'
]
molecule_table_fields = [
'accession','name','bps','gc','date'
]

info_table_fields = ['organism','contigs','bases','CDS','rRNA','tRNA','tmRNA','misc_RNA','repeat_region']
gff_fields = ['region','source','type','start','end','score','strand','phase','attributes']
skip = ['SEQF2736.1']

# should add these: 
# Missing: isolate origin, Sequencing status??, Combined length, GC percentage, ATCC stuff, num_contigs
query = """SELECT `otid_prime`.`otid` AS `otid`
   FROM `otid_prime` 
   join `taxonomy` on(`otid_prime`.`taxonomy_id` = `taxonomy`.`taxonomy_id`)
   join `genus` on(`taxonomy`.`genus_id` = `genus`.`genus_id`)
   join `species` on(`taxonomy`.`species_id` = `species`.`species_id`)
"""
global mysql_errors
mysql_errors = []
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
    


def fill_with_defaults(collector):  
    collector['organism'] = '0'
    collector['CDS'] = '0'
    collector['rRNA'] = '0'
    collector['tRNA'] = '0'
    collector['tmRNA'] = '0'
    collector['bases'] = '0'
    collector['contigs'] = '0'
    collector['misc_RNA'] = '0'
    collector['repeat_region'] = '0'
    return collector
def run(args): 
    global genome_collector
    global mysql_errors
    global dup_count
    mysql_errors = []
    dup_count = 0
    line_collector = {}
    line_collector_aa = {}
    line_collector_na = {}
    seq_count = 0
    
    if args.write2db:
        outfile = args.start_digit+'-'+args.out
        fh = open(outfile, 'w')
    for directory in os.listdir(args.indir):
        d = os.path.join(args.indir, directory)
        seqidplus = directory
        if os.path.isfile(d):
            continue
        if not os.path.isdir(d):
            if args.verbose:
                print('Dir NOT Found',d)
            continue
        if seqidplus in skip:
            continue
            
        if not seqidplus.startswith('SEQF'+args.start_digit):
            continue
        #seqidplus = seqid+'.'+args.seqid_ver_gcaid[seqid]['n']
        #if seqid not in ['SEQF10010']:
        #    continue
        print(seq_count,seqidplus,'Write:',args.write2db)
        seq_count +=1
        count =0
        err_count = 0
        
        collector = {}
        collector = fill_with_defaults(collector)
        
        
        #print(d)
        
        for filename in os.listdir(d):
            
            f = os.path.join(d, filename)
            
            if os.path.isfile(f) and f.endswith('txt'):  # there is only one
                #  All other types of sequences: rRNA, tRNA, ncRNA, etc
                
       
                #for line in gzip.open(files['faa'], 'rt'):
                #info
                # org and strain in .fsa
                
                for line in open(f, 'r'):
                    line=line.strip()
                    
                    #print(line)
                    if line.startswith('organism'):
                        collector['organism'] = line.split(':')[1].strip()
                    if line.startswith('contigs'):
                        collector['contigs'] = line.split(':')[1].strip()
                    if line.startswith('bases'):
                        collector['bases'] = line.split(':')[1].strip()
                    if line.startswith('CDS'):
                        collector['CDS'] = line.split(':')[1].strip()
                    if line.startswith('misc_RNA'):
                        collector['mRNA'] = line.split(':')[1].strip()
                    if line.startswith('rRNA'):
                        collector['rRNA'] = line.split(':')[1].strip()
                    if line.startswith('tRNA'):
                        collector['tRNA'] = line.split(':')[1].strip()
                    if line.startswith('tmRNA'):
                        collector['tmRNA'] = line.split(':')[1].strip()
                    if line.startswith('repeat_region'):
                        collector['repeat_region'] = line.split(':')[1].strip()
                    # vals = "('"+seqid+"','"+record.id+"',COMPRESS('"+str(record.seq)+"'))" 
#                     q = q_info + vals
                
                
                field_order= ['organism','contigs','bases','CDS','rRNA','tRNA','tmRNA','misc_RNA','repeat_region']
                data = '0\t'+seqidplus
                for field in field_order:
                    data += '\t'+collector[field]
                if args.verbose:
                    print()
                    print(data)
                if args.write2db:
                    write2file(data,fh) 
       
def write2file(line,fh):
    #print('writing')
    fh.write(line+'\n')                           
# def run_insert_sql(q):
#     global dup_count
#     
#     #print(q)
#     myconn.execute_no_fetch(q)
#     try:
#         myconn.execute_no_fetch(q)
#         count +=1
#     except mysql.Error as e:
#         print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
#         #print()
#     
#         #err_count +=1
#         if 'Duplicate entry' in str(e):
#             dup_count += 1
#         else:
#             mysql_errors.append((q,e))
#         #sys.exit(e)
#     except:
#         #print('\nERROR\n',q)
#         pass
#     
#     for err in mysql_errors:
#         print()
#         print(err[0],err[1])
    #print('Dup Count:', dup_count)

    
    # for seqid in genome_collector:
#         #print(seqid)
#         print(seqid,genome_collector)
def split_and_run_mysql(line_array, seqid): # must come as vals ()
    array_parts = list(divide_chunks(line_array, 10))
    global dup_count
    #print('len',len(array_parts[0]),len(array_parts[-1]))
    
    
    fields = ",".join(orf_table_fields)
    q_base = "INSERT IGNORE into `"+args.DATABASE+"`.`"+ args.table+"` (seq_id,"+fields+") VALUES "   
    for line_pts in array_parts:
        vals = ''
        
        vals = ",".join(line_pts)
        q = q_base + vals
        if not args.write2db:
            print()
            print(q)
            
        if args.write2db:
    
            try:
                myconn.execute_no_fetch(q)
                count +=1
            except mysql.Error as e:
                print()
                print(q)
                print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
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
def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]
                 
        

        
if __name__ == "__main__":

    usage = """
    USAGE:
        ./add_genomes_to_PROKKA_META_dbV10_1.py 
        
        host and annotation will determine directory to search
        
        -host/--host [homd]  default:localhost
        print('None Selected: --info, --molecules,  --orf) 
        
        

    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    #parser.add_argument("-i", "--infile",   required=True,  action="store",   dest = "infile", default='none',
    #                                                help=" ")
    parser.add_argument("-a", "--anno",   required=False,  action="store",   dest = "anno",  default='prokka',
                                                    help="")
    parser.add_argument("-w", "--write",   required=False,  action="store_true",   dest = "write2db", default=False,
                                                    help=" ")
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",   dest = "verbose", default=False,
                                                    help=" ")
    parser.add_argument("-host", "--host",
                        required = False, action = 'store', dest = "dbhost", default = 'localhost',
                        help = "choices=['homd',  'localhost']")
    
    parser.add_argument("-o", "--outfile",   required=False,  action="store",    dest = "out", default='prokka_meta_info_data.tsv',
                                                    help="verbose print()")
    parser.add_argument("-s", "--start_digit",   required=False,  action="store",   dest = "start_digit", default='1',
                                                    help=" ")
     
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
            #args.indir = '/mnt/efs/bioinfo/projects/homd_add_genomes_V10.1/prokka_V10.1_all'
            args.indir = '/mnt/efs/bioinfo/projects/homd_add_genomes_V10.1_all/add_prokka/prokka'
        else:
            #args.indir = '/mnt/efs/bioinfo/projects/homd_add_genomes_V10.1/GCA_V10.1_all'
            args.indir = '/mnt/efs/bioinfo/projects/homd_add_genomes_V10.1_all/add_ncbi/GCA_V10.1_all'
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
    
    
    # seqid_file = 'new_gca_selected_8148_seqID.csv'
#     args.seqids_from_file = get_seqids_from_new_genomes_file(seqid_file)
#     args.seqid_ver_gcaid = get_seqid_ver_gcaid('seqid_ver_gcaid.txt')
    run(args)
        
        
    
    print('Done  Write?', args.write2db)
    