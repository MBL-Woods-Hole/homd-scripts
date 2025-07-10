#!/usr/bin/env python

## SEE https://docs.dhtmlx.com/suite/tree__api__refs__tree.html // new version 7 must load from json file
# this script creates a list of json objects that allows the dhtmlx javascript library
# to parse and show a taxonomy tree (Written for HOMD)
##
import os, sys
import json,glob,re
#from json import JSONEncoder
import argparse
import csv
import gzip
from Bio import SeqIO
sys.path.append('../homd-data/')
sys.path.append('../../homd-data/')
from connect import MyConnection, mysql
import datetime
ranks = ['domain','phylum','klass','order','family','genus','species']
today = str(datetime.date.today())
# fields_from_txt_files = ['Assembly name','Organism name','Infraspecific name','Taxid',
# 'BioSample','BioProject','Submitter','Date','Assembly type','Release type',
# 'Assembly level','Genome representation','Assembly method','Genome coverage',
# 'Sequencing technology','GenBank assembly accession','RefSeq assembly accession',
# 'RefSeq assembly and GenBank assemblies identical'
# ]
skip = ['SEQF2736']
fields_from_txt_files2 = {  # from ncbi txt file :: what we want in json object
# emulate this page https://www.ncbi.nlm.nih.gov/data-hub/genome/GCA_000160075.2/
#'Assembly name':'ncbi_assembly_name',  # this may be the new assembly accession
#'Organism name':'organism', 
#'Isolate':'isolate', 
#'Infraspecific name':'culture_strain',
#'Taxid':'ncbi_taxonid',
#'BioSample':'ncbi_biosample',
#'BioProject':'ncbi_bioproject',
#'Submitter':'submitter',
#'Date':'date',
#'WGS project':'wgs',   # ==Whole Genome Shotgun
#'Assembly type':'assembly_type',  #na
#'Release type':'release_type',   # major, minor
#'Assembly level':'assembly_level', # Contig, Complete Genome
#'Genome representation':'genome_rep',  # full
'Assembly method':'method',   #Velvet v. 1.2.09,   HGAP v. 3; Geneieous R7
'Genome coverage':'coverage',   # 10x, 25.98x,  >100x
'Sequencing technology':'seqtech',  # Illumina MiSeq,  PacBio; Illumina,  454
#'GenBank assembly accession':'gb_assembly',
#'RefSeq assembly accession':'refseq_assembly',
#'RefSeq assembly and GenBank assemblies identical':'',

# from PROKKA txt file : what we want
# 'organism':'organism',
# 'contigs':'ncontigs',  ## contigs for 1595 == 4 for prokka and 20 for ncbi
# 'bases':'tlength',
# 'CDS':'CDS',
# 'misc_RNA':'misc_RNA',
# 'rRNA':'rRNA',
# 'repeat_region':'repeat_region',
# 'tRNA':'tRNA',
# 'tmRNA':'tmRNA'
}
#  ACFE00000000.1  gb_accession   https://community.gep.wustl.edu/repository/course_materials_WU/annotation/Genbank_Accessions.pdf
# GCA_000174015.1  gb_assembly
# GCF_000691685.1 GCF RefSeq!!!
# equivalencies = [
#  ['from ncbi assembly_stats.txt','currently used in homd','example'],
#  ['GenBank assembly accession','gb_asmbly','GCA_000154225.1'],
#  ['Submitter','seq_center','University of Malaya'],
#  ['BioSample','ncbi_bsid','SAMEA5851866'],
#  ['BioProject','ncbi_bpid','PRJEB33885'],
#  ['Infraspecific name','ccolct','strain=BFTR-1'],
#  ['Taxid','ncbi_genomeid','411466'],
# ]
# should add these: 
# Missing: isolate origin, Sequencing status??, Combined length, GC percentage, ATCC stuff, num_contigs
query = """SELECT `otid_prime`.`otid` AS `otid`
   FROM `otid_prime` 
   join `taxonomy` on(`otid_prime`.`taxonomy_id` = `taxonomy`.`taxonomy_id`)
   join `genus` on(`taxonomy`.`genus_id` = `genus`.`genus_id`)
   join `species` on(`taxonomy`.`species_id` = `species`.`species_id`)
"""
test_genomes =['SEQF1361','SEQF2000','SEQF2543','SEQF3065','SEQF3528','SEQF3964','SEQF4396','SEQF4828','SEQF5260','SEQF5692','SEQF6124','SEQF6556','SEQF6988','SEQF7420','SEQF7852','SEQF8284','SEQF8716','SEQF9148',
'SEQF9580','SEQF10000','SEQF10001','SEQF10131','SEQF3713', 'SEQF3714', 'SEQF2736',  'SEQF2353','SEQF2534',
'SEQF1362','SEQF2001','SEQF2544','SEQF3066','SEQF3529','SEQF3965','SEQF4397','SEQF4829','SEQF5261','SEQF5693','SEQF6125','SEQF6557','SEQF6989','SEQF7421','SEQF7853','SEQF8285','SEQF8717','SEQF9149','SEQF9581',
'SEQF1363','SEQF2002','SEQF2545','SEQF3068','SEQF3530','SEQF3966','SEQF4398','SEQF4830','SEQF5262','SEQF5694','SEQF6126','SEQF6558','SEQF6990','SEQF7422','SEQF7854','SEQF8286','SEQF8718','SEQF9150','SEQF9582',
'SEQF1364','SEQF2003','SEQF2546','SEQF3070','SEQF3531','SEQF3967','SEQF4399','SEQF4831','SEQF5263','SEQF5695','SEQF6127','SEQF6559','SEQF6991','SEQF7423','SEQF7855','SEQF8287','SEQF8719','SEQF9151','SEQF9583',
'SEQF1365','SEQF2004','SEQF2547','SEQF3071','SEQF3532','SEQF3968','SEQF4400','SEQF4832','SEQF5264','SEQF5696','SEQF6128','SEQF6560','SEQF6992','SEQF7424','SEQF7856','SEQF8288','SEQF8720','SEQF9152','SEQF9584',
'SEQF1366','SEQF2005','SEQF2549','SEQF3072','SEQF3533','SEQF3969','SEQF4401','SEQF4833','SEQF5265','SEQF5697','SEQF6129','SEQF6561','SEQF6993','SEQF7425','SEQF7857','SEQF8289','SEQF8721','SEQF9153','SEQF9585'
]
# 1 aaatcaatcc caatttttaa acaatttttt taatttcata aacatatact taggatcttc
# def check_if_new(args, seqid):
#     q = "SELECT otid, seq_id from genomes where seq_id='"+seqid+"'"
#     result = myconn.execute_fetch_one(q)
#     if myconn.cursor.rowcount == 0:
#         return True
#     else:
#         return False
def get_seqid_ver_gcaid(file):
    gid_list = {}
    with open(file, 'r') as handle:
        for line in handle:
            line = line.strip().split('\t')
            print(line[0])
            gid_list[line[0]] = {}
            gid_list[line[0]]['n'] = line[1]
            gid_list[line[0]]['gca'] = line[2]
    sys.exit()
    return gid_list

def get_seqids_from_new_genomes_file(file):
    file_list = {}
    with open(file, 'r') as handle:
        first_line = handle.readline()
        for line in handle:
            line = line.strip().split('\t')
            if line[1].startswith('SEQF'):
                if '.' in line[1]:
                    file_list[line[1].split('.')[0]] = line
                else:
                    file_list[line[1]] = line
    
    #print(file_list,len(file_list))
    return file_list
    
def make_genome():
    genome = {}
    genome['otid'] = ''
    genome['gid'] = ''
    genome['organism'] = ''
    genome['genus'] = ''
    genome['species'] = ''
    genome['date'] = ''
    genome['status'] = ''   # from ncbi:  assembly_status.txt
    genome['isolate_origin'] = ''
    
    genome['submitter'] = ''
    
    genome['culture_strain'] = ''
    genome['coverage'] = ''  #Genome coverage
    
    genome['ncbi_taxonid'] = ''
    genome['ncbi_bioproject'] = ''
    genome['ncbi_biosample'] = ''
    genome['ncbi_assembly_name'] = ''  # assembly name: ASM16007v2
    #genome['gb_accession'] = ''   # ACFE00000000.1  contig related
    genome['gb_assembly'] = ''    # GCA_xxxxxx
    genome['refseq_assembly'] = ''    # GCF_xxxxxx
    genome['paired_asm_comp']=''
    genome['method']=''
    genome['seqtech']=''
    genome['wgs']=''
    genome['assembly_type']=''
    genome['release_type']=''
    genome['assembly_level']=''
    genome['genome_rep']=''
    genome['seqtech']=''
    # calculated: from genomic.fna
    genome['gc'] = ''
    genome['tlength'] = ''
    genome['ncontigs'] = ''
    
    return genome

# def counts():
#     #dir_prokka = '/mnt/efs/bioinfo/projects/homd_add_genomes_V10.1_all/add_prokka/prokka'
#     #dir_ncbi = '/mnt/efs/bioinfo/projects/homd_add_genomes_V10.1_all/add_ncbi/GCA_V10.1_all'
#     count = 0
#     for directory in os.listdir(args.prokka_dir):
#         count +=1
#     print('prokka',count)
#     count = 0
#     for directory in os.listdir(args.ncbi_dir):
#         count +=1
#     print('ncbi',count)
    
def run(args): 
    #for root, dirs, files in os.walk(args.indir):
    # displaying the contents of the CSV file
    
    global genome_collector
    global notInMaster
    notInMaster = {}
    genome_collector = {}
    otid_collector = {}
    no_org_match = {}
    culture_strain = {}
    # prokka and ncbi have the same number of dirs(genomes)
    
    print('Searching NCBI DirectoryONLY:',args.ncbi_dir)
    # has all seqids
    # master has only new seqids
    # anything remaining is already in homd
    for seqid in args.seqid_ver_gcaid:  # #8622
    
        d = os.path.join(args.ncbi_dir, seqid)
        if os.path.isfile(d):
            continue
        #if seqid in skip:
        #    continue
        
        
        seqidplus = seqid+'.'+args.seqid_ver_gcaid[seqid]['n']
        #if seqid in test_genomes:
        #if seqid not in ['SEQF1161']:
        #    continue
        culture_strain[seqid] = []
        
        
            
        genome_collector[seqid] = make_genome()
        genome_collector[seqid]['gid'] = seqidplus
        if seqid in currentTaxa:
            genome_collector[seqid]['otid'] = currentTaxa[seqid]
                          
    # fill out genus species, otid from masterDict
    print('CT',currentTaxa['SEQF3712'])
    
    for seqid in genome_collector:
        print('seqid',seqid)
        if seqid in masterDict:
            #print(seqid,masterDict[seqid])
            genome_collector[seqid]['otid'] = masterDict[seqid]['HMT-ID'].split('-', 1)[1]

    #for seqid in notInMaster:   # gives 8620
    
    #sys.exit()
    for seqid in genome_collector:   # gives 8142
        # open/parse assembly_stats file
       #  if 'otid' not in genome_collector[seqid] or genome_collector[seqid]['otid'] =='':
#             if seqid in currentTaxa:
#                 genome_collector[seqid]['otid'] = currentTaxa[seqid]
        d = args.ncbi_dir + '/'+seqid
        if not os.path.isdir(d):
            continue
        #print('DIR',d)
        
        for filename in os.listdir(d):
            f = os.path.join(d, filename)
            #print(seqid,d,f)
            if os.path.isfile(f) and f.endswith('assembly_stats.txt'):
                #print(f)
                for line in open(f, 'r'):
                    line = line.strip()
                    
                    if line.startswith('# Assembly name') and not genome_collector[seqid]['ncbi_assembly_name']:
                        genome_collector[seqid]['ncbi_assembly_name']= line.split(':')[1].strip()
                    if line.startswith('# Taxid') and not genome_collector[seqid]['ncbi_taxonid']:
                        genome_collector[seqid]['ncbi_taxonid']= line.split(':')[1].strip()
                    if line.startswith('# Organism name') and not genome_collector[seqid]['organism']:
                        genome_collector[seqid]['organism']= line.split(':')[1].strip()
                    
                    if line.startswith('# Infraspecific') and not genome_collector[seqid]['culture_strain']:
                        #genome_collector[seqid]['culture_strain']= line.split(':')[1].strip()
                        culture_strain[seqid] = [line.split(':')[1].strip()]
                    if line.startswith('# BioSample') and not genome_collector[seqid]['ncbi_biosample']:
                        genome_collector[seqid]['ncbi_biosample']= line.split(':')[1].strip()
                    if line.startswith('# BioProject') and not genome_collector[seqid]['ncbi_bioproject']:
                        genome_collector[seqid]['ncbi_bioproject']= line.split(':')[1].strip()
                    if line.startswith('# Submitter') and not genome_collector[seqid]['submitter']:
                        genome_collector[seqid]['submitter']= line.split(':')[1].strip()
                    if line.startswith('# Date') and not genome_collector[seqid]['date']:
                        genome_collector[seqid]['date']= line.split(':')[1].strip()
                    if line.startswith('# Assembly type') and not genome_collector[seqid]['assembly_type']:
                        genome_collector[seqid]['assembly_type']= line.split(':')[1].strip()
                    if line.startswith('# Release type') and not genome_collector[seqid]['release_type']:
                        genome_collector[seqid]['release_type']= line.split(':')[1].strip()
                    if line.startswith('# Assembly level') and not genome_collector[seqid]['assembly_level']:
                        genome_collector[seqid]['assembly_level']= line.split(':')[1].strip()
                    if line.startswith('# Genome representation') and not genome_collector[seqid]['genome_rep']:
                        genome_collector[seqid]['genome_rep']= line.split(':')[1].strip()
                    if line.startswith('# WGS project') and not genome_collector[seqid]['wgs']:
                        genome_collector[seqid]['wgs']= line.split(':')[1].strip()
                    if line.startswith('# Assembly method') and not genome_collector[seqid]['method']:
                        genome_collector[seqid]['method']= line.split(':')[1].strip()
                    if line.startswith('# Genome coverage') and not genome_collector[seqid]['coverage']:
                        genome_collector[seqid]['coverage']= line.split(':')[1].strip()
                    if line.startswith('# Sequencing technology') and not genome_collector[seqid]['seqtech']:
                        genome_collector[seqid]['seqtech']= line.split(':')[1].strip()
                    if line.startswith('# GenBank assembly accession') and not genome_collector[seqid]['gb_assembly']:
                        genome_collector[seqid]['gb_assembly']= line.split(':')[1].strip()
                    if line.startswith('# RefSeq assembly accession') and not genome_collector[seqid]['refseq_assembly']:
                        genome_collector[seqid]['refseq_assembly']= line.split(':')[1].strip()
                    if line.startswith('# RefSeq assembly and GenBank assemblies identical') and not genome_collector[seqid]['paired_asm_comp']:
                        genome_collector[seqid]['paired_asm_comp']= line.split(':')[1].strip()
                        
                        

            
            if os.path.isfile(f) and f.endswith('genomic.fna.gz') and not f.endswith('rna_from_genomic.fna.gz') \
                             and not f.endswith('cds_from_genomic.fna.gz'):
                #print('next file',f)
                gc = ''
                ncontigs = 0
                tlength = 0
                gccount = 0
                with gzip.open(f, "rt") as handle:
                    for record in SeqIO.parse(handle, "fasta"):
                        ncontigs += 1
                        
                        tlength += len(record.seq)
                        contiggc = re.sub('[atAT]','',str(record.seq))
                        gccount += len(contiggc)
                    
                    pctgc = (gccount / tlength) * 100
                    genome_collector[seqid]['tlength'] = str(tlength)
                    genome_collector[seqid]['ncontigs'] = str(ncontigs)
                    genome_collector[seqid]['gc'] = str(round(pctgc, 2))
                    genome_collector[seqid]['culture_strain']  = ','.join(culture_strain[seqid])
    print('LENGTH',len(genome_collector))
    if args.write2db:
        write2db(genome_collector)
        #sys.exit('xx')
    #for seqid in genome_collector:
    #    print()
    #    print(genome_collector[seqid])
    # print()
    
#     print('List of NoMatch Organisms:')    
#     nomatch_org_collector = {}
#     for seqid in no_org_match:
#         genus_species = no_org_match[seqid]['genus']+' '+no_org_match[seqid]['species']
#         if genus_species not in nomatch_org_collector:
#             nomatch_org_collector[genus_species] = []
#         nomatch_org_collector[genus_species].append(seqid)
#     for genus_species in nomatch_org_collector:
#         print(genus_species, nomatch_org_collector[genus_species],'Length:',len(nomatch_org_collector[genus_species]))
#         #print('NoMatch',seqid,no_org_match[seqid]['organism'])

def write2db(genome_collector):
    count =0
    err_count = 0
    # {'otid': '812', 'gid': 'SEQF10131', 'organism': 'Helicobacter pylori UM032 (e-proteobacteria)', 
#     'genus': 'Helicobacter', 'species': 'pylori', 'date': '2014-09-15', 'status': '', 'ncontigs': '', 
#     'submitter': 'University of Malaya', 'tlength': '1593537', 'culture_strain': 'strain=UM032', 'coverage': '>100x', 
#     'gc': '39', 'ncbi_taxonid': '1311573', 'ncbi_bpid': 'PRJNA196982', 'ncbi_bsid': 'SAMN02230257', 
#     'ncbi_assembly_name': 'ASM39245v3', 'gb_assembly': 'GCA_000392455.3', 'refseq_assembly': 'GCF_000392455.3', 
#     'assembly_type': 'na', 'release_type': 'major', 'assembly_level': 'Complete Genome', 'genome_rep': 'full', 
#     'method': 'HGAP v. 3; Geneieous R7', 'seqtech': 'PacBio; Illumina'
#     }
    
    dbfields = ['organism','status','date','ncontigs','submitter','tlength','culture_strain','isolate_origin','coverage','gc','ncbi_bioproject','ncbi_taxonid',
                'ncbi_biosample','ncbi_assembly_name','gb_assembly','refseq_assembly','assembly_type','release_type','assembly_level','genome_rep','method','seqtech','wgs']
    for seqid in genome_collector:
        
        fields = ""
        fields += ",".join(dbfields)
        q = "INSERT into `"+args.table+"` (otid,seq_id,"+fields+") VALUES "
        vals = "('"+genome_collector[seqid]['otid']+"','"+genome_collector[seqid]['gid']+"',"
        for field in dbfields:  #genome_collector[seqid]:
            if field in genome_collector[seqid]:
               #print(seqid,field,genome_collector[seqid][field])
               vals += "'"+genome_collector[seqid][field].replace("'","")+"',"
            else:
                vals += "'',"
            
        q  += vals[:-1]+")"
        #print(q)
        #count +=1
        # if seqid == 'SEQF1363':
#             print(seqid,genome_collector[seqid])
#             sys.exit('SEQF1363-from files')
        if args.write2db:
            if genome_collector[seqid]['otid']:
                try:
                    myconn.execute_no_fetch(q)
                    count +=1
                except mysql.Error as e:
                    print(seqid,"MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
                    print()
                except:
                    print(seqid,'ERROR\n',q)
                    err_count +=1
            else:
                print('NO TaxonID(otid) found for genome:',seqid)
    print('executed query count:',count)
    print('no write count:',err_count)
    if not args.write2db:
        print('\rNO WRITE to DB\r')
        # print()
#         print(masterDict['SEQF10001'])
#         print()
#         print(genome_collector['SEQF10001'])
if __name__ == "__main__":

    usage = """
    USAGE:
        ./check_new_genomes.py -i infile
        
        -f/--flag  orgs or dupes
           1) orgs: will find organism [genus and species] that is not represented in the HOMD taxa
           
        
        -host/--host [homd]  default:localhost
          

    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-w", "--write",   required=False,  action="store_true",   dest = "write2db", default=False,
                                                    help=" ")
    parser.add_argument("-t", "--table",   required=False,  action="store",   dest = "table", default='genomesV10.1',
                                                    help=" ")
    parser.add_argument("-host", "--host",
                        required = False, action = 'store', dest = "dbhost", default = 'localhost',
                        help = "choices=['homd',  'localhost']")
                        
    args = parser.parse_args()
    
    #parser.print_help(usage)
                        
    if args.dbhost == 'homd':
        #args.json_file_path = '/groups/vampsweb/vamps/nodejs/json'
        #args.TAX_DATABASE = 'HOMD_taxonomy'
        args.DATABASE = 'homd'
        #dbhost_old = '192.168.1.51'
        dbhost= '192.168.1.42'   #TESTING is 1.42  PRODUCTION is 1.40
        
        args.ncbi_dir = '/mnt/efs/bioinfo/projects/homd_add_genomes_V10.1/GCA_V10.1_all'
        args.prokka_dir = '/mnt/efs/bioinfo/projects/homd_add_genomes_V10.1/prokka_V10.1_all'
        args.master = './new_genomesV10.1.csv'

    elif args.dbhost == 'localhost':
        #args.json_file_path = '/Users/avoorhis/programming/homd-data/json'
        #args.TAX_DATABASE  = 'HOMD_taxonomy'
        args.DATABASE = 'homd'
        dbhost = 'localhost'
        #dbhost_old = 'localhost'
        args.prokka_dir = '/Users/avoorhis/programming/homd-work/new_genomesV10.1/prokka_V10.1_all/'
        
        args.ncbi_dir = '/Users/avoorhis/programming/homd-work/new_genomesV10.1/GCA_V10.1_all/'
        
    else:
        sys.exit('dbhost - error')
    
    myconn = MyConnection(host=dbhost, db=args.DATABASE,   read_default_file = "~/.my.cnf_node")
    #myconn_new = MyConnection(host=dbhost_new, db=args.NEW_DATABASE,  read_default_file = "~/.my.cnf_node")
#     if args.source not in ['segata','dewhirst','eren']:
#         sys.exit('no valid source')
#     if args.source.lower() not in args.infile.lower():
#         sys.exit('file/source mismatch')
    #open new_gca_selected_8148_seqID.csv
    masterDict = {}
    seqid_file = 'new_gca_selected_8148_seqID.csv'  # 8149
    print('getting seqids from file')
    #args.seqids_from_file = get_seqids_from_new_genomes_file(seqid_file)
    args.seqid_ver_gcaid = get_seqid_ver_gcaid('seqid_ver_gcaid.txt') #8622
    


    currentTaxa = {}
    q = "SELECT seq_id, otid from `genomesV9.15`"
    print(q)
    result = myconn.execute_fetch_select(q)
    for row in result:
        #print(row)  # ('SEQF1032', 827)
        #if row[0] =='SEQF2626':
        #   print(row)
           
        currentTaxa[row[0]] = str(row[1])
    
    #counts()
    #sys.exit()
    run(args)
    print('run Done')
    
    print('write Done')
    print('Not in csv Master List Length:',len(genome_collector))
    