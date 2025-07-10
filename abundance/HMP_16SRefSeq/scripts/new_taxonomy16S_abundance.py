#!/usr/bin/env python

import os,sys
if len(sys.argv) != 3:
    print('USAGE: new_taxonomy16S.py <date> <dbhost>')
    sys.exit()
    
date   = sys.argv[1]
dbhost = sys.argv[2]

print(date)
print(dbhost)
#sys.exit()

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
"""
./scripts/5-HMPRefSeq_gather_abundance_by_rank.py -i AKE_v1v3_pcts_SAVE.csv 
./scripts/6-HMPRefSeq_abundance_ranks_calc_means16S.py -i  AKE_v1v3_rank_abundance_sums_2024-04-24.csv
"""
pyscript5 = "5-HMPRefSeq_gather_abundance_by_rank.py"
input5 =  "%s_%s_pcts_SAVE.csv"  # use 2024-04-04
pyscript6 = "6-HMPRefSeq_abundance_ranks_calc_means16S.py"
input6 =  "%s_%s_rank_abundance_sums_"+date+".csv"  ## reset the filename date!!!!

for site in site_names:
    print()
    print(site)
    cwd = os.getcwd()
    os.chdir(site)
    cmd5v1v3 = '../scripts/'+pyscript5+' -host '+dbhost+' -i '+input5 % (site,'v1v3')
    cmd6v1v3 = '../scripts/'+pyscript6+' -host '+dbhost+' -i '+input6 % (site,'v1v3')
    cmd5v3v5 = '../scripts/'+pyscript5+' -host '+dbhost+' -i '+input5 % (site,'v3v5')
    cmd6v3v5 = '../scripts/'+pyscript6+' -host '+dbhost+' -i '+input6 % (site,'v3v5')
    os.system(cmd5v1v3)
    os.system(cmd6v1v3)
    os.system(cmd5v3v5)
    os.system(cmd6v3v5)
    
    os.chdir(cwd)
