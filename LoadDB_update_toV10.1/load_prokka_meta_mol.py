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


        
def calc_gc(seq_string):
    totalgc = re.sub('[atAT]','',seq_string)
    pctgc = len(totalgc) / len(seq_string) * 100
    return str(round(pctgc, 2))
    
def run(args):
    #for root, dirs, files in os.walk(args.indir):
    global collector
    collector = {}
    global mysql_errors
    mysql_errors = []
    
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
        
        #if seqid not in ['SEQF1161']:
        #    continue
        files = {}
        #molecules:: 'accession'(gbk or fsa),'name'(gbk or fsa),'bps'(fsa calc),'gc'(fsa calc),'date'(gbk)
        
        for filename in os.listdir(d):
            seq = ''
            f = os.path.join(d, filename)
            if os.path.isfile(f) and f.endswith('.fsa'):
                # Are these contigs or 
                files['fsa'] =f
            if os.path.isfile(f) and f.endswith('.gbk'):
                # Protein Sequences
                files['gbk']=f
            
             # fsa has >JAAE01000295.1 [gcode=11] [organism=Fusobacterium necrophorum] [strain=BFTR-1]
        with open(files['fsa'], "rt") as handle:
            mol_id = 0
            for record in SeqIO.parse(handle, "fasta"):
                acc = record.id
                # CABMIK010000017.1 [gcode=11] [organism=Fusobacterium necrophorum] [strain=NA] Fusobacterium
                desc_pts = record.description.split(' [')
                org = desc_pts[2].split('=')[1].rstrip(']')
                #print(record.description,org)
                if acc not in collector:
                    collector[acc] = {}
                #print(record.description)
                bps = str(len(str(record.seq)))
                gc = calc_gc(str(record.seq))
                #print('gc',gc)
                collector[acc]['bps'] = str(bps)
                collector[acc]['gc'] = gc
                collector[acc]['org'] = org
                collector[acc]['date'] = ''
                #print(gc,bps)
        
        
        # with open(files['gbk'], "r") as handle:
#             for line in handle:
#                 line = line.strip()
#                 pts = line.split()
#                 
#                 if line.startswith('LOCUS'):
#                     #print(seqidplus,pts)
#                     acc = pts[1]
#                     
#                     if acc in collector:
#                         collector[acc]['date'] = pts[-1]
#                         #collector[acc]['acc'] = pts[1]
#                     
#                 if line.startswith('DEFINITION'):
#                     if acc in collector:
#                         collector[acc]['org'] = ' '.join(pts[1:])
        
        for acc in collector:
            
            # 'accession','name','bps','gc','date'
            #vals = "('"+seqid+"','"+acc+"','"+collector[acc]['org']+"','"+collector[acc]['bps']+"','"+collector[acc]['gc']+"','"+collector[acc]['date']+"')"
            data = "0\t"+seqidplus+"\t"+acc+"\t"+collector[acc]['org']+"\t"+collector[acc]['bps']+"\t"+collector[acc]['gc']+"\t"+collector[acc]['date']
            if args.verbose:
                print()
                print(data)
            if args.write2db:
                write2file(data,fh)

def write2file(line,fh):
    #print('writing')
    fh.write(line+'\n')    



                 
        

        
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
    parser.add_argument("-o", "--outfile",   required=False,  action="store",    dest = "out", default='prokka_meta_mol.tsv',
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
    

    # seqid_file = 'new_gca_selected_8148_seqID.csv'
#     args.seqids_from_file = get_seqids_from_new_genomes_file(seqid_file)
#     args.seqid_ver_gcaid = get_seqid_ver_gcaid('seqid_ver_gcaid.txt')
    run(args)
        
        
    
    print('Done  Write?', args.write2db)
    