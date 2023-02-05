#
# mkcsv.sh,  4 Feb 23

for f in data/*.xml
   do
   base_file=`basename $f .xml`
   awk -f dickens.awk < $f > data/"$base_file".body
   done

