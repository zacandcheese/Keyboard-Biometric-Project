#cmd /K "$(FULL_CURRENT_PATH)"
"""
Author: Zachary Nowak 
Date:11/3/2017

Program Description: This code can record the 
Press Time and Flight Time of a tuple as a user
types a passage and it saves a matrix to a file. 
"""
#TO-DO
"""
PRESS TIME
STORING DATA
MAKING A SIGNATURE
"""

"""PYTHON/SITE PACKAGES"""
import win32api
import os
import time
import numpy as np

"""FOLDER FILES"""
import listOfAllKeys
import determineChar
#import passageMaker

"""FOLDER IMPORTS"""
#passage = passageMaker.create(something)
passage = "The quick brown fox jumps over the lazy dog talking back"
#tupleList = passageMaker.list()
#NOTE TUPLES MUST BE SAME SIZE AND NOT IN THE SAME WORD
tupleList = ["th","he","ck"]
stateDict = listOfAllKeys.stateDict
nameDict = listOfAllKeys.nameDict

"""LOCAL VARIABLES"""

timingList = [[] for i in range(len(tupleList))]#FOR TIME IT TAKES TO WRITE A WORD
pressList = [[0] for i in range(len(tupleList))]#FOR PRESS TIME [TIME, AVGPRESSTIME, COUNTER] EACH FIRST LETTER


tuplePresent = False
tupleCounter = 0
tupleTime = 0

passageTyped = ""

end = True
enterCounter = 1 #CHANGE TO 0 WHEN INCLUDING A NAMING FEATURE

print(passage)
while end:
	for i in range(0,256):
		try:
			if(win32api.GetAsyncKeyState(i) == stateDict[nameDict[i]]):
				"""DETERMINE WHAT CHAR IT IS"""
				char = nameDict[i]
				char2 = determineChar.determineChar(i,stateDict,nameDict)
						
				"""ADD TO THE STRING"""
				if char2 == "SHIFT" or char2 == "DELETE": #DO NOT ADD TO STRING
					if stateDict[char] == 0:
						stateDict[char] = -32768 #CHANGE STATES
					else: 
						stateDict[char] = 0 #CHANGES STATE
						os.system('cls')#CLEARS THE COMMAND PROMPT
						if char == "DELETE":#DELETE
							passageTyped = passageTyped[:-1]
						print(passage)
						print(passageTyped)
						
						
					"""RELEASED"""				
				elif stateDict[char] == 0:
					stateDict[char] = -32768 #CHANGE STATES
				
					"""PRESSED"""
				else:
					
					passageTyped += char2
					os.system('cls')#CLEARS THE COMMAND PROMPT
					
					if (char == '\n'):
						if(enterCounter>0):#IF ENTER IS PRESSED BREAK THE CODE
							end = False
						else:
							enterCounter+=1
		
					print(passage)
					print(passageTyped)
					
					stateDict[char] = 0 #CHANGES STATE
					"""TUPLE STUFF"""
					if tuplePresent:
						"""DETERMINE IF IT IS STILL GOOD"""
						if(passageTyped[-1] == tuple[tupleCounter]):
							"""DETERMINE IF IT IS DONE"""
							if tupleCounter == len(tupleList[0])-1:
								word = passageTyped[len(passageTyped)-(tupleCounter+1):]
								wordIndex = tupleList.index(word)
								timingList[wordIndex].append(time.time()-tupleTime)
								tuplePresent = False
								tupleCounter = 0
							else:
								tupleCounter += 1
						else:
							tuplePresent = False
							tupleCounter = 0
							
					"""DETERMINE IF IT IS A START OF A TUPLE"""		
					if not tuplePresent:
						for tuple in tupleList:
							if passageTyped[-1] == tuple[0]:
								tuplePresent = True
								tupleCounter += 1
								tupleTime = time.time()
								break
		except KeyError:
			pass
			
print("THIS IS THE TIMINGLIST", timingList)
		
getMessage = input()#PREVENT ERRORS
			
