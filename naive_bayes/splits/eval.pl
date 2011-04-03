#!/usr/local/bin/perl

use English;
use Carp;
use Getopt::Long;

sub Usage{
  my $message = shift;

  print STDERR $message, "\n" if $message;
  print STDERR "\nUsage: $0 < resultfile\n";

  print STDERR <<'EOM';
          resultfile must have a format like the following, 
          where "L" for "liberal" and "C" for "conservative".

          document_file_name_1 religion
          document_file_name_2 baseball
          document_file_name_3 windows
	      ...
          document_file_name_N ibm

EOM

    exit(1);

}

if (! &GetOptions("help", "type=s") or
    $opt_help) {
  &Usage();
}



@labels=('atheism','auto','baseball',  'christian' , 'crypt' , 'electronics' , 'graphics' , 'guns' , 'hockey' , 'ibm' , 'mac' , 'medical' , 'mideast' , 'motorcycles' , 'politics' , 'religion' , 'sale' , 'space' , 'windows' , 'winx');

@count=();
@missed=();
$total=0;
$totalmissed=0;

for ($j=0; $j<@labels; $j++){
$count[$j]=0;
$missed[$j]=0;
}


print "2";
while (<stdin>) {
print "1";
    ($id,$tag)=split; 
     for ($j=0; $j<@labels; $j++){
	if ($id =~ /$labels[$j]/ ) { 
		$count[$j]++;       
		if ($tag ne "$labels[$j]") {
	    		$missed[$j]++;
			$totalmissed++;
		} 
	}
    }
    $total++;
}

print "\n";
print "Total number of documents = $total\n";
for ($i=0;$i<@labels; $i++){
print "Total number of $labels[$i] documents = ", $count[$i],"\n";
print "Number of mistakes in $labels[$i] documents = $missed[$i]\n";
}
print "** Classification accuracy = ", ($total-$totalmissed)/$total, "\n";
