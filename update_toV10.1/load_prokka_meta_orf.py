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

def get_seqids_in_db(args, db, table):
    q = "SELECT DISTINCT seq_id from `"+db+"`.`"+table+"`"
    lst = []
    result = myconn.execute_fetch_select(q)
    for n in result:
       lst.append(n[0])
    return lst
        
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
    

                                       
def run(args):
    pass
    #'accession','length','gene','PID','product','start','stop'
    #file .fna defline acc only 10131: CP005490.3
    #Must add 
    # file gff for acc, pid
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
        
        
        for filename in os.listdir(d):
            seq = ''
            f = os.path.join(d, filename)
            if os.path.isfile(f) and f.endswith('gff'):
                # Protein Sequences
                files['gff']=f
            if os.path.isfile(f) and f.endswith('faa'):
                # Protein Sequences
                files['faa']=f
            if os.path.isfile(f) and f.endswith('ffn'):
                # Protein Sequences
                files['ffn']=f
                
        if 'gff' in files:
                  
            with open(files['gff'], "r") as handle:
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
                        
                        
                              # CDS rRNA ....
                            if pts[2] == 'CDS':
                                info = pts[-1]
                                info_dict = make_info_dict(info)
                                pid = info_dict['ID']
                                #print(pid)
                                collector[pid] = {}
                                collector[pid]['accession'] = pts[0]
                                collector[pid]['type'] = 'CDS'
                                collector[pid]['start'] = pts[3]
                                collector[pid]['stop'] = pts[4]
                                collector[pid]['length_na'] =''
                                collector[pid]['length_aa'] =''
                                collector[pid]['gc'] =''
                               
                                
                                if 'product' in info_dict:
                                    collector[pid]['product'] = info_dict['product'].replace("'","").replace("/","")
                                else:
                                    collector[pid]['product'] = ''
                                
                                if 'gene' in info_dict:
                                    collector[pid]['gene'] = info_dict['gene'].replace("'","")
                                else:
                                    collector[pid]['gene'] = ''
        if 'ffn' in files:
            with open(files['ffn'], "rt") as handle2:
                for record in SeqIO.parse(handle2, "fasta"): 
                    #print('desc',record.description)
                    pid =  record.id
                    if pid in collector:
                        #print('GOTONE',record.id)
                        gc = calc_gc(str(record.seq))
                        
                        collector[pid]['length_na'] = str(len(str(record.seq)))
                        collector[pid]['gc'] = gc
                        
        #sys.exit()                             
        if 'faa' in files:
            with open(files['faa'], "r") as handle2:
                for record in SeqIO.parse(handle2, "fasta"):
                    #print('faa',record.description)   # lcl|JAAE01000299.1_prot_KDE60728.1_2379
                    pid =  record.id
                    if pid in collector:
                        collector[pid]['length_aa'] = str(len(str(record.seq)))
                        
        for pid in collector:
            #print(pid)
            data = '0\t'+seqidplus
            data += '\t'+collector[pid]['accession']
            data += '\t'+collector[pid]['length_na']
            data += '\t'+collector[pid]['length_aa']
            data += '\t'+collector[pid]['gc']
            data += '\t'+collector[pid]['gene']
            data += '\t'+pid
            data += '\t'+collector[pid]['product']
            data += '\t'+collector[pid]['start']
            data += '\t'+collector[pid]['stop']
            if args.verbose:
                    print()
                    print(data)
            if args.write2db:
                    write2file(data,fh)    
                           
                                
                            
                    
                    

                           
def write2file(line,fh):
    #print('writing')
    fh.write(line+'\n')
    
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
    
    parser.add_argument("-s", "--start_digit",   required=False,  action="store",   dest = "start_digit", default='1',
                                                    help=" ")
    parser.add_argument("-o", "--outfile",   required=False,  action="store",    dest = "out", default='prokka_meta_orf.tsv',
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
    

    # seqid_file = 'new_gca_selected_8148_seqID.csv'
#     args.seqids_from_file = get_seqids_from_new_genomes_file(seqid_file)
    args.DATABASE = 'PROKKA_meta'
    
        
        
    run(args)
    print('Done  Write?', args.write2db)
    