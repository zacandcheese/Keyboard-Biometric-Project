import win32api
import os
import moduleForCreatingAPassword
import listOfAllKeys
import moduleForCreatingAMatrix
import time
import numpy as np





"""
[letter(in the keyToIndex), startPress, AVGPressTime, startFlight, AVGFlightTime, counter, hand(0-1)
"""
startPress 		= 1
AVGPressTime	= 2
startFlight 	= 3
AVGFlightTime 	= 4
counter 		= 5
hand 			= 6


stateDict = listOfAllKeys.stateDict
nameDict = listOfAllKeys.nameDict

flightTime = 0;
passageTyped = ""

#FIXME IMPROVE FLIGHT TIME
person = input('Enter your name: ')
filename = person+".txt"
try:
	dataMatrix = np.loadtxt(filename, delimiter=",", unpack=False)#OPEN IF EXISTS
except FileNotFoundError:
	dataMatrix = moduleForCreatingAMatrix.matrix#MAKE A NEW ONE IF NOT

keyToIndex = moduleForCreatingAMatrix.newDict


passage = moduleForCreatingAPassword.Create("Story", 20)
print(passage)
end = True
while end:
	for i in range(0,256):
		try:
			if(win32api.GetAsyncKeyState(i) == stateDict[nameDict[i]]):
				char = nameDict[i]
				dM = dataMatrix[int(keyToIndex[char])]
				if char == "SHIFT":
					pass
					#Uppercase
				if stateDict[char] == 0:#Released
					dM[AVGPressTime] = (dM[AVGPressTime]*dM[counter]+(time.time()-dM[startPress]))/(dM[counter]+1)
					#FIXME END TIMER FOR AVG TIMER(avg time*counter+ (startPress-endPress)/(counter+1)
					
					dM[startFlight] = time.time()#FIXME START TIMER
					stateDict[char] = -32768
					
				else:#Pressed
					if dM[startFlight]>0:#MEANS STARTED CODE
						dM[AVGFlightTime] = (dM[AVGFlightTime]*dM[counter]+(time.time()-dM[startFlight]))/(dM[counter]+1)
						#FIXME END TIMER FOR AVG TIMER(avg time*counter+ (startPress-endPress)/(counter+1)
					
					dM[startPress] = time.time()#FIXME START TIMER FOR PRESS TIME
					dM[counter] += 1 #counter
					os.system('cls')
					if (char == '\n')and (dM[counter]>1):#Enter
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
							pass
							passageTyped += nameDict[i]
					print(passage)
					print(passageTyped)
					stateDict[char] = 0
		except KeyError:
			pass
			
#RESET ENTER
dataMatrix[1][counter] = 0;

np.savetxt(filename, dataMatrix, fmt ='%1.4e', delimiter=',')   # X is an array
