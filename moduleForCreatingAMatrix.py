#Makes Matrix
import numpy as np
import listOfAllKeys

#Note 1 = a
#[letter, timepress, flight time]

#[blank, flighTimeStart, last letter on right hand, last lettr on left hand include b]

#another matrix which makes keyboard into a xy plane.
#use distance formula and factor in time.

#[letter, timeStartpress,AVGtimepressed,last released, AVGflight time, counter, hand(0,1)]
#(Rows, columns)
"""
Makes a Dict which corresponds key to index of matrix
"""
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

"""
matrix is the thing which will hold the data
"""
#FIXME INCLUDE SOMETHING FOR HANDEDNESS
matrix = np.zeros(shape=(72,6))
for i in range(72):
	matrix[i][0] = i

