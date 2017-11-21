__version__ = '1.0'
__author__ = 'Zachary Nowak'
"""STANDARD LIBRARY IMPORTS"""
import glob
import os
import json

#os.chdir("/Users/zacan/OneDrive/Documents/GitHub/Keyboard-Biometric-Testing/Project_Tuples/library")#Change zacan with Haley for GREEN
os.chdir("library")#Change Haley with zacan for MAIN

listOfTxtFiles = []
for file in glob.glob("*.txt"):
	listOfTxtFiles.append(file)
print(listOfTxtFiles)
for file in listOfTxtFiles:
	dict = json.load(open(file,'r'))
	#CONCLUSION COMMNON NOT COMMON
	#BALANCE OF REPETIBLE BUT VARIED
	
	#print(dict)#FOR EVERYTHING
	#print(dict['t '])
	#print(dict[' t'])
	#print(dict[u'@'])
	#print(dict['en'])
	#print(dict['ur'])
	#print(dict[' a'])