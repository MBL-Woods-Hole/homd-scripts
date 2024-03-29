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
 LOAD DATA LOCAL INFILE 'ncbi_ffn_data.txt' INTO TABLE ffn_seq (id,seq_id,mol_id,protein_id,@col4) SET seq_compressed=COMPRESS(@col4);
"""
today = str(datetime.date.today())
ncbi_orf_table_fields = [
  'accession','length','gene','PID','product','start','stop'
]

skip = ['SEQF2736.1']
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
    
# def get_seqids_in_db(args):
#     
#     if args.faa:
#        db = 'NCBI_faa'
#        table = 'protein_seq'
#     elif args.ffn:
#        db = 'NCBI_ffn'
#        table = 'ffn_seq'
#     elif args.misc:
#        db = 'NCBI_misc'
#        table = 'misc_rna_seq'
#     elif args.contig:
#        db = 'NCBI_contig'
#        table = 'contig_seq'
#     else:
#         return
#     print('getting seqids that are already in',db,table)
#     q = "SELECT DISTINCT seq_id from `"+db+"`.`"+table+"`"
#     lst = []
#     result = myconn.execute_fetch_select(q)
#     for n in result:
#        lst.append(n[0])
#     return lst
        
def calc_gc(seq_string):
    totalgc = re.sub('[atAT]','',seq_string)
    pctgc = len(totalgc) / len(seq_string) * 100
    return str(round(pctgc, 2))
    
def make_info_dict(info):
    return_dict = {}
    info_pts = info.split(';')
    #print(info_pts)
    for item in info_pts:
        i = item.split('=')
        return_dict[i[0]] = i[1]
    return  return_dict
    
def grab_gff_data(file_path):
    
    collector = {}
    nomore = False
    if os.path.isfile(file_path) and file_path.endswith('genomic.gff.gz'):
        #with open(file_path, "r") as handle:
        with gzip.open(file_path, "rt") as handle:
            mol_id = 0
            nomore = False
            for line in handle:
                line = line.strip()
                if line.startswith('##') or line.startswith('#!'):
                    continue
                    #  ##sequence-region CABMIK010000024.1 1 10250
                elif line.startswith('>'):
                    
                    nomore = True
                    continue
                if not nomore:
                    pts = line.split('\t')
                    if args.verbose:
                        print()
                        print(pts)
                    if pts[2] != 'repeat_region':
                        
                        info = pts[-1]
                        info_dict = make_info_dict(info)
                        id_pts = info_dict['ID'].split('-')
                        if len(id_pts) > 1:
                            pid = id_pts[1]
                        else:
                            pid = id_pts[0]
                        collector[pid] = {'type':pts[2],'mol_id':pts[0]}
                        
    
    return collector
    
def run(args): 
    #for root, dirs, files in os.walk(args.indir):
    global genome_collector
    global mysql_errors
    global dup_count
    
    mysql_errors = []
    dup_count = 0
    line_collector = {}
    seq_count = 1
    
    nofile_count = 0
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
        
        
        line_collector = {}
        files = {}
       
        for filename in os.listdir(d):
            
            f = os.path.join(d, filename)
            if not os.path.isfile(f):
                continue
            if f.endswith('genomic.gff.gz'):
                # Protein Sequences
                files['gff']=f
            if f.endswith('protein.faa.gz'):
                # Protein Sequences
                files['faa']=f
            if f.endswith('cds_from_genomic.fna.gz'):
                #"Nucleotide sequences from which proteins are translated from"
                files['ffn']=f
                
        if 'ffn' in files:    # already includes mol_id and protein_id
            with gzip.open(files['ffn'], "rt") as handle:
                for record in SeqIO.parse(handle, "fasta"):
                    
                    id_pts = record.id.split('_')
                    mol_id = id_pts[0].split('|')
                    if len(mol_id) >1:
                        mol_id = mol_id[1]
                    else:
                        mol_id = mol_id[0]
                    protein_id = id_pts[2]
                    #pid = record.id.split('_')[2]
                    data = '0\t'+seqidplus+'\t'+mol_id+'\t'+protein_id+'\t'+str(record.seq)
                    
                    if args.verbose:
                        print()
                        print(data)
                    if args.write2db:
                        write2file(data,fh)
        else:
            nofile_count +=1
            print(nofile_count,'None Selected: --contig, --faa,  --ffn, or --misc') 
    
    print('NoFile count',nofile_count)
def write2file(line,fh):
    #print('writing')
    fh.write(line+'\n')
        
def run_sql(q):
    global dup_count
    
    #print(q)
    myconn.execute_no_fetch(q)
    try:
        myconn.execute_no_fetch(q)
        count +=1
    except mysql.Error as e:
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
    
    for err in mysql_errors:
        print()
        print(err[0],err[1])
    #print('Dup Count:', dup_count)

    
    # for seqid in genome_collector:
#         #print(seqid)
#         print(seqid,genome_collector)
# def split_and_run_mysql(line_array, seqid):
#     array_parts = list(divide_chunks(line_array, 10))
#     global dup_count
#     #print('len',len(array_parts[0]),len(array_parts[-1]))
#     
#     
#     fields = ",".join(ncbi_orf_table_fields)
#     q_base = "INSERT into `"+args.DATABASE+"`.`"+ args.table+"` (seq_id,"+fields+") VALUES "   
#     for line_pts in array_parts:
#         vals = ''
#         
#         vals = ",".join(line_pts)
#         q = q_base+vals
#         if not args.write2db:
#             print()
#             print(q)
#             
#         if args.write2db:
#     
#             try:
#                 myconn.execute_no_fetch(q)
#                 count +=1
#             except mysql.Error as e:
#                 #print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
#                 #print()
#             
#                 #err_count +=1
#                 if 'Duplicate entry' in str(e):
#                     dup_count += 1
#                 else:
#                     mysql_errors.append((q,e))
#                 #sys.exit(e)
#             except:
#                 #print('\nERROR\n',q)
#                 pass
# def divide_chunks(l, n):
#     # looping till length l
#     for i in range(0, len(l), n):
#         yield l[i:i + n]
#                  
        

        
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
    parser.add_argument("-s", "--start_digit",   required=False,  action="store",   dest = "start_digit", default='1',
                                                    help=" ")
    parser.add_argument("-host", "--host",
                        required = False, action = 'store', dest = "dbhost", default = 'localhost',
                        help = "choices=['homd',  'localhost']")
     
    parser.add_argument("-o", "--outfile",   required=False,  action="store",    dest = "out", default='ncbi_ffn_data.tsv',
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
    #myconn_new = MyConnection(host=dbhost_new, db=args.NEW_DATABASE,  read_default_file = "~/.my.cnf_node")
#     if args.source not in ['segata','dewhirst','eren']:
#         sys.exit('no valid source')
#     if args.source.lower() not in args.infile.lower():
#         sys.exit('file/source mismatch')
 #  LOAD DATA LOCAL INFILE 'ncbi_ffn_data.txt' INTO TABLE ffn_seq (id,seq_id,mol_id,protein_id,@col4) SET seq_compressed=COMPRESS(@col4);
   
    seqid_file = 'new_gca_selected_8148_seqID.csv'
    print('getting seqids from file')
    args.seqids_from_file = get_seqids_from_new_genomes_file(seqid_file)
    args.seqid_ver_gcaid = get_seqid_ver_gcaid('seqid_ver_gcaid.txt')
    #args.seqids_to_skip = get_seqids_in_db(args)
    
    run(args)
        
    
        
        
    
    print('Done  Write?', args.write2db)
    
