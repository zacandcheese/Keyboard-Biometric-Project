#moduleForCreatingAPassword
import random
def Create(String, length):
	if(String == "Random Letters"):
		pass
		#Create random Letters
	elif(String == "Story"):
		passage = ""
		book = open("1984Chapter1.txt", "r")
		line = book.readlines()
		randomLine = random.randrange(0,len(line))
		paragraph = (line[randomLine]+line[randomLine+1])#two lines bc it it enters after every paragraph
		
		while( len(paragraph)<(7*length)):#assuming words average about 6 + 1 space
			randomLine = random.randrange(0,len(line))
			paragraph = (line[randomLine]+line[randomLine+1])#two lines bc it it enters after every paragraph
		
		counter = 0;#counts the number of spaces
		i=0;
		while(counter<length):
			passage+=paragraph[i]
			if(paragraph[i] == ' '):
				counter+=1
			i+=1;
		return(passage)
	elif(Sting == "Random Words"):
		pass
		#Create random Letters
		