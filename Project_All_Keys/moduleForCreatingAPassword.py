"""
Author: Zachary Nowak 
Date:10/31/2017

Program Description: This code can create a passage
with random letters, random words, or words from a story
"""
import random
import moduleForCreatingAMatrix
def Create(String, length):
	passage = ""
	
	if(String == "Random Letters"):
		import listOfAllKeys
		nameDict = listOfAllKeys.nameDict
		i = 17# To avoid including DELETE, \n, ENTER
		counter = 0;
		while(counter<len(nameDict)):
			for j in range(i,256):
				try:
					passage+=(nameDict[j])
					break
				except KeyError:
					None
			i=j+1
			counter+=1
		return(passage+passage)
		
	elif(String == "Story"):
		"""Opens a book and chooses a paragraph"""
		book = open("1984Chapter1.txt", "r")
		line = book.readlines()
		randomLine = random.randrange(0,len(line))
		paragraph = (line[randomLine]+line[randomLine+1])#Since every line could either be paragraph or a \n this ensures a paragraph
		
		"""Keeps looking through the document until it finds a suitable paragraph"""
		while(len(paragraph)<(7*length)):# this is assuming words average about 6 + 1 space
			randomLine = random.randrange(0,len(line))
			paragraph = (line[randomLine]+line[randomLine+1])
		
		"""Creates the the passage"""
		counter = 0;#counts the number of spaces
		i=0
		while(counter<length):
			passage+=paragraph[i]
			if(paragraph[i] == ' '):
				counter+=1
			i+=1
			
		book.close()
		return(passage)
	elif (String == "All Letters"):
		return("The quick brown fox jumps over the lazy dog")
	elif(String == "Random Words"):
		pass#FIXME
				