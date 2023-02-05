#
# all_dickens.py,  4 Feb 23

# Extract named entities from Dickens letters made available by
# Lean at hackathon

# Support for Python3 features in Python2
# from __future__ import unicode_literals
# from __future__ import print_function

import os
import spacy
import sys

# nlp = spacy.load("en_core_web_sm") # Load model for English
nlp = spacy.load("en_core_web_md") # Medium model for English
# nlp = spacy.load("en_core_web_lg") # Large model for English


# Process one file
def get_NE(file_str):
   try:
      t = open(file_str)
      t.close()
   except:
      print("File", file_str, "not found")
      return -1

   with open(file_str, encoding='utf-8') as infile:
#   with open(file_str) as infile:
      text= infile.read()
#      text = text_str.encode('utf8')
      lines = text.split('\n')
      for line in lines:
         line = nlp(line) # Do the natural language hard work

#	 Print all named entities
         for ent in line.ents:
            print(ent.text, ent.label_, ent.start_char, ent.end_char, sep=",")


# Iterate over all files in a directory
def main():
   dir_str=sys.argv[1]

   directory = os.fsencode(dir_str)
   for file in os.listdir(directory):
      filename = os.fsdecode(file)
      if filename.endswith(".body"): 
         print(os.path.join(dir_str, filename))
         get_NE(os.path.join(dir_str, filename))
      else:
         continue


if __name__ == "__main__":
   main()


