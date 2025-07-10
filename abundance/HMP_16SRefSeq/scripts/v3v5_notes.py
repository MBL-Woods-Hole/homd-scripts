#!/usr/bin/env python

import os, sys, stat
import json
import argparse
import csv
sys.path.append('../../homd-data/')
sys.path.append('/Users/avoorhis/programming/homd-data/')
sys.path.append('/Users/avoorhis/programming/')

import datetime
ranks = ['domain','phylum','klass','order','family','genus','species']
today = str(datetime.date.today())

"""

"""

ds_start_at = 1

# def get_ds_totals(args):
# 
#     fp = open(args.infile,'r')
#     dsets = {}
#     for line in fp:
#         
#         line = line.strip()
#         line_pts = line.split('\t')
#         #print(line_pts[:3],line_pts[3:] )
#         # ['HOT-ID', 'num', 'pct'] ['S700014982-AKE',....
#         if line_pts[0] == 'HOT-ID':
#             header = line
#             dataset_order = line_pts[ds_start_at:]
#             #print('dataset_order',dataset_order)
#             non_ds_order = line_pts[:ds_start_at]
#             for ds in dataset_order:
#                 dsets[ds]=0
#         else:
#             cells = line_pts[ds_start_at:]
#             
#             for i,ds in enumerate(dataset_order):
#                 dsets[ds] += float(cells[i])
#     fp.close()
#     
#     return(dsets)
    
def run(args):  # NOT dewhirst new data
    notes = {}
    singles_lookup = {}
    multiples_lookup = {}
    fp = open(args.infile,'r')
    outfp = open(args.outfile,'w')
    
    #print(args.infile)
    for line in fp:
        # first S700014982V1-V3 S700014982V3-V5
        line = line.strip()
        line_pts = line.split('\t')
        #print(line_pts[:3],line_pts[3:] )
        # ['HOT-ID', 'num', 'pct'] ['S700014982-AKE',....
        if line_pts[0] == 'Taxonomy':
            header_line = line
            outfp.write(header_line)
            outfp.write('\n')
            
        else:
            # Taxonomy	Rank	HMT	Notes	Max	AKE-mean
            tax = line_pts[0]
            rank = line_pts[1]
            hmt = line_pts[2]

            oldnote = line_pts[3]
            datarows = line_pts[4:]
            if hmt in args.good_note_collector:
                newnote = args.good_note_collector[hmt]
                #print('newnote',newnote)
            else:
                newnote = oldnote
            outfp.write(tax+'\t'+rank+'\t'+hmt+'\t'+newnote+'\t'+'\t'.join(datarows))
            outfp.write('\n')
            
           

    

    
    #outfp.write('Unmatched\t\t'+'\t'.join(unmatched_counts)+'\n')
    outfp.close()

def find_hmts_in_singles(lst, obj):
    new_lst = []
    for hmt in lst:
        if hmt in obj:
            new_lst.append(hmt)
    return new_lst
    
    


if __name__ == "__main__":

    usage = """
    USAGE:
    
    
    run in tmp/
    
    ../scripts/v1v3_notes.py -i NEWAll_Sites_v1v3_RelAbund_2024-04-03_homd.csv -r v1v3

          
       
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=True,  action="store",   dest = "infile", default=False,
                                                    help="")
    
    # parser.add_argument("-host", "--host", required = False, action = 'store', dest = "dbhost", default = 'localhost',
#                                                    help="") 
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", default=False,
                                                    help="verbose print()") 
    parser.add_argument("-outfile", "--out_file", required = False, action = 'store', dest = "outfile", 
                default = 'AllSites_NewNotes_v3v5_FINAL', help = "")
    
    parser.add_argument("-r", "--region", required = True, action = 'store', dest = "region", 
                         help = "")
    
    args = parser.parse_args()
    
    
    if args.region not in ['v3v5']:
        print(usage)
        sys.exit()
        
        
        
    notefile = '../HMP_16SRefSeq_v3v5_notes.csv'
    print('notefile',notefile)
    if os.path.exists(notefile):
        fp = open(notefile,'r')
        args.good_note_collector = {}
        for line in fp:
            line = line.strip()
            if not line:
               continue
            
            line_pts = line.split('\t')
            #print(len(line_pts),line)
            if len(line_pts) != 2:
                continue
            if line_pts[0] == 'HMT':
                continue
            otid = line_pts[0]
            note = line_pts[1]
            hmt = otid.zfill(3)
            args.good_note_collector[hmt] = note
        fp.close()
        #print(args.good_note_collector)
        #sys.exit()
    else:
        sys.exit('No Note File')
    
    for hmt in args.good_note_collector:
        #print(hmt,args.good_note_collector[hmt])
        pass
#     myconn = MyConnection(host=dbhost, db=args.NEW_DATABASE,  read_default_file = "~/.my.cnf_node")
    if args.verbose:
        print()
    if not args.infile:
        print(usage)
        sys.exit()
    
    args.outfile = args.outfile +'_'+today+'.csv'
    #args.dsets = get_ds_totals(args)
    
    run(args)
