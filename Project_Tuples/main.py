#cmd /K "$(FULL_CURRENT_PATH)"

#cd ~/Documents/GitHub/Keyboard-Biometric-Project/Project_Tuples
#sudo python -m pip install statistics
#python analyzeData.py

"""
Author: Zachary Nowak
Date:11/3/2017

Program Description: This code can record the
Press Time and Flight Time of a tuple as a user
types a passage and it saves a matrix to a file.
"""
__version__ = '1.0'
__author__ = 'Zachary Nowak'
"""STANDARD LIBRARY IMPORTS"""
import json
import platform

"""LOCAL LIBRARY IMPORTS"""
import moduleForFindingTuplesTime as FTT
#import moduleForRecordingTimelines as RT
import moduleForFindingPressTimes as FPT
import moduleForSeeingConsistency as SC
import moduleForSavingTimelines as ST
import moduleForRecordingWithGUI as GUI
import moduleForCreatingPasswordSentense as PS
import moduleForDeconstructingTimelines as DT
import createPassage

"""FOLDER IMPORTS"""
maxLengthOfPassage = 150 #Too Long
frequency = 6 #Number the tuple occurs
tupleLength = 2 #Number the length of the tuple
infile = "1984Chapter1.txt"

#Alternate between these two Passages for Warm Up
passage = createPassage.BuildSentences(infile,maxLengthOfPassage,frequency,tupleLength)
#passage = "the quick brown fox jumps over the lazy dog talking back"
#passage = "the trophy other with both graph phone phat three philly hath that weather pho"

#For Testing in differentparts of a sentence
word = open("textGoldenBird.txt","r")
sentence = word.readlines()
passage = sentence

#tupleList = passageMaker.list()
#NOTE TUPLES MUST BE SAME SIZE!!!
tupleList = createPassage.FindXTuples(passage, 9, 2)#(input string, frequency occurs, length of tuple)ACCOUNT FOR EVERYBODY (MATTS SPREAAD SHEET)
tupleList = ["tch"]   

if(platform.system() == "Darwin"):
   name = raw_input("What is your name: ")#for a Mac
   location = raw_input("What is the location: ")
   
if(platform.system() == "Windows"):
	name = input("What is your name: ")
	location = input("What is your location: ")

if(location != ""):
	location = "Applyling/"
	passage = (PS.makeSentence(tupleList)).split(".")
	print(passage)
else:
	word = open("textGoldenBird.txt","r")
	passage = word.readlines()
#CHOOSING PASSAGE



"""TYPE THE PASSAGE AND RECORD THE TIME LINE"""
#pressTimeLine,pressCharTimeLine,releaseTimeLine,releaseCharTimeLine,name = RT.start_recording(passage)
pressTimeLine,pressCharTimeLine,releaseTimeLine,releaseCharTimeLine = GUI.start_recording(passage)
ST.saveTimeLine(pressTimeLine,pressCharTimeLine,name,location)
DT.userSummary(name)
"""
""SEE CONSISTENCY""
SC.seeConsistency(pressCharTimeLine,pressTimeLine,releaseCharTimeLine, releaseTimeLine)

""COLLECT DATA FROM THE TIMELINE""
dataDict = {}
dataDict = FTT.create_dict(tupleList, pressCharTimeLine,pressTimeLine,dataDict)
dataDict = FPT.create_dict(pressCharTimeLine,pressTimeLine,releaseCharTimeLine,releaseTimeLine,dataDict)

""STORE DATA TO A FILE WITH THAT USER'S NAME""

#filename = "library/" + person + ".txt" MAIN computer
filename = "library/"+location + person + ".txt"#GREEN computer
json.dump(dataDict, open(filename, 'w'))"""