__version__ = '1.0'
__author__ = 'Zachary Nowak'
"""STANDARD LIBRARY IMPORTS"""
import glob
import os
import json

os.chdir("/Users/zacan/OneDrive/Documents/GitHub/Keyboard-Biometric-Testing/Project_Tuples/library")

listOfTxtFiles = []
for file in glob.glob("*.txt"):
	listOfTxtFiles.append(file)
print(listOfTxtFiles)
for file in listOfTxtFiles:
	dict = json.load(open(file,'r'))
	print(dict)