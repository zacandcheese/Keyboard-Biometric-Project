import json

def saveTimeLine(pressTime, charTime, person):
	#person = input('Enter your name: ')
	filename = "library/Timelines/" + person + "A.txt"#GREEN computer
	filename2 = "library/Timelines/" + person + "B.txt"#GREEN computer
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