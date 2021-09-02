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

segata_headers=['GroupG1','BM','KG','Hp','GroupG2','Th','PT','TD','Sal','GroupG3','SupP','SubP','Stool']
segata_groups = {'G1':['BM','KG','Hp'],
  'G2':['Th','PT','TD','Sal'],
  'G3':['SupP','SubP'],
  'G4':['Stool']
  }
   


 


def run_segata_csv(): 
    
   
    with open(args.infile) as csv_file:
        #csv_reader = csv.reader(csv_file, delimiter=',')  # AV comma
        
        if args.delimiter == 'tab':
            csv_reader = csv.reader(csv_file, delimiter='\t') # KK tab
        else:
            csv_reader = csv.reader(csv_file, delimiter=',') # KK tab
        line_count = 0
        data_rows = []
        indices = {}
        start = 'no'
        collector = {}
        for row in csv_reader:
            #print(row)
            if row[0] == 'Headers':
                header_row = row
                print(header_row)
                for n in header_row:
                    if n in segata_headers:
                        indices[n] = header_row.index(n)
                        print(n, header_row.index(n))
                #rkeys = list(row.keys())
                print('\n',indices)
            if  row[0] == 'Column1':
                start = 'yes'
                max_index = 1  # second column
                continue  # go to the next line
                
            if start == 'yes':
               print(row) 
               collector[row[0]] = {}
               #collector[row[0]]['max'] = row[1]
               for i,val in enumerate(row):
                   if header_row[i] in segata_headers:
                       if header_row[i] == 'GroupG1':
                           collector[row[0]]['GroupG1']={'loci':'G1-avg', 'avg':row[i],'stdev':row[i+1]}
                       elif header_row[i] == 'GroupG2':
                           collector[row[0]]['GroupG2']={'loci':'G2-avg', 'avg':row[i],'stdev':row[i+1]}
                       elif header_row[i] == 'GroupG3':
                           collector[row[0]]['GroupG3']={'loci':'G3-avg', 'avg':row[i],'stdev':row[i+1]}
                       else:
                           if header_row[i] == 'Stool': # G4 has a single el: Stool
                               collector[row[0]]['GroupG4']={'loci':'G4-avg', 'avg':row[i],'stdev':row[i+1]}
                       
                           collector[row[0]][header_row[i]]={'loci':header_row[i], 'avg':row[i],'stdev':row[i+1]}
            else:
                continue
                
    print()
    print(collector)
    filename = 'segata_taxon_abundance_data.json'
    print_dict(filename,collector)
    
def print_dict(filename, dict):
    print('writing',filename)
    with open(filename, 'w') as outfile:
        json.dump(dict, outfile, indent=args.indent)    

        
if __name__ == "__main__":

    usage = """
    USAGE:
        takes the Segata TaxonAbundances csv (outputs to JSON file)
        
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=True,  action="store",   dest = "infile", default='none',
                                                    help=" ")
    parser.add_argument("-o", "--outfileprefix",   required=False,  action="store",   dest = "outfileprefix", default='homd_data',
                                                    help=" ")
    parser.add_argument("-outdir", "--out_directory", required = False, action = 'store', dest = "outdir", default = './',
                         help = "Not usually needed if -host is accurate")
    parser.add_argument("-host", "--host",
                        required = False, action = 'store', dest = "dbhost", default = 'localhost',
                        help = "choices=['homd',  'localhost']")
    parser.add_argument("-pp", "--prettyprint",
                        required = False, action = 'store_true', dest = "prettyprint", default = False,
                        help = "output file is human friendly")
    parser.add_argument("-d", "--delimiter", required = False, action = 'store', dest = "delimiter", default = 'tab',
                         help = "Delimiter: commaAV[Default]: 'comma' or tabKK: 'tab'")
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", default=False,
                                                    help="verbose print()") 
    args = parser.parse_args()
    
    #parser.print_help(usage)
    if not os.path.exists(args.outdir):
        print("\nThe out put directory doesn't exist:: using the current dir instead\n")
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
    
    
    run_segata_csv()
   
    