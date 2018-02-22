import glob
import os
import statistics

os.chdir("library/Timelines")

listOfTxtFiles = []
for file in glob.glob("Summary/*.txt"):
	listOfTxtFiles.append(file)
print(listOfTxtFiles)

def newData(list):
	megaList = []
	for file in list:
		for line in open(file,"r").readlines():
			megaList.append(line)
    #HAVE EVERYBODIES DATA
	filename = "unique3" + ".txt"#name
	tuplesSeen = []
	
	for line in megaList:
		tuple = line.split(",")[0]
		if tuple not in tuplesSeen:
			tuplesSeen.append(tuple)
			#GIVES ALL TUPLES
			tupleList = []
			#Check all people
			numList = []
			for name in list:
				i = 0
				flag = False
				for line2 in open(name,"r").readlines():
					i+= 1
					if(line2.split(",")[0] == tuple):
						flag = True
						tupleList.append(float(line2.split(",")[3]))#Median
						numList.append(int(line2.split(",")[1]))#NUM
					elif(i==(len(open(name,"r").readlines())-1) and not flag):
						tupleList.append(" ")
						
					#if(len(dummyList)>=3):
					#	tupleList.append(statistics.median(dummyList))
					
			if(len(tupleList)>=3):
				dummyFile = open(filename, 'a')
				pString = str(tuple)+", "+str(statistics.median(numList))+", "
				for person in tupleList:
					pString += str(person)+", "
				pString += "\n"
				
				dummyFile.write(pString)
"""
find the tuple for all .txt files
if there is multiple of each, then
compare each of the text files 
print the tuple and variance
"""
   
newData(listOfTxtFiles)

