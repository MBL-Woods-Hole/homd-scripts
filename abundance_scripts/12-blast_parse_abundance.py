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
  JMW: So, what we REALLY want is # of identities / the longer of (query sequence, matched region of subject sequence).  Can we get that?
  matched region of subject sequence == length - mismatches
  
  
outfmt 7:
pident      length            mismatch    gapopen    qstart    qend  sstart   send   evalue     bitscore
% identity, alignment length, mismatches, gap opens, q.start, q.end, s.start, s.end, evalue,    bit score
94.024	    251	              15	      0	         6	       256	   247	     497	 4.98e-107	381

nident means Number of identical matches
divided by
q.end-q.start  or 

blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query V1V3_593_Firmicutes.fna -out test.out -outfmt '7 nident pident qcovhsp qcovs stitle' -max_target_seqs 30
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query V1V3_593_Firmicutes.fna -out test4.out -outfmt 0 -num_descriptions 1 -num_alignments 1
"""

blast_db_path = '../BLAST_DATABASE_ABUNDANCE'
blast_db = 'HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta'
full_blast_db = os.path.join(blast_db_path,blast_db)
blast_script_path = "./blast.sh"

# Fields: bit score, % identity, % query coverage per hsp, subject title
#blast_outfmt = "'7 bitscore pident qcovhsp stitle'"  #  qseqid sseqid
blast_outfmt = "'7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps'"
#blast_outfmt = "'7 qseqid bitscore nident pident qstart qend stitle'"
# Fields: identical, % identity, % query coverage per hsp, % query coverage per subject, subject title
#blast_outfmt = "'7 qseqid bitscore nident pident qcovs stitle'"
filename = 'queryfile.fa'
blast_cmd =  "blastn  -db %s -query %s"
blast_cmd += " -out %s.out"
blast_cmd += " -outfmt %s"
blast_cmd += " -max_target_seqs 30\n"
#header = 'OLIGOTYPE\tPHYLUM\tNUM_BEST_HITS\tBEST_HIT_%ID\tBEST_HIT_%COV\tOVERALL_%IDENT\tHMTs\tHOMD_SPECIES\tSTRAIN_CLONE\tHOMD_REFSEQ_ID\tGB_NCBI_ID\tHOMD_STATUS\n'
header = 'OLIGOTYPE\tPHYLUM\tNUM_BEST_HITS\tBEST_PCT_ID\tBEST_FULL_PCT_ID\tHMTs\tHOMD_SPECIES\tSTRAIN_CLONE\tHOMD_REFSEQ_ID\tGB_NCBI_ID\tHOMD_STATUS\n'

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
            filepath = os.path.join(args.outdir,filename)
            writeFile(filepath, txt)
            faFileNames.append(filename)

            n +=1


    f = open(blast_script_path, "w")
    txt = "#!/bin/bash\n\n"
    f.write(txt)
    
    n = 1
    for file in faFileNames:
        filepath = os.path.join(args.outdir,file)
        txt = ''
        txt += "echo '\n  Blasting "+str(n)+"/"+str(len(faFileNames))+": "+file+" in args.outdir'\n"
        txt += blast_cmd % (full_blast_db, filepath, filepath, blast_outfmt)
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
    bitscore_index = 1
    oligotype_index = 0
    pctIdentity_index = 3
    identical_index = 2
    title_index = 6
    qstart_index = 4
    qend_index = 5
    mismatches_index = 8
    alignment_index = 7
    gaps_index = 9
    qlength_index = 10
    for filename in os.listdir(args.outdir):
        if filename.endswith(".out"):
            fileid = filename.split('.')[0]
            seqfilename = fileid+'.fna'
            #print('seqfilename',seqfilename)
            qlength = get_qlength(os.path.join(args.outdir,seqfilename))
            #print('qlength',qlength)
            fileid_parts = fileid.split('_')
            phylum = fileid_parts[2]
            oligo = fileid_parts[0]+'_'+fileid_parts[1]  # for ordering later: V1V3_588
            oligo_arry.append(oligo)                     # for ordering later
            
            collector[oligo] = {}
            
            #print(fileid)
            filepath = os.path.join(args.outdir,filename)
            with open(filepath) as f:
              line_count = 0
              max_bitscore = 0
              for line in f:
                  line = line.strip()
                  if line.startswith('#'):
                      continue
                  line_count += 1
                  line_items = line.split('\t')
                  if line_count == 1:
                      max_bitscore = line_items[bitscore_index]
                      #d = grab_data(line_items,phylum,fileid)
                      collector[oligo][line+'\t'+str(qlength)] = 1

                  elif max_bitscore == line_items[bitscore_index]:
                      #d = grab_data(line_items, phylum, fileid)
                      collector[oligo][line+'\t'+str(qlength)] = 1        
    
    oligo_arry.sort()
    for oligo in oligo_arry:
        
        BEST_PCT_ID = 0.0
        BEST_myPCT_ID = 0.0
        #FULL_PCT_ID = 0.0  # identical/q-length
        BEST_FULL_PCT_ID = 0.0
        HMTs = []
        HOMD_SPECIES = []
        STRAIN_CLONE = []
        REFSEQ_ID = []
        STATUS = []
        HABITAT = []
        GB = []
        GENOME = []
        #print()
        #print()
        
        for line in collector[oligo]:
            line_items = line.split('\t')
            qlength = line_items[-1]   # last item
            # each line is 1 infile and 1 line in outfile
            #print()
            #print('line_items',line_items)
            # must combine hmts,
            #print(oligo,collector[oligo])
            PCT_ID = float(line_items[pctIdentity_index])
            if PCT_ID > BEST_PCT_ID:
                BEST_PCT_ID = PCT_ID
            
            
            #FULL_PCT_IDid = 100*( float(line_items[identical_index]) / float(line_items[qend_index]) )
            #FULL_PCT_IDid = 100*( float(line_items[identical_index]) / float(qlength) )
            ALIGNMENT_FRAC = float(int(line_items[qend_index]) - int(line_items[qstart_index]) + 1.0) / float(qlength)
            FULL_PCT_ID = PCT_ID * ALIGNMENT_FRAC

#             myPCT_ID = 100*( (float(line_items[identical_index]) - float(line_items[gaps_index]) - float(line_items[mismatches_index]))/ float(qlength) )
            #FULL_PCT_IDlen = 100*( (float(line_items[alignment_index]) - float(line_items[mismatches_index]) - float(line_items[gaps_index])) /  float(line_items[qend_index]) )
            if line_items[qend_index] != qlength:
                print('\nline_items[qend_index]',line_items[qend_index])
                print('qlength',qlength)
            if FULL_PCT_ID > BEST_FULL_PCT_ID:
                BEST_FULL_PCT_ID = FULL_PCT_ID
            # if myPCT_ID > BEST_myPCT_ID:
#                 BEST_myPCT_ID = myPCT_ID
            #  ['V1V3_001_Firmicutes', '473', '100.000', '100', 
            #'058BW009 | Streptococcus oralis subsp. dentisani clade 058 | HMT-058 | Clone: BW009 | GB: AY005042 | Status: Named | Preferred Habitat: Oral | Genome: Genome: yes']
            OLIGOTYPE = line_items[oligotype_index]  # all the same
            PHYLUM = OLIGOTYPE.split('_')[2]# all the same
            BITSCORE = line_items[bitscore_index]   # all the same
            
            stitle = line_items[title_index].split('|')
            
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
        
        hmts = ','.join(HMTs)   # Not unique the list
        #hmts = ','.join(set(HMTs))   # set() will unique the list
        sp = ','.join(HOMD_SPECIES)  # NOT Unique
        clone = ','.join(STRAIN_CLONE)
        refseq = ','.join(REFSEQ_ID)
        gb = ','.join(GB)
        status  = ','.join(STATUS)
        NUM_BEST_HITS = len(set(HMTs))  # SHOULD THIS BE UNIQUE?
        
        txt = OLIGOTYPE + '\t'
        txt += PHYLUM + '\t'
        txt += str(NUM_BEST_HITS) + '\t'
        txt += str(BEST_PCT_ID) + '\t'
        txt += str(round(BEST_FULL_PCT_ID,3)) + '\t'

        txt += hmts + '\t'
        
        txt += sp + '\t'
        txt += clone + '\t'
        txt += refseq + '\t'
        txt += gb + '\t'
        txt += status + '\t'
        txt += '\n'
#         if round(BEST_FULL_PCT_ID,3) < round(BEST_PCT_ID,3):
#             print('BEST_FULL_PCT_ID',round(BEST_FULL_PCT_ID,3),' > ','BEST_PCT_ID',BEST_PCT_ID,OLIGOTYPE)
#             print('BEST_myPCT_ID',round(BEST_myPCT_ID,3))
#        

        fout.write(txt)
        
    
    fout.close()
       
def get_qlength(seqfilename):
    
    with open(seqfilename) as f:
        seq = ''
        for line in f:
            if line.startswith('>'):
                continue
            seq += line.strip().replace('-','')
    return len(seq)
    
    

if __name__ == "__main__":

    usage = """
    USAGE:
       --source must be in ['eren2014_v1v3','eren2014_v3v5','dewhirst_35x9']
       
       To create and run BLAST on seqs from file
           ../12-blast_parse_abundance.py -i Eren2014-FromDatasetS1-oligotypesV1V3.csv (delim is comma)
       
           The input file must have a REP_SEQ column,
           and a column named OLIGOTYPE_NAME as a unique identifier for the fasta file.
       
           Each sequence (in col REP_SEQ) get written into its own .fa file which is used as
           input to the blastn command line program.
       
           All the blastn commands are written into a shell script which is run at the end of 
           this python script.
       
       To Parse the blast results:
           ../12-blast_parse_abundance.py -parse
           
           Output is a csv file named BLAST_PARSE.csv 
           
           Sample refseq defline:
               734_3930 | Streptococcus pneumoniae | HMT-734 | Strain: ATCC 33400 | GB: AF003930 | Status: Named | Preferred Habitat: Nasal | Genome: Genome: yes
           
           From JMW:
           Our goal is to use column D (REP_SEQ) in a BLAST against HOMD 16S refSeq, 
           to recreate updated versions of columns J through P (best hit pct identity, 
           best hit pct coverage, number of HMTs that are equally best hits, 
           the names of these HMTs, 
           their HMT IDs, strain/clone numbers, and NCBI ID numbers.

    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=False,  action="store",   dest = "infile", 
            default=False,  help=" ")
    
    parser.add_argument("-parse", "--parse",   required=False,  action="store_true",   dest = "parse", 
            default=False,  help=" ")
    parser.add_argument("-outdir", "--outdir",   required=False,  action="store",   dest = "outdir", 
            default='./work', help="")
    parser.add_argument("-outfile", "--out_file", required = False, action = 'store', dest = "outfile", 
            default = 'BLAST_PARSE_RESULT.csv', help = "")
    parser.add_argument("-host", "--host", required = False, action = 'store', dest = "dbhost", 
            default = 'localhost',help = "choices=['homd',  'localhost']")
    parser.add_argument("-pp", "--prettyprint",required = False, action = 'store_true', dest = "prettyprint", 
            default = False, help = "output file is human friendly")
    parser.add_argument("-d", "--delimiter", required = False, action = 'store', dest = "delimiter", 
            default = ',',help = "")
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", 
            default=False, help="verbose print()") 
    
    parser.add_argument("-s", "--source", required = True, action = 'store', dest = "source", 
                         help = "['eren2014_v1v3','eren2014_v3v5','dewhirst_35x9']")
    args = parser.parse_args()
    print(args)
    if args.source not in ['eren2014_v1v3','eren2014_v3v5','dewhirst_35x9']:
        print(usage)
        sys.exit()
                            
    if args.dbhost == 'homd':
        args.NEW_DATABASE = 'homd'
        dbhost_new= '192.168.1.40'

    elif args.dbhost == 'localhost':
        args.NEW_DATABASE = 'homd'
        dbhost_new = 'localhost'
        
    else:
        sys.exit('dbhost - error')
    
    args.outfile = args.source+'_'+args.outfile +'_'+today+'_homd.csv'
    #myconn_new = MyConnection(host=dbhost_new, db=args.NEW_DATABASE,  read_default_file = "~/.my.cnf_node")
    if args.verbose:
        print(blast_cmd % (full_blast_db, 'queryseq.fa', 'queryseq.fa', blast_outfmt))
    if args.infile:
        run_csv(args)
        print('\n')
        print('*'*60)
        print('Done creating BLAST output files')
        print('Next - parse the blast.out files which will create: BLAST_PARSE_RESULT.csv')
        print('Run: ./eren2014_abundance_parser.py -parse')
        print('*'*60,'\n')
    elif args.parse:
        run_parse(args)
    else:
        print('\n')
        print(usage)
        print('Blast command:',blast_cmd % (full_blast_db, 'queryseq.fa', 'queryseq.fa', blast_outfmt))
        print('Output file headers:',header)
        
   