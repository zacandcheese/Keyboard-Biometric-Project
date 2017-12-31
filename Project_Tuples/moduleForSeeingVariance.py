"""
Get all of the files
"""
import matplotlib.pyplot as plt
import numpy
import glob
import os
import json
"""
xValues = [1,2,3,4,4,4]
yValues = [4,3,2,1,2,3]
plt.figure("test figure")
plt.scatter(xValues,yValues)
plt.show()
"""
plt.figure("Varience")
os.chdir("library")
listOfTxtFiles = []
for file in glob.glob("*.txt"):
	listOfTxtFiles.append(file)
print(listOfTxtFiles)

referenceDict = json.load(open(listOfTxtFiles[0],'r'))
keys = list(referenceDict.keys())

print referenceDict
for file in listOfTxtFiles[::2]:#Every Other Terms
    xValues = []
    yValues = []
    i = 0
    for key in keys:
        if not (key == '@' or key == 'V'):
            dict = json.load(open(file,'r'))
            xValues.append(i)
            yValues.append(dict[key])
            i = i+1
    plt.plot(xValues,yValues,label = file)

plt.legend()
plt.show()