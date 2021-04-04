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
import copy
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
	master_obj = {}
	master_obj['id'] = 0
	master_obj['item'] = []
	arc = {'id':1,'text':"Archaea",'parent':"0",'child':"1","item":[]}
	bac = {'id':2,'text':"Bacteria",'parent':"0",'child':"1","item":[]}
	master_obj['item'].append(arc)
	master_obj['item'].append(bac)
	#print(result)
	domain_dict={}
	
	
	# {id:0,
# 		item:[
# 			{id:1,text:"first"},
# 			{id:2, text:"middle",child:"1",im0:"book.gif",
# 				item:[
# 					{id:"21", text:"child"}
# 				]},
# 			{id:3,text:"last"}
# 		]
# 	}
	
	ranks = ['domain', 'phylum', 'klass', 'order', 'family', 'genus','species']
	
	
	tempresult =[
	{'otid': 1, 'domain': 'Bacteria', 'phylum': 'Proteobacteria', 'klass': 'Alphaproteobacteria', 'order': 'Rhizobiales', 'family': 'Bartonellaceae', 'genus': 'Bartonella', 'species': 'schoenbuchensis'},
	{'otid': 99,'domain': 'Bacteria', 'phylum': 'Firmicutes', 'klass': 'Clostridia', 'order': 'Clostridiales', 'family': 'Peptostreptococcaceae [XI]', 'genus': 'Mogibacterium', 'species': 'vescum'},
	{'otid': 2, 'domain': 'Bacteria', 'phylum': 'Proteobacteria', 'klass': 'Alphaproteobacteria', 'order': 'Caulobacterales', 'family': 'Caulobacteraceae', 'genus': 'Caulobacter', 'species': 'sp. oral taxon 002'}
	]
	tempresult2 =[
	{'otid': 1, 'domain': 'Bacteria', 'phylum': 'Proteobacteria', 'klass': 'Alphaproteobacteria', 'order': 'Rhizobiales' },
	{'otid': 99,'domain': 'Bacteria', 'phylum': 'Firmicutes',     'klass': 'Clostridia',         'order': 'Clostridiales'},
	{'otid': 2, 'domain': 'Bacteria', 'phylum': 'Proteobacteria', 'klass': 'Alphaproteobacteria', 'order': 'Caulobacterales'}
	]
	tempresult3 =[
	{'otid': 1, 'domain': 'Bacteria', 'phylum': 'Proteobacteria', 'klass': 'Alphaproteobacteria' },
	{'otid': 99,'domain': 'Arturo', 'phylum': 'Firmicutes',     'klass': 'Clostridia'   },
	{'otid': 2, 'domain': 'Bacteria', 'phylum': 'hemo',         'klass': 'Alphaproteobacteria'}
	]
	new_obj ={}
	new_obj['id']='0'
	new_obj['item']=[]
	
	for obj in result:
		#print(obj)
		otid = obj['otid']
		
		lst1 = new_obj['item']
		level1 = 1+int(len(lst1))
		[index,foundobj] = find_if_present(lst1, obj['domain'])
		if foundobj:
			# already written
			idx1 = index
		else:	
			mtobj = create_empty_obj(obj['domain'],level1,'domain')
			lst1.append(mtobj)
			idx1 = len(lst1) - 1
			
		lst2 = new_obj['item'][idx1]['item']
		level2=str(2)+str(len(lst2)+1)
		[index,foundobj] = find_if_present(lst2, obj['phylum'])
		if foundobj:
			idx2 = index
		else:
			mtobj = create_empty_obj(obj['phylum'], level2, 'phylum')
			lst2.append(mtobj)
			idx2 = len(lst2) - 1
			
		lst3 = new_obj['item'][idx1]['item'][idx2]['item']
		level3 = str(3)+str(len(lst3)+1)
		[index,foundobj] = find_if_present(lst3, obj['klass'])
		if foundobj:
			idx3 = index
		else:
			mtobj = create_empty_obj(obj['klass'],level3,'klass')
			
			lst3.append(mtobj)
			idx3 = len(lst3) - 1
			
		lst4 = new_obj['item'][idx1]['item'][idx2]['item'][idx3]['item']
		level4 = str(4)+str(len(lst4)+1)
		[index,foundobj] = find_if_present(lst4, obj['order'])
		if foundobj:
			idx4 = index
		else:
			mtobj = create_empty_obj(obj['order'],level4,'order')
			lst4.append(mtobj)
			idx4 = len(lst4) - 1
		
		lst5 = new_obj['item'][idx1]['item'][idx2]['item'][idx3]['item'][idx4]['item']
		level5 = str(5)+str(len(lst5)+1)
		[index,foundobj] = find_if_present(lst5, obj['family'])
		if foundobj:
			idx5 = index
		else:
			mtobj = create_empty_obj(obj['family'],level5,'family')
			lst5.append(mtobj)
			idx5 = len(lst5) - 1
			
		lst6 = new_obj['item'][idx1]['item'][idx2]['item'][idx3]['item'][idx4]['item'][idx5]['item']
		level6 = str(6)+str(len(lst6)+1)
		[index,foundobj] = find_if_present(lst6, obj['genus'])
		if foundobj:
			idx6 = index
		else:
			mtobj = create_empty_obj(obj['genus'],level6,'genus')
			lst6.append(mtobj)
			idx6 = len(lst6) - 1
			
		lst7 = new_obj['item'][idx1]['item'][idx2]['item'][idx3]['item'][idx4]['item'][idx5]['item'][idx6]['item']
		level7 = str(7)+str(len(lst7)+1)
		[index,foundobj] = find_if_present(lst7, obj['species'])
		if foundobj:
			idx7 = index
		else:
			mtobj = create_empty_obj(obj['species'],level7,'species')
			mtobj['otid'] = otid
			mtobj['child'] = "0"
			lst7.append(mtobj)
			idx7 = len(lst7) - 1
			
			
	print(json.dumps(new_obj, indent = 1))		
	with open(args.outfile, 'w') as outfile2:
 		json.dump(new_obj, outfile2, indent=args.indent)		
			
def create_empty_obj(name, id, rank):
	obj = {
	"id":   id,
	"text": name,
	"rank": rank,
	'child':'1'
	}
	if rank != 'species':
		obj['item'] = []
	return obj	
		

		

def find_if_present(lst, taxname):
	n=0
	for obj in lst:
		#ßprint('n',obj)
		if obj['text'] == taxname:
			id= obj['id']
			return [n, obj]
			n+=1
	return [0,{}]


		

	
if __name__ == "__main__":
    import argparse
    usage = """
    USAGE: 
    	NOT USED
       prints out a json object
       compatible with DHTMLX Tree But it is not used
       because we are using dynamic loading
       using the file ??? created by homd_init_data.py
               
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
    
    



