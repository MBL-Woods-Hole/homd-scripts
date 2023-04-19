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
    if os.path.isfile(file_path) and file_path.endswith('.gff'):
        with open(file_path, "r") as handle:
            mol_id = 0
            nomore = False
            for line in handle:
                line = line.strip()
                if line.startswith('##'):
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
                        if 'ID' in info_dict:
                            collector[info_dict['ID']] = {'type':pts[2],'mol_id':pts[0]}
                        
    return collector

def run_prokka(args): 
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
    for seqid in args.seqids_from_file:
        d = os.path.join(args.indir, seqid)
    #for directory in os.listdir(args.indir):
    #    d = os.path.join(args.indir, directory)
        if os.path.isfile(d):
            continue
        if not os.path.isdir(d):
            if args.verbose:
                print('Dir NOT Found',d)
            continue
        if seqid in skip:
            continue
        if not seqid.startswith('SEQF'+args.start_digit):
            continue
        seqidplus = seqid+'.'+args.seqid_ver_gcaid[seqid]['n']
        #if seqid not in ['SEQF10010']:
        #    continue
        print(seq_count,seqidplus,args.write2db)
        #if seqid not in ['SEQF10010']:
        #    continue
        seq_count +=1
        #print(d)
        count =0
        
        err_count = 0
        
        
        #print('SEQID:',seqid)
        
        
        
        
        collector = {}
        files = {}
        
        
        #print(d)
        
        for filename in os.listdir(d):
            
            f = os.path.join(d, filename)
            if os.path.isfile(f) and f.endswith('.gff'):
                files['gff'] =f
            if os.path.isfile(f) and f.endswith('.fna'):
                # Are these contigs or 
                files['contig'] =f
            if os.path.isfile(f) and f.endswith('.faa'):
                # Protein Sequences
                files['faa']=f
            if os.path.isfile(f) and f.endswith('.ffn'):
                #"Nucleotide sequences from which proteins are translated from"
                files['ffn']=f
            if os.path.isfile(f) and f.endswith('.tsv'):
                #  All other types of sequences: rRNA, tRNA, ncRNA, etc
                files['misc_rna']=f
        #print('files',files)

        if 'misc_rna' in files:
                db = 'PROKKA_misc'
                table='misc_rna_seq'
                fields = ['seq_id','pid','rna_type','seq_compressed']
                
                
                with open(files['misc_rna'], "r") as handle:
                    for line in handle:
                        line = line.strip().split('\t')
                        
                        if len(line) != 7:
                            continue
                        if line[1] == 'CDS' or line[0] == 'locus_tag':
                            continue
                        
                        if line[0] != 'repeat_region':
                            collector[line[0]] = { "type":line[1]}
                        #collector['type'] = line[1]
                       
                with open(files['ffn'], "rt") as handle:
                    for record in SeqIO.parse(handle, "fasta"):
                        pass
                        #print(seqid,record.id) 
                        if record.id in collector:     
                           
                           collector[record.id]['seq'] = str(record.seq)
                #print()
                #print(seqid,collector) 
                
                for pid in collector:
                    
                    #vals = "('"+seqid+"','"+pid+"','"+collector[pid]['type']+"',COMPRESS('"+collector[pid]['seq']+"'))"
                    data = '0\t'+seqidplus+'\t'+pid+'\t'+collector[pid]['type']+'\t'+collector[pid]['seq']
                    
                    if args.verbose:
                        print()
                        print(data)
                    if args.write2db:
                        write2file(data,fh)
       
        else:
            print(seqid,'None Selected: --contig, --faa,  --ffn, or --misc')                 
def write2file(line,fh):
    #print('writing')
    fh.write(line+'\n')
    

    
    # for seqid in genome_collector:
#         #print(seqid)
#         print(seqid,genome_collector)
def split_and_run_mysql(line_array, seqid):
    array_parts = list(divide_chunks(line_array, 10))
    global dup_count
    #print('len',len(array_parts[0]),len(array_parts[-1]))
    
    
    fields = ",".join(ncbi_orf_table_fields)
    q_base = "INSERT into `"+args.DATABASE+"`.`"+ args.table+"` (seq_id,"+fields+") VALUES "   
    for line_pts in array_parts:
        vals = ''
        
        vals = ",".join(line_pts)
        q = q_base+vals
        if not args.write2db:
            print()
            print(q)
            
        if args.write2db:
    
            try:
                myconn.execute_no_fetch(q)
                count +=1
            except mysql.Error as e:
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
def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]
                 
        

        
if __name__ == "__main__":

    usage = """
    USAGE:
        ./add_genomes_to_PROKKA_dbV10_1.py 
        
        host and annotation will determine directory to search
        
        -host/--host [vamps]  default:localhost
        print('None Selected: --contig, --faa,  --ffn, or --misc') 
        
        

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
    parser.add_argument("-o", "--outfile",   required=False,  action="store",    dest = "out", default='prokka_misc_data.tsv',
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
    #myconn_new = MyConnection(host=dbhost_new, db=args.NEW_DATABASE,  read_default_file = "~/.my.cnf_node")
#     if args.source not in ['segata','dewhirst','eren']:
#         sys.exit('no valid source')
#     if args.source.lower() not in args.infile.lower():
#         sys.exit('file/source mismatch')
    seqid_file = 'new_gca_selected_8148_seqID.csv'
    args.seqids_from_file = get_seqids_from_new_genomes_file(seqid_file)
    args.seqid_ver_gcaid = get_seqid_ver_gcaid('seqid_ver_gcaid.txt')
    if args.anno =='prokka':
        run_prokka(args)
        
    else:
        pass
        # args.DATABASE = 'PROKKA_genomes'
#         args.table = 'ORF_seq'
#         run_prokka(args)
        
        
    
    print('Done  Write?', args.write2db)
    