#!/usr/bin/env python

# see https://www.biostars.org/p/16262/
#  http://etetoolkit.org/docs/latest/tutorial/index.htmltrees 
# http://etetoolkit.org/docs/latest/tutorial/tutorial_ncbitaxonomy.html?highlight=ncbi

#import entrez module
from Bio import Entrez

# set variables
taxids = [515482, 515474]

# set email
Entrez.email = "avoorhis@mbl.edu"

# traverse ids
for taxid in taxids:
    handle = Entrez.efetch(db="taxonomy", id=taxid, mode="text", rettype="xml")
    records = Entrez.read(handle)
    for taxon in records:
        taxid = taxon["TaxId"]
        name = taxon["ScientificName"]
        tids = []
        for t in taxon["LineageEx"]:
            tids.insert(0, t["TaxId"])
        tids.insert(0, taxid)
        print("%s\t|\t%s\t|\t%s" % (taxid, name, " ".join(tids)))

