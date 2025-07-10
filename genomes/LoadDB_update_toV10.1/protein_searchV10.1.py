#!/usr/bin/env python

## SEE https://docs.dhtmlx.com/suite/tree__api__refs__tree.html // new version 7 must load from json file
# this script creates a list of json objects that allows the dhtmlx javascript library
# to parse and show a taxonomy tree (Written for HOMD)

import os, sys
import json,gzip
import argparse
from Bio import SeqIO
import datetime
from datetime import datetime,date
ranks = ['domain','phylum','klass','order','family','genus','species']
today = str(date.today())
sys.path.append('../../homd-data/')
from connect import MyConnection
usable_annotations = ['ncbi','prokka']
# obj = {seqid:[]}             
def make_anno_object():

    new_obj={}
    new_obj['gid'] = ''
    new_obj['organism'] = ''
    new_obj['contigs'] = ''
    new_obj['bases'] = ''
    new_obj['CDS'] = ''
    new_obj['rRNA'] = ''
    new_obj['tRNA'] = ''
    new_obj['tmRNA'] = ''
    ## ignore for now repeat_region, misc_RNA
    return new_obj

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
    # loc
    
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

        
def run(args, dbs):
    #global master_lookup
    master_lookup = []
    
    table = 'protein_searchV10.1'
    q1 = "INSERT IGNORE into `homd`.`"+table+"` (gid,PID,anno,gene,product) VALUES"
    #stopped at 1302,2154
    # prokka first
    if args.prokka_only:
        count = 0
        anno = 'prokka'
        current = find_current_gids(args, table, anno)  # to speed 
        for directory in os.listdir(args.indir_prokka):
            d = os.path.join(args.indir_prokka, directory)
            
            if os.path.isfile(d):
                continue
            seqid = directory
            if seqid in current:  #this bypasses seqids that are already in table
                continue
            count +=1
            print(count,anno,seqid)
            for filename in os.listdir(d):
                f = os.path.join(d, filename)
                if os.path.isfile(f) and f.endswith('.tsv'):
                    sqlline = ''
                    for line in open(f, 'r'):
                        line = line.strip().split('\t')
                        #print(line)
                        if len(line) == 7:
                            if line[3] =='gene' and line[-1] == 'product':
                                continue
                            gene = line[3].replace("'","")
                            product=line[-1].replace("'","")
                            PID= seqid+'_'+line[0].split('_')[1]
                            #print(' ',seqid,PID,gene,product)
                            sqlline = "('"+seqid+"','"+PID+"','"+anno+"','"+gene+"','"+product+"')"
                    
                            query = q1 + sqlline
                            #print(query)
                            myconn_new.execute_no_fetch(query)
                    
                    
                    
    
    # NCBI
    print()
    print()
    print()
    print()
    if args.ncbi_only:
        count = 0
        anno = 'ncbi'
        current = find_current_gids(args, table, anno)  # to speed 
        nakeys = ['locus_tag','db_xref','protein','protein_id','location','gbkeys','pseudo']
        for directory in os.listdir(args.indir_ncbi):
            d = os.path.join(args.indir_ncbi, directory)
            
            if os.path.isfile(d):
                continue
            seqid = directory
            if seqid in current:  #this bypasses seqids that are already in table
                continue
            count += 1
            print(count,anno,seqid)
            for filename in os.listdir(d):
                f = os.path.join(d, filename)
                if os.path.isfile(f) and f.endswith('cds_from_genomic.fna.gz'):
                    with gzip.open(f, "rt") as handle:
                        for record in SeqIO.parse(handle, "fasta"):
                            #print(record.description)               
                            navalues = record.description.split('] [')
                        
                            # if pseudo=True must get pid from db_xref
                            # ODD: lcl|CU468233.1_cds_3573 [locus_tag=ABSDF_p30023] [db_xref=PSEUDO:CAP02997.1] [protein=fragment of transposase of ISAba7, IS5 family] [pseudo=true] [location=complement(19351..19902)] [gbkey=CDS]
                            # REG lcl|CU468233.1_cds_CAP02995.1_3571 [gene=csp] [locus_tag=ABSDF_p30021] [db_xref=EnsemblGenomes-Gn:ABSDF_p30021,EnsemblGenomes-Tr:CAP02995,GOA:B0VVG5,InterPro:IPR002059,InterPro:IPR011129,InterPro:IPR012156,InterPro:IPR012340,InterPro:IPR019844,UniProtKB/TrEMBL:B0VVG5] [protein=cold shock protein] [protein_id=CAP02995.1] [location=18468..18683] [gbkey=CDS]
                            #print(navalues)
                            x_array = [n.split('=') for n in navalues]
                            #print(x_array)
                            mydict = myfun(x_array)
                        
                            if 'protein_id' in mydict:
                            
                                PID = mydict['protein_id']
                                gene = mydict['gene'] or ''
                                product = mydict['product'].replace("'","") or ''
                                sqlline = "('"+seqid+"','"+PID+"','"+anno+"','"+gene+"','"+product+"')"
                                query = q1 + sqlline
                                #print(query)
                                myconn_new.execute_no_fetch(query)
                    
def find_current_gids(args, table, anno):
    new_list =[]
    q1 = "SELECT DISTINCT gid from `homd`.`"+table+"` WHERE anno = '"+anno+"'"
    #print(q1)
    result = myconn_new.execute_fetch_select(q1)
    for row in result:
        new_list.append(row[0])
    
    return new_list
    
if __name__ == "__main__":

    usage = """
    USAGE:
        protein_searchV10.1.py 
         --reads data from the ORIGINAL PROKKA and NCBI Files
        
        puts data in homd.protein_search table for use with homd db search
        
        -n/--ncbi NCBI annotations only
        -p/--prokka PROKKA annotations only
        
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    #parser.add_argument("-i", "--infile",   required=False,  action="store",   dest = "infile", default='none',
    #                                                help=" ")
    
    
    #parser.add_argument("-anno", "--annotation", required = True, action = 'store', dest = "anno",
    #                     help = "PROKKA or NCBI")
    parser.add_argument("-host", "--host",
                        required = False, action = 'store', dest = "dbhost", default = 'localhost',
                        help = "choices=['homd',  'localhost']")
    parser.add_argument("-st", "--start",
                        required = False, action = 'store', dest = "start", default = 0,
                        help = "")
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", default=False,
                                                    help="verbose print()") 
                                                    
    parser.add_argument("-n", "--ncbi",   required=False,  action="store_true",    dest = "ncbi_only", default=False,
                                                    help="ncbi_only") 
    parser.add_argument("-p", "--prokka",   required=False,  action="store_true",    dest = "prokka_only", default=False,
                                                    help="prokka_only") 
    args = parser.parse_args()
    
                                
    if args.dbhost == 'homd':
        #args.DATABASE  = 'homd'
        #dbhost_old = '192.168.1.51'
        dbhost_new = '192.168.1.42'
        args.indir_ncbi = '/mnt/efs/bioinfo/projects/homd_add_genomes_V10.1/GCA_V10.1_all'
        args.indir_prokka = '/mnt/efs/bioinfo/projects/homd_add_genomes_V10.1/prokka_V10.1_all'
        
    elif args.dbhost == 'localhost':  #default
        #args.DATABASE = 'homd'
        #dbhost_old = 'localhost'
        dbhost_new = 'localhost'
        args.indir_ncbi = '/Users/avoorhis/programming/homd-work/new_genomesV10.1/GCA_V10.1_all/'
        args.indir_prokka = '/Users/avoorhis/programming/homd-work/new_genomesV10.1/prokka_V10.1_all/'
    else:
        sys.exit('dbhost - error')
    
    
    #myconn_old = MyConnection(host=dbhost_old, read_default_file = "~/.my.cnf_node")
    myconn_new = MyConnection(host=dbhost_new, read_default_file = "~/.my.cnf_node")
    
    databases = {}
    
    
    #print('dbs',databases)
    
    run(args,databases)
    print()
    print(usage)
    print('DONE','Prokka:',args.prokka_only,'   NCBI:',args.ncbi_only)
    print()
    
