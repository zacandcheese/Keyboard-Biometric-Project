import glob
import os
import statistics

os.chdir("library/timelines")

listOfTxtFiles = []
for file in glob.glob("/Summary/*.txt"):
	listOfTxtFiles.append(file)
print(listOfTxtFiles)
listOfApplyingFiles = []
for file in glob.glob("/Applying/*.txt"):
   listOfApplyingFiles.append(file)
print(listOfApplyingFiles)

listOfGoodTuples = ["that","tch","tc","nig","ight","one","feat","ery","ca","atch","hat","be","then","very","king"]
def newData(list):
   for file in list:
      megaList = []
      for line in open(file,"r").readLines():
         megaList.append(line)
         
      tuplesSeen = []
      
      for line in megaList:
         tuple = line.split(",")[0]#tuple
         if tuple not in tuplesSeen:
            tuplesSeen.append(tuple)
            if tuple in listOfGoodTuples:
               dummyList = []
               tuple2 = line.split(",")[0]
               if(tuple == tuple2):
                  dummyList.append(float(line.split(",")[3]))#MEDIAN
   
      
"""
find the tuple for all .txt files
if there is multiple of each, then
compare each of the text files 
print the tuple and variance
"""
   
newData(listOfTxtFiles)

   
   
   

