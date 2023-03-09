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
global mysql_errors
mysql_errors = []
"""

"""
today = str(datetime.date.today())
ncbi_molecule_table_fields = [
'accession','name','bps','gc','date'
]
ncbi_orf_table_fields = [
  'accession','length','gene','PID','product','start','stop'
]
ncbi_info_table_fields = [
'assembly_name',
'organism',
'infraspecific',
'taxid',
'biosample',
'bioproject',
'submitter',
'date',
'assembly_type',
'release_type',
'assembly_level',
'genome_rep',
'wgs',
'method',
'coverage',
'seqtech',
'gb_assembly',
'refseq_assembly',
'paired_asm_comp'
]
gff_fields = ['region','source','type','start','end','score','strand','phase','attributes']
skip = ['SEQF2736.1']
#skip = ['SEQF3713', 'SEQF3714', 'SEQF2736']
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
    
def myfun(l):
    #print(l,l[0])
    locald={}
    retd = {'gene':'','start':'','stop':'','product':''}
    grab = ['gbkey','location','protein_id','protein','db_xref','locus_tag','pseudo','gene']
    for n in l:
        if n[0] in grab:
            locald[n[0]] = n[1]
    #need protein_id
    if 'protein_id' in locald:
        retd['protein_id'] = locald['protein_id']
    if 'pseudo' in locald and locald['pseudo']=='true' and 'db_xref' in locald and 'protein_id' not in locald:
        retd['protein_id'] = locald['db_xref'].split(':')[1]
    # loc variations
    # location=2193..3524
    # location=complement(5107..5550)
    #  location=complement(join(28..875,875..1127))
    #  location=join(99952..100204,100204..101081)
    
    if 'location' in locald:
        if 'complement' in locald['location']:
            # 
            if 'join' in locald['location']:
                # location=complement(join(28..875,875..1127))
                #regex = re.findall("\(join\(.*?\)\)", locald['location'])
                match = re.search(r"\(join\((.*?)\)\)", locald['location'])
                #print('XXXXXX',locald['location'],regex)
                #print('YYYY',locald['location'],match.group(1).split(','))  #28..875,875..1127
                # regex = ['(join(28..875,875..1127)']
                #sys.exit()
                loc = match.group(1).split(',')
                try:
                    retd['start'] = loc[0].split('..')[0].lstrip('(')
                    retd['stop']  = loc[1].split('..')[1].rstrip(')')
                except:
                    retd['start'] = '0'
                    retd['stop'] = '0'
            else:
                # may have complement(24249..24851)  or just '23923..24084'
                # location=complement(5107..5550)
                regex = re.findall("\(.*?\)", locald['location'])
                #print(regex)  #regex ['(19351..19902)']
                loc = regex[0].split('..')
                retd['start'] = loc[0].lstrip('(')
                retd['stop']  = loc[1].rstrip(')')
        
        else:
            #
            if 'join' in locald['location']:
                # location=join(99952..100204,100204..101081)
                regex = re.findall("\(.*?\)", locald['location'])
                loc = regex[0].split(',')
                try:
                    retd['start'] = loc[0].split('..')[0].lstrip('(')
                    retd['stop']  = loc[1].split('..')[1].rstrip(')')
                except:
                    retd['start'] = '0'
                    retd['stop'] = '0'
            else:
                # location=2193..3524
                loc = locald['location'].split('..')
                retd['start'] = loc[0]
                retd['stop'] = loc[1]
    # gene
    #print('l[0]',l[0])
    if 'gene' in locald:
        retd['gene'] = locald['gene']
    elif 'locus_tag' in locald:
        retd['gene'] = locald['locus_tag']
    elif 'locus_tag' in l[0][0]:
        #print('XX',l[0][0])
        retd['gene'] = l[0][1]
    if 'protein' in locald:
        retd['product'] = locald['protein']
    return retd


    

            
        
def run(args):
    #for root, dirs, files in os.walk(args.indir):
    global genome_collector
    genome_collector = {}
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
        line_collector = {}
        files = {}
        #if seqid not in ['SEQF1161']:
        #    continue
        # 'accession','name','bps','gc','date'
        fields = ",".join(ncbi_molecule_table_fields)
        
        for filename in os.listdir(d):
            seq = ''
            f = os.path.join(d, filename)
            
            if os.path.isfile(f) and f.endswith('genomic.gff.gz'):
                files['gff']=f
        #print(files)  
        if 'gff' in files:  
            with gzip.open(files['gff'], "rt") as handle:
                
                for line in handle:
                    line = line.strip().split('\t')
                    #print(line)
                    
                    if len(line) == 9:
                        data = '0\t'+seqidplus
                        data += '\t'+line[0]
                        data += '\t'+line[1]
                        data += '\t'+line[2]
                        data += '\t'+line[3]
                        data += '\t'+line[4]
                        data += '\t'+line[5]
                        data += '\t'+line[6]
                        data += '\t'+line[7]
                        data += '\t'+line[8]
                        #print(data)

                        if args.verbose:
                            print()
                            print(data)
                        if args.write2db:
                            write2file(data,fh)

            
def write2file(line,fh):
    #print('writing')
    fh.write(line+'\n')
                
def make_info_dict(info):
    return_dict = {}
    info_pts = info.split(';')
    #print(info_pts)
    for item in info_pts:
        i = item.split('=')
        return_dict[i[0]] = i[1]
    return  return_dict
            

    
def split_and_run_mysql(line_array, seqid):
    array_parts = list(divide_chunks(line_array, 50))
    global dup_count
    #print('len',len(array_parts[0]),len(array_parts[-1]))
    
    
    fields = ",".join(ncbi_orf_table_fields)
    q_base = "INSERT ignore into `"+args.DATABASE+"`.`"+ args.table+"` (seq_id,"+fields+") VALUES "   
    for line_pts in array_parts:
        vals = ''
        
        vals = ",".join(line_pts)
        q = q_base+vals
        if not args.write2db:
            print()
            print(q)
            
        if args.write2db:
            run_insert_sql(q)
            
def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]
                 
        

        
if __name__ == "__main__":

    usage = """
    USAGE:
        ./add_genomes_to_NCBI_METAV10_1.py 
        
        host and annotation will determine directory to search
        
        -host/--host [homd]  default:localhost
       
        print('None Selected: --info, --molecules,  --orf) 
        

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
    parser.add_argument("-o", "--outfile",   required=False,  action="store",    dest = "out", default='ncbi_meta_gff.tsv',
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
    #seqid_file = 'new_gca_selected_8148_seqID.csv'
    #args.seqids_from_file = get_seqids_from_new_genomes_file(seqid_file)
    #args.seqid_ver_gcaid = get_seqid_ver_gcaid('seqid_ver_gcaid.txt')
    
    #run mysql load data local infile
    # MUST BE ON HOST: 1.42 
    # enter mysql and choose DATABASE
    # LOAD DATA LOCAL INFILE 'filename' INTO TABLE tablename
    # 
    
    
    run(args)
    
    
    print('Done  Write?', args.write2db)
    