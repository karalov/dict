#!/usr/bin/python3
import json
import sys
#from difflib import SequenceMatcher
from difflib import get_close_matches
data=json.load(open("data.json"))

#def findSimilar(w):
#    similar={"word":"","ratio":0.6}
#    for key in data.keys():
#       ratio=SequenceMatcher(None,w,key).ratio()
#       if ratio > similar["ratio"]:
#          similar["word"]=key
#         similar["ratio"]=ratio
#    return similar
def printdata(w):
     print("---------------")
     print(w.upper()+":")
     print("---------------")
     i=1
     for out in data[w]:
         print("%s. %s" % (i,out))
         i+=1

def translate(w):
  if w.lower() in data:
      printdata(w.lower())
  elif w.title() in data:
      printdata(w.title())
  elif w.upper() in data:
      printdata(w.upper())
  else:
     similar=get_close_matches(w,data.keys(),cutoff=0.8)
     if len(similar) == 0:
         print("Not found in dictionary: '%s'" % w)
     else:
         answr=input("Did you mean %s? (y/n) " % similar[0])
         if answr.lower() == "y":
            printdata(similar[0])
         else:
             print("Not found in dictionary: '%s'" % w)

if len(sys.argv) == 1:
   word=input("Please, enter a word or expression: ")
else:
   word=' '.join(sys.argv[1:])

translate(word)
