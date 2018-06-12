#!/usr/bin/python3
import json
word=input("Please, enter a word or expression: ")
print("---------------")
print(word+":")
print("---------------")
data=json.load(open("data.json"))
if word in data:
   i=1
   for out in data[word]:
       print("%s. %s" % (i,out))
       i+=1
else:
    print("Not found in dictionary: '%s'" % word)
