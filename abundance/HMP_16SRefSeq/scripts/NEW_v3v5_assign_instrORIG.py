#!/usr/bin/env python

import os, sys, stat
import json
import argparse
import csv
sys.path.append('../../homd-data/')
sys.path.append('/Users/avoorhis/programming/homd-data/')
sys.path.append('/Users/avoorhis/programming/')
#from connect import MyConnection
import datetime
ranks = ['domain','phylum','klass','order','family','genus','species']
today = str(datetime.date.today())

"""

"""
toSuppress =[
'HMT-034',
'HMT-034-851',
'HMT-036',
'HMT-036-851',
'HMT-851',
'HMT-535-641',
'HMT-641',
'HMT-641-851',
'HMT-734-851',
'HMT-851-908',
'HMT-056',
'HMT-056-622',
'HMT-056-622-677',
'HMT-622',
'HMT-058-061-074-398-431-638-677-948',
'HMT-058-061-398-431-638-677',
'HMT-058-064-070-071-398-423-431-638-677-707',
'HMT-058-064-070-071-398-423-431-638-677-707-728-948',
'HMT-728-948',
'HMT-948',
'HMT-073-677',
'HMT-073',
'HMT-677',
'HMT-074-638',
'HMT-574',
'HMT-574-638',
'HMT-638',
'HMT-411-721',
'HMT-057-411-721',
'HMT-066-073',
'HMT-066-073-411-721',
'HMT-066-411-721',
'HMT-066-721',
'HMT-087',
'HMT-087-543',
'HMT-021-152-755',
'HMT-021-755',
'HMT-755',
'HMT-721-755',
'HMT-721',
'HMT-152',
'HMT-543',
'HMT-543-578-721-767-886',
'HMT-543-578-755-886',
'HMT-543-578-767-886',
'HMT-543-578-886',
'HMT-755-767',
'HMT-767',
'HMT-076' ,
'HMT-076-114-116-120-127-128-141-216-550-567-591-601',
'HMT-114',
'HMT-114-116-117-567-601',
'HMT-114-116-567-601',
'HMT-116',
'HMT-116-567',
'HMT-116-612',
'HMT-612',
'HMT-612-834',
'HMT-834',
'HMT-127',
'HMT-127-128',
'HMT-128',
'HMT-141',
'HMT-216-550-591',
'HMT-550',
'HMT-591',
'HMT-601',
'HMT-099-598-609-682-764',
'HMT-099-609-682-764',
'HMT-598',
'HMT-682',
'HMT-682-764',
'HMT-764',
'HMT-275',
'HMT-275-278',
'HMT-275-278-283',
'HMT-275-278-283-284',
'HMT-275-283',
'HMT-275-283-284',
'HMT-283',
'HMT-283-284',
'HMT-298',
'HMT-298-313',
'HMT-298-313-314-469-572',
'HMT-298-314-469',
'HMT-313',
'HMT-313-314-469-885',
'HMT-314-469',
'HMT-469',
'HMT-469-536',
'HMT-572',
'HMT-885',
'HMT-306',
'HMT-306-572',
'HMT-323',
'HMT-323-324-412-902',
'HMT-323-380',
'HMT-323-412',
'HMT-323-412-700',
'HMT-323-700',
'HMT-324',
'HMT-324-412',
'HMT-324-902',
'HMT-380',
'HMT-412',
'HMT-412-700-903',
'HMT-412-903',
'HMT-902',
'HMT-903',
'HMT-700',
'HMT-700-902',
'HMT-326',
'HMT-326-335-336',
'HMT-335',
'HMT-335-336',
'HMT-335-902',
'HMT-336',
'HMT-336-700',
'HMT-336-902'
]
ds_start_at = 1


def run_suppressed():
    singles = {}
    for item in toSuppress:
        pts = item.split('-')
        if len(pts) == 2:
            singles[pts[1]] = item
    
    #print(singles)
    for item in toSuppress:
        pts = item.split('-')
        if len(pts) > 2:
            parts_to_check = pts[1:]
            for hmt in parts_to_check:
                if hmt not in singles:
                   print('Not a single',hmt)
    return singles
    
    
    
def run(args):  # NOT dewhirst new data
    notes = {}
    singles_lookup = {}
    multiples_lookup = {}
    fp = open(args.infile,'r')
    outfp = open(args.outfile,'w')
    outfp.write('HOT-ID\tNotes')
    #print(args.infile)
    for line in fp:
        # first S700014982V1-V3 S700014982V3-V5
        line = line.strip()
        line_pts = line.split('\t')
        #print(line_pts[:3],line_pts[3:] )
        # ['HOT-ID', 'num', 'pct'] ['S700014982-AKE',....
        if line_pts[0] == 'HOT-ID':
            header = line
            dataset_order = line_pts[ds_start_at:]
            for ds in dataset_order:
                outfp.write('\t'+ds)
            outfp.write('\n')
            non_ds_order = line_pts[:ds_start_at]
        else:
            # collect singles
            
            
            # ['HOT-ID', 'Species', 'num_of_taxa', 'assign_reads_to', 'notes']
            hotid = line_pts[0]
            if hotid in toSuppress:
                continue
            
            cells = line_pts[ds_start_at:]
            pts = hotid.split('-')[1:]  # remove 'HMT-'
            #if '275' in hotid:
            #    print(hotid,pts)
            if len(pts) == 1:
                #print(pts[0])
                # if pts[0] in args.suppressed_singles:
#                     #notes[pts[0]] = ['No data – the v3v5 region of the 16S rRNA gene does not distinguish this species from its close relatives.']
#                     print('bypassing'pts[0])
#                     continue
#                 else:
#                     
                singles_lookup[pts[0]] = cells
                notes[pts[0]] = []
            else:
                
                multiples_lookup['-'.join(pts)] = cells
            if hotid == 'Unmatched':
                unmatched_counts = cells
            #row_sum = sum([float(x) for x in cells])
            
            
            # outfp.write(hotid)
#             for i,ct in enumerate(cells):
#                 abund = 100 * (float(ct) / float(args.dsets[dataset_order[i]]))
#                 outfp.write('\t'+str(abund))
#             outfp.write('\n')
    #print('singles_lookup',singles_lookup.keys())
    """
        # rules:
        1) Rare: if NONE of the multiples are also in standalone: add them all as singles and split the counts evenly
        2) if ALL of the multiples are present as standalones then divide them as the standalone percents dictate.
        3) if SOME are not present as standalones: if a pair: then all counts go to one.
            Common: if more than a pair?: confusing 
    """
    for hmts in multiples_lookup:
        #print()
        if hmts == 'Unmatched':
            continue
        hmts_lst = hmts.split('-')
        
        if len(hmts_lst) == 2:
            
            h1 = hmts_lst[0]
            h2 = hmts_lst[1]
            notes[h1] = []
            notes[h2] = []
            h1in = False
            h2in = False
            if h1 in singles_lookup:
                h1in = True
            if h2 in singles_lookup:
                h2in = True
                
            #print(h1in,h2in)
            if h1in and h2in:
               #print('both present as standalone',hmts_lst)
               pct1 = 0.0
               pct2 = 0.0
               if h1 in args.pct_file_collector:
                   pct1 = args.pct_file_collector[h1]
               if h2 in args.pct_file_collector:
                   pct2 = args.pct_file_collector[h2]
               
               original_cts1 = singles_lookup[h1]
               original_cts2 = singles_lookup[h2]
               
               new_cts1 = []
               new_cts2 = []
               #counts_to_split_and_add_to_original = multiples_lookup[hmts]
               for i,ds in enumerate(dataset_order):
                   #print(original_cts1[i],multiples_lookup[hmts][i], pct1, pct2)
                   #print('1 adding',float(multiples_lookup[hmts][i]) * float(pct1))
                   
                   new_cts1.append(str(float(original_cts1[i]) + float(multiples_lookup[hmts][i]) * float(pct1/100)))
                   new_cts2.append(str(float(original_cts2[i]) + float(multiples_lookup[hmts][i]) * float(pct2/100)))
               singles_lookup[h1] = new_cts1
               #print('new1',new_cts1[0])
               singles_lookup[h2] = new_cts2
               notes[h1].append('Some of these reads come from other taxa that are too close to elucidate ('+args.site+').')
               notes[h2].append('Some of these reads come from other taxa that are too close to elucidate ('+args.site+').')
            if not h1in and not h2in:
               #print('neither are present as standalone',hmts_lst)
               # add them both to singles and split the counts evenly
               #print(multiples_lookup[hmts])
               notes[h1].append('Neither HMT-'+h1+' nor HMT-'+h2+' were present singularly so these reads were split evenly at this site ('+args.site+').')
               notes[h2].append('Neither HMT-'+h1+' nor HMT-'+h2+' were present singularly so these reads were split evenly at this site ('+args.site+').')
               #print()
               #print('original',singles_lookup[h1][0])
               new_cts = [ str(float(ct)/2) for ct in multiples_lookup[hmts]]
               singles_lookup[h1] = [ str(float(ct)/2) for ct in multiples_lookup[hmts]]
               singles_lookup[h2] = [ str(float(ct)/2) for ct in multiples_lookup[hmts]]
               #print('new',new_cts[0])
            if h1in and not h2in or h2in and not h1in:
                #print('one-only as standalone',hmts_lst)
                
                
                new_cts = []
                unbalanced = False
                if h1in:
                    cts = singles_lookup[h1]
                    if h1 in args.pct_file_collector and args.pct_file_collector[hmts] > 10 * args.pct_file_collector[h1]:
                        # give 1/2 the counts to each
                        print('FOUND1 >10x',args.pct_file_collector[hmts], args.pct_file_collector[h1])
                        unbalanced = True
                        singles_lookup[h2] = [ str(float(ct)/2) for ct in multiples_lookup[hmts] ]
                        new_cts = []
                        original_cts = singles_lookup[h1]
                        for i,ds in enumerate(dataset_order):
                            new_cts.append(str(float(original_cts[i]) + float(multiples_lookup[hmts][i]) * 0.5))
                        singles_lookup[h1] = new_cts
                        notes[h1].append('the v3v5 region of 16S ribosomal RNA does not differentiate this taxon from other closely related taxa.')
                        notes[h2].append('the v3v5 region of 16S ribosomal RNA does not differentiate this taxon from other closely related taxa.')
                else:
                    cts = singles_lookup[h2]
                    #print('hmts',hmts,'h2',h2)
                    if h2 in args.pct_file_collector and args.pct_file_collector[hmts] > 10 * args.pct_file_collector[h2]:
                        # give 1/2 the counts to each
                        print('FOUND2 >10x',args.pct_file_collector[hmts], args.pct_file_collector[h2])
                        unbalanced = True
                        singles_lookup[h1] = [ str(float(ct)/2) for ct in multiples_lookup[hmts] ]
                        new_cts = []
                        original_cts = singles_lookup[h2]
                        for i,ds in enumerate(dataset_order):
                            new_cts.append(str(float(original_cts[i]) + float(multiples_lookup[hmts][i]) * 0.5))
                        singles_lookup[h2] = new_cts
                        notes[h1].append('the v3v5 region of 16S ribosomal RNA does not differentiate this taxon from other closely related taxa.')
                        notes[h2].append('the v3v5 region of 16S ribosomal RNA does not differentiate this taxon from other closely related taxa.')
                if not unbalanced:
                    
                    
                
                    for i,ds in enumerate(dataset_order):
                        new_cts.append(str(float(cts[i]) + float(multiples_lookup[hmts][i])))
                        # apply all to 
                    if h1in:
                        singles_lookup[h1] = new_cts
                        notes[h1].append('Some of these reads are from closely related HMT-'+h2+' which is not found at this site ('+args.site+').')
                    else:
                        singles_lookup[h2] = new_cts
                        notes[h2].append('Some of these reads are from closely related HMT-'+h1+' which is not found at this site ('+args.site+').')
                    
            
               
               
               
    # greater than 2 multiples
    for hmts in multiples_lookup:
        
        if hmts == 'Unmatched':
            continue
        hmts_lst = hmts.split('-')
        
        if len(hmts_lst) > 2:
            #print(hmts_lst)
            #print('\nold',hmts_lst)
            new_hmts_list = find_hmts_in_singles(hmts_lst, singles_lookup)
            #print('new',new_hmts_list)
            if len(new_hmts_list) == 0:  # means that none are in singles list
                #sys.exit('multiple >2 new list empty')
                # nothing in singles -- so add them and divide counts by len(hmts_lst)
                divide_by = len(hmts_lst)
                for hmtcode in hmts_lst:
                    if hmtcode not in notes:
                        notes[hmtcode] = []
                    # for i,ds in enumerate(dataset_order):
#                         new_cts.append(str(float(original_cts[i]) + float(multiples_lookup[hmts][i]) * float(pct/100)))
                    singles_lookup[hmtcode] = [ str(float(ct)/divide_by) for ct in multiples_lookup[hmts]]
                    notes[hmtcode].append('Site:'+args.site+' HMTs'+hmts+', Not easily differentiated from each other, so counts devided equally')
            else:
                counts_to_split_and_add_to_original = multiples_lookup[hmts]
                for hmtcode in new_hmts_list:
                    if hmtcode not in notes:
                        notes[hmtcode] = []
                
                    if hmtcode not in args.pct_file_collector:
                        pct = 0.0
                    else:
                        pct = args.pct_file_collector[hmtcode]
                    original_cts = singles_lookup[hmtcode]
                    new_cts = []
                    #print()
                    for i,ds in enumerate(dataset_order):
                        new_cts.append(str(float(original_cts[i]) + float(multiples_lookup[hmts][i]) * float(pct/100)))
                        #print('new',original_cts[i],str(float(original_cts[i]) + float(multiples_lookup[hmts][i]) * float(pct/100)))
                    singles_lookup[hmtcode] = new_cts
                    if 'Some of these reads come from other taxa that are too close to elucidate ('+args.site+').' not in notes[hmtcode]:
                        notes[hmtcode].append('Some of these reads come from other taxa that are too close to elucidate ('+args.site+').')
    for hmt in singles_lookup:
        #print('singles_lookup',hmt,notes[hmt])
        outfp.write('HMT-'+hmt+'\t'+';'.join(notes[hmt])+'\t'+'\t'.join(singles_lookup[hmt])+'\n')
        pass
    
    
    
    
    

    
    outfp.write('Unmatched\t\t'+'\t'.join(unmatched_counts)+'\n')
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
    In each site directory:
       v3v5 ONLY!!
       
    ./NEW_v3v5_assign_instr.py -i <site>_v3v5_counts_for_JMW_2024-03-06.csv 
    ../scripts/NEW_v3v5_assign_instr.py -i AKE_v3v5_counts_for_JMW_2024-03-06.csv -r v3v5 -s ake
    
    MUST find <site>_v3v5_MeanStdevPrev_forJMW_2024-03-06.csv  for percentages
    
          
       
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=True,  action="store",   dest = "infile", default=False,
                                                    help="")
    
    # parser.add_argument("-host", "--host", required = False, action = 'store', dest = "dbhost", default = 'localhost',
#                                                    help="") 
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", default=False,
                                                    help="verbose print()") 
    parser.add_argument("-outfile", "--out_file", required = False, action = 'store', dest = "outfile", 
                default = 'NEWcounts_curated', help = "")
    
    parser.add_argument("-r", "--region", required = True, action = 'store', dest = "region", 
                         help = "")
    parser.add_argument("-s", "--site", required = True, action = 'store', dest = "site", 
                         help = "")
    args = parser.parse_args()
    args.site = args.site.upper()
    site_names = [
    'AKE',  #Attached_Keratinized_gingiva
    'ANA',  #Anterior_nares
    'BMU',  #Buccal_mucosa
    'HPA',  #Hard_palate
    'LAF',  #L_Antecubital_fossa
    'LRC',  #L_Retroauricular_crease
    'MVA',  #Mid_vagina
    'PFO',  #Posterior_fornix
    'PTO',  #Palatine_Tonsils
    'RAF',  #R_Antecubital_fossa
    'RRC',  #R_Retroauricular_crease
    'SAL',  #Saliva
    'STO',  #Stool
    'SUBP', #Subgingival_plaque
    'SUPP', #Supragingival_plaque
    'THR',  #Throat
    'TDO',  #Tongue_dorsum
    'VIN'   #Vaginal_introitus
    ]
    
    if args.site not in site_names:
        sys.exit('site name not found '+args.site)
    if args.region not in ['v3v5']:
        print(usage)
        sys.exit()
        
        
        
    pctfile = args.site+'_v3v5_MeanStdevPrev_forJMW_2024-03-06.csv'
    if os.path.exists(pctfile):
        fp = open(pctfile,'r')
        args.pct_file_collector = {}
        for line in fp:

        
            line = line.strip()
            line_pts = line.split('\t')
            if line_pts[0].startswith('HMT-'):
                pct = line_pts[2]
                msid = '-'.join(line_pts[0].split('-')[1:])
                #print('XXX',msid)
                args.pct_file_collector[msid] = float(pct)
        #singles_file = '../spid_taxonomy_single.txt'
        fp.close()
        #print(args.pct_file_collector)
    else:
        sys.exit('No Pct File')
    
    args.suppressed_singles = run_suppressed()
    
#     myconn = MyConnection(host=dbhost, db=args.NEW_DATABASE,  read_default_file = "~/.my.cnf_node")
    if args.verbose:
        print()
    if not args.infile:
        print(usage)
        sys.exit()
    
    args.outfile = args.site+'_'+args.region+'_'+args.outfile +'_'+today+'_homd.csv'
    #args.dsets = get_ds_totals(args)
    
    run(args)
