#!/bin/bash

formatted_date=$(date +"%Y-%m-%d")
random=$((1 + $RANDOM % 1000))
echo "Formatted date: $formatted_date"
cwd=$(pwd)
dbhost='localhost'

cd $cwd
cd HMP_16SRefSeq
echo 'running ./scripts/new_taxonomy16S_abundance.py' $formatted_date $dbhost
./scripts/new_taxonomy16S_abundance.py ${formatted_date} ${dbhost}
mkdir ./tmp$random
cd ./tmp$random
cp ../*/*_MeanStdevPrev*${formatted_date}.csv ./
../scripts/7-meshrows.py -r v1v3  
../scripts/7-meshrows.py -r v3v5
../scripts/v1v3_notes.py -i NEWAll_Sites_v1v3_RelAbund_${formatted_date}_homd.csv -r v1v3
../scripts/v3v5_notes.py -i NEWAll_Sites_v3v5_RelAbund_${formatted_date}_homd.csv -r v3v5
../scripts/10-HMPRefSeq_load_abundance2db.py -host $dbhost -i AllSites_NewNotes_v1v3_FINAL_${formatted_date}.csv -src HMP_16S_RefSeq_v1v3 -t abundance_NEW
../scripts/10-HMPRefSeq_load_abundance2db.py -host $dbhost -i AllSites_NewNotes_v3v5_FINAL_${formatted_date}.csv -src HMP_16S_RefSeq_v3v5 -t abundance_NEW
#rm ../*/*MeanStdevPrev_byRank*
#rm ../*/*rank_abundance_sums*
