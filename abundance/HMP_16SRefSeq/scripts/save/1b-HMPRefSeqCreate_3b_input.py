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
sys.path.append('/Users/avoorhis/programming/')
sys.path.append('/Users/avoorhis/programming/homd-data/')
#from connect import MyConnection,mysql
import datetime
import requests
global mysql_errors
mysql_errors = []
"""

"""
today = str(datetime.date.today())


#['_997', '995.2', '', '997', '1017', 'HOMD', 'HMT-997', 'Bacteria', 'Gracilibacteria_(GN02)', 'Gracilibacteria_(GN02)_[C-1]', 'Gracilibacteria_(GN02)_[O-1]', 'Gracilibacteria_(GN02)_[F-1]', 'Gracilibacteria_(GN02)_[G-4]', 'bacterium_HMT_997', 'NCBI', '363464', 'Bacteria', 'Candidatus Gracilibacteria', 'NA', 'NA', 'NA', 'NA', 'NA', '', '', 'NCBI', '363464', 'HMT-997', 'Bacteria', 'Candidatus Gracilibacteria (GN02)', 'Gracilibacteria_[C-1]', 'Gracilibacteria_[O-1]', 'Gracilibacteria_[F-1]', 'Gracilibacteria_[G-4]', 'bacterium_HMT_997', 'y']
ranks = ['domain','phylum','klass','order','family','genus','species']
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

HC = {}  # for Hand Curate
HC['Bacteria;Actinobacteria;Actinobacteria;Actinomycetales;Actinomycetaceae;Actinomyces;graevenitzii'] = '866'
HC['Bacteria;Actinobacteria;Actinobacteria;Actinomycetales;Actinomycetaceae;Actinomyces;johnsonii'] = '849'
HC['Bacteria;Actinobacteria;Actinobacteria;Actinomycetales;Actinomycetaceae;Actinomyces;massiliensis'] = '852'
HC['Bacteria;Actinobacteria;Actinobacteria;Actinomycetales;Actinomycetaceae;Actinomyces;naeslundii'] = '176'
HC['Bacteria;Actinobacteria;Actinobacteria;Actinomycetales;Actinomycetaceae;Actinomyces;oris'] = '893'
HC['Bacteria;Actinobacteria;Actinobacteria;Actinomycetales;Actinomycetaceae;Schaalia;georgiae'] = '617'
HC['Bacteria;Actinobacteria;Actinobacteria;Actinomycetales;Actinomycetaceae;Schaalia;meyeri'] = '671'
HC['Bacteria;Actinobacteria;Actinobacteria;Actinomycetales;Micrococcaceae;Rothia;aeria'] = '188'
HC['Bacteria;Actinobacteria;Actinobacteria;Actinomycetales;Micrococcaceae;Rothia;dentocariosa'] = '587'
HC['Bacteria;Actinobacteria;Actinobacteria;Actinomycetales;Micrococcaceae;Rothia;mucilaginosa'] = '681'
HC['Bacteria;Actinobacteria;Actinobacteria;Corynebacteriales;Corynebacteriaceae;Corynebacterium;durum'] = '595'
HC['Bacteria;Actinobacteria;Actinobacteria;Corynebacteriales;Corynebacteriaceae;Corynebacterium;matruchotii'] = '666'
HC['Bacteria;Actinobacteria;Actinobacteria;Corynebacteriales;Corynebacteriaceae;Corynebacterium;tuberculostearicum'] = '077'
HC['Bacteria;Actinobacteria;Actinobacteria;Corynebacteriales;Corynebacteriales_[F-1];Lawsonella;clevelandensis'] = '173'
HC['Bacteria;Actinobacteria;Actinobacteria;Propionibacteriales;Propionibacteriaceae;Arachnia;rubra'] = '194'
HC['Bacteria;Actinobacteria;Actinobacteria;Propionibacteriales;Propionibacteriaceae;Cutibacterium;acnes'] = '530'
HC['Bacteria;Actinobacteria;Actinobacteria;Propionibacteriales;Propionibacteriaceae;Cutibacterium;granulosum'] = '114'
HC['Bacteria;Actinobacteria;Coriobacteriia;Coriobacteriales;Coriobacteriaceae;Atopobium;parvulum'] = '723'
HC['Bacteria;Bacteroidetes;Bacteroidia;Bacteroidales;Porphyromonadaceae;Tannerella;forsythia'] = '613'
HC['Bacteria;Bacteroidetes;Bacteroidia;Bacteroidales;Prevotellaceae;Prevotella;nanceiensis'] = '299'
HC['Bacteria;Bacteroidetes;Bacteroidia;Bacteroidales;Prevotellaceae;Prevotella;oris'] = '311'
HC['Bacteria;Bacteroidetes;Bacteroidia;Bacteroidales;Prevotellaceae;Prevotella;oulorum'] = '288'
HC['Bacteria;Bacteroidetes;Bacteroidia;Bacteroidales;Prevotellaceae;Prevotella;pleuritidis'] = '303'
HC['Bacteria;Bacteroidetes;Bacteroidia;Bacteroidales;Prevotellaceae;Prevotella;saccharolytica'] = '781'

HC['Bacteria;Firmicutes;Clostridia;Clostridiales;Peptoniphilaceae;Anaerococcus;prevotii'] = '738'
HC['Bacteria;Firmicutes;Clostridia;Clostridiales;Peptoniphilaceae;Anaerococcus;tetradius'] = '788'

HC['Bacteria;Fusobacteria;Fusobacteriia;Fusobacteriales;Fusobacteriaceae;Fusobacterium;nucleatum_subsp._vincentii'] ='200'
HC['Bacteria;Fusobacteria;Fusobacteriia;Fusobacteriales;Fusobacteriaceae;Fusobacterium;nucleatum_subsp._animalis'] = '420'
HC['Bacteria;Fusobacteria;Fusobacteriia;Fusobacteriales;Fusobacteriaceae;Fusobacterium;nucleatum_subsp._nucleatum'] = '698'
HC['Bacteria;Fusobacteria;Fusobacteriia;Fusobacteriales;Fusobacteriaceae;Fusobacterium;nucleatum_subsp._polymorphum'] ='202'

HC['Bacteria;Firmicutes;Clostridia;Clostridiales;Lachnospiraceae_[XIV];Catonella;morbi'] = '165'
HC['Bacteria;Firmicutes;Clostridia;Clostridiales;Lachnospiraceae_[XIV];Lachnoanaerobaculum;orale'] = '082'
HC['Bacteria;Firmicutes;Clostridia;Clostridiales;Lachnospiraceae_[XIV];Lachnoanaerobaculum;saburreum'] = '494'
HC['Bacteria;Firmicutes;Clostridia;Clostridiales;Lachnospiraceae_[XIV];Lachnoanaerobaculum;umeaense'] = '107'
HC['Bacteria;Firmicutes;Clostridia;Clostridiales;Lachnospiraceae_[XIV];Oribacterium;sinus'] = '457'
HC['Bacteria;Firmicutes;Clostridia;Clostridiales;Lachnospiraceae_[XIV];Shuttleworthia;satelles'] = '095'
HC['Bacteria;Firmicutes;Clostridia;Clostridiales;Peptoniphilaceae;Anaerococcus;octavius'] = '017'
HC['Bacteria;Firmicutes;Clostridia;Clostridiales;Peptoniphilaceae;Finegoldia;magna'] = '662'
HC['Bacteria;Firmicutes;Clostridia;Clostridiales;Peptoniphilaceae;Peptoniphilus;harei'] = '109'
HC['Bacteria;Firmicutes;Clostridia;Clostridiales;Peptostreptococcaceae_[XI];Mogibacterium;diversum'] = '593'
HC['Bacteria;Firmicutes;Clostridia;Clostridiales;Peptostreptococcaceae_[XI];Peptostreptococcaceae_[XI][G-1];[Eubacterium]_sulci'] = '467'
HC['Bacteria;Firmicutes;Clostridia;Clostridiales;Peptostreptococcaceae_[XI];Peptostreptococcaceae_[XI][G-7];[Eubacterium]_yurii_subsps._yurii_&_margaretiae'] = '377'
HC['Bacteria;Firmicutes;Clostridia;Clostridiales;Peptostreptococcaceae_[XI];Peptostreptococcus;stomatis'] = '112'
HC['Bacteria;Firmicutes;Mollicutes;Mycoplasmatales;Mycoplasmataceae;Mycoplasma;salivarium'] = '754'
HC['Bacteria;Fusobacteria;Fusobacteriia;Fusobacteriales;Leptotrichiaceae;Leptotrichia;goodfellowii'] = '845'
HC['Bacteria;Proteobacteria;Gammaproteobacteria;Pasteurellales;Pasteurellaceae;Aggregatibacter;paraphrophilus'] ='720'
HC['Bacteria;Proteobacteria;Betaproteobacteria;Burkholderiales;Commamonadaceae;Acidovorax;ebreus'] = '209'
HC['Bacteria;Proteobacteria;Gammaproteobacteria;Pseudomonadales;Moraxellaceae;Acinetobacter;baumannii'] = '554'
# ANA
HC['Bacteria;Actinobacteria;Actinobacteria;Actinomycetales;Actinomycetaceae;Schaalia;odontolyticus'] = '701'
HC['Bacteria;Actinobacteria;Actinobacteria;Actinomycetales;Micrococcaceae;Kocuria;palustris'] = '084'
HC['Bacteria;Actinobacteria;Actinobacteria;Actinomycetales;Micrococcaceae;Micrococcus;luteus'] = '087'
HC['Bacteria;Actinobacteria;Actinobacteria;Bifidobacteriales;Bifidobacteriaceae;Bifidobacterium;dentium'] = '588'
HC['Bacteria;Actinobacteria;Actinobacteria;Corynebacteriales;Corynebacteriaceae;Corynebacterium;accolens'] = '019'
HC['Bacteria;Actinobacteria;Actinobacteria;Corynebacteriales;Corynebacteriaceae;Corynebacterium;afermentans'] = '030'
HC['Bacteria;Actinobacteria;Actinobacteria;Corynebacteriales;Corynebacteriaceae;Corynebacterium;amycolatum'] = '031'
HC['Bacteria;Actinobacteria;Actinobacteria;Corynebacteriales;Corynebacteriaceae;Corynebacterium;appendicis'] = '033'
HC['Bacteria;Actinobacteria;Actinobacteria;Corynebacteriales;Corynebacteriaceae;Corynebacterium;aurimucosum'] = '034'
HC['Bacteria;Actinobacteria;Actinobacteria;Corynebacteriales;Corynebacteriaceae;Corynebacterium;coyleae'] = '341'
HC['Bacteria;Actinobacteria;Actinobacteria;Corynebacteriales;Corynebacteriaceae;Corynebacterium;kroppenstedtii'] = '049'
HC['Bacteria;Actinobacteria;Actinobacteria;Corynebacteriales;Corynebacteriaceae;Corynebacterium;macginleyi'] = '050'
HC['Bacteria;Actinobacteria;Actinobacteria;Corynebacteriales;Corynebacteriaceae;Corynebacterium;mucifaciens'] = '835'
HC['Bacteria;Actinobacteria;Actinobacteria;Corynebacteriales;Corynebacteriaceae;Corynebacterium;propinquum'] = '059'
HC['Bacteria;Actinobacteria;Actinobacteria;Corynebacteriales;Corynebacteriaceae;Corynebacterium;pseudodiphtheriticum'] = '060'
HC['Bacteria;Actinobacteria;Actinobacteria;Corynebacteriales;Corynebacteriaceae;Corynebacterium;singulare'] = '063'
HC['Bacteria;Actinobacteria;Actinobacteria;Corynebacteriales;Corynebacteriaceae;Corynebacterium;tuscaniense'] = '184'
HC['Bacteria;Actinobacteria;Actinobacteria;Micrococcales;Brevibacteriaceae;Brevibacterium;paucivorans'] = '340'
HC['Bacteria;Actinobacteria;Actinobacteria;Propionibacteriales;Propionibacteriaceae;Cutibacterium;avidum'] = '552'
HC['Bacteria;Bacteroidetes;Bacteroidia;Bacteroidales;Prevotellaceae;Prevotella;buccalis'] = '562'
HC['Bacteria;Proteobacteria;Alphaproteobacteria;Rhizobiales;Bradyrhizobiaceae;Afipia;broomeae'] = '559'
HC['Bacteria;Proteobacteria;Alphaproteobacteria;Rhizobiales;Bradyrhizobiaceae;Bradyrhizobium;elkanii'] = '597'
HC['Bacteria;Proteobacteria;Alphaproteobacteria;Rhizobiales;Rhizobiaceae;Mesorhizobium;loti'] = '659'
HC['Bacteria;Proteobacteria;Alphaproteobacteria;Rhodobacterales;Rhodobacteraceae;Paracoccus;yeei'] = '104'
HC['Bacteria;Proteobacteria;Betaproteobacteria;Burkholderiales;Commamonadaceae;Acidovorax;caeni'] = '211'
HC['Bacteria;Proteobacteria;Betaproteobacteria;Burkholderiales;Commamonadaceae;Acidovorax;temperans'] = '216'
HC['Bacteria;Proteobacteria;Gammaproteobacteria;Enterobacterales;Enterobacteriaceae;Proteus;mirabilis'] = '676'
HC['Bacteria;Proteobacteria;Gammaproteobacteria;Pseudomonadales;Moraxellaceae;Acinetobacter;junii'] = '282'
HC['Bacteria;Proteobacteria;Gammaproteobacteria;Pseudomonadales;Moraxellaceae;Moraxella;catarrhalis'] = '833'
HC['Bacteria;Proteobacteria;Gammaproteobacteria;Pseudomonadales;Moraxellaceae;Moraxella;lincolnii'] = '154'

HC['Bacteria;Proteobacteria;Gammaproteobacteria;Pseudomonadales;Moraxellaceae;Moraxella;nonliquefaciens'] = '098'
HC['Bacteria;Proteobacteria;Gammaproteobacteria;Pseudomonadales;Moraxellaceae;Moraxella;osloensis'] = '711'
HC['Bacteria;Proteobacteria;Gammaproteobacteria;Pseudomonadales;Pseudomonadaceae;Pseudomonas;stutzeri'] = '477'
# BMU
HC['Bacteria;Actinobacteria;Actinobacteria;Actinomycetales;Actinomycetaceae;Schaalia;lingnae_[Not_Validly_Published]'] = '181'
HC['Bacteria;Actinobacteria;Coriobacteriia;Coriobacteriales;Coriobacteriaceae;Atopobium;rimae'] = '750'
HC['Bacteria;Bacteroidetes;Bacteroidia;Bacteroidales;Prevotellaceae;Prevotella;salivae'] = '307'
HC['Bacteria;Bacteroidetes;Bacteroidia;Bacteroidales;Prevotellaceae;Prevotella;shahii'] = '795'
HC['Bacteria;Firmicutes;Clostridia;Clostridiales;Lachnospiraceae_[XIV];Oribacterium;asaccharolyticum'] = '108'
HC['Bacteria;Firmicutes;Clostridia;Clostridiales;Lachnospiraceae_[XIV];Oribacterium;parvum'] = '934'
HC['Bacteria;Firmicutes;Clostridia;Clostridiales;Lachnospiraceae_[XIV];Stomatobaculum;longum'] = '419'
HC['Bacteria;Firmicutes;Clostridia;Clostridiales;Peptostreptococcaceae_[XI];Peptostreptococcaceae_[XI][G-9];[Eubacterium]_brachy'] = '557'
#HPA
HC['Bacteria;Actinobacteria;Actinobacteria;Bifidobacteriales;Bifidobacteriaceae;Bifidobacterium;longum']='862'
#LAF
HC['Bacteria;Actinobacteria;Actinobacteria;Actinomycetales;Dermacoccaceae;Kytococcus;sedentarius'] = '855'
HC['Bacteria;Actinobacteria;Actinobacteria;Actinomycetales;Dietziaceae;Dietzia;cinnamea'] = '368'
HC['Bacteria;Actinobacteria;Actinobacteria;Corynebacteriales;Corynebacteriaceae;Corynebacterium;jeikeium'] = '047'
HC['Bacteria;Actinobacteria;Actinobacteria;Corynebacteriales;Corynebacteriaceae;Corynebacterium;massiliense'] = '333'
HC['Bacteria;Actinobacteria;Actinobacteria;Corynebacteriales;Corynebacteriaceae;Corynebacterium;minutissimum'] = '053'
HC['Bacteria;Actinobacteria;Actinobacteria;Corynebacteriales;Corynebacteriaceae;Corynebacterium;pilbarense'] = '054'

HC['Bacteria;Actinobacteria;Actinobacteria;Corynebacteriales;Corynebacteriaceae;Corynebacterium;simulans'] = '062'
HC['Bacteria;Actinobacteria;Actinobacteria;Corynebacteriales;Corynebacteriaceae;Turicella;otitidis'] = '832'
HC['Bacteria;Actinobacteria;Actinobacteria;Micrococcales;Intrasporangiaceae;Arsenicicoccus;bolidensis'] = '190'
HC['Bacteria;Actinobacteria;Actinobacteria;Micrococcales;Intrasporangiaceae;Janibacter;indicus'] = '339'
HC['Bacteria;Actinobacteria;Coriobacteriia;Coriobacteriales;Coriobacteriaceae;Atopobium;vaginae'] = '814'
HC['Bacteria;Proteobacteria;Alphaproteobacteria;Rhodobacterales;Rhodobacteraceae;Haematobacter;missouriensis'] = '316'
HC['Bacteria;Proteobacteria;Alphaproteobacteria;Sphingomonadales;Sphingomonadaceae;Sphingomonas;echinoides'] = '003'
HC['Bacteria;Proteobacteria;Gammaproteobacteria;Enterobacterales;Enterobacteriaceae;Yersinia;pestis'] = '827'
HC['Bacteria;Proteobacteria;Gammaproteobacteria;Pseudomonadales;Moraxellaceae;Acinetobacter;johnsonii'] = '297'
HC['Bacteria;Proteobacteria;Gammaproteobacteria;Pseudomonadales;Moraxellaceae;Acinetobacter;lwoffii'] = '005'
HC['Bacteria;Proteobacteria;Gammaproteobacteria;Pseudomonadales;Moraxellaceae;Acinetobacter;radioresistens'] = '010'
HC['Bacteria;Proteobacteria;Gammaproteobacteria;Pseudomonadales;Pseudomonadaceae;Pseudomonas;pseudoalcaligenes'] = '740'
#LRC
HC['Bacteria;Actinobacteria;Actinobacteria;Bifidobacteriales;Bifidobacteriaceae;Gardnerella;vaginalis']='829'
HC['Bacteria;Proteobacteria;Alphaproteobacteria;Rhizobiales;Rhizobiaceae;Agrobacterium;tumefaciens']='485'
#MVA
HC['Bacteria;Actinobacteria;Actinobacteria;Actinomycetales;Actinomycetaceae;Mobiluncus;mulieris']='830'
HC['Bacteria;Actinobacteria;Actinobacteria;Bifidobacteriales;Bifidobacteriaceae;Bifidobacterium;breve']='889'
HC['Bacteria;Actinobacteria;Actinobacteria;Corynebacteriales;Mycobacteriaceae;Mycobacterium;neoaurum']='692'
HC['Bacteria;Firmicutes;Bacilli;Lactobacillales;Lactobacillaceae;Lactobacillus;coleohominis']='816'
HC['Bacteria;Firmicutes;Bacilli;Lactobacillales;Lactobacillaceae;Lactobacillus;vaginalis']='051'
HC['Bacteria;Firmicutes;Clostridia;Clostridiales;Peptoniphilaceae;Parvimonas;micra']='111'
HC['Bacteria;Firmicutes;Clostridia;Clostridiales;Peptostreptococcaceae_[XI];Peptostreptococcus;anaerobius']='542'
HC['Bacteria;Firmicutes;Mollicutes;Mycoplasmatales;Mycoplasmataceae;Mycoplasma;hominis']='632'
HC['Bacteria;Fusobacteria;Fusobacteriia;Fusobacteriales;Leptotrichiaceae;Sneathia;amnii_[Not_Validly_Published]']='844'
#PFO
HC['Bacteria;Actinobacteria;Actinobacteria;Bifidobacteriales;Bifidobacteriaceae;Bifidobacterium;scardovii']='891'
HC['Bacteria;Firmicutes;Bacilli;Lactobacillales;Lactobacillaceae;Lactobacillus;fermentum']='608'
#PTO
HC['Bacteria;Bacteroidetes;Bacteroidia;Bacteroidales;Prevotellaceae;Prevotella;baroniae']='553'
HC['Bacteria;Bacteroidetes;Bacteroidia;Bacteroidales;Prevotellaceae;Prevotella;buccae']='560'
HC['Bacteria;Bacteroidetes;Bacteroidia;Bacteroidales;Prevotellaceae;Prevotella;dentalis']='583'
HC['Bacteria;Bacteroidetes;Bacteroidia;Bacteroidales;Prevotellaceae;Prevotella;enoeca']='600'
HC['Bacteria;Firmicutes;Clostridia;Clostridiales;Peptostreptococcaceae_[XI];Filifactor;alocis']='539'
HC['Bacteria;Firmicutes;Clostridia;Clostridiales;Peptostreptococcaceae_[XI];Mogibacterium;timidum']='042'
HC['Bacteria;Firmicutes;Clostridia;Clostridiales;Peptostreptococcaceae_[XI];Peptostreptococcaceae_[XI][G-1];[Eubacterium]_infirmum']='105'
HC['Bacteria;Firmicutes;Clostridia;Clostridiales;Peptostreptococcaceae_[XI];Peptostreptococcaceae_[XI][G-6];[Eubacterium]_nodatum']='694'
HC['Bacteria;Firmicutes;Erysipelotrichia;Erysipelotrichales;Erysipelotrichaceae;Eggerthia;catenaformis']='569'
HC['Bacteria;Firmicutes;Mollicutes;Mycoplasmatales;Mycoplasmataceae;Mycoplasma;faucium']='606'
HC['Bacteria;Firmicutes;Mollicutes;Mycoplasmatales;Mycoplasmataceae;Mycoplasma;orale']='704'
HC['Bacteria;Synergistetes;Synergistia;Synergistales;Synergistaceae;Fretibacterium;fastidiosum']='363'
#RAF
HC['Bacteria;Actinobacteria;Actinobacteria;Actinomycetales;Micrococcaceae;Kocuria;rhizophila']='197'
HC['Bacteria;Actinobacteria;Actinobacteria;Corynebacteriales;Corynebacteriaceae;Corynebacterium;diphtheriae']='591'
HC['Bacteria;Firmicutes;Clostridia;Clostridiales;Peptoniphilaceae;Peptoniphilus;indolicus']='840'
HC['Bacteria;Proteobacteria;Alphaproteobacteria;Sphingomonadales;Sphingomonadaceae;Porphyrobacter;tepidarius']='007'
#RRC
HC['Bacteria;Actinobacteria;Actinobacteria;Propionibacteriales;Propionibacteriaceae;Arachnia;propionica']='739'
#SAL
HC['Bacteria;Bacteroidetes;Bacteroidia;Bacteroidales;Prevotellaceae;Prevotella;maculosa']='289'
#SUBP
HC['Bacteria;Actinobacteria;Actinobacteria;Actinomycetales;Actinomycetaceae;Actinomyces;dentalis']='888'
HC['Bacteria;Actinobacteria;Actinobacteria;Actinomycetales;Actinomycetaceae;Actinomyces;gerencseriae']='618'
HC['Bacteria;Actinobacteria;Actinobacteria;Actinomycetales;Actinomycetaceae;Peptidiphaga;gingivicola']='848'
HC['Bacteria;Actinobacteria;Actinobacteria;Bifidobacteriales;Bifidobacteriaceae;Scardovia;wiggsiae']='195'
HC['Bacteria;Bacteroidetes;Bacteroidia;Bacteroidales;Prevotellaceae;Prevotella;loescheii']='658'
HC['Bacteria;Bacteroidetes;Bacteroidia;Bacteroidales;Prevotellaceae;Prevotella;oralis']='705'
HC['Bacteria;Firmicutes;Bacilli;Lactobacillales;Lactobacillaceae;Lactobacillus;rhamnosus']='749'
HC['Bacteria;Firmicutes;Bacilli;Lactobacillales;Lactobacillaceae;Lactobacillus;casei']='568'
HC['Bacteria;Firmicutes;Clostridia;Clostridiales;Lachnospiraceae_[XIV];Johnsonella;ignava']='635'
#THR
HC['Bacteria;Actinobacteria;Actinobacteria;Propionibacteriales;Propionibacteriaceae;Propionibacterium;acidifaciens']='191'
HC['Bacteria;Firmicutes;Bacilli;Lactobacillales;Lactobacillaceae;Lactobacillus;salivarius']='756'
#VIN
HC['Bacteria;Firmicutes;Clostridia;Clostridiales;Peptoniphilaceae;Anaerococcus;lactolyticus']='859'
HC['Bacteria;Firmicutes;Clostridia;Clostridiales;Peptoniphilaceae;Peptoniphilus;lacrimalis']='836'
HC['Bacteria;Firmicutes;Clostridia;Clostridiales;Ruminococcaceae;Fastidiosipila;sanguinis']='935'
HC['Bacteria;Proteobacteria;Alphaproteobacteria;Rhizobiales;Bradyrhizobiaceae;Bosea;vestrisii']='636'
# LAF,LRC,RAF,RRC,STO,THR
HC['Bacteria;Proteobacteria;Alphaproteobacteria;Rhizobiales;Bradyrhizobiaceae;Afipia;sp._genotype_4']='652'

def get_hots(hot_filename):
    hot_collector = {}
    fp = open(hot_filename,'r')
    for line in fp:
        line = line.strip().strip(';')
        
        pts = line.split('\t')
        hot = str(int(line[:3]))
        tax = pts[1]
        tax_pts = tax.split(';')
        
        if hot in hot_collector and tax != hot_collector[hot]["fulltax"]:
            print('Bad dupe',line,hot_collector[hot])
            sys.exit()
        #species
        hot_collector[tax] = {"hmt":hot}
        if len(tax_pts) != 7:
            print('ERROR XX',tax) 
        hot_collector[tax]["genus"]=tax_pts[-2]
        
        if ' ' in tax_pts[-1]:
            hot_collector[tax]["species"]=tax_pts[-1].split(' ')[1]
        else:
            hot_collector[tax]["species"]=tax_pts[-1]
    
    return hot_collector
    
def run():  
    
    mtx = open(args.mtx,'r')
    
    
    foutClean = open(args.outfile,'w')
    
    # check for zero sum datasets
    
    master = {}
    nov_collector = {}
    multi_tax_collector = {}
    for line in mtx:
        line = line.strip()
        line_pts = line.split('\t')
        # HMT-283 1       100    [counts]
        # HMT-275-283-284 3       0.33,0.33,0.33 [counts]
        if line_pts[0] == '#OTU ID':
            header = line_pts[1:]
            foutClean.write('HOT-ID\tnum\tpct\t'+'\t'.join(header)+'\n')
            for ds in header:
                nov_collector[ds] = 0.0
        if 'Bacteria' in line_pts[0] or line_pts[0].startswith('Archaea'):
            mtx_old_tax_pts = line_pts[0].split(';')
            counts_ary = line_pts[1:]
            
            if '_nov_' in mtx_old_tax_pts[6]:  # or mtx_old_tax_pts[6] == 'sp._genotype_4':#  LAF
                for i,ds in enumerate(header):
                    nov_collector[ds] += float(counts_ary[i])
            elif mtx_old_tax_pts[6].startswith('multispecies'):
                
                sp_pts = mtx_old_tax_pts[-1].split(' ')
                mtx_old_tax_pts[-1] = sp_pts[0]
                msid = sp_pts[1].strip('(').strip(')')
                if msid in multi_tax_collector:
                    sys.exit('msid error')
                multi_tax_collector[msid] = {}
                #print('mtx_old_tax_pts',mtx_old_tax_pts,msid)
                if msid in multi_file_collector:
                #print('multi_file_collector',multi_file_collector[msid],msid)
                    split_text_lst = []
                    split_by = len(multi_file_collector[msid]['taxa'])
                    x = (100 / split_by) / 100
                    # print('pct',multi_file_collector[tid]['ct'], x,round(x, 2))
                    numstr = str(round(x, 2))
                    for n in range(split_by):
                        split_text_lst.append(numstr)
                    split_text = ','.join(split_text_lst)
                    
                    
                    
                    cts = []
                    for i,ds in enumerate(header):
                        cts.append(str(float(counts_ary[i])/split_by))
                    multihmt = []
                    for tax in multi_file_collector[msid]['taxa']:
                        
                        if tax not in args.hot_conversion:
                            sys.exit('hot_conversion Error1')
                        multihmt.append(args.hot_conversion[tax]['hmt'])
                        #multi_tax_collector[msid][tax] = {'cts':cts,'hmt':hmt,'msid':msid,'num',split_by,'note':note}
                        note='Split evenly: group of '+str(split_by)
                    hmts = '-'.join(multihmt)
                    #print('hmts',hmts)
                    foutClean.write('HMT-'+hmts+'\t'+str(split_by)+'\t'+split_text+'\t'+'\t'.join(cts)+'\n')
                else:
                   sys.exit('no msid in multifile')
                
            else:
                mtx_old_tax_pts[-1] = mtx_old_tax_pts[-1].split(' ')[0]
                #print(mtx_old_tax_pts)
                tax = ';'.join(mtx_old_tax_pts)
                if tax not in args.hot_conversion:
                    print('HMT not found',tax)
                    hmt = 'Unknown'
                else:
                    hmt = args.hot_conversion[tax]['hmt']
                #for hmt in 
                #print('hmt',hmt)
                foutClean.write('HMT-'+hmt+'\t1\t100\t'+'\t'.join(counts_ary)+'\n')
   
    
    foutClean.write('Unmatched\tUnmatched\tUnmatched\t')
    nov_counts = []
    for ds in header:
        nov_counts.append(str(nov_collector[ds]))
    
    foutClean.write('\t'.join(nov_counts)+'\n')
    

    
if __name__ == "__main__":

    usage = """
    USAGE:
        In each site directory:
        ./1-clean_data_step1.py -i AKE_species_count_table.tsv   
          
          -d/--delete xxx  (integer min ds count to retain default:1000)
          -s/--site   Required AKE,ANA...
           MUST use the original file: XXX_species_count_table.tsv
           
        This script is the first step:
          -- counts: creates integer from float
          -- cleans the taxa name to remove 'k__','p__', 'c__' .... 
          
          -- removes datasets that sum less than XX counts (Default: keep all data)
        Does Not:
          -- Split into v1v3 and v3v5 
          -- Remove 'multi' and '_nov_' taxa
          
       1a-separate_v1v3_v3v5.py   
THIS SCRIPT  ==>        2-separate_multispecies_taxa.py
       copy all the individual site files to a common dir ~/programming/homd-work/NIH-VAMPS/v1v3
       Get file example_[date].tsv from 3-combine_sites.py  
       ***Clean out num-[site] and pct-[site]  columns  BY HAND
       ***Also change col 2& 3 to num and pct NOT num-AKE
       run 
         3a-clean big file to add zeros and fill in num and pct column    
           ../scripts/3a-clean_big_file.py -i example-v3v5.tsv   ==> zero filled
       calc abundance :
         4-abundance_calculate_pctsNEW_add_species.py and add species 
           ../scripts/4-abundance_calculate_pctsNEW_add_species.py -i zeros_filled.tsv -r v3v5
       calc mean,max,sum and dscount:
         5-abundance_mean_max.py*  
           ./scripts/5-abundance_mean_max.py -i v3v5_NIH_ALL_samples_wpcts_2023-11-09_homd.csv -r v3v5
       --source must be in ['eren2014_v1v3','eren2014_v3v5','dewhirst_35x9']
         
    """

    parser = argparse.ArgumentParser(description="." ,usage=usage)

    parser.add_argument("-i", "--infile",   required=True,  action="store",   dest = "mtx", 
                                                   help=" ")
    #parser.add_argument("-s", "--site",   required=True,  action="store",   dest = "site", 
    #                                               help=" ")
    parser.add_argument("-host", "--host",
                        required = False, action = 'store', dest = "dbhost", default = 'localhost',
                        help = "choices=['homd',  'localhost']")
    args = parser.parse_args()
    if args.dbhost == 'homd_dev':
        args.DATABASE = 'homd'
        dbhost = '192.168.1.46'
        args.prettyprint = False
    
    elif args.dbhost == 'homd_prod':
        args.DATABASE = 'homd'
        dbhost = '192.168.1.42'
        args.prettyprint = False

    elif args.dbhost == 'localhost':
        #args.json_file_path = '/Users/avoorhis/programming/homd-data/json'
        #args.TAX_DATABASE  = 'HOMD_taxonomy'
        args.DATABASE = 'homd'
        dbhost = 'localhost'
        
    else:
        sys.exit('dbhost - error')
    site_names = [
    'AKE',  #Attached_Keratinized_gingiva
    'ANA',  #Anterior_nares
    'BMU',  #Buccal_mucosa
    'HPA',  #Hard_palate
    'LAF',  #L_Antecubital_fossa
    'LRC',  #L_Retroauricular_crease
    'MVA',  #Mid_vagina
    'PFO',  #Posterior_fornix
    'PTO',  #Palatine_Tonsils
    'RAF',  #R_Antecubital_fossa
    'RRC',  #R_Retroauricular_crease
    'SAL',  #Saliva
    'STO',  #Stool
    'SUBP', #Subgingival_plaque
    'SUPP', #Supragingival_plaque
    'THR',  #Throat
    'TDO',  #Tongue_dorsum
    'VIN'   #Vaginal_introitus
    ]
    
    ifpts = args.mtx.split('_')
    args.site = ifpts[0]
    args.site = args.site.upper()
    args.region = ifpts[1]
    args.outfile = '_'.join([args.site,args.region,'sep_multiples',today+'.csv'])
    
    
    if args.site not in site_names:
        sys.exit('site name not found',args.site)
                        
    multi_file = args.site+'_spp_spids_all_tax.txt'
    args.hot_conversion = get_hots('../ref.taxonomy')
    mfp = open(multi_file,'r')
    multi_file_collector = {}
    for line in mfp:
        line = line.strip()
        line_pts = line.split('\t')
        ct = len(line_pts[1].split(';'))
        msid = line_pts[0].strip()
        
        multi_file_collector[msid] = {'ct':ct,'ids':line_pts[1],'taxa':line_pts[2:]}
    #singles_file = '../spid_taxonomy_single.txt'
    mfp.close()
    # sfp = open(singles_file,'r')
#     single_file_collector = {}
#     for line in sfp:
#         line = line.strip()
#         line_pts = line.split('\t')
#         single_file_collector[line_pts[0]] = {'taxa':line_pts[1]}
#     sfp.close()
    
    #myconn = MyConnection(host=dbhost, db=args.DATABASE,  read_default_file = "~/.my.cnf_node")
    
    run()
        
    
    # elif args.synonyms:
#         run_synonyms()
#     elif args.taxid:
#         run_taxon_id()
#     elif args.sspecies:
#         run_subspecies()
#     
    if not args:
       print('no def selected')
       print(usage)
    

    
