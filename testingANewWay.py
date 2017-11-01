#cmd /K "$(FULL_CURRENT_PATH)"
"""
Author: Zachary Nowak 
Date:10/31/2017

Program Description: This code can record the 
Press Time and Flight Time of a user as they 
type a passage and saves the matrix to a file. 
"""
import win32api
import os
import moduleForCreatingAPassword
import listOfAllKeys
import moduleForCreatingAMatrix
import time
import numpy as np
#TO-DO
#FIXME IMPROVE FLIGHT TIME

stateDict = listOfAllKeys.stateDict
nameDict = listOfAllKeys.nameDict
xDict = listOfAllKeys.xDict
yDict = listOfAllKeys.yDict
keyToIndex = moduleForCreatingAMatrix.newDict

"""[letter(in the keyToIndex), startPress, AVGPressTime, startFlight, AVGFlightTime, counter, hand(0-1)"""
#dataMatrix info
startPress 		= 1
AVGPressTime	= 2
startFlight 	= 3
AVGFlightTime 	= 4
counter 		= 5
hand 			= 6

person = input('Enter your name: ')
filename = person+".txt"
try:
	dataMatrix = np.loadtxt(filename, delimiter=",", unpack=False)#OPEN IF EXISTS
except FileNotFoundError:
	dataMatrix = moduleForCreatingAMatrix.matrix #MAKE A NEW ONE IF NOT
	
flightTime = 0;
passageTyped = ""
passage = moduleForCreatingAPassword.Create("Story", 20)#20 is the length of the story
print(passage)

end = True
while end:
	for i in range(0,256):
		try:
			if(win32api.GetAsyncKeyState(i) == stateDict[nameDict[i]]):
				char = nameDict[i]
				dM = dataMatrix[int(keyToIndex[char])]
				if char == "SHIFT": #DO NOT DO ANYTHING
					pass 
				
					"""RELEASED"""				
				if stateDict[char] == 0:
					dM[AVGPressTime] = (dM[AVGPressTime]*dM[counter]+(time.time()-dM[startPress]))/(dM[counter]+1)
					dM[startFlight] = time.time()
					stateDict[char] = -32768 #CHANGE STATES
				
					"""PRESSED"""
				else:
					if dM[startFlight]>0:#MEANS STARTED CODE
						dM[AVGFlightTime] = (dM[AVGFlightTime]*dM[counter]+(time.time()-dM[startFlight]))/(dM[counter]+1)
					dM[startPress] = time.time()
					dM[counter] += 1#ADD ONE TO THE COUNTER BECAUSE IT WAS PRESSED
					
					os.system('cls')#CLEARS THE COMMAND PROMPT
					
					if (char == '\n')and (dM[counter]>1):#IF ENTER IS PRESSED BREAK THE CODE
						end = False
						
					if char == "DELETE":#DELETE
						passageTyped = passageTyped[:-1]
						
					elif i<=57 and i>=48:#NUMBERS
						if stateDict["SHIFT"] == 0:
							passageTyped += nameDict[i-16]
						else:passageTyped += char
						
					elif char == "SHIFT":#SHIFT
						pass
					elif stateDict["SHIFT"] == 0:#UPPERCASE
						passageTyped += char
					elif char == '.':
						passageTyped+='.'
					else:#lowercase
						try:
							passageTyped += nameDict[i+32]
						except KeyError:
							passageTyped += nameDict[i]
							
					print(passage)
					print(passageTyped)
					stateDict[char] = 0 #CHANGES STATE
					
		except KeyError:
			pass
			
print("Errors: ", dataMatrix[0][counter])
#RESET ENTERS and BACKSPACES SO THEY CAN BE USED AGAIN
dataMatrix[1][counter] = 0;
dataMatrix[0][counter] = 0;

np.savetxt(filename, dataMatrix, fmt ='%1.7e', delimiter=',')#SAVES ARRAY TO FILE WITH THE PERSONS NAME
