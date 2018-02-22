import glob
import os
import statistics

os.chdir("library/Timelines")

listOfTxtFiles = []
for file in glob.glob("Summary/*.txt"):
	listOfTxtFiles.append(file)
print(listOfTxtFiles)

listOfApplyingFiles = []
for file in glob.glob("Applying/Summary/*.txt"):
   listOfApplyingFiles.append(file)
print(listOfApplyingFiles)

listOfGoodTuples = ["that","tch","tc","nig","ight","one","feat","ery","ca","atch","hat","be","then","very","king"]

def newData(applying, list):
   
   for file in list:
      megaList = []
      
      for line in open(file,"r").readlines():
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
                  for line2 in open(applying[0],"r").readlines():
                     appTuple = line2.split(",")[0]
                     if (appTuple == tuple):
                        print(tuple + " " + file + ": " + str(dummyList[0]) + " APPLIER: " + str(line2.split(",")[3]))
                        print("The difference is " + str(abs(dummyList[0]-float(line2.split(",")[3]))))
      
      print("\n")            
      
"""
find the tuple for all .txt files
if there is multiple of each, then
compare each of the text files 
print the tuple and variance
"""
   
newData(listOfApplyingFiles,listOfTxtFiles)

   
   
   

