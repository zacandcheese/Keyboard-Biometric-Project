__version__ = '1.0'
__author__ = 'Zachary Nowak'
"""STANDARD LIBRARY IMPORTS"""
import glob
import os
import json
import statistics
#os.chdir("/Users/zacan/OneDrive/Documents/GitHub/Keyboard-Biometric-Testing/Project_Tuples/library")#Change zacan with Haley for GREEN
import analyzeData
"""
os.chdir("library2")
listOfTxtFiles = []
for file in glob.glob("*.txt"):
	listOfTxtFiles.append(file)
print(listOfTxtFiles)
"""
#os.chdir("library")#Change Haley with zacan for MAIN
Attempt = json.load(open("Attempts/ETHAN_2.txt",'r'))

listOfTxtFiles = []
for file in glob.glob("*.txt"):
	listOfTxtFiles.append(file)
print(listOfTxtFiles)

referenceDict = json.load(open(listOfTxtFiles[0],'r'))



counterDict = {}
for file in listOfTxtFiles:
	counterDict[file] = 0
	
#thresholdDict = {'D': 0.00855, 'C':0.0072,'es':0.0223, 'A':0.015934,'E':0.00568,'G': 0.00624,'T':0.006, ' ': 0.00274, 'I':0.007,'R':0.0097}#, 'C':  0.006875816191300637, 'es': .083 
thresholdDict = {'es': 0.0203}#, 'C':  0.006875816191300637, 'es': .083 
keys = ['en']#, 'A', 'E', 'G', 'T', ' ', 'I', 'R', 'C', 'D']

#OUT OF 10
#keys = list(thresholdDict.keys())

for key in keys:
	for file in listOfTxtFiles:
		threshold = .001#analyzeData.getAvgForPerson(file, keys)
		dict = json.load(open(file,'r'))
		if(abs(dict[key]-Attempt[key])<threshold):
			counterDict[file] += 1
print("\n", counterDict)
