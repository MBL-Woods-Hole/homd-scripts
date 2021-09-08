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
#from connect import MyConnection
import datetime
ranks = ['domain','phylum','klass','order','family','genus','species']
today = str(datetime.date.today())

segata_headers=['BM','KG','HP','Throat','PT','TD','Saliva','SupP','SubP','Stool']
dewhirst_headers=['BM','KG','HP','TD','PT','Throat','Saliva','SupP','SubP']
eren_headers=['BM','KG','HP','TD','PT','Throat','Saliva','SupP','SubP','Stool']

   
hmt_index = 2  # only for dewhirst and eren
rank_index=3  # rank
max_segata_index=6
max_dewhirst_index=7
max_eren_index=8
max_any_index=9
data_start_index=11
segata_cols = ['mean','stdev']
eren_cols = ['mean','prevalence']
dewhirst_cols = ['mean','stdev','prevalence']


def run_abundance_csv(): 
    collector = {}
    if args.source == 'eren':
        max_index = 8
        headers = eren_headers
    elif args.source == 'segata':
        max_index = 6
        headers = segata_headers
    else:
        max_index = 7
        headers = dewhirst_headers
    # Opening JSON file
    json_file = args.outfile
    if os.path.isfile(json_file):
        f = open(json_file)
        collector = json.load(f)
        #print(collector)
        
    with open(args.infile) as csv_file:
        #csv_reader = csv.reader(csv_file, delimiter=',')  # AV comma
        
        if args.delimiter == 'tab':
            csv_reader = csv.reader(csv_file, delimiter='\t') # 
        else:
            csv_reader = csv.reader(csv_file, delimiter=',') # 
        #indices = {}
        start = 'no'
        
        for row in csv_reader:
            if row[0] == 'Headers':   # I added this keyword in the proper row[0]
                header_row = row
                #print(header_row)
                for n in header_row:
                    if n in headers:
                        #indices[n] = header_row.index(n)
                        print(n, header_row.index(n))
                #rkeys = list(row.keys())
                #print('\n',indices)
                # eg: {'BM': 11, 'KG': 13, 'HP': 15, 'Throat': 17, 'PT': 19, 'TD': 21, 'Saliva': 23, 'SupP': 25, 'SubP': 27, 'Stool': 29}
            if  row[0] == 'HOMD taxonomy':
                start = 'yes'
                continue  # go to the next row
                
            if start == 'yes':
                #print(row) 
                
                if not row[max_index]:  # will pass zero but not empty string
                   continue
                if row[0] not in collector:
                    collector[row[0]] = {}
                    if 'segata' not in collector[row[0]]:
                        collector[row[0]]['segata'] = {}
                    if 'eren' not in collector[row[0]]:
                        collector[row[0]]['eren'] = {}
                    if 'dewhirst' not in collector[row[0]]:
                        collector[row[0]]['dewhirst'] = {}
                
                collector[row[0]]['max_segata'] = row[max_segata_index]
                collector[row[0]]['max_eren'] = row[max_eren_index]
                collector[row[0]]['max_dewhirst'] = row[max_dewhirst_index]
                collector[row[0]]['max_all'] = row[max_any_index]
                if row[hmt_index]:
                    collector[row[0]]['otid'] = row[hmt_index]
                    
                for i,val in enumerate(row):
                    if header_row[i] in headers:
                        if args.source == 'eren':
                            collector[row[0]][args.source][header_row[i]]={'site':header_row[i], 'avg':row[i],'prev':row[i+1]} # for eren
                        elif args.source == 'segata':
                            collector[row[0]][args.source][header_row[i]]={'site':header_row[i], 'avg':row[i],'stdev':row[i+1]} # for segata
                        else: # dewhirst
                            collector[row[0]][args.source][header_row[i]]={'site':header_row[i], 'avg':row[i],'stdev':row[i+1],'prev':row[i+2]} # for dewhirst
            else:
                continue
                
    #print()
    #print(collector)
    filename = args.source+'_taxon_abundance_data.json'
    filename = args.outfile
    print_dict(filename,collector)
    
def print_dict(filename, dict):
    print('writing',filename)
    with open(filename, 'w') as outfile:
        json.dump(dict, outfile, indent=args.indent)    

        
if __name__ == "__main__":

    usage = """
    USAGE:
        Opens and adds to the homdData-TaxonCounts.json file 
        takes the TaxonAbundances csv (outputs to JSON file)
        Run 3 times (once for each abundance.csv file
          ./Initialize_Abundance.py -i Segata2021-09-07.csv -s segata
          ./Initialize_Abundance.py -i Eren2021-09-07.csv -s eren
          ./Initialize_Abundance.py -i Dewhirst2021-09-07.csv -s dewhirst -pp
        
        TODO add abundance data to database
        
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=True,  action="store",   dest = "infile", default='none',
                                                    help=" ")
    parser.add_argument("-s", "--source",   required=True,  action="store",   dest = "source", 
                                                    help="ONLY segata dewhirst eren")
    parser.add_argument("-o", "--outfile",   required=False,  action="store",   dest = "outfile", default='homdData-TaxonCounts.json',
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
    #myconn_new = MyConnection(host=dbhost_new, db=args.NEW_DATABASE,  read_default_file = "~/.my.cnf_node")
    if args.source not in ['segata','dewhirst','eren']:
        sys.exit('no valid source')
    if args.source.lower() not in args.infile.lower():
        sys.exit('file/source mismatch')
    
    run_abundance_csv()
   
    