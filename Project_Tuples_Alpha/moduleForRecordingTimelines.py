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
	print(passage)
	
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
						print(passage)
						print(passageTyped.lower())
						stateDict[char] = 0
					if i == 13:
						end = False
			except KeyError:
				pass
				
	getMessage = input()#PREVENTS ERRORS
	return(pressTimeLine, pressCharTimeLine, releaseTimeLine, releaseCharTimeLine)