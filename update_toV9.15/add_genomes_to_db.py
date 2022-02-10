#!/usr/bin/env python

## SEE https://docs.dhtmlx.com/suite/tree__api__refs__tree.html // new version 7 must load from json file
# this script creates a list of json objects that allows the dhtmlx javascript library
# to parse and show a taxonomy tree (Written for HOMD)
##
import os, sys
import json
#from json import JSONEncoder
import argparse
import csv
sys.path.append('../../homd-data/')
from connect import MyConnection
import datetime
ranks = ['domain','phylum','klass','order','family','genus','species']
today = str(datetime.date.today())




def run_csv(): 
    collector = {}
    extras = './extra_infoV9.15.csv'
    #/mnt/efs/bioinfo/projects/homd_add_genomes/assembly_summary_genbank_PRJN282954_tobeadded.txt
    extra_collector = {}
    with open(extras) as csv_file: 
        csv_reader = csv.DictReader(csv_file, delimiter='\t') # KK tab
        for row in csv_reader:
            genbank_assem = row['# assembly_accession']
           #  asm = ''.join(row['# assembly_accession'].split('_'))
#             print(asm)
            extra_collector[genbank_assem] = row
        print(row)
    with open(args.infile) as csv_file: 
        csv_reader = csv.DictReader(csv_file, delimiter='\t') # KK tab
        
        for row in csv_reader:
            # print()
#             print(row)
#             print(row['HMT_ID'],row['SEQ_ID'],row['Genus'],row['Species'])
            otid = row['HMT_ID']
            # check if otid exists
            verify_hmt = verify_id('otid_prime','otid',otid)
            if not verify_hmt:
                print('\notid:'+otid+' Does Not Exist\n')
            seqid = row['SEQ_ID']
            verify_seqid = verify_id('genomes','seq_id',seqid)
            if verify_seqid:
                print('\notid:'+otid+' Exists in genomes\n')
            genus = row['Genus']  # dont need this we have otid
            species = row['Species']  # dont need this we have otid
            contigs = row['Contigs']
            strain = row['Strain']
            combined_size = row['Combined_Size']
            # Flags:\n
#             11 — Annotated at HOMD with NCBI Annotation\n
#             12 -- Annotated at HOMD without NCBI Annotation\n
#             21 -- Genomes with NCBI annotation\n
#             91  - is for those NonOralRef genomes'
            habitat = row['Habitat']
            if habitat == 'NonOralRef':
                flag = '91'
            else:
                flag = '21'
            seq_source = row['Sequence_Source']
            # https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/018/141/845/GCA_018141845.1_ASM1814184v1
            seq_source_parts = seq_source.split('/')[-1].split('_')
            #print(seq_source_parts[-1])
            gca = seq_source_parts[0]+'_'+seq_source_parts[1]
            asm = seq_source_parts[2]
            print('gca',gca,'asm',asm)
            seq_center = extra_collector[gca]['submitter']
            ncbi_taxon_id = extra_collector[gca]['taxid'] # from extra table
            bioproject = extra_collector[gca]['bioproject'] # PRJ...
            biosample = extra_collector[gca]['biosample']
            # goldstamp_id == biosample_ID
            genbank_acc = asm
            genbank_assem = gca
            status = extra_collector[gca]['submitter'] #from exta table: Complete or
            # in db change gc_comment to genbank_assembly (MBL) VARCHAR(20)
            # change genbank_acc to genbank_accession: 
            # change goldstamp_id to ncbi_biosample
            # change ncbi_id to ncbi_bioproject
            # isolate origin varchar(200)
            

            q1 = "INSERT IGNORE into genomes (seq_id,otid,sequence_center,culture_collection,number_contig,combined_length,status,flag)"
            q1 += " VALUES('%s','%s','%s','%s','%s','%s','%s','%s')"
            q1 = q1 % (str(seqid),str(otid),seq_center,strain,str(contigs),str(combined_size),'Complete',flag)
            print(q1)
            myconn.execute_no_fetch(q1)
            
            q2 = "INSERT IGNORE into genomes_homd_extra (seq_id, ncbi_bioproject, ncbi_taxon_id, ncbi_biosample,"
            q2 += " genbank_accession, genbank_assembly,16S_rrna,16S_rrna_comment,biochemistry,dna_molecular_Summary,orf_annotation_Summary)"
            q2 += " VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
            q2 = q2 % (str(seqid),str(bioproject),str(ncbi_taxon_id),biosample,genbank_acc,genbank_assem,'','','','','')
            print(q2)
            myconn.execute_no_fetch(q2)
    
def verify_id(table,field,id):
    q_check = "SELECT * FROM `"+table+"` WHERE `"+field+"`='"+id+"'"
    myconn.execute_fetch_one(q_check)
    if myconn.cursor.rowcount == 0:
        return False
    else:
        return True
        
if __name__ == "__main__":

    usage = """
    USAGE:
        ./add_genomes_to_db.py -i infile
        
        infile tab delimited
          SEQID_info_V9.15-corrected.csv

    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=True,  action="store",   dest = "infile", default='none',
                                                    help=" ")
#    parser.add_argument("-s", "--source",   required=True,  action="store",   dest = "source", 
#                                                    help="ONLY segata dewhirst eren")
    
    parser.add_argument("-host", "--host",
                        required = False, action = 'store', dest = "dbhost", default = 'localhost',
                        help = "choices=['homd',  'localhost']")
    
    parser.add_argument("-d", "--delimiter", required = False, action = 'store', dest = "delimiter", default = 'tab',
                         help = "Delimiter: commaAV[Default]: 'comma' or tabKK: 'tab'")
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", default=False,
                                                    help="verbose print()") 
    args = parser.parse_args()
    
    #parser.print_help(usage)
                        
    if args.dbhost == 'homd':
        #args.json_file_path = '/groups/vampsweb/vamps/nodejs/json'
        #args.TAX_DATABASE = 'HOMD_taxonomy'
        args.DATABASE = 'homd'
        #dbhost_old = '192.168.1.51'
        dbhost= '192.168.1.40'
        args.prettyprint = False

    elif args.dbhost == 'localhost':
        #args.json_file_path = '/Users/avoorhis/programming/homd-data/json'
        #args.TAX_DATABASE  = 'HOMD_taxonomy'
        args.DATABASE = 'homd'
        dbhost = 'localhost'
        #dbhost_old = 'localhost'
        
    else:
        sys.exit('dbhost - error')
    
    myconn = MyConnection(host=dbhost, db=args.DATABASE,   read_default_file = "~/.my.cnf_node")
    #myconn_new = MyConnection(host=dbhost_new, db=args.NEW_DATABASE,  read_default_file = "~/.my.cnf_node")
#     if args.source not in ['segata','dewhirst','eren']:
#         sys.exit('no valid source')
#     if args.source.lower() not in args.infile.lower():
#         sys.exit('file/source mismatch')
    
    run_csv()
   
    