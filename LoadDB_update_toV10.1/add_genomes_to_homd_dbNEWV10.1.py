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

# should add these: 
# Missing: isolate origin, Sequencing status??, Combined length, GC percentage, ATCC stuff, num_contigs
query = """SELECT `otid_prime`.`otid` AS `otid`
   FROM `otid_prime` 
   join `taxonomy` on(`otid_prime`.`taxonomy_id` = `taxonomy`.`taxonomy_id`)
   join `genus` on(`taxonomy`.`genus_id` = `genus`.`genus_id`)
   join `species` on(`taxonomy`.`species_id` = `species`.`species_id`)
"""

def get_seqid_ver_gcaid(file8622, otidDict):  #8622
    genome_collector = {}
    with open(file8622, 'r') as handle:
        for line in handle:
            line = line.strip().split('\t')
            
            seqid = line[0]+'.'+line[1]
            otid = otidDict[seqid]
            genome = make_genome(seqid,otid)
            genome_collector[seqid] = make_genome(seqid,otid)
            
    return genome_collector

def get_dict_from_new_genomes_file(csv_file, gc8622):
    
    line_count = 0
    
    with open(csv_file, 'r') as handle:
        for line in handle:
            line_count +=1
            line_pts = line.strip().split('\t')
            
            if line_count == 1:
                continue
            if '.' in line_pts[1]:
                gid = line_pts[1]
            else:
                gid = line_pts[1] + '.' +line_pts[5].split('.')[1]
            #print(line)
            
            
            gc8622[gid]['organism'] = line_pts[12]
            
            gc8622[gid]['date'] = line_pts[19]
            gc8622[gid]['status'] = line_pts[15]
            
    
            gc8622[gid]['submitter'] = line_pts[21]  #V
            if line_pts[13] and '=' in line_pts[13]:
                gc8622[gid]['culture_strain'] = line_pts[13].split('=')[1]
                if line_pts[14]:
                    gc8622[gid]['culture_strain'] += ';'+line_pts[14]
            elif line_pts[13]:
                gc8622[gid]['culture_strain'] = line_pts[13]
                if line_pts[14]:
                    gc8622[gid]['culture_strain'] += ';'+line_pts[14]
            else:
                gc8622[gid]['culture_strain'] = line_pts[14]
            gc8622[gid]['coverage'] = ''  #Genome coverage
    
            gc8622[gid]['ncbi_taxonid'] = line_pts[10]
            gc8622[gid]['ncbi_bioproject'] = line_pts[6]
            gc8622[gid]['ncbi_biosample'] = line_pts[7]
            gc8622[gid]['ncbi_assembly_name'] = line_pts[20]  #U assembly name: ASM16007v2
           
            gc8622[gid]['gb_assembly'] = line_pts[5]    # GCA_xxxxxx
            gc8622[gid]['refseq_assembly'] = line_pts[22]    # GCF_xxxxxx
            gc8622[gid]['paired_asm_comp']=line_pts[23]
            
            gc8622[gid]['wgs']=line_pts[8]
            
            gc8622[gid]['release_type']=line_pts[17]
            gc8622[gid]['assembly_level']=line_pts[16]
            gc8622[gid]['genome_rep']=line_pts[18]
    
    
    return gc8622
           
    
    
def make_genome(seqid,otid):
    genome = {}
    genome['otid'] = otid
    genome['gid'] = seqid
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
    
def run_directories(args, gcollector): 
    #for root, dirs, files in os.walk(args.indir):
    # displaying the contents of the CSV file
    
    
    
    notInMaster = {}
    
    otid_collector = {}
    no_org_match = {}
    culture_strain = {}
    # prokka and ncbi have the same number of dirs(genomes)
    
    print('Searching NCBI DirectoryONLY:',args.ncbi_dir)
    # has all seqids
    # master has only new seqids
    # anything remaining is already in homd
    gcount = 0
    for seqid in gcollector:   # gives 
        # open/parse assembly_stats file
       #  if 'otid' not in genome_collector[seqid] or genome_collector[seqid]['otid'] =='':
#             if seqid in currentTaxa:
#                 genome_collector[seqid]['otid'] = currentTaxa[seqid]
        
        
        
        d = args.ncbi_dir + '/'+seqid
        if not os.path.isdir(d):
            continue
        
        gcount +=1
        print(gcount,d)
        for filename in os.listdir(d):
            f = os.path.join(d, filename)
            #print(seqid,d,f)
            if os.path.isfile(f) and f.endswith('assembly_stats.txt'):
                #print(f)
                for line in open(f, 'r'):
                    line = line.strip()
                    
                    if line.startswith('# Assembly name') and not gcollector[seqid]['ncbi_assembly_name']:
                        gcollector[seqid]['ncbi_assembly_name']= line.split(':')[1].strip()
                    if line.startswith('# Taxid') and not gcollector[seqid]['ncbi_taxonid']:
                        gcollector[seqid]['ncbi_taxonid']= line.split(':')[1].strip()
                    if line.startswith('# Organism name') and not gcollector[seqid]['organism']:
                        gcollector[seqid]['organism']= line.split(':')[1].strip()
                    
                    if line.startswith('# Infraspecific') and not gcollector[seqid]['culture_strain']:
                        #gcollector[seqid]['culture_strain']= line.split(':')[1].strip()
                        culture_strain[seqid] = [line.split(':')[1].strip()]
                    if line.startswith('# BioSample') and not gcollector[seqid]['ncbi_biosample']:
                        gcollector[seqid]['ncbi_biosample']= line.split(':')[1].strip()
                    if line.startswith('# BioProject') and not gcollector[seqid]['ncbi_bioproject']:
                        gcollector[seqid]['ncbi_bioproject']= line.split(':')[1].strip()
                    if line.startswith('# Submitter') and not gcollector[seqid]['submitter']:
                        gcollector[seqid]['submitter']= line.split(':')[1].strip()
                    if line.startswith('# Date') and not gcollector[seqid]['date']:
                        gcollector[seqid]['date']= line.split(':')[1].strip()
                    if line.startswith('# Assembly type') and not gcollector[seqid]['assembly_type']:
                        gcollector[seqid]['assembly_type']= line.split(':')[1].strip()
                    if line.startswith('# Release type') and not gcollector[seqid]['release_type']:
                        gcollector[seqid]['release_type']= line.split(':')[1].strip()
                    if line.startswith('# Assembly level') and not gcollector[seqid]['assembly_level']:
                        gcollector[seqid]['assembly_level']= line.split(':')[1].strip()
                    if line.startswith('# Genome representation') and not gcollector[seqid]['genome_rep']:
                        gcollector[seqid]['genome_rep']= line.split(':')[1].strip()
                    if line.startswith('# WGS project') and not gcollector[seqid]['wgs']:
                        gcollector[seqid]['wgs']= line.split(':')[1].strip()
                    if line.startswith('# Assembly method') and not gcollector[seqid]['method']:
                        gcollector[seqid]['method']= line.split(':')[1].strip()
                    if line.startswith('# Genome coverage') and not gcollector[seqid]['coverage']:
                        gcollector[seqid]['coverage']= line.split(':')[1].strip()
                    if line.startswith('# Sequencing technology') and not gcollector[seqid]['seqtech']:
                        gcollector[seqid]['seqtech']= line.split(':')[1].strip()
                    if line.startswith('# GenBank assembly accession') and not gcollector[seqid]['gb_assembly']:
                        gcollector[seqid]['gb_assembly']= line.split(':')[1].strip()
                    if line.startswith('# RefSeq assembly accession') and not gcollector[seqid]['refseq_assembly']:
                        gcollector[seqid]['refseq_assembly']= line.split(':')[1].strip()
                    if line.startswith('# RefSeq assembly and GenBank assemblies identical') and not gcollector[seqid]['paired_asm_comp']:
                        gcollector[seqid]['paired_asm_comp']= line.split(':')[1].strip()
                        
                        

            
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
                    gcollector[seqid]['tlength'] = str(tlength)
                    gcollector[seqid]['ncontigs'] = str(ncontigs)
                    gcollector[seqid]['gc'] = str(round(pctgc, 2))
                    if seqid in culture_strain:
                        gcollector[seqid]['culture_strain']  = ','.join(culture_strain[seqid])
    print('LENGTH gcollector',len(gcollector))
    return gcollector
    
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
        
        args.ncbi_dir = '/mnt/efs/bioinfo/projects/homd_add_genomes_V10.1_all/add_ncbi/GCA_V10.1_all'
        args.prokka_dir = '/mnt/efs/bioinfo/projects/homd_add_genomes_V10.1_all/add_prokka/prokka'
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
    
   
    
    
    
    
    #args.seqids_from_file = get_seqids_from_new_genomes_file(seqid_file)
    
    #print(genome_collector['SEQF1595.2'])
    
    seqid_otid8622 = 'seqid_otid.txt'  #8622  seqid-\t-otid
    master_otidDict = {}
    print('getting OTIDs from '+seqid_otid8622)
    with open(seqid_otid8622, mode ='r') as otidfile:
        for line in otidfile:
            line_pts = line.strip().split()
            master_otidDict[line_pts[0]] = line_pts[1]
    #print(master_otidDict)
    print('getting SEQIDs from seqid_ver_gcaid.txt')
    genome_collector8622 = get_seqid_ver_gcaid('seqid_ver_gcaid.txt', master_otidDict) #8622        
    
    genome_collector8622 = get_dict_from_new_genomes_file('new_gca_selected_8148_seqID.csv', genome_collector8622)
    
    genome_collector8622 = run_directories(args, genome_collector8622)  # gets ncontigs, tlength, gc count
    
    if args.write2db:
        write2db(genome_collector8622)
    
    print('run Done')
    
    print('write Done')
    print('Not in csv Master List Length:',len(genome_collector8622))
    