#!/usr/bin/env python

## SEE https://docs.dhtmlx.com/suite/tree__api__refs__tree.html // new version 7 must load from json file
# this script creates a list of json objects that allows the dhtmlx javascript library
# to parse and show a taxonomy tree (Written for HOMD)
##
import os, sys
import json
#from json import JSONEncoder
import argparse
#import ast
try:
    import mysqlclient as mysql
except ImportError:
    try:
        import pymysql as mysql
    except ImportError:
        import MySQLdb as mysql
import datetime
ranks = ['domain','phylum','klass','order','family','genus','species']
today = str(datetime.date.today())

# TABLES
taxon_tbl           = 'taxon_list'   # UNIQUE  - This is the defining table 



master_tax_lookup={}



query_taxa ="""
SELECT a.oral_taxon_id as otid, a.genus as genusTT, a.species as speciesTT
from {tbl} as a

ORDER BY otid
""".format(tbl=taxon_tbl)


counts = {}
tt_lookup = {}
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
    
    def execute_fetch_one(self, sql):
        if self.cursor:
            try:
                self.cursor.execute(sql)
                self.conn.commit()
                return self.cursor.fetchone()
            except:
                print("ERROR: query = %s" % sql)
                raise
    def execute_fetch_select(self, sql):
        if self.cursor:
            try:
                self.cursor.execute(sql)
                self.conn.commit()
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
                self.conn.commit()
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



            
            



    
# def print_dict(filename, dict):
#     with open(filename, 'w') as outfile:
#         json.dump(dict, outfile, indent=args.indent)
    


def run_site(args):
    """
   
        
    """
    global full_tax_lookup
    
        
    q1 = "select Oral_taxon_id as otid, site from  taxonid_site"
    q2 = "SELECT site,site_id from site"
    
    site_result = myconn_new.execute_fetch_select_dict(q2)
    print(site_result)
    site_lookup = {}
    for obj in site_result:
        site_lookup[obj['site']] = obj['site_id']
    otid_result = myconn_tax.execute_fetch_select_dict(q1)
    full_tax_list = []
    full_tax_lookup = {}
    collector = []
    for obj in otid_result:
        # for each otid build up the taxonomy from species => domain
        print(obj)
        #lst = [str(obj['otid']),str(site_lookup[obj['site']])]
        q3 = "INSERT IGNORE into otid_site (otid, site_id) VALUES"
        q3 += "('"+str(obj['otid'])+"',"+"'"+str(site_lookup[obj['site']])+"')"  
        
        myconn_new.execute_no_fetch(q3) 
        q4 = "SELECT LAST_INSERT_ID()"
        last_id = myconn_new.execute_fetch_one(q4) 
        if last_id[0] == 0:
            # failed to insert: 
            print(obj['otid']) 
     
    
def run_strain(args):
    
    q1 = "select Oral_taxon_id as otid, type_strain from  1_type_strain"
    
        
    otid_result = myconn_tax.execute_fetch_select_dict(q1)
    full_tax_list = []
    full_tax_lookup = {}
    collector = []
    for obj in otid_result:
        # for each otid build up the taxonomy from species => domain
        print(obj)
        #lst = [str(obj['otid']),str(site_lookup[obj['site']])]
        q2 = "INSERT IGNORE into type_strain (type_strain) VALUES ('"+obj['type_strain']+"')"
        print(q2)
        myconn_new.execute_no_fetch(q2) 
        q3 = "SELECT LAST_INSERT_ID()"
        last_id = myconn_new.execute_fetch_one(q3) 
        if last_id[0] == 0: ## already in table
            q4 = "SELECT type_strain_id from type_strain where type_strain ='"+obj['type_strain']+"'"
            print(q4)
            result = myconn_new.execute_fetch_one(q4)
            ts_id = result[0]
        else:
            ts_id = last_id[0] 
        q5 = "INSERT IGNORE into otid_type_strain (otid, type_strain_id) VALUES"
        q5 += "('"+str(obj['otid'])+"',"+"'"+str(ts_id)+"')"  
        print(q5)
        myconn_new.execute_no_fetch(q5) 
        
def ncbi_taxid(args):
    q1 = "select Oral_taxon_id as otid, NCBI_taxon_id from  1_ncbi_taxonomy"
    
        
    otid_result = myconn_tax.execute_fetch_select_dict(q1)
    full_tax_list = []
    full_tax_lookup = {}
    collector = []
    for obj in otid_result:
        # for each otid build up the taxonomy from species => domain
        print(obj)
        #lst = [str(obj['otid']),str(site_lookup[obj['site']])]
        q2 = "UPDATE otid_prime set NCBI_taxon_id='"+str(obj['NCBI_taxon_id'])+"' WHERE otid ='"+str(obj['otid'])+"'"
        print(q2)
        myconn_new.execute_no_fetch(q2) 
        

if __name__ == "__main__":

    usage = """
    USAGE:
        takes the taxonomy from the old homd to the new
        
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=False,  action="store",   dest = "infile", default='none',
                                                    help=" ")
    parser.add_argument("-o", "--outfileprefix",   required=False,  action="store",   dest = "outfileprefix", default='homd_data',
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
    #parser.print_help(usage)
    if not os.path.exists(args.outdir):
        print("\nThe out put directory doesn't exist:: using the current dir instead\n")
        args.outdir = './'                         
    if args.dbhost == 'homd':
        #args.json_file_path = '/groups/vampsweb/vamps/nodejs/json'
        args.TAX_DATABASE = 'HOMD_taxonomy'
        args.NEW_DATABASE = 'homdAV'
        dbhost = '192.168.1.51'
        args.outdir = '../homd-startup-data/'
        args.prettyprint = False

    elif args.dbhost == 'localhost':
        #args.json_file_path = '/Users/avoorhis/programming/homd-data/json'
        args.TAX_DATABASE  = 'HOMD_taxonomy'
        args.NEW_DATABASE = 'homdAV'
        dbhost = 'localhost'
    else:
        sys.exit('dbhost - error')
    args.indent = None
    if args.prettyprint:
        args.indent = 4
    myconn_tax = MyConnection(host=dbhost, db=args.TAX_DATABASE,   read_default_file = "~/.my.cnf_node")
    myconn_new = MyConnection(host=dbhost, db=args.NEW_DATABASE,  read_default_file = "~/.my.cnf_node")

    print(args)
    print('run_taxa(args)')
    #run_site(args)
    #run_strain(args)
    ncbi_taxid(args)
    
    
    