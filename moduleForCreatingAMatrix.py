"""
Author: Zachary Nowak 
Date:10/31/2017

Program Description: This code creates a newDict which corresponds
key to index in the matrix. And matrix will hold all the data of
the typist.
"""
import numpy as np
import listOfAllKeys

"""Makes a Dict which corresponds key to index of matrix"""
nameDict = listOfAllKeys.nameDict
newDict = {}
i = 0
counter = 0;
while(counter<=72):
	for j in range(i,256):
		try:
			newDict[nameDict[j]] = counter
			break
		except KeyError:
			None
	i=j+1
	counter+=1


"""matrix is the thing which will hold the data"""
#[char, startPress,AVGPressTime,startFlight, AVGFlightTime, counter, hand(0,1)]
matrix = np.zeros(shape=(72,5))
for i in range(72):
	matrix[i][0] = i
	#FIXME INCLUDE SOMETHING FOR HANDEDNESS