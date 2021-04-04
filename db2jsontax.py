#!/usr/bin/env python

## SEE https://docs.dhtmlx.com/suite/tree__api__refs__tree.html // new version 7 must load from json file
# this script creates a list of json objects that allows the dhtmlx javascript library
# to parse and show a taxonomy tree (Written for HOMD)

import os, sys
import json
try:
    import mysqlclient as mysql
except ImportError:
    try:
        import pymysql as mysql
    except ImportError:
        import MySQLdb as mysql
import datetime
ranks = ['domain','phylum','klass','order','family','genus','species']

masterList = []
counts = {}
#domains = []
query = """
SELECT oral_taxon_id as otid,Domain as domain,Phylum as phylum,Class as klass,`Order` as `order`,Family as family,Genus as genus,Species as species
from original_taxontable
ORDER BY oral_taxon_id

"""

class MyConnection:
    """
    Takes parameters from ~/.my.cnf, default host = "localhost", db="test"
    if different use my_conn = MyConnection(host, db)
    """

    def __init__(self, host = "localhost", db="test", read_default_file = ""):
        # , read_default_file=os.path.expanduser("~/.my.cnf"), port = 3306

        self.conn = None
        self.cursor = None
        self.cursorD = None
        self.rows = 0
        self.new_id = None
        self.lastrowid = None

        port_env = 3306
        try:
            print("host = " + str(host) + ", db = "+str(db))
            print("=" * 40)
            read_default_file = os.path.expanduser("~/.my.cnf_node")

            if is_local():
                host = "127.0.0.1"
                read_default_file = "~/.my.cnf_node"
            self.conn = mysql.connect(host = host, db = db, read_default_file = read_default_file, port = port_env)
            self.cursor = self.conn.cursor()
            self.cursorD = self.conn.cursor(mysql.cursors.DictCursor)

        except (AttributeError, mysql.OperationalError):
            self.conn = mysql.connect(host = host, db = db, read_default_file = read_default_file, port = port_env)
            self.cursor = self.conn.cursor()
        except mysql.Error:
            e = sys.exc_info()[1]
            print("Error %d: %s" % (e.args[0], e.args[1]))
            raise
        except:  # catch everything
            print("Unexpected:")
            print(sys.exc_info()[0])
            raise  # re-throw caught exception

    @staticmethod
    def connect(host, db, read_default_file, port_env):
        print('host ',host,' db ',db)
        return mysql.connect(host = host, db = db, read_default_file = read_default_file, port = port_env)

    def execute_fetch_select(self, sql):
        if self.cursor:
            try:
                self.cursor.execute(sql)
                return self.cursor.fetchall()
            except:
                print("ERROR: query = %s" % sql)
                raise

    def execute_no_fetch(self, sql):
        if self.cursor:
            self.cursor.execute(sql)
            self.conn.commit()
            try:
                return self.cursor._result.message
            except:
                return self.cursor._info

    def execute_fetch_select_dict(self, sql):
        if self.cursorD:
            try:
                self.cursorD.execute(sql)
                return self.cursorD.fetchall()
            except:
                print("ERROR: query = %s" % sql)
                raise
def is_local():
    print(os.uname()[1])
    dev_comps = ['avoorhis.mbl.edu', "Joannes-MacBook-Air.local"]
    if os.uname()[1] in dev_comps:
        return True
    else:
        return False

def run(args):
	global counts
	result = myconn.execute_fetch_select_dict(query)
	taxon_list = []
	#print(result)
	
	
	#with open(args.outfile, 'w') as outfile2:
	#	json.dump(result, outfile2, indent=args.indent)

	for obj in result:
		newobj={}
		newobj['otid'] = obj['otid']
		newobj['domain'] = obj['domain']
		newobj['phylum'] = obj['phylum']
		newobj['klass'] = obj['klass']
		newobj['order'] = obj['order']
		newobj['family'] = obj['family']
		newobj['genus'] = obj['genus']
		if args.meld_genus:
			newobj['species'] = obj['genus']+' '+obj['species']
		else:
			newobj['species'] = obj['species']
		taxon_list.append(newobj)
		
	with open(args.outfile, 'w') as outfile2:
		json.dump(taxon_list, outfile2, indent=args.indent)

		
	
	

		

	
	
	
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

    parser.add_argument("-o", "--outfile",   required=False,  action="store",   dest = "outfile", default='out.json',
                                                    help="Uniqued and Sorted Fasta File ")                                               
    parser.add_argument("-pt", "--allow_partial_taxa",   required=False,  action="store_true",   dest = "allow_partial_taxa", default=False,
                                                    help="Exclude rows with any empty taxa => Default")
    
    parser.add_argument("-genus", "--meld_genus_sp",   required=False,  action="store_true",   dest = "meld_genus", default=True,
                                                    help="Meld genus and species into Species Name")                                                                                                 
    parser.add_argument("-of", "--out_format",   required=False,  action="store",   choices=['list', 'obj'], dest = "output_format", default='list',
                                                    help="Either: obj or list(default)")
    parser.add_argument("-v", "--verbose",   required=False,  action="store_true",    dest = "verbose", default=False,
                                                    help="verbose print()") 
    parser.add_argument("-host", "--host",
                        required = False, action = 'store', dest = "dbhost", default = 'localhost',
                        help = "choices=['homd',  'localhost']")                                                
    parser.add_argument("-pp", "--prettyprint",
                        required = False, action = 'store_true', dest = "prettyprint", default = False,
                        help = "output file is human friendly")
                        
                        
                                                                                                                       
    args = parser.parse_args()                                                
    if args.dbhost == 'homd':
        args.json_file_path = '/groups/vampsweb/vamps/nodejs/json'
        args.NODE_DATABASE = 'HOMD_taxonomy_20210202'
        dbhost = '192.168.1.30'

    elif args.dbhost == 'localhost':
        args.json_file_path = '/Users/avoorhis/programming/homd-data/json'
        args.NODE_DATABASE = 'HOMD_taxonomy_20210202'
        dbhost = 'localhost'
    args.indent = None
    if args.prettyprint:
        args.indent = 4
    myconn = MyConnection(host=dbhost, db=args.NODE_DATABASE,  read_default_file = "~/.my.cnf_node")
#     req_query = "SELECT oral_taxon_id from taxon_list"
#     data = myconn.connect(host=args.dbhost, db=args.NODE_DATABASE, read_default_file = "~/.my.cnf_node", port_env = 3306)
#     print(myconn.execute_fetch_select(req_query))
#     sys.exit()
    print(args)
    run(args)
    
    



