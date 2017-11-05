__version__ = '1.0'
__author__ = 'Zachary Nowak'
"""STANDARD LIBRARY IMPORTS"""
from statistics import *

def create_dict(tupleList,pressCharTimeLine,pressTimeLine,dataDict):
	keyHistory = ""
	timingList = [[] for i in range(len(tupleList))]#FOR TIME IT TAKES TO WRITE A WORD
	for char in pressCharTimeLine:
		keyHistory += char
	for string in tupleList:
		i = 0
		index = tupleList.index(string)
		while(keyHistory.find(string.upper(), i))!= -1:
			position = keyHistory.find(string.upper(),i)
			i = position+len(tupleList[0])
			timingList[index].append(pressTimeLine[i - 1] - pressTimeLine[position])
	
	i = 0
	for tuple in timingList:
		#print("The history is: ", tuple)
		print("The median is: ", median(tuple))
		print("The mean is: ", harmonic_mean(tuple))
		dataDict[tupleList[i]] = median(tuple)
		i += 1
	return dataDict
