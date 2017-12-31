__version__ = '1.0'
__author__ = 'Zachary Nowak'
"""IMPORTS"""
import matplotlib.pyplot as plt
import statistics
import json
def seeConsistency(pressCharTimeLine,pressTimeLine,releaseCharTimeLine, releaseTimeLine):
	plt.figure("Letters")
	"""FIND NUMBER OF UNIQUE CHARACTERS"""
	runningHistory = ""
	for char in pressCharTimeLine:
		if char not in runningHistory:
			runningHistory+=char
	numUniqueChar = len(runningHistory)-1#DO NOT COUNT THE /n
	pressTimingList = [[] for i in range(numUniqueChar)]
	
	"""FIND THE PRESS TIMES FOR EACH LETTER"""
	for i in range(len(pressCharTimeLine)-1):
		#The function finds the initial press time in the timeline then it subtracts
		#that from the release time and that gives the total press time.
		char = pressCharTimeLine[i]
		j = 0
		while(True):
			j = releaseCharTimeLine.index(char,j)
			sum = releaseTimeLine[j]-pressTimeLine[i]
			if (sum>0):
				break
			else:
				j += 1
				
		charIndex = runningHistory.index(char)
		pressTimingList[charIndex].append(releaseTimeLine[j] - pressTimeLine[i])
		
	"""ASSIGN THE LETTER WITH IT'S MEDIAN TOTAL PRESS TIME"""	
	for i in range(len(pressTimingList)):
		dummyList = [i]*len(pressTimingList[i])
		#print(dummyList)
		#print(pressTimingList[i])
		plt.scatter(dummyList, pressTimingList[i])
		
	yList = []
	xList = range(len(pressTimingList))
	yList2 = []
	
	"""
	For the storing mean
	"""
	dataDict = {}
	for i in range(len(pressTimingList)):
		try:
			dataDict[i] = statistics.median(pressTimingList[i])
			yList.append(statistics.median(pressTimingList[i]))
			yList2.append(statistics.mean(pressTimingList[i]))
			
		except:
			dataDict[i] = pressTimingList[i]
			yList.append(pressTimingList[i])
			yList2.append(pressTimingList[i])
	
	plt.plot(xList,yList, label = "median");
	plt.plot(xList, yList2, label = "mean");	
	plt.legend()
	plt.show()
	person = input('Enter your name: ')
	#filename = "library/" + person + ".txt" MAIN computer
	filename = "library/Consistency/" + person + ".txt"#GREEN computer
	json.dump(dataDict, open(filename, 'w'))