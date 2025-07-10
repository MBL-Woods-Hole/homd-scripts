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
            cells = line_pts[ds_start_at:]
            pts = hotid.split('-')[1:]  # remove 'HMT-'
            
            if len(pts) == 1:
                #print(pts[0])
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
            if not h1in and not h2in:
               print('NEITHER are present as standalone',hmts_lst)
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
            if h1in and h2in:
               #print('BOTH present as standalone')
               pct1 = 0.0
               pct2 = 0.0
               if h1 in args.pct_file_collector:
                   pct1 = float(args.pct_file_collector[h1])
               if h2 in args.pct_file_collector:
                   pct2 = float(args.pct_file_collector[h2])
               sum_pcts = pct1 + pct2
               original_cts1 = singles_lookup[h1]
               original_cts2 = singles_lookup[h2]
               
               new_cts1 = []
               new_cts2 = []
               counts_to_split_and_add_to_original = multiples_lookup[hmts]
               #print('counts_to_split_and_add_to_original',pct1/sum_pcts,pct2/sum_pcts,counts_to_split_and_add_to_original)
               for i,ds in enumerate(dataset_order):
                   #print(original_cts1[i],multiples_lookup[hmts][i], pct1, pct2)
                   #print('1 adding',float(multiples_lookup[hmts][i]) * float(pct1))
                   counts_to_add1 = float(counts_to_split_and_add_to_original[i]) * float(pct1/sum_pcts)
                   counts_to_add2 = float(counts_to_split_and_add_to_original[i]) * float(pct2/sum_pcts)
                   new_cts1.append(str(float(original_cts1[i]) + counts_to_add1))
                   new_cts2.append(str(float(original_cts2[i]) + counts_to_add2))
               singles_lookup[h1] = new_cts1
               #print('new1',new_cts1[0])
               singles_lookup[h2] = new_cts2
               notes[h1].append('Reads equidistant to HMT-'+h1+' and HMT-'+h2+' were assigned to each taxon in proportion to the abundance of HMT-'+h1+' and HMT-'+h2+' individually at this body site ('+args.site+').')
               notes[h2].append('Reads equidistant to HMT-'+h1+' and HMT-'+h2+' were assigned to each taxon in proportion to the abundance of HMT-'+h1+' and HMT-'+h2+' individually at this body site ('+args.site+').')
               
            if h1in and not h2in or h2in and not h1in:
                #print('ONE-ONLY as standalone')
                new_cts = []
                if h1in:
                    cts = singles_lookup[h1]
                else:
                    cts = singles_lookup[h2]
                for i,ds in enumerate(dataset_order):
                    new_cts.append(str(float(cts[i]) + float(multiples_lookup[hmts][i])))
                    # apply all to 
                if h1in:
                    singles_lookup[h1] = new_cts
                    notes[h1].append('Because HMT-'+h2+' is not present individually, all equidistant reads were assigned to HMT-'+h1+' at this body site ('+args.site+').')
                else:
                    singles_lookup[h2] = new_cts
                    notes[h2].append('Because HMT-'+h1+' is not present individually, all equidistant reads were assigned to HMT-'+h2+' at this body site ('+args.site+').')

    # greater than 2 multiples
    for hmts in multiples_lookup:
        
        if hmts == 'Unmatched':
            continue
        hmts_lst = hmts.split('-')
        if args.site == 'ANA' and hmts == '216-550-591':
            #singles_lookup['550'] = [ str(float(ct)/2) for ct in multiples_lookup[hmts]]
            if '550' in singles_lookup:
                original_cts = singles_lookup['550']
                new_cts = []
                for i,ds in enumerate(dataset_order):
                    new_cts.append(str(float(original_cts[i]) + float(multiples_lookup[hmts][i])))
                singles_lookup['550'] = new_cts
            else:
                singles_lookup['550'] = multiples_lookup[hmts]
                notes['550'] =[]
                notes['591'] =[]
            notes['550'].append('Reads equidistant to Staphylococcus aureus, Acidovorax temperans, and Corynebacterium diphtheriae were assigned to Staphylococcus aureus at this body site ('+args.site+').')
            notes['216'].append('Reads equidistant to Staphylococcus aureus, Acidovorax temperans, and Corynebacterium diphtheriae were assigned to Staphylococcus aureus at this body site ('+args.site+').')
            notes['591'].append('Reads equidistant to Staphylococcus aureus, Acidovorax temperans, and Corynebacterium diphtheriae were assigned to Staphylococcus aureus at this body site ('+args.site+').')
            #sys.exit('apply all to 550')
            
        if len(hmts_lst) > 2:
            #print(hmts_lst)
            #print('\nold',hmts_lst)
            new_hmts_list = find_hmts_in_singles(hmts_lst, singles_lookup)
            #print('new',new_hmts_list)
            if len(new_hmts_list) == 0:  # means that none are in singles list
                #sys.exit('multiple >2 new list empty')
                # nothing in singles -- so add them as singles and divide counts by len(hmts_lst)
                divide_by = len(hmts_lst)
                for hmtcode in hmts_lst:
                    if hmtcode not in notes:
                        notes[hmtcode] = []
                    # for i,ds in enumerate(dataset_order):
#                         new_cts.append(str(float(original_cts[i]) + float(multiples_lookup[hmts][i]) * float(pct/100)))
                    singles_lookup[hmtcode] = [ str(float(ct)/divide_by) for ct in multiples_lookup[hmts]]
                    notes[hmtcode].append('HMTs'+hmts+' were not present singularly so these reads were split evenly at this body site ('+args.site+')')
            else:
                #print()
                counts_to_split_and_add_to_original = multiples_lookup[hmts]
                #print(hmts_lst,new_hmts_list)
                #print(new_hmts_list,'counts',counts_to_split_and_add_to_original)
                sum_pct = 0.0
                for hmtcode in new_hmts_list:
                    if hmtcode not in args.pct_file_collector.keys():
                        sum_pct += 0.0
                        #print('no',hmtcode)
                    else:
                        sum_pct += args.pct_file_collector[hmtcode]
                        #print('yes',hmtcode)
                        
                for hmtcode in new_hmts_list:
                    if hmtcode not in notes:
                        notes[hmtcode] = []
                    original_cts = singles_lookup[hmtcode]
                                    
                    if hmtcode not in args.pct_file_collector.keys():
                        pct2 = 0.0
                    else:
                        pct2 = args.pct_file_collector[hmtcode]
                    pct = pct2 / sum_pct
                    #print(hmtcode,'pct',pct2,sum_pct,pct)
                    
                    new_cts = []
                    
                    #print(hmts_lst)
                    for i,ds in enumerate(dataset_order):
                        if ds == 'S700014982-AKE':
                            #print(hmtcode,'counts[i]',counts_to_split_and_add_to_original[i])
                            pass
                        counts_to_add = float(counts_to_split_and_add_to_original[i]) * float(pct)
                        new_cts.append(str(float(original_cts[i]) + counts_to_add))
                        #print('new',original_cts[i],str(float(original_cts[i]) + float(multiples_lookup[hmts][i]) * float(pct/100)))
                    singles_lookup[hmtcode] = new_cts
                    #if 'Some of these reads come from other taxa that are too close to elucidate ('+args.site+').' not in notes[hmtcode]:
                    notes[hmtcode].append('Some of the reads equidistant from these taxa ('+hmts+') are included in HMT-'+hmtcode+' because they are too close to differentiate at this site ('+args.site+').')
                        
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
       v1v3 ONLY!!
       
    ./NEW_v1v3_assign_instr.py -i <site>_v1v3_counts_for_JMW_2024-03-06.csv 
    ../scripts/NEW_v1v3_assign_instr.py -i AKE_v1v3_counts_for_JMW_2024-03-06.csv -r v1v3 -s ake
    
    MUST find <site>_v1v3_MeanStdevPrev_forJMW_2024-03-06.csv  for percentages
   
    ['058', '398', '677'] ['058', '398', '677']

counts ['50.0']
['058', '398', '677']
058 pct 0.0023090649603152965 pct2=0.09824 sum_pct=42.545359999999995 pct/100=2.3090649603152964e-05
['058', '398', '677']
058 counts[i] 50.0
398 pct 0.04210329869109111 1.7913 42.545359999999995 0.0004210329869109111
['058', '398', '677']
398 counts[i] 50.0
677 pct 0.9555876363485937 40.65582 42.545359999999995 0.009555876363485937
['058', '398', '677']
677 counts[i] 50.0


          
       
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
    if args.region not in ['v1v3']:
        print(usage)
        sys.exit()
        
        
        
    pctfile = args.site+'_v1v3_MeanStdevPrev_forJMW_2024-03-06.csv'
    print('pctfile',pctfile)
    if os.path.exists(pctfile):
        fp = open(pctfile,'r')
        args.pct_file_collector = {}
        for line in fp:
            # HMTs  Max AKE-mean    AKE-10p AKE-90p AKE-sd  AKE-prev
    #         HMT-866   0.03861 0.03861 0.0 0.07374 0.16619 32.86713
    #         HMT-849   0.02354 0.02354 0.0 0.02515 0.13937 20.27972
        
            line = line.strip()
            line_pts = line.split('\t')
            if line_pts[0].startswith('HMT-'):
                pct = line_pts[2]
                msid = '-'.join(line_pts[0].split('-')[1:])
                 
                args.pct_file_collector[msid] = float(pct)
        #singles_file = '../spid_taxonomy_single.txt'
        fp.close()
        #print(args.pct_file_collector)
        #sys.exit()
    else:
        sys.exit('No Pct File')
    
    
#     myconn = MyConnection(host=dbhost, db=args.NEW_DATABASE,  read_default_file = "~/.my.cnf_node")
    if args.verbose:
        print()
    if not args.infile:
        print(usage)
        sys.exit()
    
    args.outfile = args.site+'_'+args.region+'_'+args.outfile +'_'+today+'_homd.csv'
    #args.dsets = get_ds_totals(args)
    
    run(args)
