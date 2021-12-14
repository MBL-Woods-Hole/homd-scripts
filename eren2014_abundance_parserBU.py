#!/usr/bin/env python

import os, sys, stat
import json
import argparse
import csv
#from connect import MyConnection
import datetime
ranks = ['domain','phylum','klass','order','family','genus','species']
today = str(datetime.date.today())

"""
input csv file:   Eren2014-FromDatasetS1-oligotypesV1V3.csv
from col D3 each sequence gets blasted (blastn) against
  homd-scripts/blastdb_refseq_V15.22.p9/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta*
  
  From JMW:
           Our goal is to use column D (REP_SEQ) in a BLAST against HOMD 16S refSeq, 
           to recreate updated versions of columns J through P (best hit % identity, 
           best hit % coverage, number of HMTs that are equally best hits, 
           the names of these HMTs, 
           their HMT IDs, strain/clone numbers, and NCBI ID numbers.
  
  Query coverage: the % of the contig (query) length that aligns with the NCBI hit (Subject).  
  A small query coverage % means only a tiny portion of the contig is aligning. 
  If there is an alignment with 100% identity and a 5% query coverage, the sequence is probably not that taxon.

outfmt 7:
% identity, alignment length, mismatches, gap opens, q. start, q. end, s. start, s. end, evalue,    bit score
94.024	    251	              15	      0	         6	       256	   247	     497	 4.98e-107	381
98

q len 250 -mm = 235
s len 250
"""
directory_to_search = './'
blast_db_path = '../BLASTDB_ABUND'
blast_db = 'HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta'
full_blast_db = os.path.join(blast_db_path,blast_db)
blast_script_path = "./blast.sh"
blast_outfmt = "'6 bitscore pident qcovhsp stitle'"  #  qseqid sseqid
filename = 'queryfile.fa'
blast_cmd =  "blastn  -db %s -query %s"
blast_cmd += " -out %s.out"
blast_cmd += " -outfmt %s"
blast_cmd += " -max_target_seqs 30\n"
header = 'OLIGOTYPE\tPHYLUM\tNUM_BEST_HITS\tBEST_HIT_%ID\tBEST_HIT_%COV\tOVERALL_%IDENT\tHMTs\tHOMD_SPECIES\tSTRAIN_CLONE\tHOMD_REFSEQ_ID\tGB_NCBI_ID\tHOMD_STATUS\n'

def run_csv(args):

    with open(args.infile) as csv_file:
        #csv_reader = csv.reader(csv_file, delimiter=',')  # AV comma
        
        if args.delimiter == 'tab':
            csv_reader = csv.DictReader(csv_file, delimiter='\t') # KK tab
        else:
            csv_reader = csv.DictReader(csv_file, delimiter=',') # KK tab
        n=1
        faFileNames = []
        for row in csv_reader:
            # row['OLIGOTYPE_NAME'] is unique
            #print(row['OLIGOTYPE_NAME'], row['REP_SEQ'])
            # write int shell script like in "run_blast_no_cluster.py" in homd
            # each seq needs its own file
            txt = '>'+row['OLIGOTYPE_NAME']+'\n'
            txt += row['REP_SEQ']+'\n'
            filename = row['OLIGOTYPE_NAME']+'.fna'
            # blastn -db -query -outfmt -out
            writeFile(filename, txt)
            faFileNames.append(filename)

            n +=1


    f = open(blast_script_path, "w")
    txt = "#!/bin/bash\n\n"
    f.write(txt)
    
    n = 1
    for file in faFileNames:
        txt = ''
        txt += "echo '\n  Blasting "+str(n)+"/"+str(len(faFileNames))+": "+file+"'\n"
        txt += blast_cmd % (full_blast_db, file, file, blast_outfmt)
        f.write(txt)
        n += 1
       
    
    f.close()
    os.chmod(blast_script_path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IROTH | stat.S_IXOTH)
    # run it
    os.system(blast_script_path)
       
def writeFile(name, data):
    f = open(name, "w")
    f.write(data)
    f.close()
    
def run_parse(args):
    fout = open(args.outfile,'w')
    fout.write(header)
    collector = {}
    oligo_arry =[]
    for filename in os.listdir(directory_to_search):
        if filename.endswith(".out"):
            fileid = filename.split('.')[0]
            fileid_parts = fileid.split('_')
            phylum = fileid_parts[2]
            oligo = fileid_parts[0]+'_'+fileid_parts[1]  # for ordering later: V1V3_588
            oligo_arry.append(oligo)                     # for ordering later
            
            collector[oligo] = {}
            
            #print(fileid)
            with open(filename) as f:
              line_count = 0
              max_bitscore = 0
              for line in f:
                  line = line.strip()
                  line_count += 1
                  line_items = line.split('\t')
                  if line_count == 1:
                      max_bitscore = line_items[0]
                      #d = grab_data(line_items,phylum,fileid)
                      collector[oligo][fileid+'\t'+line] = 1

                  elif max_bitscore == line_items[0]:
                      #d = grab_data(line_items, phylum, fileid)
                      collector[oligo][fileid+'\t'+line] = 1
                          
                      
    
    oligo_arry.sort()
    for oligo in oligo_arry:
        
        BEST_HIT_ID = 0
        BEST_HIT_COV = 0
        HMTs = []
        HOMD_SPECIES = []
        STRAIN_CLONE = []
        REFSEQ_ID = []
        STATUS = []
        HABITAT = []
        GB = []
        GENOME = []
        print()
        print()
        for line in collector[oligo]:
            line_items = line.split('\t')
            # each line is 1 infile and 1 line in outfile
            #print()
            print('line_items',line_items)
            # must combine hmts,
            #print(oligo,collector[oligo])
            if float(line_items[2]) > BEST_HIT_ID:
                BEST_HIT_ID = float(line_items[2])
            if int(float(line_items[3])) > BEST_HIT_COV:
                BEST_HIT_COV = float(line_items[3])
            #  ['V1V3_001_Firmicutes', '473', '100.000', '100', 
            #'058BW009 | Streptococcus oralis subsp. dentisani clade 058 | HMT-058 | Clone: BW009 | GB: AY005042 | Status: Named | Preferred Habitat: Oral | Genome: Genome: yes']
            OLIGOTYPE = line_items[0]  # all the same
            PHYLUM = OLIGOTYPE.split('_')[2]# all the same
            BITSCORE = line_items[1]   # all the same
            
            stitle = line_items[4].split('|')
            
            refseq = stitle[0].strip()
            REFSEQ_ID.append(refseq)
            
            species = stitle[1].strip()
            HOMD_SPECIES.append(species)
            
            HMT = stitle[2].strip()
            HMTs.append(HMT)
            
            clone = stitle[3].strip()
            STRAIN_CLONE.append(clone)
            
            gb = stitle[4].strip().split()[1]
            GB.append(gb)
            
            status = stitle[5].strip().split()[1]
            STATUS.append(status)
            
            habitat = stitle[6].strip()
            HABITAT.append(habitat)
            
            genome = stitle[7].strip()
            GENOME.append(genome)
        # header = 'OLIGOTYPE\tPHYLUM\tHMTs\tNUM_BEST_HITS\tBEST_HIT_ID\tBEST_HIT_COV\tHOMD_SPECIES\tSTRAIN_CLONE\tHOMD_REFSEQ_ID\tGB_NCBI_ID\tHOMD_STATUS\n'
        # Q/S qseqid/sseqid
        hmts = ','.join(set(HMTs))   # set() will uniqe the list
        sp = ','.join(HOMD_SPECIES)  # NOT Unique
        clone = ','.join(STRAIN_CLONE)
        refseq = ','.join(REFSEQ_ID)
        gb = ','.join(GB)
        status  = ','.join(STATUS)
        NUM_BEST_HITS = len(set(HMTs))
        OVERALL = BEST_HIT_ID * BEST_HIT_COV /100
        txt = OLIGOTYPE + '\t'
        txt += PHYLUM + '\t'
        txt += str(NUM_BEST_HITS) + '\t'
        txt += str(BEST_HIT_ID) + '\t'
        txt += str(BEST_HIT_COV) + '\t'
        txt += str(OVERALL) + '\t'
        txt += hmts + '\t'
        
        txt += sp + '\t'
        txt += clone + '\t'
        txt += refseq + '\t'
        txt += gb + '\t'
        txt += status + '\t'
        txt += '\n'
            

        fout.write(txt)
        
    
    fout.close()    

# def grab_data(line_array,phylum,fileid):
#     #print(line_array)
#     
#     # line_array[0] == best bitscore
#     # line_array[1] == BEST_HIT_ID
#     # line_array[2] == BEST_HIT_COV
#     # also want NUM_BEST_HITS
#     data = line_array[len(line_array)-1].split('|')
#     if len(data) == 8:
#       id = data[0].strip()
#       name = data[1].strip()
#       hmt = data[2].strip()
#       clone = data[3].strip()
#       gb = data[4].strip()
#       status = data[5].strip()
#       habitat = data[6].strip()
#       genome = data[7].strip()
#        
#     else:
#       return {}
#     return {"oligotype":fileid,
#             "phylum":phylum,
#             "bitscore":line_array[0],
#             "hitpctID":line_array[1],
#             "hitcoverage":line_array[2],
#             "refseq_id":id,
#             "species":name,
#             "HMT":hmt,
#             "clone":clone,
#             "gb":gb,
#             "status":status,
#             "habitat":habitat,
#             "genome":genome
#             }
#     
#     
if __name__ == "__main__":

    usage = """
    USAGE:
       To create and run BLAST on seqs from file
           eren2014_abundance_parser.py -i Eren2014-FromDatasetS1-oligotypesV1V3.csv (delim is comma)
       
           The input file must have a REP_SEQ column,
           and a column named OLIGOTYPE_NAME as a unique identifier for the fasta file.
       
           Each sequence (in col REP_SEQ) get written into its own .fa file which is used as
           input to the blastn command line program.
       
           All the blastn commands are written into a shell script which is run at the end of 
           this python script.
       
       To Parse the blast results:
           eren2014_abundance_parser.py -parse
           
           Output is a csv file named BLAST_PARSE.csv 
           
           Sample refseq defline:
               734_3930 | Streptococcus pneumoniae | HMT-734 | Strain: ATCC 33400 | GB: AF003930 | Status: Named | Preferred Habitat: Nasal | Genome: Genome: yes
           
           From JMW:
           Our goal is to use column D (REP_SEQ) in a BLAST against HOMD 16S refSeq, 
           to recreate updated versions of columns J through P (best hit % identity, 
           best hit % coverage, number of HMTs that are equally best hits, 
           the names of these HMTs, 
           their HMT IDs, strain/clone numbers, and NCBI ID numbers.

    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=False,  action="store",   dest = "infile", default=False,
                                                    help=" ")
    
    parser.add_argument("-parse", "--parse",   required=False,  action="store_true",   dest = "parse", default=False,
                                                    help=" ")
    parser.add_argument("-outfile", "--out_file", required = False, action = 'store', dest = "outfile", default = 'BLAST_PARSE.csv',
                         help = "Not usually needed if -host is accurate")
    parser.add_argument("-host", "--host",
                        required = False, action = 'store', dest = "dbhost", default = 'localhost',
                        help = "choices=['homd',  'localhost']")
    parser.add_argument("-pp", "--prettyprint",
                        required = False, action = 'store_true', dest = "prettyprint", default = False,
                        help = "output file is human friendly")
    parser.add_argument("-d", "--delimiter", required = False, action = 'store', dest = "delimiter", default = ',',
                         help = "")
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", default=False,
                                                    help="verbose print()") 
    args = parser.parse_args()
    
    #parser.print_help(usage)
    
    args.outdir = './'                         
    if args.dbhost == 'homd':
        #args.json_file_path = '/groups/vampsweb/vamps/nodejs/json'
        #args.TAX_DATABASE = 'HOMD_taxonomy'
        args.NEW_DATABASE = 'homd'
        #dbhost_old = '192.168.1.51'
        dbhost_new= '192.168.1.40'
        args.outdir = '../homd-startup-data/'
        args.prettyprint = False

    elif args.dbhost == 'localhost':
        #args.json_file_path = '/Users/avoorhis/programming/homd-data/json'
        #args.TAX_DATABASE  = 'HOMD_taxonomy'
        args.NEW_DATABASE = 'homd'
        dbhost_new = 'localhost'
        #dbhost_old = 'localhost'
        
    else:
        sys.exit('dbhost - error')
    args.indent = None
    if args.prettyprint:
        args.indent = 4
    #myconn_tax = MyConnection(host=dbhost_old, db=args.TAX_DATABASE,   read_default_file = "~/.my.cnf_node")
    #myconn_new = MyConnection(host=dbhost_new, db=args.NEW_DATABASE,  read_default_file = "~/.my.cnf_node")
    if args.verbose:
        print(blast_cmd % (full_blast_db, 'queryseq.fa', 'queryseq.fa', blast_outfmt))
    if args.infile:
        run_csv(args)
    elif args.parse:
        run_parse(args)
    else:
        print()
        print('Blast command:',blast_cmd % (full_blast_db, 'queryseq.fa', 'queryseq.fa', blast_outfmt))
        print('Output file headers:',header)
        print(usage)
   