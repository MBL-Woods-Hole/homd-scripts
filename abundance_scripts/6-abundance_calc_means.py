#!/usr/bin/env python

import os, sys, stat
import json
import argparse
import csv
from connect import MyConnection
import datetime
ranks = ['domain','phylum','klass','order','family','genus','species']
today = str(datetime.date.today())
from statistics import mean,stdev
"""

"""
directory_to_search = './'

#header = 'OLIGOTYPE\tPHYLUM\tNUM_BEST_HITS\tBEST_HIT_%ID\tBEST_HIT_%COV\tOVERALL_%IDENT\tHMTs\tHOMD_SPECIES\tSTRAIN_CLONE\tHOMD_REFSEQ_ID\tGB_NCBI_ID\tHOMD_STATUS\n'
#header = 'OLIGOTYPE\tPHYLUM\tNUM_BEST_HITS\tBEST_PCT_ID\tBEST_FULL_PCT_ID\tHMTs\tHOMD_SPECIES\tSTRAIN_CLONE\tHOMD_REFSEQ_ID\tGB_NCBI_ID\tHOMD_STATUS\n'
site_order = ['BM','HP','KG','PT','ST','SUBP','SUPP','SV','TD','TH']

def calc(row, site, fxn):
    data = []
    for key in row.keys():
        items = key.split('-')
        if len(items) == 2 and items[1] == site:
            #print(key,site,row[key])
            data.append(float(row[key]))
    if fxn == 'mean':
        return mean(data)
    if fxn == 'sd':
        return stdev(data)
    if fxn == 'prev':
        
        # of individuals in which this HMT is non-zero at this site)
        # /(total number of individuals for whom we have samples at this site) = 77
        return 100*(float(len([x for x in data if x > 0])) / float(len(data)))
           
      
        
def run(args):
    file1 = []
    file_lookup = {}
    problem_list =[]
    lookup = {}
    with open(args.infile) as csv_file: 
        
        csv_reader = csv.DictReader(csv_file, delimiter='\t') # 
        #file1.append( {rows[0]:rows[1] for rows in reader} )
        gut_count = 0
        nomatch_count = 0
        for row in csv_reader:
            lookup[row['HMT']] = row
            file_lookup[row['HMT']] = {}
            file_lookup[row['HMT']]['Notes']= row['Notes']
            for site in site_order:
                file_lookup[row['HMT']][site+'-MEAN'] = calc(row, site, 'mean')
                file_lookup[row['HMT']][site+'-SD']   = calc(row, site, 'sd')
                file_lookup[row['HMT']][site+'-PREV'] = calc(row, site, 'prev')
            for key in row.keys():
                items = key.split('-')
                if len(items) == 2 and items[1] in site_order:
                    file_lookup[row['HMT']][key] = row[key]
    header = ''        
    
    header += 'HMT\tNOTES'
    for site in site_order:
        header += '\t'+site+'-MEAN'
        header += '\t'+site+'-SD'
        header += '\t'+site+'-PREV'
    header += '\n'
    
    
  
    fout = open(args.outfile,'w')
    fout.write(header)
    #for oligotype in file1_newlookup:
    
    for hmt in file_lookup:
        txt =  hmt
        txt += '\t'+file_lookup[hmt]['Notes']
        for site in site_order:
            txt += '\t'+str(round(file_lookup[hmt][site+'-MEAN'],3))
            txt += '\t'+str(round(file_lookup[hmt][site+'-SD'],3))
            txt += '\t'+str(round(file_lookup[hmt][site+'-PREV'],3))
        txt += '\n'
   
        fout.write(txt)
    fout.close()
            
    
    


if __name__ == "__main__":

    usage = """
    USAGE:
       
           
       ../6-abundance_calc_means.py -i HOMD_NEWcoalesce01.csv   
       
       this end point is not used:
       eren2014_v1v3_MeanStdevPrev_2021-12-23_homd.csv 
       
       --source must be in ['eren2014_v1v3','eren2014_v3v5','dewhirst_35x9'] 
      
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=False,  action="store",   dest = "infile", default=False,
                                                    help="HOMD_NEWcoalesce01.csv")
    
    parser.add_argument("-host", "--host", required = False, action = 'store', dest = "dbhost", default = 'localhost',
                                                   help="") 
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", default=False,
                                                    help="verbose print()") 
    
    parser.add_argument("-outfile", "--out_file", required = False, action = 'store', dest = "outfile", 
            default = 'MeanStdevPrev', help = "")
    parser.add_argument("-s", "--source", required = True, action = 'store', dest = "source", 
                         help = "['eren2014_v1v3','eren2014_v3v5','dewhirst_35x9']")
    args = parser.parse_args()
    
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
    myconn_new = MyConnection(host=dbhost_new, db=args.NEW_DATABASE,  read_default_file = "~/.my.cnf_node")
    if args.verbose:
        print()
    if not args.infile:
        print(usage)
        sys.exit()
        
    run(args)
