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

skip = ['SEQF2736']
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
    seqid_count = 0
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
    
def run_ncbi(args): 
    #for root, dirs, files in os.walk(args.indir):
    global genome_collector
    global mysql_errors
    global dup_count
    mysql_errors = []
    dup_count = 0
    line_collector = {}
    seq_count = 1
    if args.write2db:
        outfile = args.start_digit+'-'+args.out
        fh = open(outfile, 'w')
    for seqid in args.seqid_ver_gcaid:
        #print(seq_count,'SEQ From File',seqid)
        d = os.path.join(args.indir, seqid)
    #for directory in os.listdir(args.indir):
    #    d = os.path.join(args.indir, directory)
        #print(d,os.path.isdir(d))
        if os.path.isfile(d) or not os.path.isdir(d):
            continue
        
        if seqid in skip:
            continue
        if not seqid.startswith('SEQF'+args.start_digit):
            continue
        seqidplus = seqid+'.'+args.seqid_ver_gcaid[seqid]['n']
        # if seqid not in ['SEQF10010']:
#            continue
        print(seq_count,seqidplus,'Write:',args.write2db)
        seq_count +=1
        count =0
        err_count = 0
        
        
        line_collector = {}
        files = {}
       
        for filename in os.listdir(d):
            
            f = os.path.join(d, filename)
            if os.path.isfile(f) and f.endswith('genomic.fna.gz') and not f.endswith('rna_from_genomic.fna.gz') \
                             and not f.endswith('cds_from_genomic.fna.gz'):
                # Are these contigs or 
                files['contig'] =f
            if os.path.isfile(f) and f.endswith('genomic.gff.gz'):
                # Protein Sequences
                files['gff']=f
            if os.path.isfile(f) and f.endswith('protein.faa.gz'):
                # Protein Sequences
                files['faa']=f
            if os.path.isfile(f) and f.endswith('cds_from_genomic.fna.gz'):
                #"Nucleotide sequences from which proteins are translated from"
                files['ffn']=f
            if os.path.isfile(f) and f.endswith('rna_from_genomic.fna.gz'):
                #  All other types of sequences: rRNA, tRNA, ncRNA, etc
                files['misc_rna']=f
            

        #elif args.faa:     # update to include mol_id
        count = 0
        if 'contig' in files:
            if 'contig' in files:  # seqf10010 has no protein.faa file
                #for line in gzip.open(files['faa'], 'rt'):
                
                fields = ['seq_id','mol_id','seq_compressed']
                with gzip.open(files['contig'], "rt") as handle:
                    for record in SeqIO.parse(handle, "fasta"):
                        #print(record.id)
                        mol_id = record.id
                        data = '0\t'+seqidplus+'\t'+mol_id+'\t'+str(record.seq)
                        if args.verbose:
                            print()
                            print(data)
                        if args.write2db:
                            write2file(data,fh)
                            

        else:
            print(seqid,'faa not-found or None Selected: --contig, --faa,  --ffn, or --misc') 
            
# mysql -h localhost -u root -p  NCBI_faa  --execute="LOAD DATA LOCAL INFILE 'ncbi_faa_data.txt' INTO TABLE table_name(col1, col2, col3, @col4_comp_data) SET col4=COMPRESS(@col4_comp_data) FIELDS TERMINATED BY '\\t' LINES TERMINATED BY '\\n' IGNORE 1 LINES; SHOW WARNINGS"
            
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
    parser.add_argument("-s", "--start_digit",   required=False,  action="store",   dest = "start_digit", default='1',
                                                    help=" ")
    parser.add_argument("-host", "--host",
                        required = False, action = 'store', dest = "dbhost", default = 'localhost',
                        help = "choices=['homd',  'localhost']")
    
    parser.add_argument("-o", "--outfile",   required=False,  action="store",    dest = "out", default='ncbi_contig_data.tsv',
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
    """
    
 LOAD DATA LOCAL INFILE '1-ncbi_contig_data.tsv' INTO TABLE contig_seq_load (id,seq_id,mol_id,@col3) SET seq_compressed=COMPRESS(@col3);
"""
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
        
        
    
    print('Done  Write?', args.write2db)
    
