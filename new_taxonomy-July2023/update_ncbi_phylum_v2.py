#!/usr/bin/env python

## SEE https://docs.dhtmlx.com/suite/tree__api__refs__tree.html // new version 7 must load from json file
# this script creates a list of json objects that allows the dhtmlx javascript library
# to parse and show a taxonomy tree (Written for HOMD)
##
import os, sys
import gzip
import json
#from json import JSONEncoder
import argparse
import csv,re
from Bio import SeqIO
sys.path.append('../homd-data/')
sys.path.append('../../homd-data/')

from connect import MyConnection,mysql
import datetime
import requests
global mysql_errors
mysql_errors = []
"""

"""
today = str(datetime.date.today())

#spreadsheet file:  HOMD_NCBI_Taxonomy_Compairson_V2-fd-12.csv
#['_997', '995.2', '', '997', '1017', 'HOMD', 'HMT-997', 'Bacteria', 'Gracilibacteria_(GN02)', 'Gracilibacteria_(GN02)_[C-1]', 'Gracilibacteria_(GN02)_[O-1]', 'Gracilibacteria_(GN02)_[F-1]', 'Gracilibacteria_(GN02)_[G-4]', 'bacterium_HMT_997', 'NCBI', '363464', 'Bacteria', 'Candidatus Gracilibacteria', 'NA', 'NA', 'NA', 'NA', 'NA', '', '', 'NCBI', '363464', 'HMT-997', 'Bacteria', 'Candidatus Gracilibacteria (GN02)', 'Gracilibacteria_[C-1]', 'Gracilibacteria_[O-1]', 'Gracilibacteria_[F-1]', 'Gracilibacteria_[G-4]', 'bacterium_HMT_997', 'y']
new_fi = {
   "hmt":27,  # AB
   "nd": 28,  # AC
   "np": 29,
   "nk": 30,
   "no": 31,
   "nf": 32,
   "ng": 33,
   "ns": 34,
   "taxid":26 #AA
}

old_fi = {  #orange
    "nd": 7,  # H
   "np": 8,
   "nk": 9,
   "no": 10,
   "nf": 11,
   "ng": 12,
   "ns": 13
}
hmts_with_ssp =[  # 19 of them
'411','431',
'578',
'638',
'721',
'818',
'886',
'938',
'58','398','707','106','70','71','377',
'420','698','202','200'   # 4Fusobacterium
]
skip_TM7 = True  # taxonomy only not for ncbi_taxon_id

def clean_hmt(s):
    
    return str(int(s.split('-')[1]))  # strips zeros HMT-058 => 58
    
def get_taxonomy_obj():
    collect = {}
    q = "SELECT otid,taxonomy_id from otid_prime"
    result = myconn.execute_fetch_select(q)
    for row in result:
        
        collect[str(row[0])] = str(row[1])
    return collect
    
def run_taxonomy():
    fp = open(args.infile,'r')
    synonym = []
    pcollector={}
    start = 1
    new_phylum =''
    old_phylum = ''
    otid=''
    new_taxonid=''
    """
    1) get taxonomy ID from otid_prime for each otid
    for each rank:
    DOMAIN:
       "select domain_id from domain where domain='pts[fi[nd]]'"
       if comes back empty must insert and get new domain_id
    
    
    Hi all (from Floyd 20230808

Attached is an excel file with all the updates. 

Columns E-N (orange) are the current taxonomy

Columns O-W (Blue) are what George pull out based upon Taxon ID (write or wrong)

Columns AD-AL are my version of what names should be changed to (Changes highlighted in pink)

George’s suggested new NCBI Taxon ID is in column X

MY corrected taxon ID in in column AA

Other columns make comments or point to various things.

I have not finished updating TM7 or other candidate phyla radiation taxa, so they should remain unchanged for now.
    """
    
    skipped = []
    q_synonym_insert_base = "INSERT into `synonym` (otid, synonym) VALUES('%s','%s')"
    for line in fp:
        line = line.strip()
        pts = line.split('\t')
        if len(pts) > 5 and pts[0][0] != '[':
            
            hmt = pts[new_fi['hmt']]
            hmtno = clean_hmt(hmt)
            
            args.abund_ids = []
            if skip_TM7 and pts[new_fi['np']].startswith('Candidatus'):
                skipped.append(hmt)
                continue
            #print(hmtno, hmt)
            
            new_tax=[pts[new_fi['nd']],pts[new_fi['np']],pts[new_fi['nk']],pts[new_fi['no']],pts[new_fi['nf']],pts[new_fi['ng']],pts[new_fi['ns']]]
            old_tax=[pts[old_fi['nd']],pts[old_fi['np']],pts[old_fi['nk']],pts[old_fi['no']],pts[old_fi['nf']],pts[old_fi['ng']],pts[old_fi['ns']]]
            if hmtno in hmts_with_ssp:
                print('OLD',';'.join(old_tax))
                print('NEW',';'.join(new_tax))
                continue
            
            
            # DOMAIN
            d = pts[new_fi['nd']]
            
            
            q_domain_select = "SELECT domain_id FROM `domain` where `domain`='%s'" % (d)
            res_domain = myconn.execute_fetch_one(q_domain_select)
            if myconn.cursor.rowcount > 0:
                domain_id = res_domain[0]
            else:
                # INSERT
                # We have a new domain MUST add "domain: pts[fi['nd']] to synonyms table
                # add to collector for synonym table for insertion later
                print('NEW DOMAIN! ('+pts[new_fi['nd']]+') for',hmt)
                q_domain_insert = "INSERT into `domain` (`domain`) VALUES('%s')" % (d)
                #print(q_synonym_insert)
                print(q_domain_insert)
                myconn.execute_no_fetch(q_domain_insert)
                domain_id = myconn.cursor.lastrowid
            print('domain ID',domain_id)
            
            # PHYLUM
            p = pts[new_fi['np']]
            p_old = pts[old_fi['np']]
            args.abund_ids.append(['phylum',p_old, p])
            if p == 'NA':
                p = 'phylum_NA'
            q_phylum_select = "SELECT phylum_id FROM `phylum` where `phylum`='%s'" % (p)
            print(q_phylum_select)
            res_phylum = myconn.execute_fetch_one(q_phylum_select)
            print(res_phylum)
            print(myconn.cursor.rowcount)
            if myconn.cursor.rowcount > 0:
                phylum_id = res_phylum[0]
            else:
                # INSERT
                print('NEW PHYLUM! ('+pts[new_fi['np']]+') for',hmt)
                q_phylum_insert = "INSERT into `phylum` (`phylum`) VALUES('%s')" % (p)
                #print(q_synonym_insert)
                print(q_phylum_insert)
                myconn.execute_no_fetch(q_phylum_insert)
                phylum_id = myconn.cursor.lastrowid
            print('phylum ID',phylum_id)
            
            # KLASS
            k = pts[new_fi['nk']]
            k_old = pts[old_fi['nk']]
            args.abund_ids.append(['klass',k_old, k])
            if k == 'NA':
                k = 'class_NA'
            q_klass_select = "SELECT klass_id FROM `klass` where `klass`='%s'" % (k)
            res_klass = myconn.execute_fetch_one(q_klass_select)
            if myconn.cursor.rowcount > 0:
                klass_id = res_klass[0]
            else:
                # INSERT
                print('NEW KLASS! ('+pts[new_fi['nk']]+') for',hmt)
                q_klass_insert = "INSERT into `klass` (`klass`) VALUES('%s')" % (k)
                #print(q_synonym_insert)
                print(q_klass_insert)
                myconn.execute_no_fetch(q_klass_insert)
                klass_id = myconn.cursor.lastrowid
            print('klass ID',klass_id)
            
            # ORDER
            o = pts[new_fi['no']]
            o_old = pts[old_fi['no']]
            args.abund_ids.append(['order',o_old, o])
            if o == 'NA':
                o = 'order_NA'
            q_order_select = "SELECT order_id FROM `order` where `order`='%s'" % (o)
            res_order = myconn.execute_fetch_one(q_order_select)
            if myconn.cursor.rowcount > 0:
                order_id = res_order[0]
                
            else:
                # INSERT
                print('NEW ORDER! ('+pts[new_fi['no']]+') for',hmt)
                q_order_insert = "INSERT into `order` (`order`) VALUES('%s')" % (o)
                #print(q_synonym_insert)
                print(q_order_insert)
                myconn.execute_no_fetch(q_order_insert)
                order_id = myconn.cursor.lastrowid
            print('order ID',order_id)
            
            
            # FAMILY
            f = pts[new_fi['nf']]
            f_old = pts[old_fi['nf']]
            args.abund_ids.append(['family',f_old, f])
            if f == 'NA':
                f = 'family_NA'
            q_family_select = "SELECT family_id FROM `family` where `family`='%s'" % (f)
            res_family = myconn.execute_fetch_one(q_family_select)
            if myconn.cursor.rowcount > 0:
                family_id = res_family[0]
            else:
                # INSERT
                print('NEW FAMILY! ('+pts[new_fi['nf']]+') for',hmt)
                q_family_insert = "INSERT into `family` (`family`) VALUES('%s')" % (f)
                #print(q_synonym_insert)
                print(q_family_insert)
                myconn.execute_no_fetch(q_family_insert)
                family_id = myconn.cursor.lastrowid
            print('family ID',family_id)
            
            # GENUS
            g = pts[new_fi['ng']]
            g_old = pts[old_fi['ng']]
            args.abund_ids.append(['genus',g_old, g])
            if g == 'NA':
                g = 'genus_NA'
            q_genus_select = "SELECT genus_id FROM `genus` where `genus`='%s'" % (g)
            res_genus = myconn.execute_fetch_one(q_genus_select)
            if myconn.cursor.rowcount > 0:
                genus_id = res_genus[0]
            else:
                # INSERT
                print('NEW GENUS! ('+pts[new_fi['ng']]+') for',hmt)
                q_genus_insert = "INSERT into `genus` (`genus`) VALUES('%s')" % (g)
                print(q_genus_insert)
                myconn.execute_no_fetch(q_genus_insert)
                genus_id = myconn.cursor.lastrowid
            print('genus ID',genus_id)
            
            # SPECIES
            s = pts[new_fi['ns']]
            s_old = pts[old_fi['ns']]
            args.abund_ids.append(['species',s_old, s])
            if s == 'NA':
                s = 'species_NA'
            q_species_select = "SELECT species_id FROM `species` where `species`='%s'" % (s)
            res_species = myconn.execute_fetch_one(q_species_select)
            if myconn.cursor.rowcount > 0:
                species_id = res_species[0]
            else:
                # INSERT
                print('NEW SPECIES! ('+pts[new_fi['ns']]+') for',hmt)
                q_species_insert = "INSERT into `species` (`species`) VALUES('%s')" % (s)
                print(q_species_insert)
                myconn.execute_no_fetch(q_species_insert)
                species_id = myconn.cursor.lastrowid
            print('species ID',species_id)
            
            ## UPDATE taxonomy table
            q_tax   = "UPDATE taxonomy set domain_id='%s', phylum_id='%s', klass_id='%s', order_id='%s', family_id='%s', genus_id='%s', species_id='%s' WHERE taxonomy_id='%s'"
            
            qt = q_tax % (domain_id,phylum_id,klass_id,order_id,family_id,genus_id,species_id, args.taxonomy_obj[hmtno])
            #qa = q_abund % (domain_id,phylum_id,klass_id,order_id,family_id,genus_id,species_id, hmtno)
            if args.write2db:
                myconn.execute_no_fetch(qt)
                #myconn.execute_no_fetch(qa)
            else:
                print('taxonomy update:', qt)
                print('NO WRITE, add -w to command')
    #print('synonym',synonym)
           
            
    print('skipped (Candidatus)',skipped)
    
#LOCALHOST:: 
#synonyms_local_host = [['488', 'Order: Nanosynbacterales'], ['488', 'Family: Nanosynbacteraceae'], ['488', 'Genus: Nanosynbacter'], ['952', 'Species: lyticus'], ['348', 'Order: NA'], ['348', 'Family: NA'], ['348', 'Genus: NA'], ['346', 'Order: Saccharimonadales'], ['346', 'Genus: Nanosynsacchari'], ['870', 'Order: Nanogingivales'], ['870', 'Family: Nanogingivaceae'], ['870', 'Genus: Nanogingivalis'], ['870', 'Species: gingivalicus'], ['355', 'Order: unnamed'], ['355', 'Family: unnamed'], ['355', 'Genus: unnamed'], ['364', 'Order: Nanosyncoccales'], ['364', 'Genus: Nanosyncoccus'], ['356', 'Order: Nanoperiomorbales'], ['356', 'Family: Nanoperiomorbaceae'], ['356', 'Genus: Nanoperiomorbus'], ['356', 'Species: periodonticus'], ['988', 'Family: Saccharimonadaceae'], ['988', 'Genus: Saccharimonas'], ['345', 'Order: Absconditabacteria_[O-1]'], ['345', 'Family: Absconditabacteria_[F-1]'], ['345', 'Genus: Absconditabacteria_[G-1]'], ['368', 'Order: Mycobacteriales'], ['193', 'Species: modestum'], ['286', 'Species: serpentiformis'], ['553', 'Genus: Segatella'], ['562', 'Genus: Hoylesella'], ['583', 'Genus: Hallella'], ['317', 'Species: conceptionensis (NVP)'], ['526', 'Species: Koreensis (NVP)'], ['431', 'Species: infantis clade 431'], ['638', 'Species: infantis clade 638'], ['058', 'Species: sp. oral taxon 058'], ['070', 'Species: sp. oral taxon 070'], ['075', 'Genus: Oscillospiraceae_[G-1]'], ['085', 'Genus: Oscillospiraceae_[G-2]'], ['366', 'Genus: Oscillospiraceae_[G-3]'], ['435', 'Family: Syntrophomonadaceae'], ['561', 'Order: Mycoplasmoidales'], ['561', 'Family: Metamycoplasmataceae'], ['561', 'Genus: Metamycoplasma'], ['616', 'Genus: Mycoplasmoides'], ['202', 'Species: polymorphum'], ['330', 'Family: Pseudobdellovibrionaceae'], ['559', 'Family: Nitrobacteraceae'], ['316', 'Family: Paracoccaceae'], ['196', 'Family: Hyphomicrobiales_incertae_sedis'], ['209', 'Genus: Diaphorobacter'], ['041', 'Order: Desulfobulbales'], ['720', 'Species: paraphrophilus_drop'], ['554', 'Order: Moraxellales'], ['477', 'Genus: Stutzerimonas'], ['363', 'Family: Aminobacteriaceae'], ['996', 'Order: Gracilibacteria_[O-1]'], ['996', 'Family: Gracilibacteria_[F-1]'], ['996', 'Genus: Gracilibacteria_[G-3]'], ['997', 'Genus: Gracilibacteria_[G-4]'], ['999', 'Order: Eremiobacterota_[O-1]'], ['999', 'Family: Eremiobacterota_[F-1]'], ['999', 'Genus: Eremiobacterota_G-1]']]

    
def run_synonyms():
    fp = open(args.infile,'r')
    
    ranks = ['domain','phylum','klass','order','family','genus','species']
    q_synonym_insert_base = "INSERT IGNORE into `synonym` (otid, synonym) VALUES('%s','%s')"
    for line in fp:
        line = line.strip()
        pts = line.split('\t')
        if len(pts) > 5 and pts[0][0] != '[':
            
            hmt = pts[new_fi['hmt']]
            hmtno = clean_hmt(hmt)
            if skip_TM7 and pts[new_fi['np']].startswith('Candidatus'):
                continue
            
            if pts[old_fi['nd']] != pts[new_fi['nd']]:
                # need to update synonyms
                q_synonym_insert = q_synonym_insert_base % (hmtno,'Domain: '+pts[old_fi['nd']])
                # disregard Domain
            if pts[old_fi['np']] != pts[new_fi['np']]:
                q_synonym_insert = q_synonym_insert_base % (hmtno,'Phylum: '+pts[old_fi['np']])
                if args.write2db:
                    myconn.execute_no_fetch(q_synonym_insert)
                else:
                    print('NO WRITE',q_synonym_insert)
            if pts[old_fi['nk']] != pts[new_fi['nk']]:
                q_synonym_insert = q_synonym_insert_base % (hmtno,'Class: '+pts[old_fi['nk']])
                if args.write2db:
                    myconn.execute_no_fetch(q_synonym_insert)
                else:
                    print('NO WRITE',q_synonym_insert)
            if pts[old_fi['no']] != pts[new_fi['no']]:
                q_synonym_insert = q_synonym_insert_base % (hmtno,'Order: '+pts[old_fi['no']])
                if args.write2db:
                    myconn.execute_no_fetch(q_synonym_insert)
                else:
                    print('NO WRITE',q_synonym_insert)
            if pts[old_fi['nf']] != pts[new_fi['nf']]:
                q_synonym_insert = q_synonym_insert_base % (hmtno,'Family: '+pts[old_fi['nf']])
                if args.write2db:
                    myconn.execute_no_fetch(q_synonym_insert)
                else:
                    print('NO WRITE',q_synonym_insert)
            if pts[old_fi['ng']] != pts[new_fi['ng']]:
                q_synonym_insert = q_synonym_insert_base % (hmtno,'Genus: '+pts[old_fi['ng']])
                if args.write2db:
                    myconn.execute_no_fetch(q_synonym_insert)
                else:
                    print('NO WRITE',q_synonym_insert)
            if pts[old_fi['ns']] != pts[new_fi['ns']]:
                q_synonym_insert = q_synonym_insert_base % (hmtno,'Species: '+pts[old_fi['ns']])
                if args.write2db:
                    myconn.execute_no_fetch(q_synonym_insert)
                else:
                    print('NO WRITE',q_synonym_insert)

def run_taxon_id():
    fp = open(args.infile,'r')
    
    for line in fp:
        line = line.strip()
        pts = line.split('\t')
        
        if len(pts) > 5 and pts[0][0] != '[':
            
            hmt = pts[new_fi['hmt']]
            
            hmtno = clean_hmt(hmt)
            ncbi_taxon_id = pts[new_fi['taxid']]
            if ncbi_taxon_id:
                
                q = "UPDATE otid_prime set ncbi_taxon_id='%s' WHERE otid='%s'" % (ncbi_taxon_id,hmtno)
                if args.write2db:
                    myconn.execute_no_fetch(q)
                else:
                    print('NO WRITE',q)

def run_subspecies():
    fp = open(args.infile,'r')
    skipped = []
    collector = {}
    count = 0
    change_phylum_only = ['818','938','578','886','431','638','398','707','411','721','106','377','71']  #13
                
    # remove ssp
    # update species & delete subspecies
    fusobacterium = ['420','698','202','200']  # 4-Fusobacterium]
    # update species & delete subspecies
    #oralis remove ssp
    oralis = ['58','70']
    
    for line in fp:
        line = line.strip()
        pts = line.split('\t')
        if len(pts) > 5 and pts[0][0] != '[':
            
            hmt = pts[new_fi['hmt']]
            hmtno = clean_hmt(hmt)
            if skip_TM7 and pts[new_fi['np']].startswith('Candidatus'):
                skipped.append(hmt)
                continue
            
            new_tax=[pts[new_fi['nd']],pts[new_fi['np']],pts[new_fi['nk']],pts[new_fi['no']],pts[new_fi['nf']],pts[new_fi['ng']],pts[new_fi['ns']]]
            old_tax=[pts[old_fi['nd']],pts[old_fi['np']],pts[old_fi['nk']],pts[old_fi['no']],pts[old_fi['nf']],pts[old_fi['ng']],pts[old_fi['ns']]]
            
            if hmtno in hmts_with_ssp:
                collector[hmtno] = pts
                
    for HMT in collector:
        print(HMT)
        pts = collector[HMT]
        fullhmt = pts[new_fi['hmt']]
        new_tax=[pts[new_fi['nd']],pts[new_fi['np']],pts[new_fi['nk']],pts[new_fi['no']],pts[new_fi['nf']],pts[new_fi['ng']],pts[new_fi['ns']]]
        old_tax=[pts[old_fi['nd']],pts[old_fi['np']],pts[old_fi['nk']],pts[old_fi['no']],pts[old_fi['nf']],pts[old_fi['ng']],pts[old_fi['ns']]]
        print('OLD',old_tax)
        print('NEW',new_tax)
        #print(collector[HMT])
        
        update_phylum(HMT, pts[old_fi['np']], pts[new_fi['np']])
        # if pts[old_fi['nd']] != pts[new_fi['nd']]:
#             print(HMT,'diff','domain',pts[old_fi['nd']],pts[new_fi['nd']])
#         if pts[old_fi['np']] != pts[new_fi['np']]:
#             print(HMT,'diff','phylum',pts[old_fi['np']],pts[new_fi['np']])
#         if pts[old_fi['nk']] != pts[new_fi['nk']]:
#             print(HMT,'diff','Class',pts[old_fi['nk']],pts[new_fi['nk']])
#         if pts[old_fi['no']] != pts[new_fi['no']]:
#             print(HMT,'diff','order',pts[old_fi['no']],pts[new_fi['no']])
#         if pts[old_fi['nf']] != pts[new_fi['nf']]:
#             print(HMT,'diff','family',pts[old_fi['nf']],pts[new_fi['nf']])
#         if pts[old_fi['ng']] != pts[new_fi['ng']]:
#             print(HMT,'diff','genus',pts[old_fi['ng']],pts[new_fi['ng']])
#         if pts[old_fi['ns']] != pts[new_fi['ns']]:
#             print(HMT,'diff','species',pts[old_fi['ns']],pts[new_fi['ns']])
        if HMT in oralis:
            # update species & delete subspecies
            # sp format:  sp._HMT_448
            print(HMT,'oralis')
            update_species(HMT, pts[old_fi['ns']], 'sp._'+fullhmt)
            delete_subspecies(HMT)
            # print('OLD',old_tax)
#             print('NEW',new_tax)
        if HMT in fusobacterium:  
            # update species & delete subspecies
            print(HMT,'fusobacterium')
            # print('OLD',old_tax)
#             print('NEW',new_tax)
            update_species(HMT, pts[old_fi['ns']], pts[new_fi['ns']])
            delete_subspecies(HMT)
            
            
def delete_subspecies(hmt):
    qt = "UPDATE taxonomy set subspecies_id='1' WHERE taxonomy_id='%s'"  % (args.taxonomy_obj[hmt])
    
    if args.write2db:
        myconn.execute_no_fetch(qt)
    else:
        print('taxonomy update:', qt)
        print('NO WRITE, add -w to command')

def update_phylum(hmt, old_phylum, new_phylum):
    print('updating_phylum')
    print(hmt, old_phylum, new_phylum)
    p = new_phylum
    if p == 'NA':
        p = 'phylum_NA'
    q_phylum_select = "SELECT phylum_id FROM `phylum` where `phylum`='%s'" % (p)
    res_phylum = myconn.execute_fetch_one(q_phylum_select)
    if myconn.cursor.rowcount > 0:
        phylum_id = res_phylum[0]
    else:
        # INSERT
        print('NEW PHYLUM! ('+new_phylum+')for',hmt)
        #q_synonym_insert = q_synonym_insert_base % (hmtno, 'Phylum: '+p)
        q_phylum_insert = "INSERT into `phylum` (`phylum`) VALUES('%s')" % (p)
        #print(q_synonym_insert)
        print(q_phylum_insert)
        #myconn.execute_no_fetch(q_synonym_insert)
        myconn.execute_no_fetch(q_phylum_insert)
        phylum_id = myconn.cursor.lastrowid
    
    q_tax = "UPDATE taxonomy set phylum_id='%s' WHERE taxonomy_id='%s'"
    
    qt = q_tax % (phylum_id, args.taxonomy_obj[hmt])
    if args.write2db:
        myconn.execute_no_fetch(qt)
        
    else:
        print('taxonomy update:', qt)
        print('NO WRITE, add -w to command')

def update_species(hmt, old_species, new_species):
    print('updating_species')
    print(hmt, old_species, new_species)
    s = new_species
    if s == 'NA':
        s = 'species_NA'
    q_species_select = "SELECT species_id FROM `species` where `species`='%s'" % (s)
    res_species = myconn.execute_fetch_one(q_species_select)
    if myconn.cursor.rowcount > 0:
        species_id = res_species[0]
    else:
        # INSERT
        print('NEW SPECIES! ('+new_species+') for',hmt)
        q_species_insert = "INSERT into `species` (`species`) VALUES('%s')" % (s)
        print(q_species_insert)
        myconn.execute_no_fetch(q_species_insert)
        species_id = myconn.cursor.lastrowid
    
    q_tax = "UPDATE taxonomy set species_id='%s' WHERE taxonomy_id='%s'"
    
    qt = q_tax % (species_id, args.taxonomy_obj[hmt])
    if args.write2db:
        myconn.execute_no_fetch(qt)
      
    else:
        print('taxonomy update:', qt)
        print('NO WRITE, add -w to command')
     
if __name__ == "__main__":

    usage = """
    USAGE:
        ./update_ncbi_phylum_v2.py 
         Version 2 needs Floyd's spreadsheet:
              HOMD_NCBI_Taxonomy_Compairson_V2-fd-12.csv
              
        -i/--infile REQUIRED 
        
        AND One Of:
        -t/--taxonomy The bigone
        -s/--synonyms  write updates/changes to synonym table
        -tid/--taxonid  update ncbi_taxon_id into otid_prime
        -ssp/--subspecies requies special handling
        
        
        -host/--host [homd]  default:localhost
       
        

    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=True,  action="store",   dest = "infile", default='none',
                                                   help=" ")
    # parser.add_argument("-a", "--anno",   required=False,  action="store",   dest = "anno",  default='ncbi',
#                                                     help="")
    parser.add_argument("-w", "--write",   required=False,  action="store_true",   dest = "write2db", default=False,
                                                help=" ")
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",   dest = "verbose", default=False,
                                                    help=" ")
    parser.add_argument("-host", "--host",
                        required = False, action = 'store', dest = "dbhost", default = 'localhost',
                        help = "choices=['homd',  'localhost']")
    parser.add_argument("-t", "--taxonomy",   required=False,  action="store_true",   dest = "taxonomy", default=False,
                                                    help=" ")
    parser.add_argument("-s", "--synonyms",   required=False,  action="store_true",   dest = "synonyms", default=False,
                                                    help=" ")
    parser.add_argument("-tid", "--taxonid",   required=False,  action="store_true",   dest = "taxid", default=False,
                                                    help=" ")
    parser.add_argument("-ssp", "--subspecies",   required=False,  action="store_true",   dest = "sspecies", default=False,
                                                    help=" ")
   
    # parser.add_argument("-s", "--start_digit",   required=False,  action="store",   dest = "start_digit", default='1',
#                                                     help=" ")
#     parser.add_argument("-o", "--outfile",   required=False,  action="store",    dest = "out", default='ncbi_meta_info.tsv',
#                                                     help="verbose print()")
    args = parser.parse_args()
    
    #parser.print_help(usage)
                        
    if args.dbhost == 'homd_dev':
        #args.json_file_path = '/groups/vampsweb/vamps/nodejs/json'
        #args.TAX_DATABASE = 'HOMD_taxonomy'
        args.DATABASE = 'homd'
        #dbhost_old = '192.168.1.51'
        dbhost= '192.168.1.46'   #TESTING is 1.46  PRODUCTION is 1.42
        #dbhost= '192.168.1.42' 
        args.prettyprint = False
        #args.ncbi_dir = '/mnt/efs/bioinfo/projects/homd_add_genomes_V10.1/GCA_V10.1_all'
        #args.prokka_dir = '/mnt/efs/bioinfo/projects/homd_add_genomes_V10.1/prokka_V10.1_all'
    elif args.dbhost == 'homd_prod':  
        args.DATABASE = 'homd'
        #dbhost_old = '192.168.1.51'
        dbhost= '192.168.1.42' 
    elif args.dbhost == 'localhost':
        #args.json_file_path = '/Users/avoorhis/programming/homd-data/json'
        #args.TAX_DATABASE  = 'HOMD_taxonomy'
        args.DATABASE = 'homd'
        dbhost = 'localhost'
        
        #dbhost_old = 'localhost'
    else:
        sys.exit('dbhost - error')
    
    
    myconn = MyConnection(host=dbhost, db=args.DATABASE,  read_default_file = "~/.my.cnf_node")

    args.indent = 4
    args.taxonomy_obj = get_taxonomy_obj()
    
    if args.taxonomy:
        run_taxonomy()
    elif args.synonyms:
        run_synonyms()
    elif args.taxid:
        run_taxon_id()
    elif args.sspecies:
        run_subspecies()
    
    else:
       print('no def selected')
       print(usage)
    

    
