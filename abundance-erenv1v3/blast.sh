#!/bin/bash

echo '
  Blasting 1/593: V1V3_001_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_001_Firmicutes.fna -out ./work/V1V3_001_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 2/593: V1V3_002_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_002_Firmicutes.fna -out ./work/V1V3_002_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 3/593: V1V3_003_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_003_Firmicutes.fna -out ./work/V1V3_003_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 4/593: V1V3_004_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_004_Firmicutes.fna -out ./work/V1V3_004_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 5/593: V1V3_005_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_005_Actinobacteria.fna -out ./work/V1V3_005_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 6/593: V1V3_006_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_006_Firmicutes.fna -out ./work/V1V3_006_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 7/593: V1V3_007_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_007_Bacteroidetes.fna -out ./work/V1V3_007_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 8/593: V1V3_008_Epsilonproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_008_Epsilonproteobacteria.fna -out ./work/V1V3_008_Epsilonproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 9/593: V1V3_009_TM7.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_009_TM7.fna -out ./work/V1V3_009_TM7.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 10/593: V1V3_010_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_010_Betaproteobacteria.fna -out ./work/V1V3_010_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 11/593: V1V3_011_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_011_Actinobacteria.fna -out ./work/V1V3_011_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 12/593: V1V3_012_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_012_Gammaproteobacteria.fna -out ./work/V1V3_012_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 13/593: V1V3_013_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_013_Firmicutes.fna -out ./work/V1V3_013_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 14/593: V1V3_014_Fusobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_014_Fusobacteria.fna -out ./work/V1V3_014_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 15/593: V1V3_015_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_015_Firmicutes.fna -out ./work/V1V3_015_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 16/593: V1V3_016_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_016_Firmicutes.fna -out ./work/V1V3_016_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 17/593: V1V3_017_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_017_Firmicutes.fna -out ./work/V1V3_017_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 18/593: V1V3_018_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_018_Betaproteobacteria.fna -out ./work/V1V3_018_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 19/593: V1V3_019_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_019_Betaproteobacteria.fna -out ./work/V1V3_019_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 20/593: V1V3_020_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_020_Betaproteobacteria.fna -out ./work/V1V3_020_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 21/593: V1V3_021_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_021_Firmicutes.fna -out ./work/V1V3_021_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 22/593: V1V3_022_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_022_Actinobacteria.fna -out ./work/V1V3_022_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 23/593: V1V3_023_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_023_Bacteroidetes.fna -out ./work/V1V3_023_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 24/593: V1V3_024_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_024_Firmicutes.fna -out ./work/V1V3_024_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 25/593: V1V3_025_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_025_Firmicutes.fna -out ./work/V1V3_025_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 26/593: V1V3_026_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_026_Firmicutes.fna -out ./work/V1V3_026_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 27/593: V1V3_027_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_027_Bacteroidetes.fna -out ./work/V1V3_027_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 28/593: V1V3_028_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_028_Bacteroidetes.fna -out ./work/V1V3_028_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 29/593: V1V3_029_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_029_Firmicutes.fna -out ./work/V1V3_029_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 30/593: V1V3_030_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_030_Firmicutes.fna -out ./work/V1V3_030_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 31/593: V1V3_031_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_031_Bacteroidetes.fna -out ./work/V1V3_031_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 32/593: V1V3_032_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_032_Bacteroidetes.fna -out ./work/V1V3_032_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 33/593: V1V3_033_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_033_Firmicutes.fna -out ./work/V1V3_033_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 34/593: V1V3_034_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_034_Actinobacteria.fna -out ./work/V1V3_034_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 35/593: V1V3_035_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_035_Bacteroidetes.fna -out ./work/V1V3_035_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 36/593: V1V3_036_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_036_Actinobacteria.fna -out ./work/V1V3_036_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 37/593: V1V3_037_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_037_Firmicutes.fna -out ./work/V1V3_037_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 38/593: V1V3_038_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_038_Firmicutes.fna -out ./work/V1V3_038_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 39/593: V1V3_039_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_039_Bacteroidetes.fna -out ./work/V1V3_039_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 40/593: V1V3_040_Fusobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_040_Fusobacteria.fna -out ./work/V1V3_040_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 41/593: V1V3_041_TM7.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_041_TM7.fna -out ./work/V1V3_041_TM7.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 42/593: V1V3_042_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_042_Bacteroidetes.fna -out ./work/V1V3_042_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 43/593: V1V3_043_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_043_Actinobacteria.fna -out ./work/V1V3_043_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 44/593: V1V3_044_Fusobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_044_Fusobacteria.fna -out ./work/V1V3_044_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 45/593: V1V3_045_Fusobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_045_Fusobacteria.fna -out ./work/V1V3_045_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 46/593: V1V3_046_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_046_Bacteroidetes.fna -out ./work/V1V3_046_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 47/593: V1V3_047_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_047_Actinobacteria.fna -out ./work/V1V3_047_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 48/593: V1V3_048_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_048_Actinobacteria.fna -out ./work/V1V3_048_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 49/593: V1V3_049_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_049_Betaproteobacteria.fna -out ./work/V1V3_049_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 50/593: V1V3_050_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_050_Firmicutes.fna -out ./work/V1V3_050_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 51/593: V1V3_051_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_051_Betaproteobacteria.fna -out ./work/V1V3_051_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 52/593: V1V3_052_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_052_Betaproteobacteria.fna -out ./work/V1V3_052_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 53/593: V1V3_053_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_053_Actinobacteria.fna -out ./work/V1V3_053_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 54/593: V1V3_054_Fusobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_054_Fusobacteria.fna -out ./work/V1V3_054_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 55/593: V1V3_055_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_055_Firmicutes.fna -out ./work/V1V3_055_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 56/593: V1V3_056_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_056_Bacteroidetes.fna -out ./work/V1V3_056_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 57/593: V1V3_057_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_057_Firmicutes.fna -out ./work/V1V3_057_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 58/593: V1V3_058_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_058_Firmicutes.fna -out ./work/V1V3_058_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 59/593: V1V3_059_Epsilonproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_059_Epsilonproteobacteria.fna -out ./work/V1V3_059_Epsilonproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 60/593: V1V3_060_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_060_Bacteroidetes.fna -out ./work/V1V3_060_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 61/593: V1V3_061_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_061_Firmicutes.fna -out ./work/V1V3_061_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 62/593: V1V3_062_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_062_Bacteroidetes.fna -out ./work/V1V3_062_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 63/593: V1V3_063_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_063_Firmicutes.fna -out ./work/V1V3_063_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 64/593: V1V3_064_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_064_Bacteroidetes.fna -out ./work/V1V3_064_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 65/593: V1V3_065_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_065_Bacteroidetes.fna -out ./work/V1V3_065_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 66/593: V1V3_066_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_066_Actinobacteria.fna -out ./work/V1V3_066_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 67/593: V1V3_067_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_067_Actinobacteria.fna -out ./work/V1V3_067_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 68/593: V1V3_068_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_068_Bacteroidetes.fna -out ./work/V1V3_068_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 69/593: V1V3_069_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_069_Bacteroidetes.fna -out ./work/V1V3_069_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 70/593: V1V3_070_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_070_Actinobacteria.fna -out ./work/V1V3_070_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 71/593: V1V3_071_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_071_Firmicutes.fna -out ./work/V1V3_071_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 72/593: V1V3_072_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_072_Betaproteobacteria.fna -out ./work/V1V3_072_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 73/593: V1V3_073_Fusobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_073_Fusobacteria.fna -out ./work/V1V3_073_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 74/593: V1V3_074_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_074_Bacteroidetes.fna -out ./work/V1V3_074_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 75/593: V1V3_075_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_075_Firmicutes.fna -out ./work/V1V3_075_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 76/593: V1V3_076_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_076_Bacteroidetes.fna -out ./work/V1V3_076_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 77/593: V1V3_077_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_077_Gammaproteobacteria.fna -out ./work/V1V3_077_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 78/593: V1V3_078_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_078_Firmicutes.fna -out ./work/V1V3_078_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 79/593: V1V3_079_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_079_Bacteroidetes.fna -out ./work/V1V3_079_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 80/593: V1V3_080_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_080_Betaproteobacteria.fna -out ./work/V1V3_080_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 81/593: V1V3_081_Fusobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_081_Fusobacteria.fna -out ./work/V1V3_081_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 82/593: V1V3_082_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_082_Firmicutes.fna -out ./work/V1V3_082_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 83/593: V1V3_083_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_083_Bacteroidetes.fna -out ./work/V1V3_083_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 84/593: V1V3_084_Fusobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_084_Fusobacteria.fna -out ./work/V1V3_084_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 85/593: V1V3_085_Epsilonproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_085_Epsilonproteobacteria.fna -out ./work/V1V3_085_Epsilonproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 86/593: V1V3_086_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_086_Firmicutes.fna -out ./work/V1V3_086_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 87/593: V1V3_087_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_087_Firmicutes.fna -out ./work/V1V3_087_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 88/593: V1V3_088_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_088_Actinobacteria.fna -out ./work/V1V3_088_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 89/593: V1V3_089_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_089_Betaproteobacteria.fna -out ./work/V1V3_089_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 90/593: V1V3_090_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_090_Actinobacteria.fna -out ./work/V1V3_090_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 91/593: V1V3_091_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_091_Actinobacteria.fna -out ./work/V1V3_091_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 92/593: V1V3_092_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_092_Betaproteobacteria.fna -out ./work/V1V3_092_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 93/593: V1V3_093_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_093_Firmicutes.fna -out ./work/V1V3_093_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 94/593: V1V3_094_Fusobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_094_Fusobacteria.fna -out ./work/V1V3_094_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 95/593: V1V3_095_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_095_Betaproteobacteria.fna -out ./work/V1V3_095_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 96/593: V1V3_096_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_096_Firmicutes.fna -out ./work/V1V3_096_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 97/593: V1V3_097_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_097_Actinobacteria.fna -out ./work/V1V3_097_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 98/593: V1V3_098_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_098_Gammaproteobacteria.fna -out ./work/V1V3_098_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 99/593: V1V3_099_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_099_Firmicutes.fna -out ./work/V1V3_099_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 100/593: V1V3_100_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_100_Firmicutes.fna -out ./work/V1V3_100_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 101/593: V1V3_101_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_101_Actinobacteria.fna -out ./work/V1V3_101_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 102/593: V1V3_102_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_102_Gammaproteobacteria.fna -out ./work/V1V3_102_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 103/593: V1V3_103_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_103_Firmicutes.fna -out ./work/V1V3_103_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 104/593: V1V3_104_Fusobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_104_Fusobacteria.fna -out ./work/V1V3_104_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 105/593: V1V3_105_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_105_Firmicutes.fna -out ./work/V1V3_105_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 106/593: V1V3_106_Epsilonproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_106_Epsilonproteobacteria.fna -out ./work/V1V3_106_Epsilonproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 107/593: V1V3_107_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_107_Firmicutes.fna -out ./work/V1V3_107_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 108/593: V1V3_108_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_108_Actinobacteria.fna -out ./work/V1V3_108_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 109/593: V1V3_109_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_109_Actinobacteria.fna -out ./work/V1V3_109_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 110/593: V1V3_110_TM7.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_110_TM7.fna -out ./work/V1V3_110_TM7.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 111/593: V1V3_111_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_111_Bacteroidetes.fna -out ./work/V1V3_111_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 112/593: V1V3_112_Epsilonproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_112_Epsilonproteobacteria.fna -out ./work/V1V3_112_Epsilonproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 113/593: V1V3_113_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_113_Firmicutes.fna -out ./work/V1V3_113_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 114/593: V1V3_114_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_114_Firmicutes.fna -out ./work/V1V3_114_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 115/593: V1V3_115_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_115_Actinobacteria.fna -out ./work/V1V3_115_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 116/593: V1V3_116_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_116_Actinobacteria.fna -out ./work/V1V3_116_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 117/593: V1V3_117_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_117_Bacteroidetes.fna -out ./work/V1V3_117_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 118/593: V1V3_118_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_118_Firmicutes.fna -out ./work/V1V3_118_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 119/593: V1V3_119_TM7.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_119_TM7.fna -out ./work/V1V3_119_TM7.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 120/593: V1V3_120_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_120_Actinobacteria.fna -out ./work/V1V3_120_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 121/593: V1V3_121_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_121_Bacteroidetes.fna -out ./work/V1V3_121_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 122/593: V1V3_122_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_122_Actinobacteria.fna -out ./work/V1V3_122_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 123/593: V1V3_123_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_123_Bacteroidetes.fna -out ./work/V1V3_123_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 124/593: V1V3_124_Fusobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_124_Fusobacteria.fna -out ./work/V1V3_124_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 125/593: V1V3_125_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_125_Bacteroidetes.fna -out ./work/V1V3_125_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 126/593: V1V3_126_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_126_Firmicutes.fna -out ./work/V1V3_126_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 127/593: V1V3_127_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_127_Bacteroidetes.fna -out ./work/V1V3_127_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 128/593: V1V3_128_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_128_Actinobacteria.fna -out ./work/V1V3_128_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 129/593: V1V3_129_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_129_Bacteroidetes.fna -out ./work/V1V3_129_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 130/593: V1V3_130_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_130_Betaproteobacteria.fna -out ./work/V1V3_130_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 131/593: V1V3_131_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_131_Bacteroidetes.fna -out ./work/V1V3_131_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 132/593: V1V3_132_TM7.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_132_TM7.fna -out ./work/V1V3_132_TM7.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 133/593: V1V3_133_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_133_Actinobacteria.fna -out ./work/V1V3_133_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 134/593: V1V3_134_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_134_Firmicutes.fna -out ./work/V1V3_134_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 135/593: V1V3_135_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_135_Gammaproteobacteria.fna -out ./work/V1V3_135_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 136/593: V1V3_136_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_136_Actinobacteria.fna -out ./work/V1V3_136_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 137/593: V1V3_137_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_137_Firmicutes.fna -out ./work/V1V3_137_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 138/593: V1V3_138_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_138_Firmicutes.fna -out ./work/V1V3_138_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 139/593: V1V3_139_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_139_Bacteroidetes.fna -out ./work/V1V3_139_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 140/593: V1V3_140_Fusobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_140_Fusobacteria.fna -out ./work/V1V3_140_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 141/593: V1V3_141_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_141_Actinobacteria.fna -out ./work/V1V3_141_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 142/593: V1V3_142_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_142_Actinobacteria.fna -out ./work/V1V3_142_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 143/593: V1V3_143_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_143_Firmicutes.fna -out ./work/V1V3_143_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 144/593: V1V3_144_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_144_Bacteroidetes.fna -out ./work/V1V3_144_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 145/593: V1V3_145_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_145_Gammaproteobacteria.fna -out ./work/V1V3_145_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 146/593: V1V3_146_TM7.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_146_TM7.fna -out ./work/V1V3_146_TM7.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 147/593: V1V3_147_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_147_Actinobacteria.fna -out ./work/V1V3_147_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 148/593: V1V3_148_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_148_Bacteroidetes.fna -out ./work/V1V3_148_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 149/593: V1V3_149_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_149_Firmicutes.fna -out ./work/V1V3_149_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 150/593: V1V3_150_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_150_Firmicutes.fna -out ./work/V1V3_150_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 151/593: V1V3_151_Fusobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_151_Fusobacteria.fna -out ./work/V1V3_151_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 152/593: V1V3_152_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_152_Gammaproteobacteria.fna -out ./work/V1V3_152_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 153/593: V1V3_153_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_153_Bacteroidetes.fna -out ./work/V1V3_153_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 154/593: V1V3_154_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_154_Actinobacteria.fna -out ./work/V1V3_154_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 155/593: V1V3_155_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_155_Betaproteobacteria.fna -out ./work/V1V3_155_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 156/593: V1V3_156_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_156_Firmicutes.fna -out ./work/V1V3_156_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 157/593: V1V3_157_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_157_Betaproteobacteria.fna -out ./work/V1V3_157_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 158/593: V1V3_158_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_158_Firmicutes.fna -out ./work/V1V3_158_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 159/593: V1V3_159_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_159_Actinobacteria.fna -out ./work/V1V3_159_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 160/593: V1V3_160_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_160_Actinobacteria.fna -out ./work/V1V3_160_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 161/593: V1V3_161_Fusobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_161_Fusobacteria.fna -out ./work/V1V3_161_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 162/593: V1V3_162_TM7.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_162_TM7.fna -out ./work/V1V3_162_TM7.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 163/593: V1V3_163_Fusobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_163_Fusobacteria.fna -out ./work/V1V3_163_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 164/593: V1V3_164_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_164_Bacteroidetes.fna -out ./work/V1V3_164_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 165/593: V1V3_165_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_165_Actinobacteria.fna -out ./work/V1V3_165_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 166/593: V1V3_166_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_166_Bacteroidetes.fna -out ./work/V1V3_166_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 167/593: V1V3_167_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_167_Betaproteobacteria.fna -out ./work/V1V3_167_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 168/593: V1V3_168_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_168_Bacteroidetes.fna -out ./work/V1V3_168_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 169/593: V1V3_169_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_169_Bacteroidetes.fna -out ./work/V1V3_169_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 170/593: V1V3_170_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_170_Bacteroidetes.fna -out ./work/V1V3_170_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 171/593: V1V3_171_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_171_Bacteroidetes.fna -out ./work/V1V3_171_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 172/593: V1V3_172_TM7.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_172_TM7.fna -out ./work/V1V3_172_TM7.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 173/593: V1V3_173_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_173_Firmicutes.fna -out ./work/V1V3_173_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 174/593: V1V3_174_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_174_Firmicutes.fna -out ./work/V1V3_174_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 175/593: V1V3_175_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_175_Firmicutes.fna -out ./work/V1V3_175_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 176/593: V1V3_176_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_176_Actinobacteria.fna -out ./work/V1V3_176_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 177/593: V1V3_177_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_177_Betaproteobacteria.fna -out ./work/V1V3_177_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 178/593: V1V3_178_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_178_Bacteroidetes.fna -out ./work/V1V3_178_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 179/593: V1V3_179_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_179_Gammaproteobacteria.fna -out ./work/V1V3_179_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 180/593: V1V3_180_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_180_Actinobacteria.fna -out ./work/V1V3_180_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 181/593: V1V3_181_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_181_Betaproteobacteria.fna -out ./work/V1V3_181_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 182/593: V1V3_182_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_182_Actinobacteria.fna -out ./work/V1V3_182_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 183/593: V1V3_183_Spirochaetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_183_Spirochaetes.fna -out ./work/V1V3_183_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 184/593: V1V3_184_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_184_Actinobacteria.fna -out ./work/V1V3_184_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 185/593: V1V3_185_TM7.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_185_TM7.fna -out ./work/V1V3_185_TM7.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 186/593: V1V3_186_Fusobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_186_Fusobacteria.fna -out ./work/V1V3_186_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 187/593: V1V3_187_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_187_Actinobacteria.fna -out ./work/V1V3_187_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 188/593: V1V3_188_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_188_Actinobacteria.fna -out ./work/V1V3_188_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 189/593: V1V3_189_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_189_Firmicutes.fna -out ./work/V1V3_189_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 190/593: V1V3_190_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_190_Betaproteobacteria.fna -out ./work/V1V3_190_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 191/593: V1V3_191_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_191_Firmicutes.fna -out ./work/V1V3_191_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 192/593: V1V3_192_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_192_Firmicutes.fna -out ./work/V1V3_192_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 193/593: V1V3_193_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_193_Bacteroidetes.fna -out ./work/V1V3_193_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 194/593: V1V3_194_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_194_Actinobacteria.fna -out ./work/V1V3_194_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 195/593: V1V3_195_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_195_Firmicutes.fna -out ./work/V1V3_195_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 196/593: V1V3_196_Fusobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_196_Fusobacteria.fna -out ./work/V1V3_196_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 197/593: V1V3_197_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_197_Bacteroidetes.fna -out ./work/V1V3_197_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 198/593: V1V3_198_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_198_Firmicutes.fna -out ./work/V1V3_198_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 199/593: V1V3_199_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_199_Firmicutes.fna -out ./work/V1V3_199_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 200/593: V1V3_200_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_200_Bacteroidetes.fna -out ./work/V1V3_200_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 201/593: V1V3_201_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_201_Firmicutes.fna -out ./work/V1V3_201_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 202/593: V1V3_202_Fusobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_202_Fusobacteria.fna -out ./work/V1V3_202_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 203/593: V1V3_203_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_203_Gammaproteobacteria.fna -out ./work/V1V3_203_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 204/593: V1V3_204_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_204_Bacteroidetes.fna -out ./work/V1V3_204_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 205/593: V1V3_205_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_205_Actinobacteria.fna -out ./work/V1V3_205_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 206/593: V1V3_206_Fusobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_206_Fusobacteria.fna -out ./work/V1V3_206_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 207/593: V1V3_207_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_207_Actinobacteria.fna -out ./work/V1V3_207_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 208/593: V1V3_208_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_208_Firmicutes.fna -out ./work/V1V3_208_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 209/593: V1V3_209_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_209_Actinobacteria.fna -out ./work/V1V3_209_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 210/593: V1V3_210_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_210_Bacteroidetes.fna -out ./work/V1V3_210_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 211/593: V1V3_211_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_211_Actinobacteria.fna -out ./work/V1V3_211_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 212/593: V1V3_212_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_212_Firmicutes.fna -out ./work/V1V3_212_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 213/593: V1V3_213_Fusobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_213_Fusobacteria.fna -out ./work/V1V3_213_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 214/593: V1V3_214_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_214_Firmicutes.fna -out ./work/V1V3_214_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 215/593: V1V3_215_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_215_Gammaproteobacteria.fna -out ./work/V1V3_215_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 216/593: V1V3_216_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_216_Bacteroidetes.fna -out ./work/V1V3_216_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 217/593: V1V3_217_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_217_Gammaproteobacteria.fna -out ./work/V1V3_217_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 218/593: V1V3_218_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_218_Firmicutes.fna -out ./work/V1V3_218_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 219/593: V1V3_219_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_219_Actinobacteria.fna -out ./work/V1V3_219_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 220/593: V1V3_220_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_220_Betaproteobacteria.fna -out ./work/V1V3_220_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 221/593: V1V3_221_Fusobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_221_Fusobacteria.fna -out ./work/V1V3_221_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 222/593: V1V3_222_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_222_Firmicutes.fna -out ./work/V1V3_222_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 223/593: V1V3_223_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_223_Bacteroidetes.fna -out ./work/V1V3_223_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 224/593: V1V3_224_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_224_Bacteroidetes.fna -out ./work/V1V3_224_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 225/593: V1V3_225_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_225_Bacteroidetes.fna -out ./work/V1V3_225_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 226/593: V1V3_226_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_226_Firmicutes.fna -out ./work/V1V3_226_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 227/593: V1V3_227_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_227_Bacteroidetes.fna -out ./work/V1V3_227_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 228/593: V1V3_228_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_228_Gammaproteobacteria.fna -out ./work/V1V3_228_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 229/593: V1V3_229_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_229_Bacteroidetes.fna -out ./work/V1V3_229_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 230/593: V1V3_230_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_230_Firmicutes.fna -out ./work/V1V3_230_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 231/593: V1V3_231_TM7.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_231_TM7.fna -out ./work/V1V3_231_TM7.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 232/593: V1V3_232_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_232_Actinobacteria.fna -out ./work/V1V3_232_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 233/593: V1V3_233_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_233_Actinobacteria.fna -out ./work/V1V3_233_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 234/593: V1V3_234_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_234_Actinobacteria.fna -out ./work/V1V3_234_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 235/593: V1V3_235_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_235_Actinobacteria.fna -out ./work/V1V3_235_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 236/593: V1V3_236_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_236_Bacteroidetes.fna -out ./work/V1V3_236_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 237/593: V1V3_237_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_237_Bacteroidetes.fna -out ./work/V1V3_237_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 238/593: V1V3_238_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_238_Firmicutes.fna -out ./work/V1V3_238_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 239/593: V1V3_239_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_239_Actinobacteria.fna -out ./work/V1V3_239_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 240/593: V1V3_240_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_240_Actinobacteria.fna -out ./work/V1V3_240_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 241/593: V1V3_241_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_241_Bacteroidetes.fna -out ./work/V1V3_241_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 242/593: V1V3_242_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_242_Actinobacteria.fna -out ./work/V1V3_242_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 243/593: V1V3_243_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_243_Actinobacteria.fna -out ./work/V1V3_243_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 244/593: V1V3_244_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_244_Bacteroidetes.fna -out ./work/V1V3_244_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 245/593: V1V3_245_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_245_Bacteroidetes.fna -out ./work/V1V3_245_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 246/593: V1V3_246_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_246_Bacteroidetes.fna -out ./work/V1V3_246_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 247/593: V1V3_247_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_247_Gammaproteobacteria.fna -out ./work/V1V3_247_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 248/593: V1V3_248_Epsilonproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_248_Epsilonproteobacteria.fna -out ./work/V1V3_248_Epsilonproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 249/593: V1V3_249_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_249_Gammaproteobacteria.fna -out ./work/V1V3_249_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 250/593: V1V3_250_TM7.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_250_TM7.fna -out ./work/V1V3_250_TM7.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 251/593: V1V3_251_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_251_Firmicutes.fna -out ./work/V1V3_251_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 252/593: V1V3_252_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_252_Firmicutes.fna -out ./work/V1V3_252_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 253/593: V1V3_253_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_253_Bacteroidetes.fna -out ./work/V1V3_253_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 254/593: V1V3_254_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_254_Betaproteobacteria.fna -out ./work/V1V3_254_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 255/593: V1V3_255_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_255_Bacteroidetes.fna -out ./work/V1V3_255_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 256/593: V1V3_256_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_256_Firmicutes.fna -out ./work/V1V3_256_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 257/593: V1V3_257_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_257_Actinobacteria.fna -out ./work/V1V3_257_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 258/593: V1V3_258_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_258_Bacteroidetes.fna -out ./work/V1V3_258_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 259/593: V1V3_259_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_259_Firmicutes.fna -out ./work/V1V3_259_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 260/593: V1V3_260_Fusobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_260_Fusobacteria.fna -out ./work/V1V3_260_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 261/593: V1V3_261_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_261_Gammaproteobacteria.fna -out ./work/V1V3_261_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 262/593: V1V3_262_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_262_Firmicutes.fna -out ./work/V1V3_262_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 263/593: V1V3_263_Fusobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_263_Fusobacteria.fna -out ./work/V1V3_263_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 264/593: V1V3_264_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_264_Bacteroidetes.fna -out ./work/V1V3_264_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 265/593: V1V3_265_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_265_Actinobacteria.fna -out ./work/V1V3_265_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 266/593: V1V3_266_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_266_Actinobacteria.fna -out ./work/V1V3_266_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 267/593: V1V3_267_Fusobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_267_Fusobacteria.fna -out ./work/V1V3_267_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 268/593: V1V3_268_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_268_Firmicutes.fna -out ./work/V1V3_268_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 269/593: V1V3_269_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_269_Firmicutes.fna -out ./work/V1V3_269_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 270/593: V1V3_270_Epsilonproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_270_Epsilonproteobacteria.fna -out ./work/V1V3_270_Epsilonproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 271/593: V1V3_271_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_271_Actinobacteria.fna -out ./work/V1V3_271_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 272/593: V1V3_272_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_272_Firmicutes.fna -out ./work/V1V3_272_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 273/593: V1V3_273_Fusobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_273_Fusobacteria.fna -out ./work/V1V3_273_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 274/593: V1V3_274_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_274_Actinobacteria.fna -out ./work/V1V3_274_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 275/593: V1V3_275_Fusobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_275_Fusobacteria.fna -out ./work/V1V3_275_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 276/593: V1V3_276_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_276_Bacteroidetes.fna -out ./work/V1V3_276_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 277/593: V1V3_277_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_277_Bacteroidetes.fna -out ./work/V1V3_277_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 278/593: V1V3_278_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_278_Firmicutes.fna -out ./work/V1V3_278_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 279/593: V1V3_279_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_279_Firmicutes.fna -out ./work/V1V3_279_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 280/593: V1V3_280_Fusobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_280_Fusobacteria.fna -out ./work/V1V3_280_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 281/593: V1V3_281_Fusobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_281_Fusobacteria.fna -out ./work/V1V3_281_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 282/593: V1V3_282_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_282_Firmicutes.fna -out ./work/V1V3_282_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 283/593: V1V3_283_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_283_Bacteroidetes.fna -out ./work/V1V3_283_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 284/593: V1V3_284_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_284_Betaproteobacteria.fna -out ./work/V1V3_284_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 285/593: V1V3_285_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_285_Bacteroidetes.fna -out ./work/V1V3_285_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 286/593: V1V3_286_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_286_Firmicutes.fna -out ./work/V1V3_286_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 287/593: V1V3_287_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_287_Firmicutes.fna -out ./work/V1V3_287_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 288/593: V1V3_288_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_288_Firmicutes.fna -out ./work/V1V3_288_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 289/593: V1V3_289_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_289_Actinobacteria.fna -out ./work/V1V3_289_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 290/593: V1V3_290_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_290_Betaproteobacteria.fna -out ./work/V1V3_290_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 291/593: V1V3_291_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_291_Firmicutes.fna -out ./work/V1V3_291_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 292/593: V1V3_292_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_292_Bacteroidetes.fna -out ./work/V1V3_292_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 293/593: V1V3_293_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_293_Bacteroidetes.fna -out ./work/V1V3_293_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 294/593: V1V3_294_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_294_Bacteroidetes.fna -out ./work/V1V3_294_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 295/593: V1V3_295_TM7.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_295_TM7.fna -out ./work/V1V3_295_TM7.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 296/593: V1V3_296_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_296_Actinobacteria.fna -out ./work/V1V3_296_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 297/593: V1V3_297_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_297_Bacteroidetes.fna -out ./work/V1V3_297_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 298/593: V1V3_298_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_298_Gammaproteobacteria.fna -out ./work/V1V3_298_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 299/593: V1V3_299_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_299_Actinobacteria.fna -out ./work/V1V3_299_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 300/593: V1V3_300_Fusobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_300_Fusobacteria.fna -out ./work/V1V3_300_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 301/593: V1V3_301_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_301_Firmicutes.fna -out ./work/V1V3_301_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 302/593: V1V3_302_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_302_Gammaproteobacteria.fna -out ./work/V1V3_302_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 303/593: V1V3_303_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_303_Firmicutes.fna -out ./work/V1V3_303_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 304/593: V1V3_304_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_304_Betaproteobacteria.fna -out ./work/V1V3_304_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 305/593: V1V3_305_Fusobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_305_Fusobacteria.fna -out ./work/V1V3_305_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 306/593: V1V3_306_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_306_Bacteroidetes.fna -out ./work/V1V3_306_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 307/593: V1V3_307_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_307_Firmicutes.fna -out ./work/V1V3_307_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 308/593: V1V3_308_Spirochaetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_308_Spirochaetes.fna -out ./work/V1V3_308_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 309/593: V1V3_309_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_309_Firmicutes.fna -out ./work/V1V3_309_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 310/593: V1V3_310_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_310_Bacteroidetes.fna -out ./work/V1V3_310_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 311/593: V1V3_311_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_311_Firmicutes.fna -out ./work/V1V3_311_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 312/593: V1V3_312_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_312_Gammaproteobacteria.fna -out ./work/V1V3_312_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 313/593: V1V3_313_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_313_Bacteroidetes.fna -out ./work/V1V3_313_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 314/593: V1V3_314_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_314_Firmicutes.fna -out ./work/V1V3_314_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 315/593: V1V3_315_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_315_Bacteroidetes.fna -out ./work/V1V3_315_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 316/593: V1V3_316_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_316_Firmicutes.fna -out ./work/V1V3_316_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 317/593: V1V3_317_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_317_Bacteroidetes.fna -out ./work/V1V3_317_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 318/593: V1V3_318_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_318_Bacteroidetes.fna -out ./work/V1V3_318_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 319/593: V1V3_319_Fusobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_319_Fusobacteria.fna -out ./work/V1V3_319_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 320/593: V1V3_320_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_320_Firmicutes.fna -out ./work/V1V3_320_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 321/593: V1V3_321_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_321_Bacteroidetes.fna -out ./work/V1V3_321_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 322/593: V1V3_322_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_322_Betaproteobacteria.fna -out ./work/V1V3_322_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 323/593: V1V3_323_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_323_Actinobacteria.fna -out ./work/V1V3_323_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 324/593: V1V3_324_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_324_Actinobacteria.fna -out ./work/V1V3_324_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 325/593: V1V3_325_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_325_Firmicutes.fna -out ./work/V1V3_325_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 326/593: V1V3_326_Spirochaetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_326_Spirochaetes.fna -out ./work/V1V3_326_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 327/593: V1V3_327_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_327_Firmicutes.fna -out ./work/V1V3_327_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 328/593: V1V3_328_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_328_Betaproteobacteria.fna -out ./work/V1V3_328_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 329/593: V1V3_329_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_329_Firmicutes.fna -out ./work/V1V3_329_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 330/593: V1V3_330_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_330_Betaproteobacteria.fna -out ./work/V1V3_330_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 331/593: V1V3_331_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_331_Actinobacteria.fna -out ./work/V1V3_331_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 332/593: V1V3_332_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_332_Firmicutes.fna -out ./work/V1V3_332_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 333/593: V1V3_333_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_333_Firmicutes.fna -out ./work/V1V3_333_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 334/593: V1V3_334_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_334_Firmicutes.fna -out ./work/V1V3_334_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 335/593: V1V3_335_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_335_Gammaproteobacteria.fna -out ./work/V1V3_335_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 336/593: V1V3_336_Fusobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_336_Fusobacteria.fna -out ./work/V1V3_336_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 337/593: V1V3_337_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_337_Bacteroidetes.fna -out ./work/V1V3_337_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 338/593: V1V3_338_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_338_Firmicutes.fna -out ./work/V1V3_338_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 339/593: V1V3_339_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_339_Firmicutes.fna -out ./work/V1V3_339_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 340/593: V1V3_340_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_340_Actinobacteria.fna -out ./work/V1V3_340_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 341/593: V1V3_341_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_341_Betaproteobacteria.fna -out ./work/V1V3_341_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 342/593: V1V3_342_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_342_Bacteroidetes.fna -out ./work/V1V3_342_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 343/593: V1V3_343_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_343_Firmicutes.fna -out ./work/V1V3_343_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 344/593: V1V3_344_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_344_Firmicutes.fna -out ./work/V1V3_344_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 345/593: V1V3_345_Fusobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_345_Fusobacteria.fna -out ./work/V1V3_345_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 346/593: V1V3_346_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_346_Gammaproteobacteria.fna -out ./work/V1V3_346_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 347/593: V1V3_347_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_347_Actinobacteria.fna -out ./work/V1V3_347_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 348/593: V1V3_348_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_348_Firmicutes.fna -out ./work/V1V3_348_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 349/593: V1V3_349_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_349_Firmicutes.fna -out ./work/V1V3_349_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 350/593: V1V3_350_Fusobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_350_Fusobacteria.fna -out ./work/V1V3_350_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 351/593: V1V3_351_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_351_Actinobacteria.fna -out ./work/V1V3_351_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 352/593: V1V3_352_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_352_Firmicutes.fna -out ./work/V1V3_352_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 353/593: V1V3_353_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_353_Actinobacteria.fna -out ./work/V1V3_353_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 354/593: V1V3_354_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_354_Firmicutes.fna -out ./work/V1V3_354_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 355/593: V1V3_355_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_355_Actinobacteria.fna -out ./work/V1V3_355_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 356/593: V1V3_356_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_356_Bacteroidetes.fna -out ./work/V1V3_356_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 357/593: V1V3_357_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_357_Firmicutes.fna -out ./work/V1V3_357_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 358/593: V1V3_358_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_358_Bacteroidetes.fna -out ./work/V1V3_358_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 359/593: V1V3_359_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_359_Bacteroidetes.fna -out ./work/V1V3_359_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 360/593: V1V3_360_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_360_Firmicutes.fna -out ./work/V1V3_360_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 361/593: V1V3_361_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_361_Firmicutes.fna -out ./work/V1V3_361_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 362/593: V1V3_362_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_362_Actinobacteria.fna -out ./work/V1V3_362_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 363/593: V1V3_363_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_363_Bacteroidetes.fna -out ./work/V1V3_363_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 364/593: V1V3_364_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_364_Bacteroidetes.fna -out ./work/V1V3_364_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 365/593: V1V3_365_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_365_Bacteroidetes.fna -out ./work/V1V3_365_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 366/593: V1V3_366_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_366_Firmicutes.fna -out ./work/V1V3_366_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 367/593: V1V3_367_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_367_Firmicutes.fna -out ./work/V1V3_367_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 368/593: V1V3_368_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_368_Actinobacteria.fna -out ./work/V1V3_368_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 369/593: V1V3_369_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_369_Actinobacteria.fna -out ./work/V1V3_369_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 370/593: V1V3_370_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_370_Bacteroidetes.fna -out ./work/V1V3_370_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 371/593: V1V3_371_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_371_Actinobacteria.fna -out ./work/V1V3_371_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 372/593: V1V3_372_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_372_Gammaproteobacteria.fna -out ./work/V1V3_372_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 373/593: V1V3_373_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_373_Actinobacteria.fna -out ./work/V1V3_373_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 374/593: V1V3_374_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_374_Firmicutes.fna -out ./work/V1V3_374_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 375/593: V1V3_375_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_375_Bacteroidetes.fna -out ./work/V1V3_375_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 376/593: V1V3_376_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_376_Gammaproteobacteria.fna -out ./work/V1V3_376_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 377/593: V1V3_377_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_377_Firmicutes.fna -out ./work/V1V3_377_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 378/593: V1V3_378_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_378_Firmicutes.fna -out ./work/V1V3_378_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 379/593: V1V3_379_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_379_Bacteroidetes.fna -out ./work/V1V3_379_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 380/593: V1V3_380_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_380_Actinobacteria.fna -out ./work/V1V3_380_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 381/593: V1V3_381_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_381_Betaproteobacteria.fna -out ./work/V1V3_381_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 382/593: V1V3_382_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_382_Firmicutes.fna -out ./work/V1V3_382_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 383/593: V1V3_383_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_383_Actinobacteria.fna -out ./work/V1V3_383_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 384/593: V1V3_384_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_384_Bacteroidetes.fna -out ./work/V1V3_384_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 385/593: V1V3_385_TM7.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_385_TM7.fna -out ./work/V1V3_385_TM7.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 386/593: V1V3_386_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_386_Firmicutes.fna -out ./work/V1V3_386_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 387/593: V1V3_387_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_387_Firmicutes.fna -out ./work/V1V3_387_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 388/593: V1V3_388_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_388_Bacteroidetes.fna -out ./work/V1V3_388_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 389/593: V1V3_389_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_389_Firmicutes.fna -out ./work/V1V3_389_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 390/593: V1V3_390_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_390_Bacteroidetes.fna -out ./work/V1V3_390_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 391/593: V1V3_391_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_391_Actinobacteria.fna -out ./work/V1V3_391_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 392/593: V1V3_392_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_392_Firmicutes.fna -out ./work/V1V3_392_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 393/593: V1V3_393_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_393_Bacteroidetes.fna -out ./work/V1V3_393_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 394/593: V1V3_394_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_394_Firmicutes.fna -out ./work/V1V3_394_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 395/593: V1V3_395_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_395_Firmicutes.fna -out ./work/V1V3_395_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 396/593: V1V3_396_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_396_Betaproteobacteria.fna -out ./work/V1V3_396_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 397/593: V1V3_397_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_397_Bacteroidetes.fna -out ./work/V1V3_397_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 398/593: V1V3_398_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_398_Firmicutes.fna -out ./work/V1V3_398_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 399/593: V1V3_399_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_399_Actinobacteria.fna -out ./work/V1V3_399_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 400/593: V1V3_400_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_400_Bacteroidetes.fna -out ./work/V1V3_400_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 401/593: V1V3_401_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_401_Bacteroidetes.fna -out ./work/V1V3_401_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 402/593: V1V3_402_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_402_Bacteroidetes.fna -out ./work/V1V3_402_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 403/593: V1V3_403_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_403_Firmicutes.fna -out ./work/V1V3_403_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 404/593: V1V3_404_Epsilonproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_404_Epsilonproteobacteria.fna -out ./work/V1V3_404_Epsilonproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 405/593: V1V3_405_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_405_Firmicutes.fna -out ./work/V1V3_405_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 406/593: V1V3_406_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_406_Firmicutes.fna -out ./work/V1V3_406_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 407/593: V1V3_407_Fusobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_407_Fusobacteria.fna -out ./work/V1V3_407_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 408/593: V1V3_408_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_408_Firmicutes.fna -out ./work/V1V3_408_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 409/593: V1V3_409_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_409_Actinobacteria.fna -out ./work/V1V3_409_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 410/593: V1V3_410_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_410_Actinobacteria.fna -out ./work/V1V3_410_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 411/593: V1V3_411_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_411_Betaproteobacteria.fna -out ./work/V1V3_411_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 412/593: V1V3_412_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_412_Firmicutes.fna -out ./work/V1V3_412_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 413/593: V1V3_413_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_413_Actinobacteria.fna -out ./work/V1V3_413_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 414/593: V1V3_414_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_414_Actinobacteria.fna -out ./work/V1V3_414_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 415/593: V1V3_415_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_415_Actinobacteria.fna -out ./work/V1V3_415_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 416/593: V1V3_416_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_416_Firmicutes.fna -out ./work/V1V3_416_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 417/593: V1V3_417_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_417_Bacteroidetes.fna -out ./work/V1V3_417_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 418/593: V1V3_418_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_418_Firmicutes.fna -out ./work/V1V3_418_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 419/593: V1V3_419_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_419_Betaproteobacteria.fna -out ./work/V1V3_419_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 420/593: V1V3_420_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_420_Firmicutes.fna -out ./work/V1V3_420_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 421/593: V1V3_421_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_421_Betaproteobacteria.fna -out ./work/V1V3_421_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 422/593: V1V3_422_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_422_Bacteroidetes.fna -out ./work/V1V3_422_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 423/593: V1V3_423_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_423_Actinobacteria.fna -out ./work/V1V3_423_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 424/593: V1V3_424_Spirochaetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_424_Spirochaetes.fna -out ./work/V1V3_424_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 425/593: V1V3_425_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_425_Bacteroidetes.fna -out ./work/V1V3_425_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 426/593: V1V3_426_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_426_Gammaproteobacteria.fna -out ./work/V1V3_426_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 427/593: V1V3_427_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_427_Firmicutes.fna -out ./work/V1V3_427_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 428/593: V1V3_428_Epsilonproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_428_Epsilonproteobacteria.fna -out ./work/V1V3_428_Epsilonproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 429/593: V1V3_429_Fusobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_429_Fusobacteria.fna -out ./work/V1V3_429_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 430/593: V1V3_430_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_430_Betaproteobacteria.fna -out ./work/V1V3_430_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 431/593: V1V3_431_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_431_Bacteroidetes.fna -out ./work/V1V3_431_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 432/593: V1V3_432_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_432_Firmicutes.fna -out ./work/V1V3_432_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 433/593: V1V3_433_Fusobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_433_Fusobacteria.fna -out ./work/V1V3_433_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 434/593: V1V3_434_Spirochaetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_434_Spirochaetes.fna -out ./work/V1V3_434_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 435/593: V1V3_435_Fusobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_435_Fusobacteria.fna -out ./work/V1V3_435_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 436/593: V1V3_436_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_436_Firmicutes.fna -out ./work/V1V3_436_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 437/593: V1V3_437_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_437_Betaproteobacteria.fna -out ./work/V1V3_437_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 438/593: V1V3_438_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_438_Actinobacteria.fna -out ./work/V1V3_438_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 439/593: V1V3_439_Actinobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_439_Actinobacteria.fna -out ./work/V1V3_439_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 440/593: V1V3_440_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_440_Bacteroidetes.fna -out ./work/V1V3_440_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 441/593: V1V3_441_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_441_Bacteroidetes.fna -out ./work/V1V3_441_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 442/593: V1V3_442_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_442_Betaproteobacteria.fna -out ./work/V1V3_442_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 443/593: V1V3_443_Spirochaetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_443_Spirochaetes.fna -out ./work/V1V3_443_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 444/593: V1V3_444_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_444_Firmicutes.fna -out ./work/V1V3_444_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 445/593: V1V3_445_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_445_Firmicutes.fna -out ./work/V1V3_445_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 446/593: V1V3_446_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_446_Bacteroidetes.fna -out ./work/V1V3_446_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 447/593: V1V3_447_Spirochaetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_447_Spirochaetes.fna -out ./work/V1V3_447_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 448/593: V1V3_448_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_448_Bacteroidetes.fna -out ./work/V1V3_448_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 449/593: V1V3_449_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_449_Firmicutes.fna -out ./work/V1V3_449_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 450/593: V1V3_450_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_450_Gammaproteobacteria.fna -out ./work/V1V3_450_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 451/593: V1V3_451_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_451_Bacteroidetes.fna -out ./work/V1V3_451_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 452/593: V1V3_452_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_452_Bacteroidetes.fna -out ./work/V1V3_452_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 453/593: V1V3_453_Fusobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_453_Fusobacteria.fna -out ./work/V1V3_453_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 454/593: V1V3_454_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_454_Bacteroidetes.fna -out ./work/V1V3_454_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 455/593: V1V3_455_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_455_Betaproteobacteria.fna -out ./work/V1V3_455_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 456/593: V1V3_456_Spirochaetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_456_Spirochaetes.fna -out ./work/V1V3_456_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 457/593: V1V3_457_Spirochaetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_457_Spirochaetes.fna -out ./work/V1V3_457_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 458/593: V1V3_458_Spirochaetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_458_Spirochaetes.fna -out ./work/V1V3_458_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 459/593: V1V3_459_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_459_Betaproteobacteria.fna -out ./work/V1V3_459_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 460/593: V1V3_460_Epsilonproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_460_Epsilonproteobacteria.fna -out ./work/V1V3_460_Epsilonproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 461/593: V1V3_461_Spirochaetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_461_Spirochaetes.fna -out ./work/V1V3_461_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 462/593: V1V3_462_Spirochaetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_462_Spirochaetes.fna -out ./work/V1V3_462_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 463/593: V1V3_463_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_463_Bacteroidetes.fna -out ./work/V1V3_463_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 464/593: V1V3_464_Epsilonproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_464_Epsilonproteobacteria.fna -out ./work/V1V3_464_Epsilonproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 465/593: V1V3_465_Epsilonproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_465_Epsilonproteobacteria.fna -out ./work/V1V3_465_Epsilonproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 466/593: V1V3_466_Spirochaetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_466_Spirochaetes.fna -out ./work/V1V3_466_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 467/593: V1V3_467_Epsilonproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_467_Epsilonproteobacteria.fna -out ./work/V1V3_467_Epsilonproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 468/593: V1V3_468_Spirochaetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_468_Spirochaetes.fna -out ./work/V1V3_468_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 469/593: V1V3_469_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_469_Bacteroidetes.fna -out ./work/V1V3_469_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 470/593: V1V3_470_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_470_Bacteroidetes.fna -out ./work/V1V3_470_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 471/593: V1V3_471_Spirochaetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_471_Spirochaetes.fna -out ./work/V1V3_471_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 472/593: V1V3_472_Spirochaetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_472_Spirochaetes.fna -out ./work/V1V3_472_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 473/593: V1V3_473_Spirochaetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_473_Spirochaetes.fna -out ./work/V1V3_473_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 474/593: V1V3_474_Spirochaetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_474_Spirochaetes.fna -out ./work/V1V3_474_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 475/593: V1V3_475_Spirochaetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_475_Spirochaetes.fna -out ./work/V1V3_475_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 476/593: V1V3_476_Spirochaetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_476_Spirochaetes.fna -out ./work/V1V3_476_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 477/593: V1V3_477_Epsilonproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_477_Epsilonproteobacteria.fna -out ./work/V1V3_477_Epsilonproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 478/593: V1V3_478_Spirochaetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_478_Spirochaetes.fna -out ./work/V1V3_478_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 479/593: V1V3_479_Spirochaetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_479_Spirochaetes.fna -out ./work/V1V3_479_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 480/593: V1V3_480_Epsilonproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_480_Epsilonproteobacteria.fna -out ./work/V1V3_480_Epsilonproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 481/593: V1V3_481_Spirochaetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_481_Spirochaetes.fna -out ./work/V1V3_481_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 482/593: V1V3_482_Spirochaetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_482_Spirochaetes.fna -out ./work/V1V3_482_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 483/593: V1V3_483_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_483_Bacteroidetes.fna -out ./work/V1V3_483_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 484/593: V1V3_484_Spirochaetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_484_Spirochaetes.fna -out ./work/V1V3_484_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 485/593: V1V3_485_Spirochaetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_485_Spirochaetes.fna -out ./work/V1V3_485_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 486/593: V1V3_486_Spirochaetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_486_Spirochaetes.fna -out ./work/V1V3_486_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 487/593: V1V3_487_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_487_Bacteroidetes.fna -out ./work/V1V3_487_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 488/593: V1V3_488_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_488_Firmicutes.fna -out ./work/V1V3_488_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 489/593: V1V3_489_Epsilonproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_489_Epsilonproteobacteria.fna -out ./work/V1V3_489_Epsilonproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 490/593: V1V3_490_Spirochaetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_490_Spirochaetes.fna -out ./work/V1V3_490_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 491/593: V1V3_491_Spirochaetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_491_Spirochaetes.fna -out ./work/V1V3_491_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 492/593: V1V3_492_Spirochaetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_492_Spirochaetes.fna -out ./work/V1V3_492_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 493/593: V1V3_493_Spirochaetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_493_Spirochaetes.fna -out ./work/V1V3_493_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 494/593: V1V3_494_Spirochaetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_494_Spirochaetes.fna -out ./work/V1V3_494_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 495/593: V1V3_495_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_495_Firmicutes.fna -out ./work/V1V3_495_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 496/593: V1V3_496_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_496_Firmicutes.fna -out ./work/V1V3_496_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 497/593: V1V3_497_Spirochaetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_497_Spirochaetes.fna -out ./work/V1V3_497_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 498/593: V1V3_498_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_498_Bacteroidetes.fna -out ./work/V1V3_498_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 499/593: V1V3_499_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_499_Bacteroidetes.fna -out ./work/V1V3_499_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 500/593: V1V3_500_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_500_Bacteroidetes.fna -out ./work/V1V3_500_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 501/593: V1V3_501_Spirochaetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_501_Spirochaetes.fna -out ./work/V1V3_501_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 502/593: V1V3_502_Spirochaetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_502_Spirochaetes.fna -out ./work/V1V3_502_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 503/593: V1V3_503_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_503_Bacteroidetes.fna -out ./work/V1V3_503_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 504/593: V1V3_504_Epsilonproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_504_Epsilonproteobacteria.fna -out ./work/V1V3_504_Epsilonproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 505/593: V1V3_505_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_505_Bacteroidetes.fna -out ./work/V1V3_505_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 506/593: V1V3_506_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_506_Bacteroidetes.fna -out ./work/V1V3_506_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 507/593: V1V3_507_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_507_Firmicutes.fna -out ./work/V1V3_507_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 508/593: V1V3_508_Epsilonproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_508_Epsilonproteobacteria.fna -out ./work/V1V3_508_Epsilonproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 509/593: V1V3_509_Spirochaetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_509_Spirochaetes.fna -out ./work/V1V3_509_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 510/593: V1V3_510_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_510_Bacteroidetes.fna -out ./work/V1V3_510_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 511/593: V1V3_511_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_511_Bacteroidetes.fna -out ./work/V1V3_511_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 512/593: V1V3_512_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_512_Firmicutes.fna -out ./work/V1V3_512_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 513/593: V1V3_513_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_513_Bacteroidetes.fna -out ./work/V1V3_513_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 514/593: V1V3_514_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_514_Bacteroidetes.fna -out ./work/V1V3_514_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 515/593: V1V3_515_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_515_Bacteroidetes.fna -out ./work/V1V3_515_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 516/593: V1V3_516_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_516_Bacteroidetes.fna -out ./work/V1V3_516_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 517/593: V1V3_517_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_517_Bacteroidetes.fna -out ./work/V1V3_517_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 518/593: V1V3_518_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_518_Betaproteobacteria.fna -out ./work/V1V3_518_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 519/593: V1V3_519_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_519_Firmicutes.fna -out ./work/V1V3_519_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 520/593: V1V3_520_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_520_Bacteroidetes.fna -out ./work/V1V3_520_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 521/593: V1V3_521_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_521_Firmicutes.fna -out ./work/V1V3_521_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 522/593: V1V3_522_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_522_Bacteroidetes.fna -out ./work/V1V3_522_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 523/593: V1V3_523_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_523_Bacteroidetes.fna -out ./work/V1V3_523_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 524/593: V1V3_524_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_524_Firmicutes.fna -out ./work/V1V3_524_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 525/593: V1V3_525_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_525_Firmicutes.fna -out ./work/V1V3_525_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 526/593: V1V3_526_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_526_Bacteroidetes.fna -out ./work/V1V3_526_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 527/593: V1V3_527_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_527_Bacteroidetes.fna -out ./work/V1V3_527_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 528/593: V1V3_528_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_528_Bacteroidetes.fna -out ./work/V1V3_528_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 529/593: V1V3_529_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_529_Firmicutes.fna -out ./work/V1V3_529_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 530/593: V1V3_530_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_530_Firmicutes.fna -out ./work/V1V3_530_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 531/593: V1V3_531_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_531_Bacteroidetes.fna -out ./work/V1V3_531_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 532/593: V1V3_532_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_532_Bacteroidetes.fna -out ./work/V1V3_532_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 533/593: V1V3_533_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_533_Bacteroidetes.fna -out ./work/V1V3_533_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 534/593: V1V3_534_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_534_Bacteroidetes.fna -out ./work/V1V3_534_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 535/593: V1V3_535_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_535_Firmicutes.fna -out ./work/V1V3_535_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 536/593: V1V3_536_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_536_Firmicutes.fna -out ./work/V1V3_536_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 537/593: V1V3_537_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_537_Bacteroidetes.fna -out ./work/V1V3_537_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 538/593: V1V3_538_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_538_Bacteroidetes.fna -out ./work/V1V3_538_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 539/593: V1V3_539_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_539_Bacteroidetes.fna -out ./work/V1V3_539_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 540/593: V1V3_540_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_540_Firmicutes.fna -out ./work/V1V3_540_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 541/593: V1V3_541_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_541_Bacteroidetes.fna -out ./work/V1V3_541_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 542/593: V1V3_542_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_542_Firmicutes.fna -out ./work/V1V3_542_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 543/593: V1V3_543_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_543_Firmicutes.fna -out ./work/V1V3_543_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 544/593: V1V3_544_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_544_Betaproteobacteria.fna -out ./work/V1V3_544_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 545/593: V1V3_545_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_545_Bacteroidetes.fna -out ./work/V1V3_545_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 546/593: V1V3_546_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_546_Firmicutes.fna -out ./work/V1V3_546_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 547/593: V1V3_547_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_547_Bacteroidetes.fna -out ./work/V1V3_547_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 548/593: V1V3_548_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_548_Bacteroidetes.fna -out ./work/V1V3_548_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 549/593: V1V3_549_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_549_Bacteroidetes.fna -out ./work/V1V3_549_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 550/593: V1V3_550_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_550_Betaproteobacteria.fna -out ./work/V1V3_550_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 551/593: V1V3_551_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_551_Bacteroidetes.fna -out ./work/V1V3_551_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 552/593: V1V3_552_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_552_Firmicutes.fna -out ./work/V1V3_552_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 553/593: V1V3_553_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_553_Firmicutes.fna -out ./work/V1V3_553_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 554/593: V1V3_554_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_554_Firmicutes.fna -out ./work/V1V3_554_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 555/593: V1V3_555_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_555_Firmicutes.fna -out ./work/V1V3_555_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 556/593: V1V3_556_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_556_Bacteroidetes.fna -out ./work/V1V3_556_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 557/593: V1V3_557_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_557_Firmicutes.fna -out ./work/V1V3_557_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 558/593: V1V3_558_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_558_Betaproteobacteria.fna -out ./work/V1V3_558_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 559/593: V1V3_559_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_559_Bacteroidetes.fna -out ./work/V1V3_559_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 560/593: V1V3_560_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_560_Bacteroidetes.fna -out ./work/V1V3_560_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 561/593: V1V3_561_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_561_Firmicutes.fna -out ./work/V1V3_561_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 562/593: V1V3_562_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_562_Firmicutes.fna -out ./work/V1V3_562_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 563/593: V1V3_563_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_563_Firmicutes.fna -out ./work/V1V3_563_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 564/593: V1V3_564_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_564_Firmicutes.fna -out ./work/V1V3_564_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 565/593: V1V3_565_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_565_Bacteroidetes.fna -out ./work/V1V3_565_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 566/593: V1V3_566_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_566_Betaproteobacteria.fna -out ./work/V1V3_566_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 567/593: V1V3_567_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_567_Firmicutes.fna -out ./work/V1V3_567_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 568/593: V1V3_568_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_568_Bacteroidetes.fna -out ./work/V1V3_568_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 569/593: V1V3_569_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_569_Bacteroidetes.fna -out ./work/V1V3_569_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 570/593: V1V3_570_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_570_Firmicutes.fna -out ./work/V1V3_570_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 571/593: V1V3_571_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_571_Bacteroidetes.fna -out ./work/V1V3_571_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 572/593: V1V3_572_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_572_Bacteroidetes.fna -out ./work/V1V3_572_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 573/593: V1V3_573_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_573_Betaproteobacteria.fna -out ./work/V1V3_573_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 574/593: V1V3_574_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_574_Firmicutes.fna -out ./work/V1V3_574_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 575/593: V1V3_575_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_575_Bacteroidetes.fna -out ./work/V1V3_575_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 576/593: V1V3_576_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_576_Betaproteobacteria.fna -out ./work/V1V3_576_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 577/593: V1V3_577_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_577_Bacteroidetes.fna -out ./work/V1V3_577_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 578/593: V1V3_578_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_578_Bacteroidetes.fna -out ./work/V1V3_578_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 579/593: V1V3_579_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_579_Bacteroidetes.fna -out ./work/V1V3_579_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 580/593: V1V3_580_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_580_Bacteroidetes.fna -out ./work/V1V3_580_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 581/593: V1V3_581_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_581_Bacteroidetes.fna -out ./work/V1V3_581_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 582/593: V1V3_582_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_582_Firmicutes.fna -out ./work/V1V3_582_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 583/593: V1V3_583_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_583_Bacteroidetes.fna -out ./work/V1V3_583_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 584/593: V1V3_584_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_584_Bacteroidetes.fna -out ./work/V1V3_584_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 585/593: V1V3_585_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_585_Bacteroidetes.fna -out ./work/V1V3_585_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 586/593: V1V3_586_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_586_Bacteroidetes.fna -out ./work/V1V3_586_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 587/593: V1V3_587_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_587_Bacteroidetes.fna -out ./work/V1V3_587_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 588/593: V1V3_588_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_588_Bacteroidetes.fna -out ./work/V1V3_588_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 589/593: V1V3_589_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_589_Firmicutes.fna -out ./work/V1V3_589_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 590/593: V1V3_590_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_590_Firmicutes.fna -out ./work/V1V3_590_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 591/593: V1V3_591_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_591_Firmicutes.fna -out ./work/V1V3_591_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 592/593: V1V3_592_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_592_Firmicutes.fna -out ./work/V1V3_592_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 593/593: V1V3_593_Firmicutes.fna in args.outdir'
blastn  -db ../BLASTDB_ABUND/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V1V3_593_Firmicutes.fna -out ./work/V1V3_593_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
