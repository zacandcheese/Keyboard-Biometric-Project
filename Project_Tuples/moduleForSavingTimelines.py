import json

def saveTimeLine(pressTime, charTime):
	person = input('Enter your name: ')
	filename = "library/Timelines/" + person + "A.txt"#GREEN computer
	filename2 = "library/Timelines/" + person + "B.txt"#GREEN computer
	outfile = open(filename, 'w')
	outfile2 = open(filename2, 'w')
	for press in pressTime:
		outfile.write(str(press)+"\n")
	for char in charTime:
		outfile2.write(str(char)+ "\n")
	#with open("file.txt", "w") as output:
		#output.write(str(values))
saveTimeLine([1,2,3,4,5],['a','b','c','d','e'])