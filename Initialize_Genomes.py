#!/usr/bin/env python

## SEE https://docs.dhtmlx.com/suite/tree__api__refs__tree.html // new version 7 must load from json file
# this script creates a list of json objects that allows the dhtmlx javascript library
# to parse and show a taxonomy tree (Written for HOMD)

import os, sys
import json
import argparse
try:
    import mysqlclient as mysql
except ImportError:
    try:
        import pymysql as mysql
    except ImportError:
        import MySQLdb as mysql
import datetime
from datetime import datetime,date
ranks = ['domain','phylum','klass','order','family','genus','species']
today = str(date.today())


# TABLES
#update_date_tbl = 'static_genomes_update_date'  # this seems to be the LONG list of gids -- use it first then fill in
index_tbl       = 'HOMD_seqid_taxonid_index'   # match w/ otid OTID Not Unique 
seq_genomes_tbl = 'seq_genomes' #  has genus,species,status,#ofcontigs,combinedlength,flag,oralpathogen-+
seq_extra_tbl   = 'seq_genomes_extra' # has ncbi_id,ncbi_taxid,GC --and alot more

# first_query ="""
#     SELECT seq_id as gid, date
#     from {tbl}
#     ORDER BY gid
# """.format(tbl=update_date_tbl)
# 2
idx_query ="""   
    SELECT seq_id as gid,
    Oral_taxon_id as otid
    from {tbl}
    ORDER BY gid
""".format(tbl=index_tbl)
# 1
first_genomes_query ="""
    SELECT seq_id as gid,
    genus,
    species,
    status,
    number_contig as ncontigs,
    combined_length as tlength,
    oral_pathogen as oral_path,
    culture_collection as ccolct,
    sequence_center as seq_center
    from {tbl}
    ORDER BY gid
""".format(tbl=seq_genomes_tbl)
# 3
extra_query ="""
    SELECT seq_id as gid,
    ncbi_id,
    ncbi_taxon_id as ncbi_taxid,
    isolate_origin as io,
    GC as gc,
    atcc_medium_number as atcc_mn,
    non_atcc_medium as non_atcc_mn
    from {tbl}
    ORDER BY gid
""".format(tbl=seq_extra_tbl)

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

def create_genome(gid):  # basics - page1 Table: seq_genomes  seqid IS UNIQUE
    """  alternative to a Class which seems to not play well with JSON """
    genome = {}
    genome['gid'] 		= gid
    genome['genus'] 	= ''   # table 1
    genome['species'] 	= ''   # table 1
    genome['status']	= ''   # table 1
    genome['ncontigs'] 	= ''   # table 1
    genome['seq_center'] = ''   # table 1
    genome['tlength'] 	= ''   # table 1
    genome['oral_path'] = ''   # table 1
    genome['ccolct'] 	= ''  # table 1 --is a list but presented in a single (comma separated) field in the db
    
    genome['gc'] 		= ''   # table 2
    genome['ncbi_taxid'] = ''   # table 2
    genome['ncbi_id'] 	= ''   # table 2
    genome['io'] 		= ''   # table 2
    genome['atcc_mn'] 	= ''   # table 2
    genome['non_atcc_mn'] = ''   # table 2
    
    genome['otid'] 		= ''   # index table
    return genome

def create_genome2(gid):  # description - page2 Table: seq_genomes_extra
    """  alternative to a Class which seems to not play well with JSON 
    1 otid								#table1
    2  homd seqid						#table1
    3  genus species					#table1
    4  genome sequence name  # How is this different than genus-species?
    5  comments on name
    6  culture collection entry number  # table
    7  isolate origin   				# table2
    8  sequencing status   				# table
    9  ncbi taxid   					# table1
    10 ncbi genome bioproject id   		# table
    11 ncbi genome biosample id   		# table
    12 genbank acc id   				# table2
    13 genbank assbly id   				# table
    14 number of contigs and singlets	   # table
    15 combined lengths (bps)	   		# table
    16 GC percentage				   # table1
    17 sequencing center		   # table1
    18 ATCC medium number		   # table2
    19 non-ATCC medium			   # table2
    20 16s rna gene sequence		   # table  ????
    21 comments					   # table
    
    """
    genome = {}
    genome['gid'] 		= gid
    genome['otid'] 		= ''   #table 1
    genome['genus'] 	= ''   #table 1
    genome['species'] 	= ''   #table 1
    genome['date'] 		= ''     #used ??
    genome['status']	= ''  	#used ??
    genome['NCBI_taxid'] = ''   # table 
    genome['ncontigs'] = ''
    genome['gc'] 		= ''
    genome['tlength'] 	= ''
    genome['oral_path'] = ''
    genome['ccolct'] = ''  # is a list but presented in a single (comma separated) field in the db
    
    
master_lookup = {}    
# def run_first(args):
#     """ date not used: lets not query this table"""
#     global master_lookup
#     result = myconn.execute_fetch_select_dict(first_query)
#     
#     for obj in result:
#         print(obj)
#         
#         created_date = datetime.strptime(str(obj['date']), '%Y-%m-%d')
#         
#         if obj['gid'] not in master_lookup:
#             taxonObj = create_genome(obj['gid']) 
#             taxonObj['date'] = str(created_date)[:10]
#         else:
#             print('duplicate gid',obj['gid'])
#             sys.exit()
#         master_lookup[obj['gid']] = taxonObj
              
def run_first(args):
    """ date not used: lets not query this table"""
    global master_lookup
    result = myconn.execute_fetch_select_dict(first_genomes_query)
    
    for obj in result:
        #print(obj)
        
        if obj['gid'] not in master_lookup:
            taxonObj = create_genome(obj['gid']) 
            taxonObj['genus'] = obj['genus']
            taxonObj['species'] = obj['species']
            taxonObj['status'] = obj['status']
            taxonObj['ncontigs'] = obj['ncontigs']
            taxonObj['seq_center'] = obj['seq_center']
            taxonObj['tlength'] = obj['tlength']
            taxonObj['oral_path'] = obj['oral_path']
            taxonObj['ccolct'] = obj['ccolct']
            
        else:
            print('duplicate gid',obj['gid'])
            sys.exit()
        master_lookup[obj['gid']] = taxonObj    

def run_second(args):
    global master_lookup
    result = myconn.execute_fetch_select_dict(idx_query)
    
    for obj in result:  
        if obj['gid'] not in master_lookup:
            print('Adding an Empty genome this needs attention! (gid='+str(obj['gid'])+')  -Continuing')
            taxonObj = create_genome(obj['gid'])   # create an empty taxon object
            master_lookup[obj['gid']] = taxonObj
        else:
            master_lookup[obj['gid']]['otid'] = obj['otid'] 
            
    
        
def run_third(args):
    global master_lookup
    result = myconn.execute_fetch_select_dict(extra_query)    
    #seq_id as gid,genus,species,status,number_contig,combined_length,oral_path
        
    for obj in result:  
        if obj['gid'] not in master_lookup:
            print('Adding an Empty genome this needs attention! (gid='+str(obj['gid'])+')  -Continuing')
            taxonObj = create_genome(obj['gid'])   # create an empty taxon object
            master_lookup[obj['gid']] = taxonObj
        

        for n in obj:
            if n == 'gc':
                master_lookup[obj['gid']]['gc'] = obj['gc']
            if n == 'ncbi_taxid':
                master_lookup[obj['gid']]['ncbi_taxid'] = obj['ncbi_taxid']
            if n == 'ncbi_id':
                master_lookup[obj['gid']]['ncbi_id'] = obj['ncbi_id']
            if n == 'io':
                master_lookup[obj['gid']]['io'] = obj['io']
            if n == 'atcc_mn':
                master_lookup[obj['gid']]['atcc_mn'] = obj['atcc_mn']
            if n == 'non_atcc_mn':
                master_lookup[obj['gid']]['non_atcc_mn'] = obj['non_atcc_mn']
           
            	
    with open(os.path.join(args.outdir,args.outfileprefix+'_lookup.json'), 'w') as outfile1:
        json.dump(master_lookup, outfile1, indent=args.indent)
        
            
if __name__ == "__main__":

    usage = """
    USAGE:
        homd_init_genome_data.py
        
        will print out the need initialization files for homd
        Needs MySQL: tries to read your ~/.my.cnf_node
        
           -outdir Output directory [default]
        for homd site
           -host homd
           
        for debugging
          -pp  pretty print
          -o <outfile>  Change outfile name from 'taxonomy'*
        
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=False,  action="store",   dest = "infile", default='none',
                                                    help=" ")
    parser.add_argument("-o", "--outfileprefix",   required=False,  action="store",   dest = "outfileprefix", default='homd_genome',
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
        args.NODE_DATABASE = 'HOMD_genomes_new'
        dbhost = '192.168.1.51'
        args.outdir = '../homd-startup-data/'
        args.prettyprint = False
        
    elif args.dbhost == 'localhost':  #default
        args.NODE_DATABASE = 'HOMD_genomes_new'
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
    run_second(args)
    run_third(args)
    