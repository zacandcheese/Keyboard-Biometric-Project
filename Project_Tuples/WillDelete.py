#Testing File
word = open("Blank TEXT.txt","r")
sentence = word.readlines()
#print(sentence[1])
import glob
import os
import json
import statistics
#os.chdir("/Users/zacan/OneDrive/Documents/GitHub/Keyboard-Biometric-Testing/Project_Tuples/library")#Change zacan with Haley for GREEN
os.chdir("library/Timelines")#Change Haley with zacan for MAIN

listOfTxtFiles = []
for file in glob.glob("*.txt"):
	listOfTxtFiles.append(file)
print(listOfTxtFiles)
#PressList
pressListFile = open(listOfTxtFiles[0],"r").readlines()
pressList = []
for pInt in pressListFile:
	pressList.append(int(pInt[0:-9])+int(pInt[11:-1])*10**-(len(pInt)-13))

#CharList
charListFile = open(listOfTxtFiles[1],"r").readlines()
charList = []
for pChar in charListFile:
	charList.append((pChar))

a = []
i = 0
#for char in charList:
#	a.append([char, pressList[i]])
print(pressList)
