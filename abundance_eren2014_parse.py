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
from connect import MyConnection
import datetime
ranks = ['domain','phylum','klass','order','family','genus','species']
today = str(datetime.date.today())

"""
input csv file:   Eren2014-FromDatasetS1-oligotypesV1V3.csv
from col D3 each sequence gets blasted (blastn) against
  blastdb_refseq_V15.22.p9/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta*

"""
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
            print(row['OLIGOTYPE_NAME'],row['REP_SEQ'])
            # write int shell script like in "run_blast_no_cluster.py" in homd
            # each seq needs its own file
            txt = '>'+row['OLIGOTYPE_NAME']+'\n'
            txt += row['REP_SEQ']+'\n'
            filename = row['OLIGOTYPE_NAME']+'.fna'
            # blastn -db -query -outfmt -out
            writeFile(filename, txt)
            faFileNames.append(filename)
            
            
            n +=1
    f = open("shell_script.sh", "w")
    txt = "#!/bin/bash\n\n"
    #-outfmt "7 qacc sacc sallseqid"
    for file in  faFileNames:
        txt += "blastn  -db ../blastdb_refseq_V15.22.p9/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -outfmt 1 -query "+file  + " -out "+file+".out\n"
    f.write(txt)
    f.close()
       
def writeFile(name, data):
    f = open(name, "w")
    f.write(data)
    f.close()
    
def createBatchBlastFileText(args, filesArray, details_dict):
    fileText ='#!/bin/bash\n\n'
    fileText += 'cd '+ os.path.join(details_dict['blastdbPath'],details_dict['ext']) + '\n\n'
    for file in filesArray:
        fileText += os.path.join(details_dict['programPath'], details_dict['program'])
        
        # if details_dict['site'] == 'localhome':
#             fileText += ' -db /Users/avoorhis/programming/blast_db/HOMD_16S_rRNA_RefSeq_V15.22.fasta'
#         elif details_dict['site'] == 'localmbl':
#             fileText += ' -db /Users/avoorhis/programming/blast-db-testing/HOMD_16S_rRNA_RefSeq_V15.22.fasta'
#             ##fileText += ' -db /Users/avoorhis/programming/blast-db-testing/B6/B6'
#         else:   # HOMD Default
        fileText += ' -db ' + details_dict['blastdb']
        #fileText += ' -db ' + details_dict['blastdb']
        fileText += ' -evalue ' + details_dict['expect']
        fileText += ' -query ' + os.path.join(details_dict['blastDir'],file)
        fileText += ' -max_target_seqs ' + details_dict['maxTargetSeqs']  # use if outfmt >4
        fileText += ' ' + details_dict['advanced']
        if details_dict['blastFxn'] == 'genome':
            fileText += ' -html'   ## dont use this with other -outfmt
        else:
            fileText += ' -outfmt 15'   ## 15 JSON
        ##fileText += ' -outfmt 16'   ## 16 XML
        
        fileText += ' -out ' +  os.path.join(details_dict['blastDir'],'blast_results', file+'.out') 
        # blasterror.log will always be created but may be zero length
        # whereas pythonerror.log will only be present if script error
        fileText += " 1>/dev/null 2>>" + details_dict['blastDir'] + "/blasterror.log;"
        fileText += '\n'
    
    return fileText
    
    
if __name__ == "__main__":

    usage = """
    USAGE:
       
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=True,  action="store",   dest = "infile", default='none',
                                                    help=" ")
    
    
    parser.add_argument("-host", "--host",
                        required = False, action = 'store', dest = "dbhost", default = 'localhost',
                        help = "choices=['homd',  'localhost']")
    parser.add_argument("-pp", "--prettyprint",
                        required = False, action = 'store_true', dest = "prettyprint", default = False,
                        help = "output file is human friendly")
    parser.add_argument("-d", "--delimiter", required = False, action = 'store', dest = "delimiter", default = ',',
                         help = "Delimiter: commaAV[Default]: 'comma' or tabKK: 'tab'")
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
    myconn_new = MyConnection(host=dbhost_new, db=args.NEW_DATABASE,  read_default_file = "~/.my.cnf_node")
    
    
    run_csv(args)
   