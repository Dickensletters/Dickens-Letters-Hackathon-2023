Code developed on Saturday at the Dickens letters hackathon.

data/

Directory containing xml files supplied by Leon.  Some file suffixes were in upper case (i.e., XML), and were converted to lower case (i.e., xml).

mkcsv.sh

Extract body of letter from xml file.  Loops over all xml files in data directory, output written to a corresponding .body file.

dickens.awk 

Called by mkcsv.sh

python3 dickvol.py file.txt

Loop over all the lines in file.txt, extracting named entities

python3 all_dickens.py data/

Loop over all .body files in the data directory, for each file extract the named entities.

l700ne.txt

Named entities extracted from all .body files in data


