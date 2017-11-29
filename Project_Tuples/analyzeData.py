__version__ = '1.0'
__author__ = 'Zachary Nowak'
"""STANDARD LIBRARY IMPORTS"""
import glob
import os
import json
import statistics
#os.chdir("/Users/zacan/OneDrive/Documents/GitHub/Keyboard-Biometric-Testing/Project_Tuples/library")#Change zacan with Haley for GREEN
os.chdir("library")#Change Haley with zacan for MAIN

listOfTxtFiles = []
for file in glob.glob("*.txt"):
	listOfTxtFiles.append(file)
print(listOfTxtFiles)

referenceDict = json.load(open(listOfTxtFiles[0],'r'))
keys = list(referenceDict.keys())

consistencyDict = {}
varianceDict = {}

for key in keys:
	listForKey = []
	if not (key == '@' or key == 'V'): #NO MISTAKES
		for file in listOfTxtFiles:
			dict = json.load(open(file,'r'))
			listForKey.append(dict[key])
			
		listForKeyForEachPerson = []
		for i in range(int((len(listForKey))/2)):
			listForKeyForEachPerson.append(statistics.variance(listForKey[i*2:i*2+2]))
	
		consistencyDict[key] = statistics.mean(listForKeyForEachPerson)
		varianceDict[key] = statistics.variance(listForKey)

#SORTED LOW TO HIGH
#print(sorted(consistencyDict, key=consistencyDict.get))
#print("\n")
#print(sorted(varianceDict, key=varianceDict.get))
consistencyList = sorted(consistencyDict, key=consistencyDict.get)
varianceList = sorted(varianceDict, key=varianceDict.get)

#CONCLUSION COMMNON NOT COMMON
#BALANCE OF REPETIBLE BUT VARIED
keys = list(consistencyDict.keys())
sumDict = {}
for key in keys:
	sumDict[key] = len(consistencyList)-consistencyList.index(key)+ varianceList.index(key)
print("\n",sumDict)
print("\n", sorted(sumDict, key = sumDict.get))	

"""
orderedList = [];
for num in sorted(consistencyDict.values()):
	for key, value in consistencyDict.items():
		if num == value:
			orderedList.append(key)
			
print(orderedList)
"""

