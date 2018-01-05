__version__ = '1.0'
__author__ = 'Zachary Nowak'
"""STANDARD LIBRARY IMPORTS"""
import time
import os

"""THIRD PARTY LIBRARY IMPORTS"""
import win32api

"""LOCAL LIBRARY IMPORTS"""
import listOfAllKeys

stateDict = listOfAllKeys.stateDict
nameDict = listOfAllKeys.nameDict

def start_recording(passage):
	passageTyped = ""
	end = True
	counter = 0
	print(passage[counter])
	numLines = countlines(passage)-1 #numLines is 1 over because the first element is 0
	
	pressTimeLine = []
	pressCharTimeLine = []
	releaseTimeLine = []
	releaseCharTimeLine = []
	#MAKE THE TIMELINES
	while end:
		for i in range(0,256):
			try: 
				if(win32api.GetAsyncKeyState(i) == stateDict[nameDict[i]]):
					char = nameDict[i]
					"""RELEASED"""
					if stateDict[char] == 0:
						releaseTimeLine.append(time.time())
						releaseCharTimeLine.append(nameDict[i])
						stateDict[char] = -32768 #CHANGE STATES
					
					else:
						"""PRESSED"""
						pressTimeLine.append(time.time())
						pressCharTimeLine.append(nameDict[i])
						
						if i == 8:
							passageTyped = passageTyped[:-1]
						else:
							passageTyped += nameDict[i]
						os.system('cls')
						print(passage[counter].lower())
						print(passageTyped.lower())
						stateDict[char] = 0
					if i == 13:
						if counter != numLines:
							counter +=1
							reset()#ADDED THIS
							passageTyped = ""
							print(passage[counter])
						else:
							end = False
							
			except KeyError:
				pass
				
	
	reset()
	print(pressTimeLine)
	print(pressCharTimeLine)
	return(pressTimeLine, pressCharTimeLine, releaseTimeLine, releaseCharTimeLine)

def countlines(passage):
	i = 0
	for line in passage:
		i += 1
	return(i)
	
def reset():
	try:
		getMessage = input()#PREVENTS ERRORS
	except SyntaxError or NameError:
		pass
	os.system('cls')