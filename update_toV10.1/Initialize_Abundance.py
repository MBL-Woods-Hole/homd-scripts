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
sys.path.append('../../../homd-data/')
from connect import MyConnection
import datetime
ranks = ['domain','phylum','klass','order','family','genus','species']
today = str(datetime.date.today())

# segata_headers=['BM','KG','HP','Throat','PT','TD','Saliva','SupP','SubP','Stool']
# dewhirst_headers=['BM','KG','HP','TD','PT','Throat','Saliva','SupP','SubP']
# eren_headers=['BM','KG','HP','TD','PT','Throat','Saliva','SupP','SubP','Stool']
headers = ['SubP','SupP','KG','BM','HP','SV','TH','PT','TD','NS','ST']

   
hmt_index = 2  # only for dewhirst and eren
rank_index=3  # rank
max_segata_index=6
max_dewhirst_index=7
max_eren_index=8
max_any_index=9
start_segata_index=11
segata_col_count=20  # header row =='BM'
start_dewhirst_index=31
dewhirst_col_count=27  # header row =='BM'
start_eren_index=59
eren_col_count=20  # header row =='BM'
data_start_index=11
segata_cols = ['mean','stdev']
eren_cols = ['mean','prevalence']
dewhirst_cols = ['mean','stdev','prevalence']

# to correct for the few subspecies in HOMD::
subspecies = {}
subspecies['reuteri clade 818'] = ['reuteri','clade_818']  # tax_parts 6 and 7
subspecies['reuteri clade 938'] = ['reuteri','clade_938'] 
subspecies['cristatus clade 578'] = ['cristatus','clade_578'] 
subspecies['cristatus clade 886'] = ['cristatus','clade_886'] 
subspecies['infantis clade 431'] = ['infantis','clade_431'] 
subspecies['infantis clade 638'] = ['infantis','clade_638'] 
subspecies['oralis subsp. dentisani clade 058'] = ['oralis','subsp._dentisani_clade_058'] 
subspecies['oralis subsp. dentisani clade 398'] = ['oralis','subsp._dentisani_clade_398'] 
subspecies['oralis subsp. oralis'] = ['oralis','subsp._oralis'] 
subspecies['oralis subsp. tigurinus clade 070'] = ['oralis','subsp._tigurinus_clade_070'] 
subspecies['oralis subsp. tigurinus clade 071'] = ['oralis','subsp._tigurinus_clade_071'] 
subspecies['parasanguinis clade 411'] = ['parasanguinis','clade_411']
subspecies['parasanguinis clade 721'] = ['parasanguinis','clade_721']
subspecies['[Eubacterium] yurii subsp. schtitka'] = ['[Eubacterium] yurii','subsp._schtitka'] 
subspecies['[Eubacterium] yurii subsps. yurii & margaretiae'] = ['[Eubacterium] yurii','subsps._yurii_&_margaretiae']
subspecies['nucleatum subsp. animalis'] = ['nucleatum','subsp._animalis'] 
subspecies['nucleatum subsp. nucleatum'] = ['nucleatum','subsp._nucleatum'] 
subspecies['nucleatum subsp. polymorphum'] = ['nucleatum','subsp._polymorphum'] 
subspecies['nucleatum subsp. vincentii'] = ['nucleatum','subsp._vincentii'] 
"""
CREATE TABLE `abundance` (
  `abundance_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `reference` varchar(300) NOT NULL DEFAULT '',
  `otid` varchar(11) NOT NULL DEFAULT '',
  `domain_id` int(11) unsigned NOT NULL,
  `phylum_id` int(11) unsigned NOT NULL,
  `klass_id` int(11) unsigned NOT NULL,
  `order_id` int(11) unsigned NOT NULL,
  `family_id` int(11) unsigned NOT NULL,
  `genus_id` int(11) unsigned NOT NULL,
  `species_id` int(11) unsigned NOT NULL,
  `subspecies_id` int(11) unsigned NOT NULL,
  `notes` text,
  `level` varchar(12) NOT NULL DEFAULT '',
  `max` varchar(10) NOT NULL DEFAULT '',
  `BM_mean` varchar(11) NOT NULL DEFAULT '',
  `BM_prev` varchar(11) DEFAULT '',
  `BM_sd` varchar(11) NOT NULL DEFAULT '',
  `KG_mean` varchar(11) NOT NULL DEFAULT '',
  `KG_prev` varchar(11) NOT NULL DEFAULT '',
  `KG_sd` varchar(11) NOT NULL DEFAULT '',
  `HP_mean` varchar(11) NOT NULL DEFAULT '',
  `HP_prev` varchar(11) NOT NULL DEFAULT '',
  `HP_sd` varchar(11) NOT NULL DEFAULT '',
  `TD_mean` varchar(11) NOT NULL DEFAULT '',
  `TD_prev` varchar(11) NOT NULL DEFAULT '',
  `TD_sd` varchar(11) NOT NULL DEFAULT '',
  `PT_mean` varchar(11) NOT NULL DEFAULT '',
  `PT_prev` varchar(11) NOT NULL DEFAULT '',
  `PT_sd` varchar(11) NOT NULL DEFAULT '',
  `TH_mean` varchar(11) NOT NULL DEFAULT '',
  `TH_prev` varchar(11) NOT NULL DEFAULT '',
  `TH_sd` varchar(11) NOT NULL DEFAULT '',
  `SV_mean` varchar(11) NOT NULL DEFAULT '',
  `SV_prev` varchar(11) NOT NULL DEFAULT '',
  `SV_sd` varchar(11) NOT NULL DEFAULT '',
  `SupP_mean` varchar(11) NOT NULL DEFAULT '',
  `SupP_prev` varchar(11) NOT NULL DEFAULT '',
  `SupP_sd` varchar(11) NOT NULL DEFAULT '',
  `SubP_mean` varchar(11) NOT NULL DEFAULT '',
  `SubP_prev` varchar(11) NOT NULL DEFAULT '',
  `SubP_sd` varchar(11) NOT NULL DEFAULT '',
  `NS_mean` varchar(11) DEFAULT ' ',
  `NS_prev` varchar(11) DEFAULT '',
  `NS_sd` varchar(11) NOT NULL DEFAULT '',
  `ST_mean` varchar(11) NOT NULL DEFAULT '',
  `ST_prev` varchar(11) NOT NULL DEFAULT '',
  `ST_sd` varchar(11) NOT NULL DEFAULT '',
  PRIMARY KEY (`abundance_id`),
  UNIQUE KEY `reference` (`reference`,`BM_mean`,`domain_id`,`phylum_id`,`klass_id`,`order_id`,`family_id`,`genus_id`,`species_id`,`subspecies_id`),
  KEY `abundance_id_ibfk_3` (`otid`),
  KEY `phylum_id` (`phylum_id`),
  KEY `klass_id` (`klass_id`),
  KEY `order_id` (`order_id`),
  KEY `family_id` (`family_id`),
  KEY `genus_id` (`genus_id`),
  KEY `species_id` (`species_id`),
  KEY `subspecies_id` (`subspecies_id`),
  CONSTRAINT `abundance_copy4_ibfk_1` FOREIGN KEY (`domain_id`) REFERENCES `domain` (`domain_id`) ON UPDATE CASCADE,
  CONSTRAINT `abundance_copy4_ibfk_2` FOREIGN KEY (`phylum_id`) REFERENCES `phylum` (`phylum_id`) ON UPDATE CASCADE,
  CONSTRAINT `abundance_copy4_ibfk_3` FOREIGN KEY (`klass_id`) REFERENCES `klass` (`klass_id`) ON UPDATE CASCADE,
  CONSTRAINT `abundance_copy4_ibfk_4` FOREIGN KEY (`order_id`) REFERENCES `order` (`order_id`) ON UPDATE CASCADE,
  CONSTRAINT `abundance_copy4_ibfk_5` FOREIGN KEY (`family_id`) REFERENCES `family` (`family_id`) ON UPDATE CASCADE,
  CONSTRAINT `abundance_copy4_ibfk_6` FOREIGN KEY (`genus_id`) REFERENCES `genus` (`genus_id`) ON UPDATE CASCADE,
  CONSTRAINT `abundance_copy4_ibfk_7` FOREIGN KEY (`species_id`) REFERENCES `species` (`species_id`) ON UPDATE CASCADE,
  CONSTRAINT `abundance_copy4_ibfk_8` FOREIGN KEY (`subspecies_id`) REFERENCES `subspecies` (`subspecies_id`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

"""


    
def run_abundance_db(): 
    TCcollector = {}
    filestarter = 'homdData-TaxonCounts.json'
    #json_file = args.outfile
    json_file = filestarter
    if os.path.isfile(json_file):
        f = open(json_file)
        TCcollector = json.load(f)
    sites = []
    for n in headers:
        sites.append(n+'_mean')
        sites.append(n+'_10p')
        sites.append(n+'_90p')
        sites.append(n+'_sd')
        sites.append(n+'_prev')
    q = "SELECT otid,notes,`level`,reference,concat_ws(';',`domain`,`phylum`,`klass`,`order`,`family`,`genus`,`species`,`subspecies`) as taxonomy, "+','.join(sites)
    q += " FROM abundance"
    q += " JOIN `domain` using(domain_id)"
    q += " JOIN `phylum` using(phylum_id)"
    q += " JOIN `klass` using(klass_id)"
    q += " JOIN `order` using(order_id)"
    q += " JOIN `family` using(family_id)"
    q += " JOIN `genus` using(genus_id)"
    q += " JOIN `species` using(species_id)"
    q += " JOIN `subspecies` using(subspecies_id)"
    print(q)
    
    
    result = myconn_new.execute_fetch_select_dict(q)
    """
    {'abundance_id': 1148, 'reference': 'Dewhirst35x9', 'otid': '362', 'taxonomy': 'Bacteria;Synergistetes;Synergistia;Synergistales;Synergistaceae;Fretibacterium;sp. HMT 362', 'level': 'Species', 'max': '0.02095498', 'BM_mean': 
'0.002', 'BM_prev': '12.5', 'BM_sd': '0.007', 'KG_mean': '0', 'KG_prev': '5.9', 'KG_sd': '0.001', 'HP_mean': '0', 'HP_prev': '7.7', 'HP_sd': '0.001', 'TD_mean': '0', 'TD_prev': '3.1', 'TD_sd': '0.001', 'PT_mean': '0.006', 
'PT_prev': '6.9', 'PT_sd': '0.03', 'Throat_mean': '0', 'Throat_prev': '3.2', 'Throat_sd': '0', 'Saliva_mean': '0', 'Saliva_prev': '6.1', 'Saliva_sd': '0.001', 'SupP_mean': '0', 'SupP_prev': '5.7', 'SupP_sd': '0.001', 
'SubP_mean': '0.021', 'SubP_prev': '9.7', 'SubP_sd': '0.1', 'Stool_mean': '', 'Stool_prev': '', 'Stool_sd': ''}
    """
    
    #header_prefixes = ['BM','KG','HP','TD','PT','TH','SV','SupP','SubP','ST']
    #header_prefixes = ['SubP','SupP','KG','BM','HP','SV','TH','PT','TD','NS','ST']
    #segata_header_prefixes = ['BM','KG','HP','TD','PT','TH','SV','SupP','SubP','ST']
    #eren_header_prefixes =   ['BM','KG','HP','TD','PT','TH','SV','SupP','SubP','ST']
    site_prefixes    = ['SubP','SupP','KG','BM','HP','SV','TH','PT','TD']
    eren_site_prefixes     = site_prefixes + ['ST']
    segata_site_prefixes   = site_prefixes + ['ST']
    dewhirst_site_prefixes = site_prefixes + ['NS'] 
    #['BM','KG','HP','TD','PT','TH','SV','SupP','SubP','NS']
    print(segata_site_prefixes)
    for row in result:
        #print(row)
        max_segata, max_eren, max_dewhirst = 0,0,0
        taxon_string = fix_taxonomy(row['taxonomy'])
        #taxon_string = row['taxonomy']
        # tax_parts = taxon_string.split(';')
#         if len(tax_parts) == 7:
#             #print('found clade')
#             taxon_string = ';'.join(tax_parts[:6])+';'+tax_parts[5]+' '+tax_parts[6]
#             
#             if 'clade' in tax_parts[6] or 'subsp' in tax_parts[6]:
#                 #print('found clade')
#                 if tax_parts[6] in subspecies:
#                     taxon_string =';'.join(tax_parts[:6])+';'+tax_parts[5]+' '+subspecies[tax_parts[6]][0]+';'+subspecies[tax_parts[6]][1]
        if taxon_string not in TCcollector:
            print('!Missing from TaxonCounts.json -('+row['reference']+')::'+taxon_string)
            TCcollector[taxon_string] = {}
        TCcollector[taxon_string]['otid'] = row['otid']
        #TCcollector[taxon_string]['max_all'] = row['max']
        if 'notes' not in TCcollector[taxon_string]:
            TCcollector[taxon_string]['notes'] = {}
        if 'segata' not in TCcollector[taxon_string]:
            TCcollector[taxon_string]['segata'] = {}
        if 'eren_v1v3' not in TCcollector[taxon_string]:
            TCcollector[taxon_string]['eren_v1v3'] = {}
        if 'eren_v3v5' not in TCcollector[taxon_string]:
            TCcollector[taxon_string]['eren_v3v5'] = {}
        if 'dewhirst' not in TCcollector[taxon_string]:
            TCcollector[taxon_string]['dewhirst'] = {}
        
        if row['reference'].startswith('Segata'):
            for p in segata_site_prefixes:
                
                max_segata = get_max(row, p, max_segata)
                TCcollector[taxon_string]['segata'][p] = {'site':p,'avg':row[p+'_mean'],'prev':row[p+'_prev'],'sd':row[p+'_sd']}
            TCcollector[taxon_string]['max_segata'] = max_segata
            TCcollector[taxon_string]['notes']['segata'] = row['notes']
        if row['reference'].startswith('Eren2014_v1v3'):
            for p in eren_site_prefixes:
                max_eren = get_max(row, p, max_eren)
                TCcollector[taxon_string]['eren_v1v3'][p] = {'site':p,'avg':row[p+'_mean'],'prev':row[p+'_prev'],'sd':row[p+'_sd'],'10p':row[p+'_10p'],'90p':row[p+'_90p']}
            TCcollector[taxon_string]['max_erenv1v3'] = max_eren
            TCcollector[taxon_string]['notes']['eren_v1v3'] = row['notes']
        if row['reference'].startswith('Eren2014_v3v5'):
            for p in eren_site_prefixes:
                max_eren = get_max(row, p, max_eren)
                TCcollector[taxon_string]['eren_v3v5'][p] = {'site':p,'avg':row[p+'_mean'],'prev':row[p+'_prev'],'sd':row[p+'_sd'],'10p':row[p+'_10p'],'90p':row[p+'_90p']}
            TCcollector[taxon_string]['max_erenv3v5'] = max_eren
            TCcollector[taxon_string]['notes']['eren_v3v5'] = row['notes']
        if row['reference'].startswith('Dewhirst'):
            for p in dewhirst_site_prefixes:
                max_dewhirst = get_max(row, p, max_dewhirst)
                TCcollector[taxon_string]['dewhirst'][p] = {'site':p,'avg':row[p+'_mean'],'prev':row[p+'_prev'],'sd':row[p+'_sd'],'10p':row[p+'_10p'],'90p':row[p+'_90p']}
            TCcollector[taxon_string]['max_dewhirst'] = max_dewhirst
            TCcollector[taxon_string]['notes']['dewhirst'] = row['notes']
        
    #print(TCcollector)
    #for s in TCcollector:
    #    print('max_eren-s',s,TCcollector[s])
    filename = args.outfile
    print_dict(filename, TCcollector)
    
"""
if species: species == genus+species
Bacteria;Firmicutes;Bacilli;Lactobacillales;Aerococcaceae;Abiotrophia;Abiotrophia defectiva": {"tax_cnt": 1, "gcnt": 1, "refcnt": 1, 
"segata": {}, 
"eren": {"BM": {"site": "BM", "avg": "0.274", "prev": "61.039"}, "KG": {"site": "KG", "avg": "0.163", "prev": "32.468"}, "HP": {"site": "HP", "avg": "0.13", "prev": "53.247"}, "TD": {"site": "TD", "avg": "0.013", "prev": 
"20.779"}, "PT": {"site": "PT", "avg": "0.026", "prev": "31.169"}, "Throat": {"site": "Throat", "avg": "0.038", "prev": "24.675"}, "Saliva": {"site": "Saliva", "avg": "0.174", "prev": "42.857"}, "SupP": {"site": "SupP", "avg": 
"0.484", "prev": "75.325"}, "SubP": {"site": "SubP", "avg": "0.489", "prev": "63.636"}, "Stool": {"site": "Stool", "avg": "0", "prev": "1.299"}}, 
"dewhirst": {"BM": {"site": "BM", "avg": "0.192", "stdev": "0.343", "prev": "75"}, "KG": {"site": "KG", "avg": "0.081", "stdev": "0.14", "prev": "61.8"}, "HP": {"site": "HP", "avg": "0.138", "stdev": "0.289", "prev": "76.9"}, 
"TD": {"site": "TD", "avg": "0.006", "stdev": "0.008", "prev": "56.3"}, "PT": {"site": "PT", "avg": "0.017", "stdev": "0.037", "prev": "62.1"}, "Throat": {"site": "Throat", "avg": "0.019", "stdev": "0.039", "prev": "61.3"}, 
"Saliva": {"site": "Saliva", "avg": "0.083", "stdev": "0.168", "prev": "79.6"}, "SupP": {"site": "SupP", "avg": "0.244", "stdev": "0.415", "prev": "71.4"}, "SubP": {"site": "SubP", "avg": "0.099", "stdev": "0.224", "prev": 
"56.9"}}, 
"max_segata": "", "max_eren": "0.489", "max_dewhirst": "0.244", "max_all": "0.489017644", "otid": "389"}
"""

def fix_taxonomy(taxonomy):
    tax_lst = taxonomy.strip(';').split(';')
    #print('\n',taxonomy)
    if len(tax_lst) < 7: # d,p,c,o,f,g
        return ';'.join(tax_lst)
    #print(tax_lst)
    if len(tax_lst) == 8:
        subsp = tax_lst[-1]
    else:
        subsp = ''
    genus = tax_lst[5]
    species = tax_lst[6]
    if subsp and 'Eubacterium' in species:
#         print('1')
        tax_lst = tax_lst[:6] +[genus+' '+species,subsp ]
        
    elif 'Eubacterium' in species:
        # print('\n',taxonomy)
#         print('2')
        
        tax_lst = tax_lst[:6] +[genus+' '+species]
#         print(';'.join(tax_lst))
    elif subsp:
#         print('3')
        #tax_lst.pop(-1)
        #tax_lst[-1] = tax_lst[-1]+' '+subsp
        tax_lst = tax_lst[:6] +[genus+' '+species,subsp]
        #print('subsp',tax_lst)
    else:
        tax_lst = tax_lst[:6] +[genus+' '+species]
    #return taxonomy.strip(';')
    #Bacteria;Synergistetes;Synergistia;Synergistales;Synergistaceae;Jonquetella
    #Bacteria;Synergistetes;Synergistia;Synergistales;Dethiosulfovibrionaceae;Jonquetella
    #Bacteria;Firmicutes;Clostridia;Eubacteriales;Peptostreptococcaceae;Peptostreptococcaceae_[G-1];Peptostreptococcaceae_[G-1] Peptostreptococcaceae_[G-1] [Eubacterium]_sulci
    #Bacteria;Firmicutes;Clostridia;Eubacteriales;Peptostreptococcaceae;Peptostreptococcaceae_[G-1];Peptostreptococcaceae_[G-1] [Eubacterium]_sulci
    #Bacteria;Firmicutes;Clostridia;Eubacteriales;Peptostreptococcaceae;Peptostreptococcaceae_[G-1];Peptostreptococcaceae_[G-1] [Eubacterium]_sulci
    #Bacteria;Firmicutes;Clostridia;Eubacteriales;Peptostreptococcaceae;Peptostreptococcaceae_[G-1];Peptostreptococcaceae_[G-1] [Eubacterium]_sulci
    return ';'.join(tax_lst)
    
def fix_taxonomyX(taxonomy):
    """
    subspecies were put in separate col in script: abundance_scripts/10-load_abundance2dbNEW.py and stored in db
    Here we append subspecies back to species
    """
    tax_lst = taxonomy.split(';')
    new_tax = []
    subsp = tax_lst[-1]
    
    # if subsp:
#         tax_lst.pop(-1)
#         tax_lst[-1] = tax_lst[-1]+' '+subsp
    for name in tax_lst:
        if name:
            new_tax.append(name)
    return ';'.join(new_tax)
    
def get_max(row, p, max_ref):
    test = row[p+'_mean']
    
    if not test.strip():
        return 0
    if not max_ref:
        max_ref = 0.0
    if float(test) > float(max_ref):
        max_ref = float(test)
    if max_ref == 0:
        return ''
    return max_ref
    
def print_dict(filename, dict):
    print('Re-Writing',filename)
    with open(filename, 'w') as outfile:
        json.dump(dict, outfile, indent=args.indent)    

        
if __name__ == "__main__":

    usage = """
    USAGE:
        Opens and adds to the homdData-TaxonCounts.json file 
        MUST be run AFTER Initialize_Taxonomy.py
        ./Initialize_Abundance.py (now gets data from DB table: 'abundance')
        
        OLD:
        Run 3 times (once for each abundance.csv file
          ./Initialize_Abundance.py -i Segata2021-09-07.csv -s segata
          ./Initialize_Abundance.py -i Eren2021-09-07.csv -s eren
          ./Initialize_Abundance.py -i Dewhirst2021-09-07.csv -s dewhirst -pp
        
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=False,  action="store",   dest = "infile", default='none',
                                                    help=" ")
#    parser.add_argument("-s", "--source",   required=True,  action="store",   dest = "source", 
#                                                    help="ONLY segata dewhirst eren")
    parser.add_argument("-o", "--outfile",   required=False,  action="store",   dest = "outfile", 
            default='homdData-TaxonCounts.json',  help=" ")
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
   
    myconn_new = MyConnection(host=dbhost_new, db=args.NEW_DATABASE,  read_default_file = "~/.my.cnf_node")
    run_abundance_db()
   
    
