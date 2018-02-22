import glob
import os
import statistics

def tupleList(user):
   os.chdir("library/timelines/summary")
   listOfTxtFiles = []
   for file in glob.glob("*.txt"):
	   listOfTxtFiles.append(file)
   print(listOfTxtFiles)
   megaList = []
   for file in listOfTxtFiles:
      for line in open(file,"r").readlines(): 
         megaList.append(line)
   for line in megaList:
	   print(line.split(","))
   print(megaList)
tupleList(1)