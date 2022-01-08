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
site_order_dewhirst = ['BM','HP','KG','PT','SUBP','SUPP','SV','TD','TH','NS']



def calc(row, site, fxn):
    data = []
    for key in row.keys():
        items = key.split('-')
        #UC06-SUBP1  UC06-SUBP2 UC06-SUBP
        if len(items) == 2 and site in items[1]:
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
    if args.source == 'dewhirst_35x9':
        sites = site_order_dewhirst
    else:
        sites = site_order
    
    lookup = {}
    with open(args.infile) as csv_file: 
        
        csv_reader = csv.DictReader(csv_file, delimiter='\t')
        #file1.append( {rows[0]:rows[1] for rows in reader} )
        gut_count = 0
        nomatch_count = 0
        row_count = 1
        for row in csv_reader:
       
            lookup[row['Taxonomy']] = {}
            lookup[row['Taxonomy']]['Rank']= row['Rank']
            lookup[row['Taxonomy']]['HMT']= row['HMT']
            lookup[row['Taxonomy']]['Note']= row['Notes']
            rowmax = 0
            for site in sites:
                print(site,row)
                mean = calc(row, site.upper(), 'mean')
                if mean > rowmax:
                    rowmax = mean
                lookup[row['Taxonomy']][site+'-mean'] = mean
                lookup[row['Taxonomy']][site+'-sd']   = calc(row, site.upper(), 'sd')
                lookup[row['Taxonomy']][site+'-prev'] = calc(row, site.upper(), 'prev')
            lookup[row['Taxonomy']]['Max'] = rowmax
            
            row_count += 1
            
    header = ''        
    
    header += 'Taxonomy\tRank\tHMT\tNotes\tMax'
    for site in sites:
        header += '\t'+site.upper()+'-mean'
        header += '\t'+site.upper()+'-sd'
        header += '\t'+site.upper()+'-prev'
    header += '\n'
    
    
  
    fout = open(args.outfile,'w')
    fout.write(header)
    #for oligotype in file1_newlookup:
    
    for tax in lookup:
        txt =  tax
        txt += '\t'+lookup[tax]['Rank']
        txt += '\t'+lookup[tax]['HMT']
        txt += '\t'+lookup[tax]['Note']
        txt += '\t'+str(round(lookup[tax]['Max'],3))
        for site in sites:
            txt += '\t'+str(round(lookup[tax][site+'-mean'],3))
            txt += '\t'+str(round(lookup[tax][site+'-sd'],3))
            txt += '\t'+str(round(lookup[tax][site+'-prev'],3))
        txt += '\n'
   
        fout.write(txt)
    fout.close()
            
    
    


if __name__ == "__main__":

    usage = """
    USAGE:
       
           
       ../9-abunance_ranks_calc_means.py -i {source}_rank_abundance_sums_{date}_homd.csv
       --source must be in ['eren2014_v1v3','eren2014_v3v5','dewhirst_35x9']
      
     
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=False,  action="store",   dest = "infile", 
            default=False, help="HOMD_NEWcoalesce01.csv")
    
    parser.add_argument("-host", "--host", required = False, action = 'store', dest = "dbhost", 
            default = 'localhost',help="") 
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", 
            default=False, help="verbose print()") 
    parser.add_argument("-outfile", "--out_file", required = False, action = 'store', dest = "outfile", 
            default = 'MeanStdevPrev_byRankFINAL', help = "")
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
