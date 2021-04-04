#!/usr/bin/env python

## SEE https://docs.dhtmlx.com/suite/tree__api__refs__tree.html // new version 7 must load from json file
# this script creates a list of json objects that allows the dhtmlx javascript library
# to parse and show a taxonomy tree (Written for HOMD)

import os, sys
import json
ranks = ['domain','phylum','klass','order','family','genus','species']

masterList = []
counts = {}
#domains = []

# [{bacteria:
# 
# }]
def run(args):
	global counts
	csv_fh = open(args.infile,'r')
	
	for line in csv_fh:
		line = line.strip()
		#good_line = []
			
		if not line:
			continue
		line = line.split("\t")
		
		if len(line) == 0:  
			continue
		if len(line) not in [7,14]:
			if args.verbose:
				print('excluding(size)',line)
			continue
		if '' in line and not args.allow_partial_taxa:
			if args.verbose:
				print('excluding("")',line)
			continue
		if any('empty_' in s for s in line) and not args.allow_partial_taxa:
			if args.verbose:
				print('excluding(empty_)',line)
			continue
		if any('_NA' in s for s in line) and not args.allow_partial_taxa:
			if args.verbose:
				print('excluding(_NA)',line)
			continue	
		if  not args.include_euks and line[0][:6] == 'Eukary':
			if args.verbose:
				print('excluding(euks)',line)
			continue
		
		# exclude some phyla (use only what is currently in HOMD)
		if line[1] not in (good_homd_bac_phyla + good_homd_arc_phyla):
			if args.verbose:
				print('excluding(bad phylum)',line)
			continue
		
		
		taxa_lst = line[:7]
		id_lst = line[7:]
		
		if args.meld_genus and (taxa_lst[5] != '' or taxa_lst[6] != ''):
			taxa_lst[6] = taxa_lst[5] +' '+taxa_lst[6]
		
		#bad_line = exclude_lineage(taxa_lst)
		
		
			
		if args.verbose:
			print('good row: ',line)
		counts = get_counts(line)
		if args.output_format == 'list':
			masterList.append(create_list_obj(taxa_lst, id_lst))
		else:
			masterList.append(taxa_lst)
	
	print('out format: ',args.output_format)
	
	if args.verbose:
		print('counts: ',json.dumps(counts, indent = 3))
	outFile = open('taxcounts.json', 'w')
	outFile.write(json.dumps(counts, indent = 3))
	if args.output_format == 'list':
		json_list_type(args, masterList)
	else:
		json_obj_type(args, masterList)   #default json_obj
		

		
	
	
def json_list_type(args, lst):
	"""
	  DEFAULT: This def takes a csv file and outputs a LIST of json objects:
	  [
		   {
			  "domain": "domain Archaea",
			  "phylum": "phylum Euryarchaeota",
			  "class": "class Halobacteria",
			  "order": "order Halobacteriales",
			  "family": "family Halobacteriaceae",
			  "genus": "genus Halalkalicoccus",
			  "species": "species jeotgali",
			  "domain_id": "2",
			  "phylum_id": "6",
			  "class_id": "3",
			  "order_id": "10",
			  "family_id": "7",
			  "genus_id": "5",
			  "species_id": "1017"
		   },
		   {
			  "domain": "domain Archaea",
			  "phylum": "phylum Euryarchaeota",
			  "class": "class Halobacteria",
	  ....
	  ]
	"""
	
	print_json(args, lst)
	
		
		
def json_obj_type(args, lst):
	"""
	  This def takes a csv file and outputs a JSON object for each domain:
	  [ {
		  "value": "domain Archaea",
		  "rank": "domain",
		  "id": "domain Archaea",
		  "items": [
			 {
				"value": "phylum Euryarchaeota",
				"rank": "phylum",
				"id": "phylum Euryarchaeota",
				"items": [
				   {
					  "value": "class Halobacteria",
					  "rank": "class",
					  "id": "class Halobacteria",
					  "items": [
	  .....
	  ]
	  
	  
	"""
	print('\n')
	newmasterList = []
	
	for n in range(len(lst)):
		
		#['Bacteria', 'Acidobacteria', 'Acidobacteriia', 'Acidobacteriales']
		
		
		nextList = []
		for m in range(len(ranks)): # 7
			tax_name = lst[n][m]
			
			if m==0:
				nextList = newmasterList
			if lst[n][m]:
				sid = ranks[m]+' '+ tax_name
				#sid= lst[n][m]
				#print('sid',sid,n,m)
				#print(nextList)
				c = find_if_in(nextList, sid)
					#print(c)
					#phylum_name = tax_rows[n][m]
				if c == []: # 
					obk = {}
					obk["value"] = sid
					obk["rank"] = ranks[m]
					obk["id"] = sid
					obk["count"] = '0'
					obk["items"] = []
					
					nextList.append(obk)
					nextList = obk["items"]
				else:
					nextList = c[0]['items']
	print_json(args, newmasterList)
	
	
def exclude_lineage(line):
	#lineage = ';'.join(line)
	#print(lineage)
	for l in bad_taxa:
		if l in line:
			print('found bad taxa: ',line)
			return True
	for l in bad_lineages:
		if l in line:
			print('found bad lineage: ',line)
			return True
	return False
	
					
def get_counts(gline):
	global counts
# 	for n in range(len(lst)):
# 		
# 		nextList = []
	if args.verbose:
		print('counts::parsing ',gline)
	for m in range(len(ranks)): # 7
		tax_name = gline[m]
		
		#counts = get_counts(counts,  m, lst[n])

		sumdtaxname = []
		for d in range(m+1):
			sumdtaxname.append(gline[d])
		long_tax_name = ';'.join(sumdtaxname)
		#print('long_tax_name ',long_tax_name)
		if  long_tax_name in counts:
			counts[long_tax_name] +=1
		else:
			counts[long_tax_name] = 1
	if args.verbose:
		print('returning: ',counts)
	return counts		
	
def print_json(args, listOjson):
	if args.outfile:
		#outFile = open(args.outfile, 'w')
		outFile = open(args.outfile, 'w')
		outFile.write(json.dumps(listOjson, indent = 3))
		
def find_if_in(obj, name):
	return [x for x in obj if x['value'] == name]   #if tax_rows[n][m] in myobj	
	
def create_list_obj(line, id_lst):
	new_obj ={}
			
	for n in range(7):
		#new_obj[ranks[n]] = ranks[n] +' '+ taxa_lst[n]
		new_obj[ranks[n]] = line[n]
	if id_lst:
		for n in range(7):
			new_obj[ranks[n]+'_id'] = id_lst[n]
	return new_obj
	
	
	
if __name__ == "__main__":
    import argparse
    usage = """
    USAGE: taxonomy_csv2json.py -i <tab separated taxonomy file direct from mysql>
            -euk/--include_euks   	::Default is to exclude Eukaryotes (for HOMD)
            -pt/--allow_partial_taxa  	::Default is to exclude taxa with empty tax_names 
                                     		( either '' or *_NA or empty_*)
            -o/--outfile  		::Default is out.json
            -genus/--meld_genus_sp 	::Default is to NOT combine genus and species (into Species)
            -of/--out_format  Either json_obj(default) or json_list
            
        Input file format: <TAB> separated list of tax names: domain p c o f g species
        == sample ==
        Bacteria	Acidobacteria
        Bacteria	Proteobacteria	Alphaproteobacteria
        Bacteria	Acidobacteria	Acidobacteriia	Acidobacteriales	Acidobacteriaceae	Acidobacterium	sp.
        Bacteria	Firmicutes	Clostridia	Clostridiales	Peptostreptococcaceae	Fusibacter	species_NA
        ====
               
    """
    
    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=True,  action="store",   dest = "infile", default='',
                                                    help="Uniqued and Sorted Fasta File ")
    parser.add_argument("-o", "--outfile",   required=False,  action="store",   dest = "outfile", default='out.json',
                                                    help="Uniqued and Sorted Fasta File ")                                               
    parser.add_argument("-pt", "--allow_partial_taxa",   required=False,  action="store_true",   dest = "allow_partial_taxa", default=False,
                                                    help="Exclude rows with any empty taxa => Default")
    parser.add_argument("-euk", "--include_euks",   required=False,  action="store_true",   dest = "include_euks", default=False,
                                                    help="Exclude Eukayotes => default") 
    parser.add_argument("-genus", "--meld_genus_sp",   required=False,  action="store_true",   dest = "meld_genus", default=False,
                                                    help="Meld genus and species into Species Name")                                                                                                 
    parser.add_argument("-of", "--out_format",   required=False,  action="store",   choices=['list', 'obj'], dest = "output_format", default='list',
                                                    help="Either: obj or list(default)")
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", default=False,
                                                    help="verbose print()")                                                
    args = parser.parse_args()                                                
    
    print(args)
    run(args)
    
    



