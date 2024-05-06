#!/usr/bin/perl

use strict;
use warnings;

my($USAGE) = "\nUSAGE: $0 logfilename [blast, jb, pg]\n\n";

unless(@ARGV){
    print($USAGE);
    exit;
} 
my $filename = $ARGV[0];

# unless ( open(MYFILE, $filename) ){
#     print "Cannot open \"$filename\"\n\n";
#     exit;
# }
open my $fh, '<', $filename or die $!; # open the file using lexically scoped filehandle

foreach my $line (<$fh>){
    chomp $line;
    
    if ( $line =~ /blast/){
        
        parse_line('blast', $line);
    }elsif ($line =~ /jbrowse/){
        parse_line('jbrowse', $line);
    }elsif ($line =~ /anvio/){
        parse_line('anvio', $line);
    }
}

sub parse_line {
    my ($fxn, $l) = @_;
    print "$fxn: $l\n";
    my $ip = '0';
    my $date = '';
    my @mos = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec');
    #($date, $ip) = $l =~ /^blast: \[(\d{4}-\d{2}-\d{2})\] INFO  IP:(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/;
    #print "Date: $date  IP: $ip\n";
    #  /(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/
    if($l =~ /(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/){
       $ip = $1;
       print "$ip\n";
    }
    if($l =~ /(\d{4}-\d{2}-\d{2})/){
       $date = $1;
       print "$date\n";
    }elsif($l =~ /(\d{2}\/.*\/\d{4})/) {  # 14/Mar/2024
        $date = $1;
        print "$date\n";
        my ($y,$m,$d) = $date =~ /^([0-9]{2})\/(.*)\/([0-9]{4})\z/;
        print "$y,$m,$d\n";
        my $mo = array_search(\@mos,\$m);
        print "Month: $mo  $date\n";
    }
    # should return IP, date and fxn (important for blast)
}

sub array_search {
    my ($arr, $elem) = @_;
    my $idx;
    for my $i (0..$#$arr) {
        if ($arr->[$i] eq $elem) {
            $idx = $i;
            last;
        }
    }
    return $idx;            
}