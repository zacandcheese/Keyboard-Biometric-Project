import json
import platform
import os
def saveTimeLine(pressTime, charTime, person,location):
	
	if(location != ""):
		location = "Applying/"
	
	os.chdir("library/")
	
	filename = "Timelines/" +location+ person + "A.txt"#GREEN computer
	filename2 = "Timelines/" +location+ person + "B.txt"#GREEN computer
	outfile = open(filename, 'w')
	outfile2 = open(filename2, 'w')
	Dict1 = {}
	i = 0
	for num in pressTime:
		Dict1[i] = num
		i += 1
	Dict2 = {}
	i = 0
	for char in charTime:
		Dict2[i] = char
		i += 1
	json.dump(Dict1, open(filename, 'w'))
	json.dump(Dict2, open(filename2, 'w'))