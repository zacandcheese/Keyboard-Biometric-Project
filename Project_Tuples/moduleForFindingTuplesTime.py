__version__ = '1.0'
__author__ = 'Zachary Nowak'
"""STANDARD LIBRARY IMPORTS"""
from statistics import median#FIXME

def create_dict(tupleList,pressCharTimeLine,pressTimeLine,dataDict):
	keyHistory = ""
	timingList = [[] for i in range(len(tupleList))]
	
	"""CREATE A STRING WITH ALL THE EVENTS"""
	for char in pressCharTimeLine:
		keyHistory += char
	
	"""FIND THE TIME IT TAKES TO TYPE EACH WORD FROM PRESS TO PRESS"""
	for string in tupleList:
		i = 0
		index = tupleList.index(string)
		while(keyHistory.find(string.upper(), i))!= -1:
			position = keyHistory.find(string.upper(),i)
			i = position + len(tupleList[0])
			timingList[index].append(pressTimeLine[i - 1] - pressTimeLine[position])
	
	"""ASSIGN THE TUPLE WITH IT'S MEDIAN TOTAL PRESS TIME"""
	i = 0
	for tuple in timingList:
		print('The median for ' +tupleList[i]+' : ', median(tuple))
		#print("The mean is: ", harmonic_mean(tuple))FIXME
		dataDict[tupleList[i]] = median(tuple)
		i += 1
	return dataDict
