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

"""LOCAL LIBRARY IMPORTS"""
import moduleForFindingTuplesTime as FTT
import moduleForRecordingTimelines as RT
import moduleForFindingPressTimes as FPT
import moduleForSeeingConsistency as SC
import moduleForSavingTimelines as ST
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
word = open("Blank TEXT.txt","r")
sentence = word.readlines()
passage = sentence

#tupleList = passageMaker.list()
#NOTE TUPLES MUST BE SAME SIZE!!!
tupleList = createPassage.FindXTuples(passage, 9, 2)#(input string, frequency occurs, length of tuple)

"""TYPE THE PASSAGE AND RECORD THE TIME LINE"""
pressTimeLine,pressCharTimeLine,releaseTimeLine,releaseCharTimeLine = RT.start_recording(passage)
ST.saveTimeLine(pressTimeLine,pressCharTimeLine)

"""SEE CONSISTENCY"""
SC.seeConsistency(pressCharTimeLine,pressTimeLine,releaseCharTimeLine, releaseTimeLine)

"""COLLECT DATA FROM THE TIMELINE"""
dataDict = {}
dataDict = FTT.create_dict(tupleList, pressCharTimeLine,pressTimeLine,dataDict)
dataDict = FPT.create_dict(pressCharTimeLine,pressTimeLine,releaseCharTimeLine,releaseTimeLine,dataDict)

"""STORE DATA TO A FILE WITH THAT USER'S NAME"""
person = input('Enter your name: ')
#filename = "library/" + person + ".txt" MAIN computer
filename = "library/Sentence/" + person + ".txt"#GREEN computer
json.dump(dataDict, open(filename, 'w'))
