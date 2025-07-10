#!/usr/bin/perl
use strict;
use DBI;
use Number::Format 'format_number';
use Sort::Naturally 'nsort';

if(!-e "../seqid_ftp.txt"){
   print "need to seqid_ftp.txt in the parent folder\n";
   exit;
}

my $dbip="localhost"
my $dbip1="localhost"
my $genomedb="HOMD_genomes_new";
my $my_cnf = '~/my_cnf.cnf';
my $dsn_genome =
  "DBI:mysql:$genomedb:$dbip;" . 
  "mysql_read_default_file=$my_cnf";
my $dsn_meta =
  "DBI:mysql:$metadb:$dbip1" . 
  "mysql_read_default_file=$my_cnf";
my $dsn_ncbi =
  "DBI:mysql:$metadb:$dbip1" . 
  "mysql_read_default_file=$my_cnf";
my $db_genome = DBI->connect(
    $dsn_genome, 
    undef, 
    undef, 
    {RaiseError => 1}
) or  die "DBI::errstr: $DBI::errstr";  

my $db_meta = DBI->connect(
    $dsn_meta, 
    undef, 
    undef, 
    {RaiseError => 1}
) or  die "DBI::errstr: $DBI::errstr";  


my $seq_genomes=$db_genome->prepare(qq{select seq_id, genus, species, culture_collection from seq_genomes where seq_id=?});
my $homd_tool_list=$db_genome->prepare(qq{select tool_type,seq_id,db_uid,db_uid_inNCBI from HOMD_tool_list  where seq_id=?});
my $annotated_org=$db_genome->prepare(qq{select * from annotated_org  where seq_id=?});

my $metadb="HOMD_meta_table";



my $delete_meta=$db_meta->prepare(qq{delete from all_genome_annotation where db_uid=?});
my $insert_meta=$db_meta->prepare(qq{insert into all_genome_annotation values(?,?,?)});

my $g;


my $ftpfile="../seqid_ftp.txt";
my $total=`wc -l $ftpfile`; chomp $total;

my $missfile=$ftpfile; $missfile=~s/\.txt/_missing_file\.txt/;
open(MISS,">missfile")||die;

#open(IN,"seqid_ftp.txt")||die;
open(IN,$ftpfile)||die;
while(my $line=<IN>){
#	last if $g>=10;
	chomp $line;
	my ($seqid,$ftp)=split("\t",$line);
	$ftp=~/^.+\/(.+)/;
	my $basename=$1;
	next if !$ftp;
	my $h;
	$seq_genomes->execute($seqid);
	my @tmp1;
	while (my @arr=$seq_genomes->fetchrow_array()){
		$h++;
		push(@tmp1,join("\t",@arr));
	}
	$g++;
	$homd_tool_list->execute($seqid);
	my $n; my %type;
	while(my @arr=$homd_tool_list->fetchrow_array()){
		$type{$arr[0]}++;
		$n++;	
		push(@tmp1,join("\t",@arr));
	}

	$annotated_org->execute($seqid);
	while(my @arr=$annotated_org->fetchrow_array()){
		push(@tmp1,join("\t",@arr));
	}


#	print $seqid."\t".join(";",(keys %type))."\n";
	print $seqid." has no record in HOMD_tool_list, will create new rocord\n" if !$n;
	print "Process $g/$total $seqid ...\n";
#	print join("\n",@tmp1)."\n";
#	print "\n";

system("mysql -h $dbip1 --defaults-file=$my_cnf  -e 'drop database if exists NCBI_$seqid' 2>/dev/null");
system("mysql -h $dbip1 --defaults-file=$my_cnf -e 'create database NCBI_$seqid' 2>/dev/null");
system("mysqldump -h $dbip1 --defaults-file=$my_cnf --no-data ncbi_template 2>/dev/null | mysql -h $dbip1 --defaults-file=$my_cnf NCBI_$seqid 2>/dev/null");

$delete_meta->execute("NCBI_".$seqid);
my $dsn_ncbi =
  "DBI:mysql:NCBI_$seqid:$dbip1" . 
  "mysql_read_default_file=$my_cnf";
my $db=DBI->connect( $dsn_ncbi, 
    undef, 
    undef, 
    {RaiseError => 1}
) or  die "DBI::errstr: $DBI::errstr";  

my $insert_report=$db->prepare(qq{insert into assembly_report values(?,?)});
my $insert_stats=$db->prepare(qq{insert into assembly_stats values(?,?)});
my $insert_ORF_seq=$db->prepare(qq{insert into ORF_seq values(?,?,?,?,?,?,?,?,?,?,?,?,?)});
my $insert_gff=$db->prepare(qq{insert into gff values(?,?,?,?,?,?,?,?,?)});
my $insert_genome_seq=$db->prepare(qq{insert into genome_seq values(?,?,?,?)});
my $insert_molecules=$db->prepare(qq{insert into molecules values(?,?,?,?,?,?)});
my $insert_GC_count=$db->prepare(qq{insert into GC_count values(?,?,?,?,?)});
my $insert_ORF_seq=$db->prepare(qq{insert into ORF_seq values(?,?,?,?,?,?,?,?,?,?,?,?,?)});

if(-e "../download/$basename/$basename\_assembly_report.txt"){
#print "$ftp/$basename\_assembly_report.txt\n";	
open(IN1,"../download/$basename/$basename\_assembly_report.txt")||die;
	while(my $line=<IN1>){
	chomp $line;
	if($line=~/^# (.+?)\:\s+(.+)/){
	$insert_report->execute($1,$2);
	}
}
close IN1;
}else{
	print MISS join("\t",($seqid,"Missing assembly_report.txt"))."\n";
}
#
#if(-e "$ftp/$basename\_assembly_stats.txt"){
if(-e "../download/$basename/$basename\_assembly_stats.txt"){
#print "$ftp/$basename\_assembly_stats.txt\n";
open(IN1,"../download/$basename/$basename\_assembly_stats.txt")||die;
while(my $line=<IN1>){
	chomp $line;
	if($line=~/^# (.+?)\:\s+(.+)/){
	$insert_stats->execute($1,$2);
	}
}
close IN1;
}else{
	print MISS join("\t",($seqid,"Missing assembly_stats.txt"))."\n";
}


my %pid_contig;
my %pid_start;
my %pid_stop;
my %pid_faa;
my %pid_ffn;
my %pid_gene;
my %pid_id;
my %pid_product;



if(-e "../download/$basename/$basename\_genomic.gff.gz"){
my %geneid_genename;	
#print "$ftp/$basename\_genomic.gff\n";
open(IN1,"zcat ../download/$basename/$basename\_genomic.gff.gz|")||die;
while(my $line=<IN1>){
	next if $line=~/^#/;
	last if $line=~/^>/;
	chomp $line;
	my @tmp=split("\t",$line);
	$insert_gff->execute(@tmp);
	
	if($tmp[2]eq'gene'){
		$tmp[8]=~/ID=(.+?);Name=(.+?);/;
		$geneid_genename{$1}=$2;
	}elsif($tmp[2]eq'CDS'){
	$tmp[8]=~/protein_id=(.+?);/;my $pid=$1;
	$tmp[8]=~/Parent=(.+?);/; my $geneid=$1;
#	if($tmp[8]=~/gene=(.+?);/){
	 $pid_gene{$pid}=$geneid_genename{$geneid};
#	}
	$pid_start{$pid}=($tmp[6]eq'+')?$tmp[3]:$tmp[4];
	$pid_stop{$pid}=($tmp[6]eq'+')?$tmp[4]:$tmp[3];
	$tmp[8]=~/product=(.+)/; my $product=$1; $product=~s/^(.+?);.*/$1/;
	$pid_product{$pid}=$product;
	$pid_contig{$pid}=$tmp[0];
	$insert_meta->execute("NCBI_".$seqid,$pid,$pid_product{$pid});
	}

}
close IN1;
}else{
	print MISS join("\t",($seqid,"Missing genomic.gff"))."\n";
}

mkdir("ncbi_fna_seqid") if !-e "ncbi_fna_seqid";
open(OUT,">ncbi_fna_seqid/$seqid.fna")||die;
my $contigct=1;
my $combinedbp;
open(IN1,"zcat ../download/$basename/$basename\_genomic.fna.gz|")||die;
my %contig_seq;
my %contig_gc;
my %contig_id;
my %contig_contigname;
my $totalgc;

my $first=<IN1>;chomp $first;$first=~/^>(.+?) (.+)/;my $contig=$1; my $contigname=$2;my $seq;
while(my $line=<IN1>){
	chomp $line;
	if($line=~/^>/){
		print OUT ">$seqid|$contig $contigname\n";
		print OUT $seq."\n";
		$contigct++;
		$contig_seq{$contig}=$seq;
		$combinedbp+=length($seq);
		$contig_contigname{$contig}=$contigname;
		$seq=~s/[atAT]//g;$totalgc+=length($seq);
		$line=~/^>(.+?) (.+)/;
		$contig=$1;$contigname=$2;
		$seq="";
	}else{
		$seq.=$line;
	}
}
	print OUT ">$seqid|$contig $contigname\n";
	print OUT $seq."\n";
	close OUT;
	$contig_seq{$contig}=$seq;
	$combinedbp+=length($seq);	
	$contig_contigname{$contig}=$contigname;	
	$seq=~s/[atAT]//g;$totalgc+=length($seq);
close IN1;

my $date=`date +%F`; chomp $date;

my $i=1;
my $j=1;
my $l=1;
foreach my $contig(keys %contig_seq){
	$contig_id{$contig}=$i;
	my $seq=$contig_seq{$contig};my $seq1=$seq;
	my $gc=$seq; $gc=~s/[atAT]//g; $gc=sprintf("%.2f",(length($gc)/length($seq))*100); 
	$insert_molecules->execute($i,$seqid.'|'.$contig,$contig_contigname{$contig},length($seq),$gc,$date);
	#$h_insert_contigs->execute($i,$contig,length($seq),$gc);
	my $k=1;
	while(my $kkk=substr($seq1,0,1000,'')){
	$insert_genome_seq->execute($j,$i,$k,$kkk);
	#$h_insert_genome_seq->execute($j,$i,$k,$kkk);
	$j++;
	$k++;
	}
	my $m=0;$seq1=$seq;
	while(my $five=substr($seq1,0,500,'')){
	my $gc=$five; $gc=~s/[atAT]//g; $gc=sprintf("%.2f",(length($gc)/length($five))*100);
	my $start=$m*500+1;
	my $stop=($m+1)*500;
	$insert_GC_count->execute($l,$i,$start,$stop,$gc);
	#$h_insert_GC_count->execute($l,$i,$start,$stop,$gc);
	$l++;
	$m++;
	}


	$i++;
}


####### ORF_seq table
#open(IN,"ncbi/$seqid/$seqid.ffn")||die;
if(-e "../download/$basename/$basename\_cds_from_genomic.fna.gz"){
open(IN1,"zcat ../download/$basename/$basename\_cds_from_genomic.fna.gz|")||die;

my $first=<IN1>; $first=~/protein_id=(.+?)\]/; my $pid=$1;my $seq;
while(my $line=<IN1>){
	chomp $line;
	if($line=~/^>/){
		$pid_ffn{$pid}=$seq;
		$line=~/protein_id=(.+?)\]/;
		$pid=$1;
		$seq="";
	}else{
		$seq.=$line;
	}
}
		$pid_ffn{$pid}=$seq;
close IN1;

open(IN1,"zcat ../download/$basename/$basename\_protein.faa.gz|")||die;
my $first=<IN1>; $first=~/^>(\S+)/; my $pid=$1;my $seq;
while(my $line=<IN1>){
	chomp $line;
	if($line=~/^>/){
		$pid_faa{$pid}=$seq;
		$line=~/^>(\S+)/;
		$pid=$1;
		$seq="";
	}else{
		$seq.=$line;
	}
}
		$pid_faa{$pid}=$seq;
close IN1;

my $p=1;
foreach my $pid(sort{$a cmp $b}keys %pid_faa){
#	print $pid_contig{$pid}."\n";
my @tmp=($p);
push(@tmp,$contig_id{$pid_contig{$pid}});
push(@tmp,length($pid_ffn{$pid}));
push(@tmp,$pid_gene{$pid});
push(@tmp,'');
push(@tmp,$pid);
push(@tmp,'');
push(@tmp,'');
push(@tmp,$pid_product{$pid});
push(@tmp,$pid_start{$pid});
push(@tmp,$pid_stop{$pid});
push(@tmp,$pid_ffn{$pid});
push(@tmp,$pid_faa{$pid});
$insert_ORF_seq->execute(@tmp);
$p++;
#my @tmp1=($p);
#push(@tmp1,length($pid_ffn{$pid}));
#$pid=~/^.+_(\d+)/;
#push(@tmp1,$1);
#push(@tmp1,$pid);
#push(@tmp1,$contig_id{$pid_contig{$pid}});
#push(@tmp1,$pid_start{$pid});
#push(@tmp1,$pid_stop{$pid});
#push(@tmp1,$pid_ffn{$pid});
#push(@tmp1,$pid_faa{$pid});
#push(@tmp1,0);
#$h_insert_ORF_seq->execute(@tmp1);

}

}
$db->disconnect();




#next;


$totalgc=sprintf("%.2f",($totalgc/$combinedbp)*100);

#my $delete_annotated_org=$db_genome->prepare(qq{delete from annotated_org where seq_id=? and db_name=?});
#my $insert_annotated_org=$db_genome->prepare(qq{insert into annotated_org values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)});
#$delete_annotated_org->execute($seqid,"NCBI_$seqid");
#my @tmp3=('');
#push(@tmp3,$seqid);
#push(@tmp3,"NCBI_$seqid");
#push(@tmp3,$date);
#push(@tmp3,$date);
#push(@tmp3,'');
#push(@tmp3,'1');
#push(@tmp3,'');
#push(@tmp3,$key_val{'contigs'});
#push(@tmp3,'200');
#push(@tmp3,$key_val{'contigs'});
#push(@tmp3,$key_val{'contigs'});
#push(@tmp3,$key_val{'bases'});
#push(@tmp3,$totalgc);
#push(@tmp3,$key_val{'bases'});
#$insert_annotated_org->execute(@tmp3);

my $insert_HOMD_tool_list=$db_genome->prepare(qq{insert into HOMD_tool_list values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)});

my $deactive_HOMD_tool_list=$db_genome->prepare(qq{update HOMD_tool_list set active='0' where seq_id=? and tool_type=?});
my $delete_HOMD_tool_list=$db_genome->prepare(qq{delete from HOMD_tool_list where seq_id=? and db_uid=? and tool_type=?});


$deactive_HOMD_tool_list->execute($seqid,'ncbi');
$delete_HOMD_tool_list->execute($seqid,'NCBI_$seqid','ncbi');
my @tmp4=('ncbi');
push(@tmp4,$seqid);
push(@tmp4,"NCBI_$seqid");
push(@tmp4,'');
push(@tmp4,$contigct);
push(@tmp4,$combinedbp);
push(@tmp4,$totalgc);
push(@tmp4,'');
push(@tmp4,'');
push(@tmp4,'0');
push(@tmp4,'1');
push(@tmp4,'');
push(@tmp4,'');
push(@tmp4,'1');
push(@tmp4,'0');
$insert_HOMD_tool_list->execute(@tmp4);

my $update_seq_genomes=$db_genome->prepare(qq{update seq_genomes set number_contig=?, combined_length=? where seq_id=?});
print $contigct."\t".$combinedbp."\t".$seqid."\n";

$update_seq_genomes->execute($contigct,$combinedbp,$seqid);

#$deactive_HOMD_tool_list->execute($seqid,'ncbi');
#$delete_HOMD_tool_list->execute($seqid,'NCBI_$seqid','ncbi');
#my @tmp5=('ncbi');
#push(@tmp5,$seqid);
#push(@tmp5,"NCBI_$seqid");
#push(@tmp5,'');
#push(@tmp5,$key_val{'contigs'});
#push(@tmp5,$key_val{'bases'});
#push(@tmp5,$totalgc);
#push(@tmp5,'');
#push(@tmp5,'');
#push(@tmp5,'0');
#push(@tmp5,'1');
#push(@tmp5,'');
#push(@tmp5,'');
#push(@tmp5,'1');
#push(@tmp5,'0');
#$insert_HOMD_tool_list->execute(@tmp5);

}
close MISS;

