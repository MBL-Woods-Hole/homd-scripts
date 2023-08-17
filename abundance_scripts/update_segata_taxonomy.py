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
            #q_abund = "UPDATE abundance set domain_id='%s', phylum_id='%s', klass_id='%s', order_id='%s', family_id='%s', genus_id='%s', species_id='%s' WHERE otid='%s'"
            
            qt = q_tax % (domain_id,phylum_id,klass_id,order_id,family_id,genus_id,species_id, args.taxonomy_obj[hmtno])
            #qa = q_abund % (domain_id,phylum_id,klass_id,order_id,family_id,genus_id,species_id, hmtno)
            if args.write2db:
                myconn.execute_no_fetch(qt)
                #myconn.execute_no_fetch(qa)
            else:
                print('taxonomy update:', qt)
                print('NO WRITE, add -w to command')
    #print('synonym',synonym)
           
            update_abundance = False  # USE ORIGINAL ABUNDANCE SCRIPTS TO RECREATE ABUND TABLE
            if update_abundance:
                update_abundance_ids(hmtno, args.abund_ids)
    print('skipped (Candidatus)',skipped)
    
#LOCALHOST:: 
#synonyms_local_host = [['488', 'Order: Nanosynbacterales'], ['488', 'Family: Nanosynbacteraceae'], ['488', 'Genus: Nanosynbacter'], ['952', 'Species: lyticus'], ['348', 'Order: NA'], ['348', 'Family: NA'], ['348', 'Genus: NA'], ['346', 'Order: Saccharimonadales'], ['346', 'Genus: Nanosynsacchari'], ['870', 'Order: Nanogingivales'], ['870', 'Family: Nanogingivaceae'], ['870', 'Genus: Nanogingivalis'], ['870', 'Species: gingivalicus'], ['355', 'Order: unnamed'], ['355', 'Family: unnamed'], ['355', 'Genus: unnamed'], ['364', 'Order: Nanosyncoccales'], ['364', 'Genus: Nanosyncoccus'], ['356', 'Order: Nanoperiomorbales'], ['356', 'Family: Nanoperiomorbaceae'], ['356', 'Genus: Nanoperiomorbus'], ['356', 'Species: periodonticus'], ['988', 'Family: Saccharimonadaceae'], ['988', 'Genus: Saccharimonas'], ['345', 'Order: Absconditabacteria_[O-1]'], ['345', 'Family: Absconditabacteria_[F-1]'], ['345', 'Genus: Absconditabacteria_[G-1]'], ['368', 'Order: Mycobacteriales'], ['193', 'Species: modestum'], ['286', 'Species: serpentiformis'], ['553', 'Genus: Segatella'], ['562', 'Genus: Hoylesella'], ['583', 'Genus: Hallella'], ['317', 'Species: conceptionensis (NVP)'], ['526', 'Species: Koreensis (NVP)'], ['431', 'Species: infantis clade 431'], ['638', 'Species: infantis clade 638'], ['058', 'Species: sp. oral taxon 058'], ['070', 'Species: sp. oral taxon 070'], ['075', 'Genus: Oscillospiraceae_[G-1]'], ['085', 'Genus: Oscillospiraceae_[G-2]'], ['366', 'Genus: Oscillospiraceae_[G-3]'], ['435', 'Family: Syntrophomonadaceae'], ['561', 'Order: Mycoplasmoidales'], ['561', 'Family: Metamycoplasmataceae'], ['561', 'Genus: Metamycoplasma'], ['616', 'Genus: Mycoplasmoides'], ['202', 'Species: polymorphum'], ['330', 'Family: Pseudobdellovibrionaceae'], ['559', 'Family: Nitrobacteraceae'], ['316', 'Family: Paracoccaceae'], ['196', 'Family: Hyphomicrobiales_incertae_sedis'], ['209', 'Genus: Diaphorobacter'], ['041', 'Order: Desulfobulbales'], ['720', 'Species: paraphrophilus_drop'], ['554', 'Order: Moraxellales'], ['477', 'Genus: Stutzerimonas'], ['363', 'Family: Aminobacteriaceae'], ['996', 'Order: Gracilibacteria_[O-1]'], ['996', 'Family: Gracilibacteria_[F-1]'], ['996', 'Genus: Gracilibacteria_[G-3]'], ['997', 'Genus: Gracilibacteria_[G-4]'], ['999', 'Order: Eremiobacterota_[O-1]'], ['999', 'Family: Eremiobacterota_[F-1]'], ['999', 'Genus: Eremiobacterota_G-1]']]
def update_abundance_ids(hmt, ids):
    #Missing (Segata2012)::Bacteria;Pseudomonadota;Alphaproteobacteria;Rhodobacterales;Rhodobacteraceae;Rhodobacter
    #Missing (Segata2012)::Bacteria;Synergistota;Synergistia;Synergistales;Synergistaceae;Pyramidobacter
    #Missing (Eren2014_v1v3)::Bacteria;Actinomycetota;Actinomycetia;Propionibacteriales;Propionibacteriaceae;Cutibacterium
    #Missing (Dewhirst35x9)::Bacteria;Actinomycetota;Actinomycetia;Propionibacteriales;Propionibacteriaceae;Propionibacteriaceae_[G-1]
    print(ids)

    for vals in ids:
        rank = vals[0]
        old = vals[1]
        new = vals[2]
        if old != new:
            print(hmt)
           
            #q_old = "SELECT "+rank+'_id FROM `'+rank +"` WHERE `" +rank+"`='"+ids[hmt][1]+"'"
            #q_new = "SELECT "+rank+'_id FROM `'+rank +"` WHERE `" +rank+"`='"+ids[hmt][2]+"'"
            q = "SELECT `"+rank+'`,`'+rank+'_id` FROM `'+rank +"` WHERE `" +rank+"` = '"+old+"'"
            q += " UNION SELECT `"+rank+'`,`'+rank+'_id` FROM `'+rank +"` WHERE `" +rank+"` = '"+new+"'"
            print(q)
            result = myconn.execute_fetch_select(q)
            print('  result',result)
            old_id = result[0][1]
            new_id = result[1][1]
            qupdate = "UPDATE IGNORE abundance set "+rank+"_id='"+str(new_id)+"' WHERE "+rank+"_id='"+str(old_id)+"'"
            print('  oldid',old_id,'newid',new_id)
            
            if args.write2db:
                 myconn.execute_no_fetch(qupdate)
                 #myconn.execute_no_fetch(qa)
            else:
                 print('abundance update:', qupdate)
                 print('NO WRITE, add -w to command')
    
    
    
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
    qa = "UPDATE abundance set subspecies_id='1' WHERE otid='%s'" % (hmt)
    if args.write2db:
        myconn.execute_no_fetch(qt)
        myconn.execute_no_fetch(qa)
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
    qa = "UPDATE abundance set phylum_id='%s' WHERE otid='%s'" % (phylum_id, hmt)
    
    qt = q_tax % (phylum_id, args.taxonomy_obj[hmt])
    if args.write2db:
        myconn.execute_no_fetch(qt)
        myconn.execute_no_fetch(qa)
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
    qa = "UPDATE abundance set species_id='%s' WHERE otid='%s'" % (species_id, hmt)
    qt = q_tax % (species_id, args.taxonomy_obj[hmt])
    if args.write2db:
        myconn.execute_no_fetch(qt)
        myconn.execute_no_fetch(qa)
    else:
        print('taxonomy update:', qt)
        print('NO WRITE, add -w to command')

def run_segata():
    fp1 = open(args.infile1,'r')  # Floyds File
    fp2 = open(args.infile2,'r')  # Segata Edit  File (w/ counts)
    fpout = open(args.outfile,'w')
    
    pcollector = {}  # old => new
    kcollector = {}
    ocollector = {}
    fcollector = {}
    gcollector = {}
    for line in fp1:  
        line = line.strip()
        if not line:
            continue
        pts = line.split('\t')
        if len(pts) <5:
            continue
        old_phylum = pts[old_fi['np']]
        new_phylum = pts[new_fi['np']]
        
        #print('Old phylum:',old_phylum, '    New phylum:',new_phylum)
        pcollector[old_phylum] = new_phylum.replace(' ','_')
        kcollector[pts[old_fi['nk']]] = pts[new_fi['nk']].replace(' ','_')
        ocollector[pts[old_fi['no']]] = pts[new_fi['no']].replace(' ','_')
        fcollector[pts[old_fi['nf']]] = pts[new_fi['nf']].replace(' ','_')
        gcollector[pts[old_fi['ng']]] = pts[new_fi['ng']].replace(' ','_')
    
    fpout.write('OLD_Taxonomy\tNEW_Taxonomy\tHMT\tRank\ttype\tsource\tMax\tmax any oral site\tAbundance category\tBM-mean\tBM-sd\tKG-mean\tKG-sd\tHP-mean\tHP-sd\tTH-mean\tTH-sd\tPT-mean\tPT-sd\tTD-mean\tTD-sd\tSV-mean\tSV-sd\tSUPP-mean\tSUPP-sd\tSUBP-mean\tSUBP-sd\tST-mean\tST-sd\n')
    #OLD Taxonomy','HMT','Rank','type','source','Max','max any oral site','Abundance category','BM-mean','BM-sd','KG-mean','KG-sd','HP-mean','HP-sd','TH-mean','TH-sd','PT-mean','PT-sd','TD-mean','TD-sd','SV-mean','SV-sd','SUPP-meaSUPP-sd','SUBP-mean','SUBP-sd','ST-mean','ST-sd
    for line in fp2:
        
        line = line.strip()
        pts = line.split('\t')
        add_back_on = pts[1:]
        if pts[0] == 'OLD Taxonomy':
            continue
        if len(pts) == 1:
            continue
        old_tax_string = pts[0].replace(' ','_')
        old_tax_array = old_tax_string.split(';')
        if len(old_tax_array) == 1:  # domain level
            continue
        print(old_tax_array)
        updated_tax_array = old_tax_array
        
        for i,name in enumerate(old_tax_array):
            
            if i == 0:
                continue
            if i == 1:  #Phylum
                old_phylum = old_tax_array[i]
                if old_phylum in pcollector:
                    updated_tax_array[i] = pcollector[old_phylum]
            if i == 2: # Klass
                old_class = old_tax_array[i]
                if old_class in kcollector and old_class != kcollector[old_class]:
                    updated_tax_array[i] = kcollector[old_class]
                    print('Update CLASS:',old_class,kcollector[old_class])
            if i == 3: # Order
                old_order = old_tax_array[i]
                if old_order in ocollector and old_order != ocollector[old_order]:
                    updated_tax_array[i] = ocollector[old_order]
                    print('Update ORDER:',old_order,ocollector[old_order])
            if i == 4: # Family
                old_family = old_tax_array[i]
                if old_family in fcollector and old_family != fcollector[old_family]:
                    updated_tax_array[i] = fcollector[old_family]
                    print('Update FAMILY:',old_family,fcollector[old_family])
            if i == 5: # Genus
                old_genus = old_tax_array[i]
                if old_genus in gcollector and old_genus != gcollector[old_genus]:
                    updated_tax_array[i] = gcollector[old_genus]
                    print('Update GENUS:',old_genus,gcollector[old_genus])
             
        fpout.write(old_tax_string+'\t'+';'.join(updated_tax_array)+'\t'+'\t'.join(add_back_on)+'\n')
        
        
    fp1.close()
    fp2.close()
    fpout.close
        
def run_segata2():
    fp1 = open(args.infile1,'r')  # Floyds File
    fp2 = open(args.infile2,'r')  # Segata Edit  File (w/ counts)
    fpout = open(args.outfile,'w')
    
    pcollector = {}  # old => new
    kcollector = {}
    ocollector = {}
    fcollector = {}
    gcollector = {}
    floyd_tax_collector = {}
    for line in fp1:  
        line = line.strip()
        if not line:
            continue
        pts = line.split('\t')
        if len(pts) <5:
            continue
        old_phylum = pts[old_fi['np']]
        new_phylum = pts[new_fi['np']]
        old = [ pts[old_fi['nd']].replace(' ','_'),
                pts[old_fi['np']].replace(' ','_'),
                pts[old_fi['nk']].replace(' ','_'),
                pts[old_fi['no']].replace(' ','_'),
                pts[old_fi['nf']].replace(' ','_'),
                pts[old_fi['ng']].replace(' ','_')
                ]
        new = [ pts[new_fi['nd']].replace(' ','_'),
                pts[new_fi['np']].replace(' ','_'),
                pts[new_fi['nk']].replace(' ','_'),
                pts[new_fi['no']].replace(' ','_'),
                pts[new_fi['nf']].replace(' ','_'),
                pts[new_fi['ng']].replace(' ','_')
                ]
        old_genus_taxonomy = ';'.join(old)
        new_genus_taxonomy = ';'.join(new)
        #print('old tax(Floyd)',old_genus_taxonomy)
        floyd_tax_collector[old_genus_taxonomy] = new_genus_taxonomy
        #print('Old phylum:',old_phylum, '    New phylum:',new_phylum)
        # pcollector[old_phylum] = new_phylum.replace(' ','_')
#         kcollector[pts[old_fi['nk']]] = pts[new_fi['nk']].replace(' ','_')
#         ocollector[pts[old_fi['no']]] = pts[new_fi['no']].replace(' ','_')
#         fcollector[pts[old_fi['nf']]] = pts[new_fi['nf']].replace(' ','_')
#         gcollector[pts[old_fi['ng']]] = pts[new_fi['ng']].replace(' ','_')
    custom={}
    custom['Kytococcus'] = ['Bacteria','Actinomycetota','Actinomycetes','Micrococcales','Kytococcaceae','Kytococcus']
    custom['Dietzia'] = ['Bacteria','Actinomycetota','Actinomycetes','Mycobacteriales','Dietziaceae','Dietzia']
    custom['Kocuria'] = ['Bacteria','Actinomycetota','Actinomycetes','Micrococcales','Micrococcaceae','Kocuria']
    custom['Micrococcus'] = ['Bacteria','Actinomycetota','Actinomycetes','Micrococcales','Micrococcaceae','Micrococcus']
    custom['Rothia'] = ['Bacteria','Actinobacteria','Actinomycetia','Micrococcales','Micrococcaceae','Rothia']
    custom['Lawsonella'] = ['Bacteria','Actinobacteria','Actinomycetia','Corynebacteriales','Lawsonellaceae','Lawsonella']
    custom['Atopobium'] = ['Bacteria','Actinobacteria','Coriobacteriia','Coriobacteriales','Atopobiaceae','Atopobium']
    custom['Slackia'] = ['Bacteria','Actinomycetota','Coriobacteriia','Eggerthellales','Eggerthellaceae','Slackia']
    custom['Tannerella'] = ['Bacteria','Bacteroidota','Bacteroidia','Bacteroidales','Tannerellaceae','Tannerella']
    custom['Bergeyella'] = 'many possibles'  # many possibles
    custom['Chlamydophila'] = 'not found in Floyd'
    custom['Turicella'] = 'not found in Floyd'
    custom['Ignavibacterium'] = ['Bacteria','Ignavibacteriota','Ignavibacteria','Ignavibacteriales','Ignavibacteriaceae','Ignavibacterium']
    custom['Melioribacter'] = ['Bacteria','Ignavibacteriota','Ignavibacteria','Ignavibacteriales','Melioribacteraceae','Melioribacter']
    custom['Arthrospira'] = ['Bacteria','Cyanobacteriota','Cyanophyceae','Oscillatoriales','Microcoleaceae','Arthrospira']
    custom['Pyramidobacter'] = ['Bacteria','Synergistota','Synergistia','Synergistales','Dethiosulfovibrionaceae','Pyramidobacter']
    custom['Jonquetella'] = ['Bacteria','Synergistota','Synergistia','Synergistales','Dethiosulfovibrionaceae','Jonquetella']
    custom['Treponema'] = ['Bacteria','Spirochaetota','Spirochaetia','Spirochaetales','Treponemataceae','Treponema']
    custom['Yersinia'] = ['Bacteria','Pseudomonadota','Gammaproteobacteria','Enterobacterales','Yersiniaceae','Yersinia']
    custom['Proteus'] = ['Bacteria','Pseudomonadota','Gammaproteobacteria','Enterobacterales','Morganellaceae','Proteus']
    custom['Escherichia'] = ['Bacteria','Pseudomonadota','Gammaproteobacteria','Enterobacterales','Enterobacteriaceae','Escherichia']
    custom['Escherichia/Shigella'] = ['Bacteria','Pseudomonadota','Gammaproteobacteria','Enterobacterales','Enterobacteriaceae','Escherichia']
    custom['Rhodocyclus'] =  ['Bacteria','Pseudomonadota','Betaproteobacteria','Rhodocyclales','Rhodocyclaceae','Oryzomicrobium']
    custom['Porphyrobacter']  ='not found in Floyd'
    custom['Erythromicrobium'] = 'not found in Floyd'
    custom['Mesorhizobium'] = ['Bacteria','Pseudomonadota','Alphaproteobacteria','Hyphomicrobiales','Phyllobacteriaceae','Mesorhizobium']
    custom['Agrobacterium'] = ['Bacteria','Pseudomonadota','Alphaproteobacteria','Hyphomicrobiales','Rhizobiaceae','Agrobacterium']
    custom['Defluvibacter'] ='not found in Floyd'
    custom['Ochrobactrum'] ='not found in Floyd'
    custom['Bradyrhizobium'] = ['Bacteria','Pseudomonadota','Alphaproteobacteria','Hyphomicrobiales','Nitrobacteraceae','Bradyrhizobium']
    custom['Bosea'] = ['Bacteria','Pseudomonadota','Alphaproteobacteria','Hyphomicrobiales','Boseaceae','Bosea']
    custom['Afipia'] = ['Bacteria','Pseudomonadota','Alphaproteobacteria','Hyphomicrobiales','Nitrobacteraceae','Afipia']
    custom['Bartonella'] = ['Bacteria','Pseudomonadota','Alphaproteobacteria','Hyphomicrobiales','Bartonellaceae','Bartonella']
    custom['Mycoplasma'] = 'many possibles'
    custom['Eggerthia'] = ['Bacteria','Bacillota','Erysipelotrichia','Erysipelotrichales','Coprobacillaceae','Eggerthia']
    custom['Fastidiosipila'] = ['Bacteria','Bacillota','Clostridia','Eubacteriales','Oscillospiraceae','Fastidiosipila']
    custom['Mogibacterium'] = ['Bacteria','Bacillota','Clostridia','Eubacteriales','Peptostreptococcaceae','Mogibacterium']
    custom['Filifactor'] = ['Bacteria','Bacillota','Clostridia','Eubacteriales','Peptostreptococcaceae','Filifactor']
    custom['Mollicutes_[G-1]'] = ['Bacteria','Mycoplasmatota','Mollicutes','Mollicutes_[O-1]','Mollicutes_[F-1]','Mollicutes_[G-1]']
    custom['Mollicutes_[G-2]'] = ['Bacteria','Mycoplasmatota','Mollicutes','Mollicutes_[O-2]','Mollicutes_[F-2]','Mollicutes_[G-2]']
    custom['Veillonellaceae_[G-1]'] = ['Bacteria','Firmicutes','Negativicutes','Selenomonadales','Selenomonadaceae','Veillonellaceae_[G-1]']
    custom['Syntrophomonadaceae_[VIII][G-1]'] = ['Bacteria','Bacillota','Clostridia','Eubacteriales','Syntrophomonadaceae','Syntrophomonadaceae_[VIII][G-1]']
    custom['Ruminococcaceae_[G-1]']= ['Bacteria','Bacillota','Clostridia','Eubacteriales','Oscillospiraceae','Oscillospiraceae_[G-1]']
    custom['Ruminococcaceae_[G-2]']=['Bacteria','Bacillota','Clostridia','Eubacteriales','Oscillospiraceae','Oscillospiraceae_[G-2]']
    custom['Ruminococcaceae_[G-3]'] = ['Bacteria','Bacillota','Clostridia','Eubacteriales','Oscillospiraceae','Oscillospiraceae_[G-3]']
    custom['Peptostreptococcus'] = ['Bacteria','Bacillota','Clostridia','Eubacteriales','Peptostreptococcaceae','Peptostreptococcus']
    custom['Peptoniphilus'] = ['Bacteria','Firmicutes','Tissierellia','Tissierellales','Peptoniphilaceae','Peptoniphilus']
    custom['Peptoniphilaceae_[G-1]'] = ['Bacteria','Bacillota','Tissierellia','Tissierellales','Peptoniphilaceae','Peptoniphilaceae_[G-1]']
    custom['Peptoniphilaceae_[G-2]'] = ['Bacteria','Bacillota','Tissierellia','Tissierellales','Peptoniphilaceae','Peptoniphilaceae_[G-2]']
    custom['Peptoniphilaceae_[G-3]'] = ['Bacteria','Bacillota','Tissierellia','Tissierellales','Peptoniphilaceae','Peptoniphilaceae_[G-3]']
    custom['Parvimonas'] = ['Bacteria','Bacillota','Tissierellia','Tissierellales','Peptoniphilaceae','Parvimonas']
    custom['Finegoldia'] = ['Bacteria','Bacillota','Tissierellia','Tissierellales','Peptoniphilaceae','Finegoldia']
    custom['Anaerococcus'] = ['Bacteria','Bacillota','Tissierellia','Tissierellales','Peptoniphilaceae','Anaerococcus']
    custom['Peptococcus'] = ['Bacteria','Bacillota','Clostridia','Eubacteriales','Peptococcaceae','Peptococcus']
    custom['Stomatobaculum'] = ['Bacteria','Bacillota','Clostridia','Eubacteriales','Lachnospiraceae','Stomatobaculum']
    custom['Shuttleworthia'] = ['Bacteria','Bacillota','Clostridia','Eubacteriales','Lachnospiraceae','Shuttleworthia']
    custom['Oribacterium'] = ['Bacteria','Bacillota','Clostridia','Eubacteriales','Lachnospiraceae','Oribacterium']
    custom['Lachnospiraceae_[G-10]'] = ['Bacteria','Bacillota','Clostridia','Eubacteriales','Lachnospiraceae','Lachnospiraceae_[G-10]']
    custom['Lachnospiraceae_[G-2]'] = ['Bacteria','Bacillota','Clostridia','Eubacteriales','Lachnospiraceae','Lachnospiraceae_[G-2]']
    custom['Lachnospiraceae_[G-3]'] = ['Bacteria','Bacillota','Clostridia','Eubacteriales','Lachnospiraceae','Lachnospiraceae_[G-3]']
    custom['Lachnospiraceae_[G-7]'] = ['Bacteria','Bacillota','Clostridia','Eubacteriales','Lachnospiraceae','Lachnospiraceae_[G-7]']
    custom['Lachnospiraceae_[G-8]'] = ['Bacteria','Bacillota','Clostridia','Eubacteriales','Lachnospiraceae','Lachnospiraceae_[G-8]']
    custom['Lachnospiraceae_[G-9]'] = ['Bacteria','Bacillota','Clostridia','Eubacteriales','Lachnospiraceae','Lachnospiraceae_[G-9]']
    custom['Lachnoanaerobaculum'] = ['Bacteria','Bacillota','Clostridia','Eubacteriales','Lachnospiraceae','Lachnoanaerobaculum']
    custom['Johnsonella'] = ['Bacteria','Bacillota','Clostridia','Eubacteriales','Lachnospiraceae','Johnsonella']
    custom['Catonella'] = ['Bacteria','Bacillota','Clostridia','Eubacteriales','Lachnospiraceae','Catonella']
    custom['Butyrivibrio'] = ['Bacteria','Bacillota','Clostridia','Eubacteriales','Lachnospiraceae','Butyrivibrio']
    custom['Pseudoramibacter'] = ['Bacteria','Bacillota','Clostridia','Eubacteriales','Eubacteriaceae','Pseudoramibacter']
    custom['Eubacterium'] = ['Bacteria','Bacillota','Clostridia','Eubacteriales','Eubacteriaceae','Eubacterium']
    custom['Clostridiales_[F-1][G-1]'] = ['Bacteria','Bacillota','Clostridia','Eubacteriales','Clostridiales_[F-1]','Clostridiales_[F-1][G-1]']
    custom['Clostridiales_[F-1][G-2]'] = ['Bacteria','Bacillota','Clostridia','Eubacteriales','Clostridiales_[F-1]','Clostridiales_[F-1][G-2]']
    custom['Clostridiales_[F-3][G-1]'] = ['Bacteria','Bacillota','Clostridia','Eubacteriales','Clostridiales_[F-3]','Clostridiales_[F-3][G-1]']
    phylum={}
    phylum['Absconditabacteria_(SR1)']='Candidatus_Absconditabacteria'
    phylum['Actinobacteria']          ='Actinomycetota'
    phylum['Bacteroidetes']           ='Bacteroidota'
    phylum['Chlamydiae']              ='Chlamydiota'
    phylum['Chlorobi']                ='Chlorobiota'
    phylum['Chloroflexi']             ='Chloroflexota'
    phylum['Cyanobacteria']           ='Cyanobacteriota'
    phylum['Firmicutes']              ='Bacillota'
    phylum['Fusobacteria']            ='Fusobacteriota'
    phylum['Gracilibacteria_(GN02)']  ='Candidatus_Gracilibacteria'
    phylum['Proteobacteria']          ='Pseudomonadota'
    phylum['Saccharibacteria_(TM7)']  ='Candidatus_Saccharibacteria'
    phylum['Spirochaetes']            ='Spirochaetota'
    phylum['Synergistetes']           ='Synergistota'
    phylum['WPS-2']                   ='Candidatus_Eremiobacterota'
    phylum['Euryarchaeota']           ='Euryarchaeota'
    klass={}
    klass['Ignavibacteria'] = ['Bacteria','Ignavibacteriota','Ignavibacteria']
    klass['Mollicutes']     = ['Bacteria','Mycoplasmatota','Mollicutes']

    order={}
    order['Ignavibacteria'] = ['Bacteria','Ignavibacteriota','Ignavibacteria','Ignavibacteriales']
    family={}
    family['Ignavibacteria'] = ['Bacteria','Ignavibacteriota','Ignavibacteria','Ignavibacteriales','Ignavibacteriaceae']
    #'Bacteria;Ignavibacteriota;Ignavibacteria;Ignavibacteriales;Ignavibacteriaceae;Ignavibacterium'
    fpout.write('STATUS/Rank\tOLD_SEGATA_Taxonomy\tUPDATED_HOMD_Taxonomy\tHMT\tRank\ttype\tsource\tMax\tmax any oral site\tAbundance category\tBM-mean\tBM-sd\tKG-mean\tKG-sd\tHP-mean\tHP-sd\tTH-mean\tTH-sd\tPT-mean\tPT-sd\tTD-mean\tTD-sd\tSV-mean\tSV-sd\tSUPP-mean\tSUPP-sd\tSUBP-mean\tSUBP-sd\tST-mean\tST-sd\n')
    #OLD Taxonomy','HMT','Rank','type','source','Max','max any oral site','Abundance category','BM-mean','BM-sd','KG-mean','KG-sd','HP-mean','HP-sd','TH-mean','TH-sd','PT-mean','PT-sd','TD-mean','TD-sd','SV-mean','SV-sd','SUPP-meaSUPP-sd','SUBP-mean','SUBP-sd','ST-mean','ST-sd
    match_count = 0
    nomatch_count = 0
    odities = []
    many = []
    for line in fp2:
        line = line.strip()
        pts = line.split('\t')
        add_back_on = pts[1:]
        if pts[0] == 'OLD Taxonomy':
            continue
        if len(pts) == 1:
            continue
        segata_tax_string = pts[0].replace(' ','_')
        st_array = segata_tax_string.split(';')
        if len(st_array) == 1:
            fpout.write('Domain'+'\t'+st_array[0]+'\t'+st_array[0]+'\t'+'\t'.join(add_back_on)+'\n')
        if len(st_array) == 2:
            #print('P-level',st_array)
            fpout.write('Phylum'+'\t'+';'.join(st_array)+'\t'+st_array[0]+';'+phylum[st_array[1]]+'\t'+'\t'.join(add_back_on)+'\n')
        if len(st_array) == 3:
            print('\nClass-level',st_array)
            st_string = ';'.join(st_array)
            got_one = 0
            for t in floyd_tax_collector:
               if st_string in t:
                   print('C-found',st_array)
                   got_one = 1
                   fpout.write('Class'+'\t'+st_string+'\t'+';'.join(floyd_tax_collector[t].split(';')[:3])+'\t'+'\t'.join(add_back_on)+'\n')
                   break
            if not got_one:
                if st_array[-1] in klass:
                    fpout.write('Class'+'\t'+st_string+'\t'+';'.join(klass[st_array[-1]])+'\t'+'\t'.join(add_back_on)+'\n')
                else:
                    fpout.write('Class-x'+'\t'+st_string+'\t'+'\t'+'\t'.join(add_back_on)+'\n')
            #fpout.write('Class'+'\t'+';'.join(st_array)+'\t'+st_array[0]+';'+phylum[st_array[0]]+'\n')
        if len(st_array) == 4:
            print('\nOrder-level',st_array)
            st_string = ';'.join(st_array)
            got_one = 0
            for t in floyd_tax_collector:
               if st_string in t:
                   print('O-found',st_array)
                   got_one = 1
                   fpout.write('Order'+'\t'+st_string+'\t'+';'.join(floyd_tax_collector[t].split(';')[:4])+'\t'+'\t'.join(add_back_on)+'\n')
                   break
            if not got_one:
                if st_array[-1] in order:
                    fpout.write('Order'+'\t'+st_string+'\t'+';'.join(order[st_array[-1]])+'\t'+'\t'.join(add_back_on)+'\n')
                else:
                    fpout.write('Order-x'+'\t'+st_string+'\t'+'\t'+'\t'.join(add_back_on)+'\n')
        if len(st_array) == 5:
            print('\nFamily-level',st_array)
            st_string = ';'.join(st_array)
            got_one = 0
            for t in floyd_tax_collector:
               if st_string in t:
                   print('F-found',st_array)
                   got_one = 1
                   fpout.write('Family'+'\t'+st_string+'\t'+';'.join(floyd_tax_collector[t].split(';')[:5])+'\t'+'\t'.join(add_back_on)+'\n')
                   break
            if not got_one:
                if st_array[-1] in family:
                    fpout.write('Family'+'\t'+st_string+'\t'+';'.join(family[st_array[-1]])+'\t'+'\t'.join(add_back_on)+'\n')
                else:
                    fpout.write('Family-x'+'\t'+st_string+'\t'+'\t'+'\t'.join(add_back_on)+'\n')
        
        if len(st_array) == 6:
            
            segata_tax6 = ';'.join(st_array)
            #print('Segata tax',';'.join(ot_array))
            if segata_tax6 in floyd_tax_collector:
                match_count +=1 
                #print(match_count,'GOT EXACT MATCH:',segata_tax6)
                # change each 6 from segata6 to floydNew
                fpout.write('Genus FULL MATCH'+'\t'+segata_tax6+'\t'+floyd_tax_collector[segata_tax6]+'\t'+'\t'.join(add_back_on)+'\n')
            else:
                genus = st_array[-1]
                if genus in custom:
                    if custom[genus] == 'not found in Floyd':
                        odities.append(st_array) # to be curated by Floyd
                        fpout.write('Genus NOT FOUND'+'\t'+segata_tax6+'\n')
                    elif custom[genus] == 'many possibles':
                        many.append(st_array) # to be curated by Floyd
                        fpout.write('Genus MANY'+'\t'+segata_tax6+'\n')
                    else:
                       pass
                       fpout.write('Genus MATCH'+'\t'+segata_tax6+'\t'+';'.join(custom[genus])+'\t'+'\t'.join(add_back_on)+'\n')
                       # to change to each in array
                else:
                    nomatch_count +=1  
                    #print(nomatch_count,'   No MATCH:',segata_tax6)
                    fpout.write('Genus NOT FOUND'+'\t'+segata_tax6+'\t'+'\t'+'\t'.join(add_back_on)+'\n')
if __name__ == "__main__":

    usage = """
    USAGE:
        ./update_ncbi_phylum_v2.py 
         Version 2 needs Floyd's spreadsheet:
              homd-work/new_taxonomy-July2023/HOMD_NCBI_Taxonomy_Compairson_V2-fd-12.csv
        -i1/--infile1 REQUIRED HOMD_NCBI_Taxonomy_Compairson_V2-fd-12.csv
        
              homd-scripts/abundance-segata/segata_edit20230814.csv
        -i2/--infile2 REQUIRED segata_edit20230814
        
        
        
        
        -host/--host [homd]  default:localhost
       
        

    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i1", "--infile1",   required=True,  action="store",   dest = "infile1", default='none',
                                                   help=" ")
    parser.add_argument("-i2", "--infile2",   required=True,  action="store",   dest = "infile2", default='none',
                                                   help=" ")
    
    parser.add_argument("-w", "--write",   required=False,  action="store_true",   dest = "write2db", default=False,
                                                help=" ")
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",   dest = "verbose", default=False,
                                                    help=" ")
    parser.add_argument("-host", "--host",
                        required = False, action = 'store', dest = "dbhost", default = 'localhost',
                        help = "choices=['homd',  'localhost']")
    # parser.add_argument("-t", "--taxonomy",   required=False,  action="store_true",   dest = "taxonomy", default=False,
#                                                     help=" ")
#     parser.add_argument("-s", "--synonyms",   required=False,  action="store_true",   dest = "synonyms", default=False,
#                                                     help=" ")
#     parser.add_argument("-tid", "--taxonid",   required=False,  action="store_true",   dest = "taxid", default=False,
#                                                     help=" ")
#     parser.add_argument("-ssp", "--subspecies",   required=False,  action="store_true",   dest = "sspecies", default=False,
#                                                     help=" ")
#     parser.add_argument("-a", "--abundance",   required=False,  action="store_true",   dest = "abundance", default=False,
#                                                     help=" ")
    # parser.add_argument("-s", "--start_digit",   required=False,  action="store",   dest = "start_digit", default='1',
#                                                     help=" ")
    parser.add_argument("-o", "--outfile",   required=False,  action="store",    dest = "outfile", default='segata_editUPDATED.tsv',
                                                    help="")
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
    
    #run_segata()
    run_segata2()
    sys.exit()
    
    args.taxonomy_obj = get_taxonomy_obj()
    
    if args.taxonomy:
        run_taxonomy()
    elif args.synonyms:
        run_synonyms()
    elif args.taxid:
        run_taxon_id()
    elif args.sspecies:
        run_subspecies()
    #elif args.abundance:
    #    run_abundance()
    else:
       print('no def selected')
       print(usage)
    

    
