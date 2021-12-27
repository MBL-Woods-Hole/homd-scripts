#!/bin/bash

echo '
  Blasting 1/481: V3V5_001_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_001_Firmicutes.fna -out ./work/V3V5_001_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 2/481: V3V5_002_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_002_Firmicutes.fna -out ./work/V3V5_002_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 3/481: V3V5_003_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_003_Firmicutes.fna -out ./work/V3V5_003_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 4/481: V3V5_004_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_004_Firmicutes.fna -out ./work/V3V5_004_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 5/481: V3V5_005_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_005_Betaproteobacteria.fna -out ./work/V3V5_005_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 6/481: V3V5_006_Fusobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_006_Fusobacteria.fna -out ./work/V3V5_006_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 7/481: V3V5_007_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_007_Bacteroidetes.fna -out ./work/V3V5_007_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 8/481: V3V5_008_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_008_Bacteroidetes.fna -out ./work/V3V5_008_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 9/481: V3V5_009_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_009_Firmicutes.fna -out ./work/V3V5_009_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 10/481: V3V5_010_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_010_Firmicutes.fna -out ./work/V3V5_010_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 11/481: V3V5_011_Actinobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_011_Actinobacteria.fna -out ./work/V3V5_011_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 12/481: V3V5_012_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_012_Firmicutes.fna -out ./work/V3V5_012_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 13/481: V3V5_013_Actinobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_013_Actinobacteria.fna -out ./work/V3V5_013_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 14/481: V3V5_014_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_014_Gammaproteobacteria.fna -out ./work/V3V5_014_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 15/481: V3V5_015_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_015_Gammaproteobacteria.fna -out ./work/V3V5_015_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 16/481: V3V5_016_Fusobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_016_Fusobacteria.fna -out ./work/V3V5_016_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 17/481: V3V5_017_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_017_Gammaproteobacteria.fna -out ./work/V3V5_017_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 18/481: V3V5_018_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_018_Firmicutes.fna -out ./work/V3V5_018_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 19/481: V3V5_019_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_019_Gammaproteobacteria.fna -out ./work/V3V5_019_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 20/481: V3V5_020_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_020_Betaproteobacteria.fna -out ./work/V3V5_020_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 21/481: V3V5_021_Fusobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_021_Fusobacteria.fna -out ./work/V3V5_021_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 22/481: V3V5_022_Fusobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_022_Fusobacteria.fna -out ./work/V3V5_022_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 23/481: V3V5_023_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_023_Gammaproteobacteria.fna -out ./work/V3V5_023_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 24/481: V3V5_024_Actinobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_024_Actinobacteria.fna -out ./work/V3V5_024_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 25/481: V3V5_025_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_025_Gammaproteobacteria.fna -out ./work/V3V5_025_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 26/481: V3V5_026_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_026_Bacteroidetes.fna -out ./work/V3V5_026_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 27/481: V3V5_027_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_027_Bacteroidetes.fna -out ./work/V3V5_027_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 28/481: V3V5_028_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_028_Betaproteobacteria.fna -out ./work/V3V5_028_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 29/481: V3V5_029_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_029_Bacteroidetes.fna -out ./work/V3V5_029_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 30/481: V3V5_030_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_030_Bacteroidetes.fna -out ./work/V3V5_030_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 31/481: V3V5_031_Epsilonproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_031_Epsilonproteobacteria.fna -out ./work/V3V5_031_Epsilonproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 32/481: V3V5_032_Actinobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_032_Actinobacteria.fna -out ./work/V3V5_032_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 33/481: V3V5_033_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_033_Firmicutes.fna -out ./work/V3V5_033_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 34/481: V3V5_034_Actinobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_034_Actinobacteria.fna -out ./work/V3V5_034_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 35/481: V3V5_035_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_035_Gammaproteobacteria.fna -out ./work/V3V5_035_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 36/481: V3V5_036_Fusobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_036_Fusobacteria.fna -out ./work/V3V5_036_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 37/481: V3V5_037_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_037_Gammaproteobacteria.fna -out ./work/V3V5_037_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 38/481: V3V5_038_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_038_Firmicutes.fna -out ./work/V3V5_038_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 39/481: V3V5_039_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_039_Bacteroidetes.fna -out ./work/V3V5_039_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 40/481: V3V5_040_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_040_Bacteroidetes.fna -out ./work/V3V5_040_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 41/481: V3V5_041_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_041_Gammaproteobacteria.fna -out ./work/V3V5_041_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 42/481: V3V5_042_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_042_Firmicutes.fna -out ./work/V3V5_042_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 43/481: V3V5_043_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_043_Firmicutes.fna -out ./work/V3V5_043_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 44/481: V3V5_044_Actinobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_044_Actinobacteria.fna -out ./work/V3V5_044_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 45/481: V3V5_045_Fusobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_045_Fusobacteria.fna -out ./work/V3V5_045_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 46/481: V3V5_046_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_046_Bacteroidetes.fna -out ./work/V3V5_046_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 47/481: V3V5_047_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_047_Bacteroidetes.fna -out ./work/V3V5_047_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 48/481: V3V5_048_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_048_Bacteroidetes.fna -out ./work/V3V5_048_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 49/481: V3V5_049_Fusobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_049_Fusobacteria.fna -out ./work/V3V5_049_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 50/481: V3V5_050_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_050_Betaproteobacteria.fna -out ./work/V3V5_050_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 51/481: V3V5_051_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_051_Bacteroidetes.fna -out ./work/V3V5_051_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 52/481: V3V5_052_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_052_Gammaproteobacteria.fna -out ./work/V3V5_052_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 53/481: V3V5_053_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_053_Firmicutes.fna -out ./work/V3V5_053_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 54/481: V3V5_054_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_054_Gammaproteobacteria.fna -out ./work/V3V5_054_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 55/481: V3V5_055_Fusobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_055_Fusobacteria.fna -out ./work/V3V5_055_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 56/481: V3V5_056_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_056_Bacteroidetes.fna -out ./work/V3V5_056_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 57/481: V3V5_057_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_057_Bacteroidetes.fna -out ./work/V3V5_057_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 58/481: V3V5_058_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_058_Betaproteobacteria.fna -out ./work/V3V5_058_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 59/481: V3V5_059_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_059_Bacteroidetes.fna -out ./work/V3V5_059_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 60/481: V3V5_060_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_060_Firmicutes.fna -out ./work/V3V5_060_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 61/481: V3V5_061_Actinobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_061_Actinobacteria.fna -out ./work/V3V5_061_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 62/481: V3V5_062_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_062_Firmicutes.fna -out ./work/V3V5_062_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 63/481: V3V5_063_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_063_Bacteroidetes.fna -out ./work/V3V5_063_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 64/481: V3V5_064_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_064_Bacteroidetes.fna -out ./work/V3V5_064_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 65/481: V3V5_065_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_065_Bacteroidetes.fna -out ./work/V3V5_065_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 66/481: V3V5_066_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_066_Bacteroidetes.fna -out ./work/V3V5_066_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 67/481: V3V5_067_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_067_Firmicutes.fna -out ./work/V3V5_067_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 68/481: V3V5_068_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_068_Bacteroidetes.fna -out ./work/V3V5_068_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 69/481: V3V5_069_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_069_Bacteroidetes.fna -out ./work/V3V5_069_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 70/481: V3V5_070_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_070_Firmicutes.fna -out ./work/V3V5_070_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 71/481: V3V5_071_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_071_Bacteroidetes.fna -out ./work/V3V5_071_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 72/481: V3V5_072_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_072_Firmicutes.fna -out ./work/V3V5_072_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 73/481: V3V5_073_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_073_Firmicutes.fna -out ./work/V3V5_073_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 74/481: V3V5_074_Fusobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_074_Fusobacteria.fna -out ./work/V3V5_074_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 75/481: V3V5_075_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_075_Bacteroidetes.fna -out ./work/V3V5_075_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 76/481: V3V5_076_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_076_Firmicutes.fna -out ./work/V3V5_076_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 77/481: V3V5_077_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_077_Betaproteobacteria.fna -out ./work/V3V5_077_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 78/481: V3V5_078_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_078_Gammaproteobacteria.fna -out ./work/V3V5_078_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 79/481: V3V5_079_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_079_Bacteroidetes.fna -out ./work/V3V5_079_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 80/481: V3V5_080_Actinobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_080_Actinobacteria.fna -out ./work/V3V5_080_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 81/481: V3V5_081_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_081_Bacteroidetes.fna -out ./work/V3V5_081_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 82/481: V3V5_082_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_082_Bacteroidetes.fna -out ./work/V3V5_082_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 83/481: V3V5_083_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_083_Bacteroidetes.fna -out ./work/V3V5_083_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 84/481: V3V5_084_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_084_Bacteroidetes.fna -out ./work/V3V5_084_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 85/481: V3V5_085_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_085_Bacteroidetes.fna -out ./work/V3V5_085_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 86/481: V3V5_086_Fusobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_086_Fusobacteria.fna -out ./work/V3V5_086_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 87/481: V3V5_087_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_087_Firmicutes.fna -out ./work/V3V5_087_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 88/481: V3V5_088_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_088_Bacteroidetes.fna -out ./work/V3V5_088_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 89/481: V3V5_089_Spirochaetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_089_Spirochaetes.fna -out ./work/V3V5_089_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 90/481: V3V5_090_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_090_Bacteroidetes.fna -out ./work/V3V5_090_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 91/481: V3V5_091_Actinobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_091_Actinobacteria.fna -out ./work/V3V5_091_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 92/481: V3V5_092_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_092_Firmicutes.fna -out ./work/V3V5_092_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 93/481: V3V5_093_Fusobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_093_Fusobacteria.fna -out ./work/V3V5_093_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 94/481: V3V5_094_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_094_Bacteroidetes.fna -out ./work/V3V5_094_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 95/481: V3V5_095_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_095_Gammaproteobacteria.fna -out ./work/V3V5_095_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 96/481: V3V5_096_Fusobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_096_Fusobacteria.fna -out ./work/V3V5_096_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 97/481: V3V5_097_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_097_Bacteroidetes.fna -out ./work/V3V5_097_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 98/481: V3V5_098_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_098_Gammaproteobacteria.fna -out ./work/V3V5_098_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 99/481: V3V5_099_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_099_Firmicutes.fna -out ./work/V3V5_099_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 100/481: V3V5_100_Epsilonproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_100_Epsilonproteobacteria.fna -out ./work/V3V5_100_Epsilonproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 101/481: V3V5_101_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_101_Gammaproteobacteria.fna -out ./work/V3V5_101_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 102/481: V3V5_102_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_102_Gammaproteobacteria.fna -out ./work/V3V5_102_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 103/481: V3V5_103_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_103_Bacteroidetes.fna -out ./work/V3V5_103_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 104/481: V3V5_104_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_104_Betaproteobacteria.fna -out ./work/V3V5_104_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 105/481: V3V5_105_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_105_Bacteroidetes.fna -out ./work/V3V5_105_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 106/481: V3V5_106_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_106_Firmicutes.fna -out ./work/V3V5_106_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 107/481: V3V5_107_Actinobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_107_Actinobacteria.fna -out ./work/V3V5_107_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 108/481: V3V5_108_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_108_Firmicutes.fna -out ./work/V3V5_108_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 109/481: V3V5_109_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_109_Bacteroidetes.fna -out ./work/V3V5_109_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 110/481: V3V5_110_Fusobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_110_Fusobacteria.fna -out ./work/V3V5_110_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 111/481: V3V5_111_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_111_Bacteroidetes.fna -out ./work/V3V5_111_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 112/481: V3V5_112_Spirochaetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_112_Spirochaetes.fna -out ./work/V3V5_112_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 113/481: V3V5_113_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_113_Bacteroidetes.fna -out ./work/V3V5_113_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 114/481: V3V5_114_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_114_Betaproteobacteria.fna -out ./work/V3V5_114_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 115/481: V3V5_115_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_115_Firmicutes.fna -out ./work/V3V5_115_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 116/481: V3V5_116_Actinobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_116_Actinobacteria.fna -out ./work/V3V5_116_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 117/481: V3V5_117_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_117_Betaproteobacteria.fna -out ./work/V3V5_117_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 118/481: V3V5_118_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_118_Bacteroidetes.fna -out ./work/V3V5_118_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 119/481: V3V5_119_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_119_Firmicutes.fna -out ./work/V3V5_119_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 120/481: V3V5_120_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_120_Gammaproteobacteria.fna -out ./work/V3V5_120_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 121/481: V3V5_121_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_121_Bacteroidetes.fna -out ./work/V3V5_121_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 122/481: V3V5_122_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_122_Bacteroidetes.fna -out ./work/V3V5_122_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 123/481: V3V5_123_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_123_Bacteroidetes.fna -out ./work/V3V5_123_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 124/481: V3V5_124_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_124_Bacteroidetes.fna -out ./work/V3V5_124_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 125/481: V3V5_125_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_125_Firmicutes.fna -out ./work/V3V5_125_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 126/481: V3V5_126_Fusobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_126_Fusobacteria.fna -out ./work/V3V5_126_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 127/481: V3V5_127_Spirochaetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_127_Spirochaetes.fna -out ./work/V3V5_127_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 128/481: V3V5_128_Actinobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_128_Actinobacteria.fna -out ./work/V3V5_128_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 129/481: V3V5_129_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_129_Bacteroidetes.fna -out ./work/V3V5_129_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 130/481: V3V5_130_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_130_Bacteroidetes.fna -out ./work/V3V5_130_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 131/481: V3V5_131_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_131_Firmicutes.fna -out ./work/V3V5_131_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 132/481: V3V5_132_Epsilonproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_132_Epsilonproteobacteria.fna -out ./work/V3V5_132_Epsilonproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 133/481: V3V5_133_Fusobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_133_Fusobacteria.fna -out ./work/V3V5_133_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 134/481: V3V5_134_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_134_Bacteroidetes.fna -out ./work/V3V5_134_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 135/481: V3V5_135_Spirochaetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_135_Spirochaetes.fna -out ./work/V3V5_135_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 136/481: V3V5_136_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_136_Bacteroidetes.fna -out ./work/V3V5_136_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 137/481: V3V5_137_Actinobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_137_Actinobacteria.fna -out ./work/V3V5_137_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 138/481: V3V5_138_Actinobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_138_Actinobacteria.fna -out ./work/V3V5_138_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 139/481: V3V5_139_Actinobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_139_Actinobacteria.fna -out ./work/V3V5_139_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 140/481: V3V5_140_Fusobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_140_Fusobacteria.fna -out ./work/V3V5_140_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 141/481: V3V5_141_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_141_Firmicutes.fna -out ./work/V3V5_141_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 142/481: V3V5_142_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_142_Bacteroidetes.fna -out ./work/V3V5_142_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 143/481: V3V5_143_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_143_Bacteroidetes.fna -out ./work/V3V5_143_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 144/481: V3V5_144_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_144_Firmicutes.fna -out ./work/V3V5_144_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 145/481: V3V5_145_Fusobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_145_Fusobacteria.fna -out ./work/V3V5_145_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 146/481: V3V5_146_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_146_Betaproteobacteria.fna -out ./work/V3V5_146_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 147/481: V3V5_147_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_147_Bacteroidetes.fna -out ./work/V3V5_147_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 148/481: V3V5_148_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_148_Firmicutes.fna -out ./work/V3V5_148_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 149/481: V3V5_149_Fusobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_149_Fusobacteria.fna -out ./work/V3V5_149_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 150/481: V3V5_150_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_150_Bacteroidetes.fna -out ./work/V3V5_150_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 151/481: V3V5_151_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_151_Gammaproteobacteria.fna -out ./work/V3V5_151_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 152/481: V3V5_152_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_152_Bacteroidetes.fna -out ./work/V3V5_152_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 153/481: V3V5_153_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_153_Firmicutes.fna -out ./work/V3V5_153_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 154/481: V3V5_154_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_154_Gammaproteobacteria.fna -out ./work/V3V5_154_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 155/481: V3V5_155_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_155_Bacteroidetes.fna -out ./work/V3V5_155_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 156/481: V3V5_156_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_156_Bacteroidetes.fna -out ./work/V3V5_156_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 157/481: V3V5_157_Fusobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_157_Fusobacteria.fna -out ./work/V3V5_157_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 158/481: V3V5_158_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_158_Bacteroidetes.fna -out ./work/V3V5_158_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 159/481: V3V5_159_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_159_Firmicutes.fna -out ./work/V3V5_159_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 160/481: V3V5_160_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_160_Bacteroidetes.fna -out ./work/V3V5_160_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 161/481: V3V5_161_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_161_Bacteroidetes.fna -out ./work/V3V5_161_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 162/481: V3V5_162_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_162_Bacteroidetes.fna -out ./work/V3V5_162_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 163/481: V3V5_163_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_163_Betaproteobacteria.fna -out ./work/V3V5_163_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 164/481: V3V5_164_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_164_Firmicutes.fna -out ./work/V3V5_164_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 165/481: V3V5_165_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_165_Bacteroidetes.fna -out ./work/V3V5_165_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 166/481: V3V5_166_Fusobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_166_Fusobacteria.fna -out ./work/V3V5_166_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 167/481: V3V5_167_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_167_Bacteroidetes.fna -out ./work/V3V5_167_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 168/481: V3V5_168_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_168_Firmicutes.fna -out ./work/V3V5_168_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 169/481: V3V5_169_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_169_Betaproteobacteria.fna -out ./work/V3V5_169_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 170/481: V3V5_170_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_170_Gammaproteobacteria.fna -out ./work/V3V5_170_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 171/481: V3V5_171_Fusobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_171_Fusobacteria.fna -out ./work/V3V5_171_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 172/481: V3V5_172_Actinobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_172_Actinobacteria.fna -out ./work/V3V5_172_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 173/481: V3V5_173_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_173_Bacteroidetes.fna -out ./work/V3V5_173_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 174/481: V3V5_174_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_174_Bacteroidetes.fna -out ./work/V3V5_174_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 175/481: V3V5_175_Fusobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_175_Fusobacteria.fna -out ./work/V3V5_175_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 176/481: V3V5_176_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_176_Bacteroidetes.fna -out ./work/V3V5_176_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 177/481: V3V5_177_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_177_Firmicutes.fna -out ./work/V3V5_177_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 178/481: V3V5_178_Fusobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_178_Fusobacteria.fna -out ./work/V3V5_178_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 179/481: V3V5_179_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_179_Bacteroidetes.fna -out ./work/V3V5_179_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 180/481: V3V5_180_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_180_Firmicutes.fna -out ./work/V3V5_180_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 181/481: V3V5_181_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_181_Bacteroidetes.fna -out ./work/V3V5_181_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 182/481: V3V5_182_Fusobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_182_Fusobacteria.fna -out ./work/V3V5_182_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 183/481: V3V5_183_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_183_Bacteroidetes.fna -out ./work/V3V5_183_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 184/481: V3V5_184_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_184_Betaproteobacteria.fna -out ./work/V3V5_184_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 185/481: V3V5_185_Fusobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_185_Fusobacteria.fna -out ./work/V3V5_185_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 186/481: V3V5_186_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_186_Bacteroidetes.fna -out ./work/V3V5_186_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 187/481: V3V5_187_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_187_Firmicutes.fna -out ./work/V3V5_187_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 188/481: V3V5_188_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_188_Bacteroidetes.fna -out ./work/V3V5_188_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 189/481: V3V5_189_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_189_Firmicutes.fna -out ./work/V3V5_189_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 190/481: V3V5_190_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_190_Betaproteobacteria.fna -out ./work/V3V5_190_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 191/481: V3V5_191_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_191_Bacteroidetes.fna -out ./work/V3V5_191_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 192/481: V3V5_192_Actinobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_192_Actinobacteria.fna -out ./work/V3V5_192_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 193/481: V3V5_193_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_193_Firmicutes.fna -out ./work/V3V5_193_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 194/481: V3V5_194_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_194_Bacteroidetes.fna -out ./work/V3V5_194_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 195/481: V3V5_195_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_195_Firmicutes.fna -out ./work/V3V5_195_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 196/481: V3V5_196_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_196_Bacteroidetes.fna -out ./work/V3V5_196_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 197/481: V3V5_197_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_197_Firmicutes.fna -out ./work/V3V5_197_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 198/481: V3V5_198_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_198_Firmicutes.fna -out ./work/V3V5_198_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 199/481: V3V5_199_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_199_Gammaproteobacteria.fna -out ./work/V3V5_199_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 200/481: V3V5_200_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_200_Firmicutes.fna -out ./work/V3V5_200_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 201/481: V3V5_201_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_201_Bacteroidetes.fna -out ./work/V3V5_201_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 202/481: V3V5_202_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_202_Bacteroidetes.fna -out ./work/V3V5_202_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 203/481: V3V5_203_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_203_Bacteroidetes.fna -out ./work/V3V5_203_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 204/481: V3V5_204_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_204_Bacteroidetes.fna -out ./work/V3V5_204_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 205/481: V3V5_205_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_205_Bacteroidetes.fna -out ./work/V3V5_205_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 206/481: V3V5_206_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_206_Firmicutes.fna -out ./work/V3V5_206_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 207/481: V3V5_207_Fusobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_207_Fusobacteria.fna -out ./work/V3V5_207_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 208/481: V3V5_208_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_208_Firmicutes.fna -out ./work/V3V5_208_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 209/481: V3V5_209_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_209_Firmicutes.fna -out ./work/V3V5_209_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 210/481: V3V5_210_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_210_Betaproteobacteria.fna -out ./work/V3V5_210_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 211/481: V3V5_211_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_211_Betaproteobacteria.fna -out ./work/V3V5_211_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 212/481: V3V5_212_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_212_Firmicutes.fna -out ./work/V3V5_212_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 213/481: V3V5_213_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_213_Bacteroidetes.fna -out ./work/V3V5_213_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 214/481: V3V5_214_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_214_Firmicutes.fna -out ./work/V3V5_214_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 215/481: V3V5_215_Fusobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_215_Fusobacteria.fna -out ./work/V3V5_215_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 216/481: V3V5_216_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_216_Bacteroidetes.fna -out ./work/V3V5_216_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 217/481: V3V5_217_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_217_Bacteroidetes.fna -out ./work/V3V5_217_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 218/481: V3V5_218_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_218_Firmicutes.fna -out ./work/V3V5_218_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 219/481: V3V5_219_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_219_Bacteroidetes.fna -out ./work/V3V5_219_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 220/481: V3V5_220_Actinobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_220_Actinobacteria.fna -out ./work/V3V5_220_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 221/481: V3V5_221_Fusobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_221_Fusobacteria.fna -out ./work/V3V5_221_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 222/481: V3V5_222_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_222_Bacteroidetes.fna -out ./work/V3V5_222_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 223/481: V3V5_223_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_223_Bacteroidetes.fna -out ./work/V3V5_223_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 224/481: V3V5_224_Spirochaetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_224_Spirochaetes.fna -out ./work/V3V5_224_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 225/481: V3V5_225_Spirochaetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_225_Spirochaetes.fna -out ./work/V3V5_225_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 226/481: V3V5_226_Actinobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_226_Actinobacteria.fna -out ./work/V3V5_226_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 227/481: V3V5_227_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_227_Betaproteobacteria.fna -out ./work/V3V5_227_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 228/481: V3V5_228_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_228_Gammaproteobacteria.fna -out ./work/V3V5_228_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 229/481: V3V5_229_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_229_Gammaproteobacteria.fna -out ./work/V3V5_229_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 230/481: V3V5_230_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_230_Bacteroidetes.fna -out ./work/V3V5_230_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 231/481: V3V5_231_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_231_Firmicutes.fna -out ./work/V3V5_231_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 232/481: V3V5_232_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_232_Firmicutes.fna -out ./work/V3V5_232_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 233/481: V3V5_233_Actinobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_233_Actinobacteria.fna -out ./work/V3V5_233_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 234/481: V3V5_234_Actinobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_234_Actinobacteria.fna -out ./work/V3V5_234_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 235/481: V3V5_235_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_235_Firmicutes.fna -out ./work/V3V5_235_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 236/481: V3V5_236_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_236_Firmicutes.fna -out ./work/V3V5_236_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 237/481: V3V5_237_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_237_Bacteroidetes.fna -out ./work/V3V5_237_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 238/481: V3V5_238_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_238_Firmicutes.fna -out ./work/V3V5_238_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 239/481: V3V5_239_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_239_Bacteroidetes.fna -out ./work/V3V5_239_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 240/481: V3V5_240_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_240_Bacteroidetes.fna -out ./work/V3V5_240_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 241/481: V3V5_241_Fusobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_241_Fusobacteria.fna -out ./work/V3V5_241_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 242/481: V3V5_242_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_242_Gammaproteobacteria.fna -out ./work/V3V5_242_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 243/481: V3V5_243_Actinobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_243_Actinobacteria.fna -out ./work/V3V5_243_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 244/481: V3V5_244_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_244_Bacteroidetes.fna -out ./work/V3V5_244_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 245/481: V3V5_245_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_245_Bacteroidetes.fna -out ./work/V3V5_245_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 246/481: V3V5_246_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_246_Bacteroidetes.fna -out ./work/V3V5_246_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 247/481: V3V5_247_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_247_Firmicutes.fna -out ./work/V3V5_247_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 248/481: V3V5_248_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_248_Firmicutes.fna -out ./work/V3V5_248_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 249/481: V3V5_249_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_249_Gammaproteobacteria.fna -out ./work/V3V5_249_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 250/481: V3V5_250_Fusobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_250_Fusobacteria.fna -out ./work/V3V5_250_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 251/481: V3V5_251_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_251_Bacteroidetes.fna -out ./work/V3V5_251_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 252/481: V3V5_252_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_252_Bacteroidetes.fna -out ./work/V3V5_252_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 253/481: V3V5_253_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_253_Bacteroidetes.fna -out ./work/V3V5_253_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 254/481: V3V5_254_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_254_Gammaproteobacteria.fna -out ./work/V3V5_254_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 255/481: V3V5_255_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_255_Betaproteobacteria.fna -out ./work/V3V5_255_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 256/481: V3V5_256_Fusobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_256_Fusobacteria.fna -out ./work/V3V5_256_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 257/481: V3V5_257_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_257_Bacteroidetes.fna -out ./work/V3V5_257_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 258/481: V3V5_258_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_258_Bacteroidetes.fna -out ./work/V3V5_258_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 259/481: V3V5_259_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_259_Firmicutes.fna -out ./work/V3V5_259_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 260/481: V3V5_260_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_260_Gammaproteobacteria.fna -out ./work/V3V5_260_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 261/481: V3V5_261_Fusobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_261_Fusobacteria.fna -out ./work/V3V5_261_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 262/481: V3V5_262_Fusobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_262_Fusobacteria.fna -out ./work/V3V5_262_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 263/481: V3V5_263_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_263_Bacteroidetes.fna -out ./work/V3V5_263_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 264/481: V3V5_264_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_264_Bacteroidetes.fna -out ./work/V3V5_264_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 265/481: V3V5_265_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_265_Betaproteobacteria.fna -out ./work/V3V5_265_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 266/481: V3V5_266_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_266_Firmicutes.fna -out ./work/V3V5_266_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 267/481: V3V5_267_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_267_Firmicutes.fna -out ./work/V3V5_267_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 268/481: V3V5_268_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_268_Firmicutes.fna -out ./work/V3V5_268_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 269/481: V3V5_269_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_269_Betaproteobacteria.fna -out ./work/V3V5_269_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 270/481: V3V5_270_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_270_Gammaproteobacteria.fna -out ./work/V3V5_270_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 271/481: V3V5_271_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_271_Firmicutes.fna -out ./work/V3V5_271_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 272/481: V3V5_272_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_272_Bacteroidetes.fna -out ./work/V3V5_272_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 273/481: V3V5_273_Fusobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_273_Fusobacteria.fna -out ./work/V3V5_273_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 274/481: V3V5_274_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_274_Bacteroidetes.fna -out ./work/V3V5_274_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 275/481: V3V5_275_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_275_Firmicutes.fna -out ./work/V3V5_275_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 276/481: V3V5_276_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_276_Firmicutes.fna -out ./work/V3V5_276_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 277/481: V3V5_277_Epsilonproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_277_Epsilonproteobacteria.fna -out ./work/V3V5_277_Epsilonproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 278/481: V3V5_278_Fusobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_278_Fusobacteria.fna -out ./work/V3V5_278_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 279/481: V3V5_279_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_279_Gammaproteobacteria.fna -out ./work/V3V5_279_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 280/481: V3V5_280_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_280_Firmicutes.fna -out ./work/V3V5_280_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 281/481: V3V5_281_Fusobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_281_Fusobacteria.fna -out ./work/V3V5_281_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 282/481: V3V5_282_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_282_Bacteroidetes.fna -out ./work/V3V5_282_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 283/481: V3V5_283_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_283_Firmicutes.fna -out ./work/V3V5_283_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 284/481: V3V5_284_Fusobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_284_Fusobacteria.fna -out ./work/V3V5_284_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 285/481: V3V5_285_Actinobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_285_Actinobacteria.fna -out ./work/V3V5_285_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 286/481: V3V5_286_Actinobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_286_Actinobacteria.fna -out ./work/V3V5_286_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 287/481: V3V5_287_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_287_Firmicutes.fna -out ./work/V3V5_287_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 288/481: V3V5_288_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_288_Bacteroidetes.fna -out ./work/V3V5_288_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 289/481: V3V5_289_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_289_Gammaproteobacteria.fna -out ./work/V3V5_289_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 290/481: V3V5_290_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_290_Bacteroidetes.fna -out ./work/V3V5_290_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 291/481: V3V5_291_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_291_Firmicutes.fna -out ./work/V3V5_291_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 292/481: V3V5_292_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_292_Bacteroidetes.fna -out ./work/V3V5_292_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 293/481: V3V5_293_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_293_Bacteroidetes.fna -out ./work/V3V5_293_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 294/481: V3V5_294_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_294_Bacteroidetes.fna -out ./work/V3V5_294_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 295/481: V3V5_295_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_295_Firmicutes.fna -out ./work/V3V5_295_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 296/481: V3V5_296_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_296_Bacteroidetes.fna -out ./work/V3V5_296_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 297/481: V3V5_297_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_297_Bacteroidetes.fna -out ./work/V3V5_297_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 298/481: V3V5_298_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_298_Bacteroidetes.fna -out ./work/V3V5_298_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 299/481: V3V5_299_Fusobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_299_Fusobacteria.fna -out ./work/V3V5_299_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 300/481: V3V5_300_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_300_Bacteroidetes.fna -out ./work/V3V5_300_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 301/481: V3V5_301_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_301_Bacteroidetes.fna -out ./work/V3V5_301_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 302/481: V3V5_302_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_302_Bacteroidetes.fna -out ./work/V3V5_302_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 303/481: V3V5_303_Spirochaetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_303_Spirochaetes.fna -out ./work/V3V5_303_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 304/481: V3V5_304_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_304_Firmicutes.fna -out ./work/V3V5_304_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 305/481: V3V5_305_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_305_Firmicutes.fna -out ./work/V3V5_305_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 306/481: V3V5_306_Spirochaetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_306_Spirochaetes.fna -out ./work/V3V5_306_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 307/481: V3V5_307_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_307_Bacteroidetes.fna -out ./work/V3V5_307_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 308/481: V3V5_308_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_308_Firmicutes.fna -out ./work/V3V5_308_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 309/481: V3V5_309_Actinobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_309_Actinobacteria.fna -out ./work/V3V5_309_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 310/481: V3V5_310_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_310_Firmicutes.fna -out ./work/V3V5_310_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 311/481: V3V5_311_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_311_Firmicutes.fna -out ./work/V3V5_311_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 312/481: V3V5_312_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_312_Gammaproteobacteria.fna -out ./work/V3V5_312_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 313/481: V3V5_313_Spirochaetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_313_Spirochaetes.fna -out ./work/V3V5_313_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 314/481: V3V5_314_Fusobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_314_Fusobacteria.fna -out ./work/V3V5_314_Fusobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 315/481: V3V5_315_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_315_Bacteroidetes.fna -out ./work/V3V5_315_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 316/481: V3V5_316_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_316_Firmicutes.fna -out ./work/V3V5_316_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 317/481: V3V5_317_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_317_Gammaproteobacteria.fna -out ./work/V3V5_317_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 318/481: V3V5_318_Actinobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_318_Actinobacteria.fna -out ./work/V3V5_318_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 319/481: V3V5_319_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_319_Bacteroidetes.fna -out ./work/V3V5_319_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 320/481: V3V5_320_Actinobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_320_Actinobacteria.fna -out ./work/V3V5_320_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 321/481: V3V5_321_Actinobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_321_Actinobacteria.fna -out ./work/V3V5_321_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 322/481: V3V5_322_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_322_Firmicutes.fna -out ./work/V3V5_322_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 323/481: V3V5_323_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_323_Firmicutes.fna -out ./work/V3V5_323_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 324/481: V3V5_324_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_324_Bacteroidetes.fna -out ./work/V3V5_324_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 325/481: V3V5_325_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_325_Firmicutes.fna -out ./work/V3V5_325_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 326/481: V3V5_326_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_326_Bacteroidetes.fna -out ./work/V3V5_326_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 327/481: V3V5_327_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_327_Firmicutes.fna -out ./work/V3V5_327_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 328/481: V3V5_328_Actinobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_328_Actinobacteria.fna -out ./work/V3V5_328_Actinobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 329/481: V3V5_329_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_329_Bacteroidetes.fna -out ./work/V3V5_329_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 330/481: V3V5_330_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_330_Bacteroidetes.fna -out ./work/V3V5_330_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 331/481: V3V5_331_Spirochaetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_331_Spirochaetes.fna -out ./work/V3V5_331_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 332/481: V3V5_332_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_332_Firmicutes.fna -out ./work/V3V5_332_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 333/481: V3V5_333_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_333_Firmicutes.fna -out ./work/V3V5_333_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 334/481: V3V5_334_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_334_Bacteroidetes.fna -out ./work/V3V5_334_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 335/481: V3V5_335_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_335_Firmicutes.fna -out ./work/V3V5_335_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 336/481: V3V5_336_Spirochaetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_336_Spirochaetes.fna -out ./work/V3V5_336_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 337/481: V3V5_337_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_337_Firmicutes.fna -out ./work/V3V5_337_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 338/481: V3V5_338_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_338_Bacteroidetes.fna -out ./work/V3V5_338_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 339/481: V3V5_339_Spirochaetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_339_Spirochaetes.fna -out ./work/V3V5_339_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 340/481: V3V5_340_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_340_Bacteroidetes.fna -out ./work/V3V5_340_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 341/481: V3V5_341_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_341_Gammaproteobacteria.fna -out ./work/V3V5_341_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 342/481: V3V5_342_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_342_Bacteroidetes.fna -out ./work/V3V5_342_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 343/481: V3V5_343_Spirochaetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_343_Spirochaetes.fna -out ./work/V3V5_343_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 344/481: V3V5_344_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_344_Bacteroidetes.fna -out ./work/V3V5_344_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 345/481: V3V5_345_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_345_Firmicutes.fna -out ./work/V3V5_345_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 346/481: V3V5_346_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_346_Bacteroidetes.fna -out ./work/V3V5_346_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 347/481: V3V5_347_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_347_Bacteroidetes.fna -out ./work/V3V5_347_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 348/481: V3V5_348_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_348_Firmicutes.fna -out ./work/V3V5_348_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 349/481: V3V5_349_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_349_Firmicutes.fna -out ./work/V3V5_349_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 350/481: V3V5_350_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_350_Bacteroidetes.fna -out ./work/V3V5_350_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 351/481: V3V5_351_Spirochaetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_351_Spirochaetes.fna -out ./work/V3V5_351_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 352/481: V3V5_352_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_352_Bacteroidetes.fna -out ./work/V3V5_352_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 353/481: V3V5_353_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_353_Bacteroidetes.fna -out ./work/V3V5_353_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 354/481: V3V5_354_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_354_Bacteroidetes.fna -out ./work/V3V5_354_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 355/481: V3V5_355_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_355_Bacteroidetes.fna -out ./work/V3V5_355_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 356/481: V3V5_356_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_356_Bacteroidetes.fna -out ./work/V3V5_356_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 357/481: V3V5_357_Spirochaetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_357_Spirochaetes.fna -out ./work/V3V5_357_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 358/481: V3V5_358_Spirochaetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_358_Spirochaetes.fna -out ./work/V3V5_358_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 359/481: V3V5_359_Spirochaetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_359_Spirochaetes.fna -out ./work/V3V5_359_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 360/481: V3V5_360_Spirochaetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_360_Spirochaetes.fna -out ./work/V3V5_360_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 361/481: V3V5_361_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_361_Bacteroidetes.fna -out ./work/V3V5_361_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 362/481: V3V5_362_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_362_Bacteroidetes.fna -out ./work/V3V5_362_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 363/481: V3V5_363_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_363_Bacteroidetes.fna -out ./work/V3V5_363_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 364/481: V3V5_364_Spirochaetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_364_Spirochaetes.fna -out ./work/V3V5_364_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 365/481: V3V5_365_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_365_Bacteroidetes.fna -out ./work/V3V5_365_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 366/481: V3V5_366_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_366_Bacteroidetes.fna -out ./work/V3V5_366_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 367/481: V3V5_367_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_367_Firmicutes.fna -out ./work/V3V5_367_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 368/481: V3V5_368_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_368_Bacteroidetes.fna -out ./work/V3V5_368_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 369/481: V3V5_369_Spirochaetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_369_Spirochaetes.fna -out ./work/V3V5_369_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 370/481: V3V5_370_Spirochaetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_370_Spirochaetes.fna -out ./work/V3V5_370_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 371/481: V3V5_371_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_371_Bacteroidetes.fna -out ./work/V3V5_371_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 372/481: V3V5_372_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_372_Bacteroidetes.fna -out ./work/V3V5_372_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 373/481: V3V5_373_Spirochaetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_373_Spirochaetes.fna -out ./work/V3V5_373_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 374/481: V3V5_374_Epsilonproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_374_Epsilonproteobacteria.fna -out ./work/V3V5_374_Epsilonproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 375/481: V3V5_375_Gammaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_375_Gammaproteobacteria.fna -out ./work/V3V5_375_Gammaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 376/481: V3V5_376_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_376_Bacteroidetes.fna -out ./work/V3V5_376_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 377/481: V3V5_377_Epsilonproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_377_Epsilonproteobacteria.fna -out ./work/V3V5_377_Epsilonproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 378/481: V3V5_378_Spirochaetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_378_Spirochaetes.fna -out ./work/V3V5_378_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 379/481: V3V5_379_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_379_Firmicutes.fna -out ./work/V3V5_379_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 380/481: V3V5_380_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_380_Bacteroidetes.fna -out ./work/V3V5_380_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 381/481: V3V5_381_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_381_Bacteroidetes.fna -out ./work/V3V5_381_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 382/481: V3V5_382_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_382_Firmicutes.fna -out ./work/V3V5_382_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 383/481: V3V5_383_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_383_Bacteroidetes.fna -out ./work/V3V5_383_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 384/481: V3V5_384_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_384_Betaproteobacteria.fna -out ./work/V3V5_384_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 385/481: V3V5_385_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_385_Bacteroidetes.fna -out ./work/V3V5_385_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 386/481: V3V5_386_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_386_Bacteroidetes.fna -out ./work/V3V5_386_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 387/481: V3V5_387_Spirochaetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_387_Spirochaetes.fna -out ./work/V3V5_387_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 388/481: V3V5_388_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_388_Firmicutes.fna -out ./work/V3V5_388_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 389/481: V3V5_389_Spirochaetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_389_Spirochaetes.fna -out ./work/V3V5_389_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 390/481: V3V5_390_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_390_Firmicutes.fna -out ./work/V3V5_390_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 391/481: V3V5_391_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_391_Firmicutes.fna -out ./work/V3V5_391_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 392/481: V3V5_392_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_392_Firmicutes.fna -out ./work/V3V5_392_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 393/481: V3V5_393_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_393_Bacteroidetes.fna -out ./work/V3V5_393_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 394/481: V3V5_394_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_394_Bacteroidetes.fna -out ./work/V3V5_394_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 395/481: V3V5_395_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_395_Bacteroidetes.fna -out ./work/V3V5_395_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 396/481: V3V5_396_Spirochaetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_396_Spirochaetes.fna -out ./work/V3V5_396_Spirochaetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 397/481: V3V5_397_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_397_Bacteroidetes.fna -out ./work/V3V5_397_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 398/481: V3V5_398_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_398_Firmicutes.fna -out ./work/V3V5_398_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 399/481: V3V5_399_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_399_Firmicutes.fna -out ./work/V3V5_399_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 400/481: V3V5_400_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_400_Bacteroidetes.fna -out ./work/V3V5_400_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 401/481: V3V5_401_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_401_Firmicutes.fna -out ./work/V3V5_401_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 402/481: V3V5_402_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_402_Betaproteobacteria.fna -out ./work/V3V5_402_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 403/481: V3V5_403_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_403_Firmicutes.fna -out ./work/V3V5_403_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 404/481: V3V5_404_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_404_Firmicutes.fna -out ./work/V3V5_404_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 405/481: V3V5_405_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_405_Firmicutes.fna -out ./work/V3V5_405_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 406/481: V3V5_406_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_406_Bacteroidetes.fna -out ./work/V3V5_406_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 407/481: V3V5_407_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_407_Bacteroidetes.fna -out ./work/V3V5_407_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 408/481: V3V5_408_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_408_Bacteroidetes.fna -out ./work/V3V5_408_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 409/481: V3V5_409_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_409_Bacteroidetes.fna -out ./work/V3V5_409_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 410/481: V3V5_410_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_410_Bacteroidetes.fna -out ./work/V3V5_410_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 411/481: V3V5_411_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_411_Firmicutes.fna -out ./work/V3V5_411_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 412/481: V3V5_412_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_412_Firmicutes.fna -out ./work/V3V5_412_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 413/481: V3V5_413_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_413_Betaproteobacteria.fna -out ./work/V3V5_413_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 414/481: V3V5_414_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_414_Bacteroidetes.fna -out ./work/V3V5_414_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 415/481: V3V5_415_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_415_Bacteroidetes.fna -out ./work/V3V5_415_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 416/481: V3V5_416_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_416_Firmicutes.fna -out ./work/V3V5_416_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 417/481: V3V5_417_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_417_Firmicutes.fna -out ./work/V3V5_417_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 418/481: V3V5_418_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_418_Bacteroidetes.fna -out ./work/V3V5_418_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 419/481: V3V5_419_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_419_Firmicutes.fna -out ./work/V3V5_419_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 420/481: V3V5_420_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_420_Firmicutes.fna -out ./work/V3V5_420_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 421/481: V3V5_421_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_421_Bacteroidetes.fna -out ./work/V3V5_421_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 422/481: V3V5_422_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_422_Firmicutes.fna -out ./work/V3V5_422_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 423/481: V3V5_423_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_423_Firmicutes.fna -out ./work/V3V5_423_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 424/481: V3V5_424_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_424_Bacteroidetes.fna -out ./work/V3V5_424_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 425/481: V3V5_425_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_425_Firmicutes.fna -out ./work/V3V5_425_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 426/481: V3V5_426_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_426_Firmicutes.fna -out ./work/V3V5_426_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 427/481: V3V5_427_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_427_Bacteroidetes.fna -out ./work/V3V5_427_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 428/481: V3V5_428_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_428_Bacteroidetes.fna -out ./work/V3V5_428_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 429/481: V3V5_429_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_429_Bacteroidetes.fna -out ./work/V3V5_429_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 430/481: V3V5_430_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_430_Firmicutes.fna -out ./work/V3V5_430_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 431/481: V3V5_431_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_431_Firmicutes.fna -out ./work/V3V5_431_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 432/481: V3V5_432_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_432_Firmicutes.fna -out ./work/V3V5_432_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 433/481: V3V5_433_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_433_Bacteroidetes.fna -out ./work/V3V5_433_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 434/481: V3V5_434_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_434_Firmicutes.fna -out ./work/V3V5_434_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 435/481: V3V5_435_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_435_Bacteroidetes.fna -out ./work/V3V5_435_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 436/481: V3V5_436_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_436_Firmicutes.fna -out ./work/V3V5_436_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 437/481: V3V5_437_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_437_Firmicutes.fna -out ./work/V3V5_437_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 438/481: V3V5_438_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_438_Firmicutes.fna -out ./work/V3V5_438_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 439/481: V3V5_439_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_439_Firmicutes.fna -out ./work/V3V5_439_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 440/481: V3V5_440_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_440_Firmicutes.fna -out ./work/V3V5_440_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 441/481: V3V5_441_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_441_Firmicutes.fna -out ./work/V3V5_441_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 442/481: V3V5_442_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_442_Firmicutes.fna -out ./work/V3V5_442_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 443/481: V3V5_443_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_443_Firmicutes.fna -out ./work/V3V5_443_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 444/481: V3V5_444_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_444_Firmicutes.fna -out ./work/V3V5_444_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 445/481: V3V5_445_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_445_Firmicutes.fna -out ./work/V3V5_445_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 446/481: V3V5_446_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_446_Firmicutes.fna -out ./work/V3V5_446_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 447/481: V3V5_447_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_447_Firmicutes.fna -out ./work/V3V5_447_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 448/481: V3V5_448_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_448_Firmicutes.fna -out ./work/V3V5_448_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 449/481: V3V5_449_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_449_Firmicutes.fna -out ./work/V3V5_449_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 450/481: V3V5_450_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_450_Bacteroidetes.fna -out ./work/V3V5_450_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 451/481: V3V5_451_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_451_Bacteroidetes.fna -out ./work/V3V5_451_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 452/481: V3V5_452_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_452_Firmicutes.fna -out ./work/V3V5_452_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 453/481: V3V5_453_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_453_Firmicutes.fna -out ./work/V3V5_453_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 454/481: V3V5_454_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_454_Firmicutes.fna -out ./work/V3V5_454_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 455/481: V3V5_455_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_455_Bacteroidetes.fna -out ./work/V3V5_455_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 456/481: V3V5_456_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_456_Bacteroidetes.fna -out ./work/V3V5_456_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 457/481: V3V5_457_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_457_Firmicutes.fna -out ./work/V3V5_457_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 458/481: V3V5_458_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_458_Bacteroidetes.fna -out ./work/V3V5_458_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 459/481: V3V5_459_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_459_Firmicutes.fna -out ./work/V3V5_459_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 460/481: V3V5_460_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_460_Bacteroidetes.fna -out ./work/V3V5_460_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 461/481: V3V5_461_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_461_Firmicutes.fna -out ./work/V3V5_461_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 462/481: V3V5_462_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_462_Betaproteobacteria.fna -out ./work/V3V5_462_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 463/481: V3V5_463_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_463_Firmicutes.fna -out ./work/V3V5_463_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 464/481: V3V5_464_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_464_Bacteroidetes.fna -out ./work/V3V5_464_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 465/481: V3V5_465_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_465_Bacteroidetes.fna -out ./work/V3V5_465_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 466/481: V3V5_466_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_466_Firmicutes.fna -out ./work/V3V5_466_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 467/481: V3V5_467_Betaproteobacteria.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_467_Betaproteobacteria.fna -out ./work/V3V5_467_Betaproteobacteria.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 468/481: V3V5_468_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_468_Bacteroidetes.fna -out ./work/V3V5_468_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 469/481: V3V5_469_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_469_Firmicutes.fna -out ./work/V3V5_469_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 470/481: V3V5_470_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_470_Bacteroidetes.fna -out ./work/V3V5_470_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 471/481: V3V5_471_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_471_Firmicutes.fna -out ./work/V3V5_471_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 472/481: V3V5_472_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_472_Bacteroidetes.fna -out ./work/V3V5_472_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 473/481: V3V5_473_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_473_Bacteroidetes.fna -out ./work/V3V5_473_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 474/481: V3V5_474_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_474_Bacteroidetes.fna -out ./work/V3V5_474_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 475/481: V3V5_475_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_475_Firmicutes.fna -out ./work/V3V5_475_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 476/481: V3V5_476_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_476_Bacteroidetes.fna -out ./work/V3V5_476_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 477/481: V3V5_477_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_477_Bacteroidetes.fna -out ./work/V3V5_477_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 478/481: V3V5_478_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_478_Bacteroidetes.fna -out ./work/V3V5_478_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 479/481: V3V5_479_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_479_Bacteroidetes.fna -out ./work/V3V5_479_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 480/481: V3V5_480_Bacteroidetes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_480_Bacteroidetes.fna -out ./work/V3V5_480_Bacteroidetes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
echo '
  Blasting 481/481: V3V5_481_Firmicutes.fna in args.outdir'
blastn  -db ../BLAST_DATABASE_ABUNDANCE/HOMD_16S_rRNA_RefSeq_V15.22.p9.fasta -query ./work/V3V5_481_Firmicutes.fna -out ./work/V3V5_481_Firmicutes.fna.out -outfmt '7 qseqid bitscore nident pident qstart qend stitle length mismatch gaps' -max_target_seqs 30
