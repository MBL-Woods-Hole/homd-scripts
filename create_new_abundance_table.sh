#!/bin/bash

# create_new_abundance_table.sh
args=("$@")
echo $# arguments passed
dbhost=''
if [ $# == 0 ]; then
   echo "Enter either 'localhost' or 'homd_dev' on command line to access the correct database"
   exit
else
  echo ${args[0]}
  dbhost=${args[0]}
fi
# shoud be host name homd_dev or homd or localhost

formatted_date=$(date +"%Y-%m-%d")
random=$((1 + $RANDOM % 100))
echo "Formatted date: $formatted_date"
cwd=$(pwd)

cd $cwd
cd ./Dewhirst
./scripts/5a-abundance_hmt2taxonomy.py -host $dbhost -i dewhirst_35x9_coalesce_2022-01-08_homd.csv -s dewhirst
./scripts/5b-gather_abundance_by_rank.py -i dewhirst_taxonomyNpcts_${formatted_date}_homd.csv -s dewhirst
./scripts/6-abunance_ranks_calc_means.py -i dewhirst_rank_abundance_sums_${formatted_date}_homd.csv -s dewhirst
./scripts/10-load_DewhirstErenAbundance2db.py -host $dbhost -i dewhirst_MeanStdevPrev_byRankFINAL_${formatted_date}_homd.csv -src dewhirst -t abundance_NEW

cd $cwd
cd HMP_16SRefSeq
./scripts/new_taxonomy.py ${formatted_date} ${dbhost}
mkdir ./tmp$random
cd ./tmp$random
cp ../*/*_MeanStdevPrev_byRankFINAL_${formatted_date}.csv ./
../scripts/7-meshrows.py -r v1v3  
../scripts/7-meshrows.py -r v3v5
../scripts/v1v3_notes.py -i NEWAll_Sites_v1v3_RelAbund_${formatted_date}_homd.csv -r v1v3
../scripts/v3v5_notes.py -i NEWAll_Sites_v3v5_RelAbund_${formatted_date}_homd.csv -r v3v5
../scripts/10-HMPRefSeq_load_abundance2db.py -host $dbhost -i AllSites_NewNotes_v1v3_FINAL_${formatted_date}.csv -src HMP_16S_RefSeq_v1v3 -t abundance_NEW
../scripts/10-HMPRefSeq_load_abundance2db.py -host $dbhost -i AllSites_NewNotes_v3v5_FINAL_${formatted_date}.csv -src HMP_16S_RefSeq_v3v5 -t abundance_NEW

cd $cwd
cd ./Eren
./scripts/7a-DewhirstErenabundance_hmt2taxonomy.py -host $dbhost -r v1v3 -i eren2014_v1v3_coalesce_2022-02-03_homd.csv;
./scripts/7a-DewhirstErenabundance_hmt2taxonomy.py -host $dbhost -r v3v5 -i eren2014_v3v5_coalesce_2022-02-03_homd.csv
./scripts/8-DEgather_abundance_by_rank.py -r v1v3 -i v1v3_taxonomyNpcts_${formatted_date}_homd.csv;
./scripts/8-DEgather_abundance_by_rank.py -r v3v5 -i v3v5_taxonomyNpcts_${formatted_date}_homd.csv
./scripts/9-DEabunance_ranks_calc_means.py -r v1v3 -i v1v3_rank_abundance_sums_${formatted_date}_homd.csv;
./scripts/9-DEabunance_ranks_calc_means.py -r v3v5 -i v3v5_rank_abundance_sums_${formatted_date}_homd.csv
./scripts/10-load_DewhirstErenAbundance2db.py -host $dbhost -src eren_v1v3 -i v1v3_MeanStdevPrev_byRankFINAL_${formatted_date}.csv -t abundance_NEW
./scripts/10-load_DewhirstErenAbundance2db.py -host $dbhost -src eren_v3v5 -i v3v5_MeanStdevPrev_byRankFINAL_${formatted_date}.csv -t abundance_NEW

cd $cwd
cd ./HMP_MetaPhlan
./scripts/5a-find_taxa_from_db.py -host $dbhost -i species-rel_abs-sp2363_x_m2365EDIT.csv
./scripts/5b-unique_tax_strings.py -i HMP_Meta_with_taxstrings_${formatted_date}.csv
./scripts/5c-gather_abundance_by_rank.py -host $dbhost -i HMP_Unique_taxstrings_${formatted_date}.csv
./scripts/6-abunance_ranks_calc_means.py -i HMP_NEWrank_abundance_sums_${formatted_date}_homd.csv
./scripts/10-load_abundance2db.py -host $dbhost -i HMPMeanStdevPrev_byRankFINAL_${formatted_date}_homd.csv -t abundance_NEW

