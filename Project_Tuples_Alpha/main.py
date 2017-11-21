#cmd /K "$(FULL_CURRENT_PATH)"
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
#import passageMaker

"""FOLDER IMPORTS"""
#passage = passageMaker.create(something)
#passage = "The quick brown fox jumps over the lazy dog talking back"
passage = "the trophy other with both graph phone phat three philly hath that weather pho "

#tupleList = passageMaker.list()
#NOTE TUPLES MUST BE SAME SIZE!!!
tupleList = ["th", "ph"]

"""TYPE THE PASSAGE AND RECORD THE TIME LINE"""
pressTimeLine,pressCharTimeLine,releaseTimeLine,releaseCharTimeLine = RT.start_recording(passage)

"""COLLECT DATA FROM THE TIMELINE"""
dataDict = {}
dataDict = FTT.create_dict(tupleList, pressCharTimeLine,pressTimeLine,dataDict)	
dataDict = FPT.create_dict(pressCharTimeLine,pressTimeLine,releaseCharTimeLine,releaseTimeLine,dataDict)

"""STORE DATA TO A FILE WITH THAT USER'S NAME"""
person = input('Enter your name: ')
filename = "library/" + person + ".txt"
json.dump(dataDict, open(filename, 'w'))