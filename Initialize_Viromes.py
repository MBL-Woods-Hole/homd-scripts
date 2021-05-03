#!/usr/bin/env python

## SEE https://docs.dhtmlx.com/suite/tree__api__refs__tree.html // new version 7 must load from json file
# this script creates a list of json objects that allows the dhtmlx javascript library
# to parse and show a taxonomy tree (Written for HOMD)

import os, sys
import json
import argparse

import datetime
from datetime import datetime,date
ranks = ['domain','phylum','klass','order','family','genus','species']
today = str(date.today())
from connect import MyConnection

# TABLES
#update_date_tbl = 'static_genomes_update_date'  # this seems to be the LONG list of gids -- use it first then fill in
#index_tbl       = 'seqid_otid_index'   # match w/ otid OTID Not Unique 
#seq_genomes_tbl = 'seq_genomes' #  has genus,species,status,#ofcontigs,combinedlength,flag,oralpathogen-+
#seq_extra_tbl   = 'seq_genomes_extra' # has ncbi_id,ncbi_taxid,GC --and alot more

first_query ="""
    SELECT virus_id as vid, Assembly_NCBI,SRA_Accession_NCBI,Submitters_NCBI,Release_Date_NCBI,	
	Family_NCBI,Genus_NCBI,Species_NCBI,Molecule_type_NCBI,Sequence_Type_NCBI,Geo_Location_NCBI,
	USA_NCBI,Host_NCBI,Isolation_Source_NCBI,Collection_Date_NCBI,BioSample_NCBI,GenBank_Title_NCBI	
    from virus_data1
    ORDER BY vid
"""




def create_virome(vid):  # basics - page1 Table: seq_genomes  seqid IS UNIQUE
    """  alternative to a Class which seems to not play well with JSON 
    
    virus_id	int(11) unsigned	NO	PRI	NULL	auto_increment
	Assembly_NCBI	varchar(50)	NO			
	SRA_Accession_NCBI	varchar(100)	NO			
	Submitters_NCBI	text	YES		NULL	
	Release_Date_NCBI	varchar(50)	YES		NULL	
	Family_NCBI	varchar(50)	YES		NULL	
	Genus_NCBI	varchar(50)	YES		NULL	
	Species_NCBI	varchar(100)	YES		NULL	
	Molecule_type_NCBI	varchar(50)	YES		NULL	
	Sequence_Type_NCBI	varchar(50)	YES		NULL	
	Geo_Location_NCBI	varchar(100)	YES		NULL	
	USA_NCBI	varchar(10)	YES		NULL	
	Host_NCBI	varchar(100)	YES		NULL	
	Isolation_Source_NCBI	varchar(100)	YES		NULL	
	Collection_Date_NCBI	varchar(100)	YES		NULL	
	BioSample_NCBI	varchar(20)	YES		NULL	
	GenBank_Title_NCBI	varchar(100)	YES		NULL	
	KK_Host_standardized_name	varchar(50)	YES		NULL	
	KK_On_2021_109_initialization_list	varchar(20)	YES		NULL	
    """
    genome = {}
    genome['vid'] 		= vid
    genome['family_ncbi'] = ''  
    genome['genus_ncbi'] 	= ''   # 
    genome['species_ncbi'] 	= ''   #
    genome['assembly_ncbi']	= ''   # 
    genome['sra_accession_ncbi'] 	= ''   #
    #genome['submitters_ncbi'] = ''   # 
    genome['release_date_ncbi'] 	= ''   # 
    genome['molecule_type_ncbi'] 	= ''  # 
    genome['sequence_type_ncbi'] 		= ''   # table 2
    #qgenome['geo_location_ncbi'] = ''   # table 2
    #genome['usa_ncbi'] 	= ''   # table 2
    genome['host_ncbi'] = ''
    genome['isolation_source_ncbi'] 		= ''   # table 2
    genome['collection_date_ncbi'] 	= ''   # table 2
    genome['biosample_ncbi'] = ''   # table 2
    genome['genbank_title_ncbi'] 	= ''
    
    return genome


    
    
master_lookup = {}    

              
def run_first(args):
    """ date not used"""
    global master_lookup
    result = myconn.execute_fetch_select_dict(first_query)
    lst = []
    for obj in result:
        vid = str(obj['vid'])
        vobj = create_virome(vid)
        
        
        # use vobj to screen out from full mysql query
        obj_lower =  {k.lower(): v for k, v in obj.items() if k.lower() in vobj.keys()}
        # [f(x) for x in sequence if condition]
        lst.append(obj_lower)
        master_lookup[vid] = {}
        for n in obj_lower:
            if n in vobj:
                master_lookup[vid][n] = obj_lower[n]
        
        
          
    file1 = os.path.join(args.outdir,args.outfileprefix+'_lookup.json')
    file2 = os.path.join(args.outdir,args.outfileprefix+'_list.json')
    print('writing',file1)
    with open(file1, 'w') as outfile1:
        json.dump(master_lookup, outfile1, indent=args.indent)
    print('writing',file2)
    with open(file2, 'w') as outfile1:
        json.dump(lst, outfile1, indent=args.indent)    
            
if __name__ == "__main__":

    usage = """
    USAGE:
        homd_init_virome_data.py
        
       
        
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=False,  action="store",   dest = "infile", default='none',
                                                    help=" ")
    parser.add_argument("-o", "--outfileprefix",   required=False,  action="store",   dest = "outfileprefix", default='homd_virome',
                                                    help=" ")
    parser.add_argument("-outdir", "--out_directory", required = False, action = 'store', dest = "outdir", default = './',
                         help = "Not usually needed if -host is accurate")
    parser.add_argument("-host", "--host",
                        required = False, action = 'store', dest = "dbhost", default = 'localhost',
                        help = "choices=['homd',  'localhost']")
    parser.add_argument("-pp", "--prettyprint",
                        required = False, action = 'store_true', dest = "prettyprint", default = False,
                        help = "output file is human friendly")
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", default=False,
                                                    help="verbose print()") 
    args = parser.parse_args()
    
    if not os.path.exists(args.outdir):
        print("\nThe out put directory doesn't exist:: using the current dir instead\n")
        args.outdir = './'                         
    if args.dbhost == 'homd':
        args.DATABASE  = 'homdAV'
        dbhost = '192.168.1.51'
        args.outdir = '../homd-startup-data/'
        args.prettyprint = False
        
    elif args.dbhost == 'localhost':  #default
        args.NODE_DATABASE = 'homdAV'
        dbhost = 'localhost'
    else:
    	sys.exit('dbhost - error')
    args.indent = None
    if args.prettyprint:
        args.indent = 4
    print()
    myconn = MyConnection(host=dbhost, db=args.NODE_DATABASE,  read_default_file = "~/.my.cnf_node")

    print(args)
    run_first(args)
    # run_second(args)
#     run_third(args)
    