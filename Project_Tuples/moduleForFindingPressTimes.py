__version__ = '1.0'
__author__ = 'Zachary Nowak'
"""STANDARD LIBRARY IMPORTS"""
from statistics import *

def create_dict(pressCharTimeLine,pressTimeLine,releaseCharTimeLine, releaseTimeLine, dataDict):
	
	#FIND UNIQUE CHARACTERS
	runningHistory = ""
	for char in pressCharTimeLine:
		if char not in runningHistory:
			runningHistory+=char
	numUniqueChar = len(runningHistory)-1#DO NOT COUNT THE /n
	pressTimingList = [[] for i in range(numUniqueChar)]
	for i in range(len(pressCharTimeLine)-1):
		char = pressCharTimeLine[i]
		j = releaseCharTimeLine.index(char, i)
		charIndex = runningHistory.index(char)
		pressTimingList[charIndex].append(releaseTimeLine[j] - pressTimeLine[i])
	for i in range(len(pressTimingList)):
		char = runningHistory[i]
		list = pressTimingList[i]
		dataDict[char] = median(list) 
	return dataDict
