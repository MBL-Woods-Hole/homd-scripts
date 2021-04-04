#!/usr/bin/env python

## SEE https://docs.dhtmlx.com/suite/tree__api__refs__tree.html // new version 7 must load from json file
# this script creates a list of json objects that allows the dhtmlx javascript library
# to parse and show a taxonomy tree (Written for HOMD)

import os, sys
import json
ranks = ['domain','phylum','klass','order','family','genus','species']
homd_bac_phyla = [ 'Absconditabacteria',
 'Actinobacteria',
 'Bacteroidetes',
 'Chlamydiae',
 'Chlorobi',
 'Chloroflexi',
 'Cyanobacteria',
 'Firmicutes',
 'Fusobacteria',
 'Gracilibacteria',
 'Proteobacteria',
 'Saccharibacteria',
 'Spirochaetes',
 'Synergistetes',
 'WPS-2']
homd_arc_phyla =['Euryarchaeota']
# ['Bacteria', 'Acidobacteria', 'Acidobacteriia', 'Acidobacteriales', 'Acidobacteriaceae', 'Acidobacterium']

masterList = []
#domains = []

# [{bacteria:
# 
# }]
def run(args):
	

	csv_fh = open(args.infile,'r')
	for line in csv_fh:
		line = line.strip()
		good_line = []
			
		if not line:
			continue
		line = line.split("\t")
		
		if len(line) == 0:  
			continue
		taxa_lst = line[:7]
		id_lst = line[7:]
		if  not args.include_euks and taxa_lst[0][:6] == 'Eukary':
			print('excluding(euks)',taxa_lst)
			continue
		#print(line)
		#line = [x for x in line if '_NA' not in x]
		if len(taxa_lst) > len(ranks):                 
			print('excluding(too long)',taxa_lst)
			continue
		if len(taxa_lst) < len(ranks):
			print(taxa_lst)
			print('excluding(too short)',taxa_lst)
			continue
		
		
		# exclude some phyla
		# if taxa_lst[1] in (homd_bac_phyla + homd_arc_phyla):
# 			pass
# 		else:
# 			print('excluding(phylum)',taxa_lst)
# 			continue
		
		
		if args.allow_partial_taxa:
			# add everything
			#tax_rows.append(line)
			good_line = taxa_lst
			
		else:
			#print(line)
			#print( any('_NA' in s for s in line) )
			#line = [x for x in line if '_NA' not in x]
			exclusions = ['', 'empty_', '_NA']
			if '' in taxa_lst:
				print("excluding('')",taxa_lst)
				
			elif any('empty_' in s for s in taxa_lst):
				print('excluding(empty_)',taxa_lst)
				
			elif any('_NA' in s for s in taxa_lst):
				print('excluding(_NA)',taxa_lst)
				
			else:
				good_line = taxa_lst
				
		
		#print(taxa_lst)
		#print(id_lst)
		if args.meld_genus and (taxa_lst[5] != '' or taxa_lst[6] != ''):
			taxa_lst[6] = taxa_lst[5] +' '+taxa_lst[6]
		#print(good_line)	
		counts = {}
		
		
		if good_line:
			
			if args.output_format == 'json_list':
				masterList.append(create_list_obj(taxa_lst, id_lst))
			else:
				masterList.append(taxa_lst)
	#print('good',taxJSONList)
	print('out format ',args.output_format)
	if args.output_format == 'json_list':
		list_type(args, masterList)
	else:
		json_type(args, masterList)

		
	
	
def list_type(args, lst):
	"""
	  This def takes a csv file and outputs a LIST of json objects:
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
	"""
	print_json(args, lst)
	
		
		
def json_type(args, lst):
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
		print('good row: ',lst[n])
		#['Bacteria', 'Acidobacteria', 'Acidobacteriia', 'Acidobacteriales']
		
		
		nextList = []
		for m in range(len(ranks)): # 7
			if m==0:
				nextList = newmasterList
			if lst[n][m]:
				sid = ranks[m]+' '+lst[n][m]
				sid= lst[n][m]
				print('sid',sid,n,m)
				print(nextList)
				c = find_if_in(nextList, sid)
					#print(c)
					#phylum_name = tax_rows[n][m]
				if c == []: # 
					obk = {}
					obk["value"] = sid
					obk["rank"] = ranks[m]
					obk["id"] = sid
					obk["items"] = []
					nextList.append(obk)
					nextList = obk["items"]
				else:
					nextList = c[0]['items']
	print_json(args, newmasterList)
	
				
	
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
                                                    help="Exclude rows with any empty taxa. Default")
    parser.add_argument("-euk", "--include_euks",   required=False,  action="store_true",   dest = "include_euks", default=False,
                                                    help="Exclude Eukayotes") 
    parser.add_argument("-genus", "--meld_genus_sp",   required=False,  action="store_true",   dest = "meld_genus", default=False,
                                                    help="Meld genus and species into Species Name")                                                                                                 
    parser.add_argument("-of", "--out_format",   required=False,  action="store",   dest = "output_format", default='json_obj',
                                                    help="Either: json_obj(default) or json_list")
    args = parser.parse_args()                                                
    
    print(args)
    run(args)
    sys.exit()
    
    if args.output_format == 'json_list':
    	run_list(args)
    else:
    	run_obj(args)                                                
    

    



