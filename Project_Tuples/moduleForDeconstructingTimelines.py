#Testing File
word = open("Blank TEXT.txt","r")
sentence = word.readlines()
#print(sentence[1])
import glob
import os
import json
import statistics
import string

#os.chdir("/Users/zacan/OneDrive/Documents/GitHub/Keyboard-Biometric-Testing/Project_Tuples/library")#Change zacan with Haley for GREEN
os.chdir("library/Timelines")#Change Haley with zacan for MAIN


def makeTable(intDict, charDict):
	"""
	list of all tuples found in what the person typed
	# of appearances, median, variance
	"""
	totalSentence = ""
	for i in range(len(charDict)):
		#if charDict[str(i)] != "\n":
		totalSentence += charDict[str(i)]
		
	print(totalSentence)
	#File
	person = input("Enter Name: ")
	filename = "Summary/" + person + ".txt"#GREEN computer
	
	#cycle all letters
	for i in ([""]+list(string.ascii_lowercase)):
		for j in ([""]+list(string.ascii_lowercase)):
			for k in (list(string.ascii_lowercase)):
				for l in (list(string.ascii_lowercase)):
					tuple = i+j+k+l
					if tuple in totalSentence.lower():
						allTimes = []
						for m in range(len(totalSentence)-len(tuple)):
							pTuple = ""
							for n in range(len(tuple)):
								pTuple += totalSentence[(m+n)].lower()
							if (pTuple == tuple):
								allTimes.append(intDict[str(m+len(tuple)-1)]-intDict[str(m)])
						#ADD IT TO FILE
						if len(allTimes)>=3:
							print(tuple,len(allTimes),statistics.mean(allTimes),statistics.median(allTimes), statistics.variance(allTimes))
							dummyFile = open(filename, 'a')
							dummyFile.write(str(tuple)+","+str(len(allTimes))+","+str(statistics.mean(allTimes))+","+str(statistics.median(allTimes))+","+str(statistics.variance(allTimes))+"\n")
					#The entire sentence of what they wrote
					#list of every appearances, time for each
	

listOfTxtFiles = []
for file in glob.glob("*.txt"):
	listOfTxtFiles.append(file)
print(listOfTxtFiles)
numFiles = round(len(listOfTxtFiles)/2)

for num in range(numFiles):
	intDict = json.load(open(listOfTxtFiles[num*2],'r'))
	charDict = json.load(open(listOfTxtFiles[num*2+1],'r'))
	#print(intDict)
	#print(charDict)
	makeTable(intDict, charDict)
	print("\n")

