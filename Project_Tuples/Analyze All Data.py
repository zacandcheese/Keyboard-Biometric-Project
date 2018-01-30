import glob
import os
import statistics

os.chdir("library/timelines/summary")

listOfTxtFiles = []
for file in glob.glob("*.txt"):
	listOfTxtFiles.append(file)
print(listOfTxtFiles)

def newData(list):
	minorList = []
	megaList = []
	for file in list:
		for line in open(file,"r").readlines():#open the file, read all lines, add each line to the megalist
			megaList.append(line)
	#for line in megaList:
	#   print(line.split(","))
	#print(megaList)
   
	fileName = "Analyze/" + "Mean and Variance data" + ".txt"
	tuplesSeen = []
	for line in megaList:
		tuple = line.split(",")[0]#tuple
		if tuple not in tuplesSeen:
			tuplesSeen.append(tuple)
			dummyList = []
			dummyList2 = []
			for line in megaList:#searches
				tuple2 = line.split(",")[0]
				if(tuple == tuple2):
					dummyList.append(float(line.split(",")[3]))#MEDIAN
					dummyList2.append(float(line.split(",")[4]))#VARIANCE
               

			if(len(dummyList)>=3 and len(dummyList2)>=3):
				print(tuple, statistics.variance(dummyList),statistics.variance(dummyList2))
				dummyFile = open(fileName, 'a')
				dummyFile.write((str(tuple))+","+str(statistics.variance(dummyList))+","+str(statistics.variance(dummyList2))+"\n")

   
      
"""
find the tuple for all .txt files
if there is multiple of each, then
compare each of the text files 
print the tuple and variance
"""
   
newData(listOfTxtFiles)

   
   
   

