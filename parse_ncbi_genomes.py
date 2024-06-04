#!/usr/bin/env python

## SEE https://docs.dhtmlx.com/suite/tree__api__refs__tree.html // new version 7 must load from json file
# this script creates a list of json objects that allows the dhtmlx javascript library
# to parse and show a taxonomy tree (Written for HOMD)
##
import os, sys
import gzip
import json
#from json import JSONEncoder
from pprint import pprint
import argparse
import csv,re
from Bio import SeqIO
sys.path.append('/home/ubuntu/homd-work/')
sys.path.append('/Users/avoorhis/programming/')
from connect import MyConnection,mysql
import datetime
import requests
global mysql_errors
mysql_errors = []
"""

"""
today = str(datetime.date.today())


#['_997', '995.2', '', '997', '1017', 'HOMD', 'HMT-997', 'Bacteria', 'Gracilibacteria_(GN02)', 'Gracilibacteria_(GN02)_[C-1]', 'Gracilibacteria_(GN02)_[O-1]', 'Gracilibacteria_(GN02)_[F-1]', 'Gracilibacteria_(GN02)_[G-4]', 'bacterium_HMT_997', 'NCBI', '363464', 'Bacteria', 'Candidatus Gracilibacteria', 'NA', 'NA', 'NA', 'NA', 'NA', '', '', 'NCBI', '363464', 'HMT-997', 'Bacteria', 'Candidatus Gracilibacteria (GN02)', 'Gracilibacteria_[C-1]', 'Gracilibacteria_[O-1]', 'Gracilibacteria_[F-1]', 'Gracilibacteria_[G-4]', 'bacterium_HMT_997', 'y']
ranks = ['domain','phylum','klass','order','family','genus','species']

def clean_hmt(s):
    
    return str(int(s.split('-')[1]))  # strips zeros HMT-058 => 58
    
def create_empty():
    temp = {}
    
    temp['gc'] =''#                      assemblyStats.gcPercent
    temp['ncontigs'] =''#                assemblyStats.numberOfContigs
    temp['tlength'] =''#                 assemblyStats.totalSequenceLength
    temp['coverage'] =''#                assemblyStats.genomeCoverage
    
    temp['status'] =''#                  assemblyInfo.assemblyStatus
    temp['date'] =''#                    assemblyInfo.releaseDate
    temp['submitter'] =''#               assemblyInfo.submitter
    temp['ncbi_bioproject'] =''#         assemblyInfo.bioprojectAccession
    temp['ncbi_assembly_name'] =''#      assemblyInfo.assemblyName
    temp['assembly_type'] =''#           assemblyInfo.assemblyType
    temp['assembly_level'] =''#          assemblyInfo.assemblyLevel
    temp['method'] =''#                  assemblyInfo.assemblyMethod
    temp['seqtech'] =''#                 assemblyInfo.sequencingTech
    
    temp['ncbi_biosample'] =''#          assemblyInfo.biosample.accession
    temp['refseq_assembly'] =''#         assemblyInfo.pairedAssembly.accession
    
    temp['culture_strain'] =''#          organism.infraspecificNames
    temp['organism'] =''#                organism.organismname
    temp['ncbi_taxonid'] =''#            organism.taxId
    
    temp['wgs'] =''#                     wgsInfo.wgsProjectAccession
    
    return temp
    
def run(args):
    collector = {}  
    """
    
    """
    fp = open(args.infile,'r')
    count = 0
    
    nohmt = 0
    nohmtstr = ''
    for line in fp:
        line = line.strip()
        infoline = json.loads(line)
        acc = infoline['accession']
        collector[acc] = create_empty()
        if 'assemblyStats' in infoline:
            if 'gcPercent' in infoline['assemblyStats']:
                collector[acc]['gc'] = infoline['assemblyStats']['gcPercent']
            if 'numberOfContigs' in infoline['assemblyStats']:
                collector[acc]['ncontigs'] = infoline['assemblyStats']['numberOfContigs']
            if 'totalSequenceLength' in infoline['assemblyStats']:
                collector[acc]['tlength'] = infoline['assemblyStats']['totalSequenceLength']
            if 'genomeCoverage' in infoline['assemblyStats']:
                collector[acc]['coverage'] = infoline['assemblyStats']['genomeCoverage']
            
        if 'assemblyInfo' in infoline:
             if 'assemblyStatus' in infoline['assemblyInfo']:
                 collector[acc]['status'] = infoline['assemblyInfo']['assemblyStatus']
             if 'releaseDate' in infoline['assemblyInfo']:
                 collector[acc]['date'] = infoline['assemblyInfo']['releaseDate']
             if 'submitter' in infoline['assemblyInfo']:
                 collector[acc]['submitter'] = infoline['assemblyInfo']['submitter']
             if 'bioprojectAccession' in infoline['assemblyInfo']:
                 collector[acc]['ncbi_bioproject'] = infoline['assemblyInfo']['bioprojectAccession']
             if 'assemblyName' in infoline['assemblyInfo']:
                 collector[acc]['ncbi_assembly_name'] = infoline['assemblyInfo']['assemblyName']
             if 'assemblyType' in infoline['assemblyInfo']:
                 collector[acc]['assembly_type'] = infoline['assemblyInfo']['assemblyType']
             if 'assemblyLevel' in infoline['assemblyInfo']:
                 collector[acc]['assembly_level'] = infoline['assemblyInfo']['assemblyLevel']
             if 'assemblyMethod' in infoline['assemblyInfo']:
                 collector[acc]['method'] = infoline['assemblyInfo']['assemblyMethod']
             if 'sequencingTech' in infoline['assemblyInfo']:
                 collector[acc]['seqtech'] = infoline['assemblyInfo']['sequencingTech']
             if 'biosample' in infoline['assemblyInfo']:
                 if 'accession' in infoline['assemblyInfo']['biosample']:
                     collector[acc]['ncbi_biosample'] = infoline['assemblyInfo']['biosample']['accession']
             if 'pairedAssembly' in infoline['assemblyInfo']:
                 if 'accession' in infoline['assemblyInfo']['pairedAssembly']:
                     collector[acc]['refseq_assembly'] = infoline['assemblyInfo']['pairedAssembly']['accession']
        if 'organism' in infoline:
            if 'infraspecificNames' in infoline['organism']:
                for key, value in infoline['organism']['infraspecificNames'].items():
                    collector[acc]['culture_strain'] += key+':'+value+';'
                collector[acc]['culture_strain'] = collector[acc]['culture_strain'][:-1]  #remove end ';'
            
            
            if 'organismName' in infoline['organism']:
                collector[acc]['organism'] = infoline['organism']['organismName']
            if 'taxId' in infoline['organism']:
                collector[acc]['ncbi_taxonid'] = infoline['organism']['taxId']
        if 'wgsInfo' in infoline:
            if 'wgsProjectAccession' in infoline['wgsInfo']:
                collector[acc]['wgs'] = infoline['wgsInfo']['wgsProjectAccession']
        
        
        if args.printonly:
            print()
            print(infoline['accession'],'(available metadata) =>\nannotationInfo:')
            pprint(infoline['annotationInfo'])
            print('assemblyInfo:')
            pprint(infoline['assemblyInfo'])
            print('assemblyStats:')
            pprint(infoline['assemblyStats'])
            print('organism:')
            pprint(infoline['organism'])
            print('wgsInfo:')
            pprint(infoline['wgsInfo'])
        
    
    
    for acc in collector:
        q = "UPDATE genomes"
        q += " SET culture_strain='"+collector[acc]['culture_strain'].replace("'","")+"',"
        q += " organism='"+collector[acc]['organism'].replace("'","")+"',"
        q += " coverage='"+collector[acc]['coverage']+"',"
        q += " status='"+collector[acc]['status']+"',"
        q += " date='"+collector[acc]['date']+"',"
        q += " submitter='"+collector[acc]['submitter'].replace("'","")+"',"
        q += " ncontigs='"+str(collector[acc]['ncontigs'])+"',"
        q += " tlength='"+str(collector[acc]['tlength'])+"',"
        q += " ncbi_bioproject='"+collector[acc]['ncbi_bioproject']+"',"
        q += " ncbi_taxonid='"+str(collector[acc]['ncbi_taxonid'])+"',"
        q += " ncbi_biosample='"+collector[acc]['ncbi_biosample']+"',"
        q += " ncbi_assembly_name='"+collector[acc]['ncbi_assembly_name']+"',"
        q += " gc='"+str(collector[acc]['gc'])+"',"
        q += " refseq_assembly='"+collector[acc]['refseq_assembly']+"',"
        q += " assembly_type='"+collector[acc]['assembly_type']+"',"
        q += " assembly_level='"+collector[acc]['assembly_level']+"',"
        q += " method='"+collector[acc]['method'].replace("'","")+"',"
        q += " wgs='"+collector[acc]['wgs']+"',"
        q += " seqtech='"+collector[acc]['seqtech']+"'"
    
        q += " WHERE gb_assembly='%s'" % (acc)
        
        #if args.verbose:
        print('\n',q)
        if args.update:
            myconn.execute_no_fetch(q)

     
if __name__ == "__main__":

    usage = """
    USAGE:
    
==========================================================================================
==========================================================================================
Current fields:

culture_strain                            organism.infraspecificNames
organism                                  organism.organismname
coverage                                  assemblyStats.genomeCoverage
status                                    assemblyInfo.assemblyStatus
date                                      assemblyInfo.releaseDate
submitter                                 assemblyInfo.submitter
ncontigs                                  assemblyStats.numberOfContigs
tlength                                   assemblyStats.totalSequenceLength
XXXisolate_origin    ????? not found on ncbi
ncbi_bioproject                           assemblyInfo.bioprojectAccession
ncbi_taxonid                              organism.taxId
ncbi_biosample                            assemblyInfo.biosample.accession
ncbi_assembly_name                        assemblyInfo.assemblyName
gc                                        assemblyStats.gcPercent
gb_assembly                               KEY == infoline['accession']
refseq_assembly                           assemblyInfo.pairedAssembly.accession
assembly_type                             assemblyInfo.assemblyType
release_type           ???? not found on ncbi
assembly_level                            assemblyInfo.assemblyLevel
genome_rep             ???? not found on ncbi
method                                    assemblyInfo.assemblyMethod
wgs                                       wgsInfo.wgsProjectAccession
seqtech                                   assemblyInfo.sequencingTech

==========================================================================================
==========================================================================================
GCA_000691745.1 =>
annotationInfo:
{'method': 'Best-placed reference protein set; GeneMarkS+',
 'name': 'NCBI Prokaryotic Genome Annotation Pipeline (PGAP)',
 'pipeline': 'NCBI Prokaryotic Genome Annotation Pipeline (PGAP)',
 'provider': 'NCBI',
 'releaseDate': '2014-01-06',
 'softwareVersion': '2.3 (rev. 423251)',
 'stats': {'geneCounts': {'nonCoding': 47,
                          'proteinCoding': 2368,
                          'pseudogene': 18,
                          'total': 2433}}}

assemblyInfo:
{'assemblyLevel': 'Contig',                                                          SAVE
 'assemblyMethod': 'Velvet v. 1.2.09',                                               SAVE
 'assemblyName': 'FnecDJ-2v1.0',                                                     SAVE
 'assemblyStatus': 'current',                                                        SAVE
 'assemblyType': 'haploid',                                                          SAVE
 'bioprojectAccession': 'PRJNA232682',                                               SAVE
 'bioprojectLineage': [{'bioprojects': [{'accession': 'PRJNA232682',
                                         'title': 'Fusobacterium necrophorum '
                                                  'DJ-2 Genome sequencing and '
                                                  'assembly'}]}],
 'biosample': {'accession': 'SAMN02781280',                                          SAVE
               'attributes': [{'name': 'geo_loc_name', 'value': 'USA'},
                              {'name': 'isolation_source', 'value': 'jaw'},
                              {'name': 'strain', 'value': 'DJ-2'},
                              {'name': 'host', 'value': 'deer'}],
               'bioprojects': [{'accession': 'PRJNA232682'}],                        SAVE
               'description': {'organism': {'organismName': 'Fusobacterium '
                                                            'necrophorum DJ-2',
                                            'taxId': 1441737},
                               'title': 'Sample from Fusobacterium necrophorum '
                                        'DJ-2'},
               'lastUpdated': '2014-05-15T15:46:12.567',
               'models': ['Generic'],
               'owner': {'name': 'Newport Laboratories, A Sanofi Company'},
               'package': 'Generic.1.0',
               'publicationDate': '2014-05-15T15:46:12.567',
               'sampleIds': [{'db': 'GenBank', 'value': 'JAAH'}],
               'status': {'status': 'live', 'when': '2014-05-15T15:46:12.567'},
               'submissionDate': '2014-05-15T15:46:12.567'},
 'comments': 'Bacteria and source DNA available from Newport Laboratories, A '
             'Sanofi Company, 1520 Prairie Dr, Worthington, MN 56187, USA\n'
             'Annotation was added by the NCBI Prokaryotic Genome Annotation '
             'Pipeline (released 2013). Information about the Pipeline can be '
             'found here: http://www.ncbi.nlm.nih.gov/genome/annotation_prok/',
 'description': 'Fusobacterium necrophorum strain DJ-2 Version 1',
 'pairedAssembly': {'accession': 'GCF_000691745.1',
                    'annotationName': 'NCBI Prokaryotic Genome Annotation '
                                      'Pipeline (PGAP)',
                    'status': 'current'},
 'releaseDate': '2014-05-15',                                                        SAVE
 'sequencingTech': 'Illumina MiSeq',                                                 SAVE
 'submitter': 'Newport Laboratories, A Sanofi company'}                              SAVE

assemblyStats:
{'contigL50': 20,
 'contigN50': 35631,
 'gcCount': '855966',
 'gcPercent': 34.0,                                                                  SAVE
 'genomeCoverage': '26.0x',                                                          SAVE
 'numberOfComponentSequences': 226,
 'numberOfContigs': 226,                                                             SAVE
 'totalSequenceLength': '2520807',                                                   SAVE
 'totalUngappedLength': '2520807'}

organism:
{'infraspecificNames': {'strain': 'DJ-2'},                                           SAVE
 'organismName': 'Fusobacterium necrophorum DJ-2',                                   SAVE
 'taxId': 1441737}                                                                   SAVE

wgsInfo:
{'masterWgsUrl': 'https://www.ncbi.nlm.nih.gov/nuccore/JAAH00000000.1',
 'wgsContigsUrl': 'https://www.ncbi.nlm.nih.gov/Traces/wgs/JAAH01?',
 'wgsProjectAccession': 'JAAH01'}                                                    SAVE
==========================================================================================
==========================================================================================
       
        1) create txt file of GenBank accessions - one per line: assm_accs.txt
        2) run this command (supplied by NCBI) to download JSON file of metadata for each acc:
            ./datasets download genome accession --inputfile assm_accs.txt --include none (to get only the metadata and no seqs)
        3) Now run this python script to access the metadata
             homd-scripts/parse_ncbi_genomes.py
                 -i/--infile ncbi_dataset/data/assembly_data_report.jsonl
                 -p/--printonly (no update -- print out ncbi json)
                 -v/--verbose   (no update -- print out sql updates)
                 -u/--update (no output) to change the database
                 
        Break down a large file
        sed -n 8001,9000p assm_accs_full.txt > assm_accs_1000_9.txt
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    
    parser.add_argument("-i", "--infile",   required=True,  action="store",   dest = "infile", 
                                                   help=" ")
   
    parser.add_argument("-w", "--write",   required=False,  action="store_true",   dest = "write2db", default=False,
                                                help=" ")
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",   dest = "verbose", default=False,
                                                    help=" ")
    parser.add_argument("-p", "--printonly",   required=False,  action="store_true",   dest = "printonly", default=False,
                                                    help=" ")
    parser.add_argument("-u", "--update",   required=False,  action="store_true",   dest = "update", default=False,
                                                    help=" ")
    parser.add_argument("-host", "--host",
                        required = False, action = 'store', dest = "dbhost", default = 'localhost',
                        help = "choices=['homd',  'localhost']")
    
    

    args = parser.parse_args()
    
    if args.printonly:
        args.update = False
        args.verbose = False
    if args.update:
        args.printonly = False
        args.verbose = False
    
                        
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
        
        #dbhost_old = 'localhost'
    else:
        sys.exit('dbhost - error')
    
    
    myconn = MyConnection(host=dbhost, db=args.DATABASE,  read_default_file = "~/.my.cnf_node")
    
    
    run(args)
    if args.update:
        print('\nDone Updating Database')
    else:
        print('\nDatabase Not Updated!')
    if not args:
       print(usage)
    

    
