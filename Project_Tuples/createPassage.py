# ReadSentence
#
#  Reads a string from standard input
#
#  returns string
#
#  Matt Nowak 11.5.2017
import os
import collections

def MeetCritera(s,max,freq,length):
	tlist = FindXTuples(s,freq, length)
	if (len(s) <max and len(tlist)>0):
		return(True)
	return(False)
  
def BuildSentences(f,max, freq, length):
	file = open(f,"r")
	s=""
	while True:
		c=file.read(1)
		if not c:
			break
		elif(c != '.'):
			s += c
		else:
			if MeetCritera(s,max,freq,length):
				#print(s.lower())
				break
			s=""
	return(s.lower())

def BuildTuples(passage, length_of_tuple):
	tupleDict = {}
	for i in range(len(passage)-length_of_tuple):
		tupleDict[(passage[0+i:length_of_tuple+i])] = 0
	for i in range(len(passage)-length_of_tuple):
		tupleDict[passage[0+i:length_of_tuple+i]] += 1
	#print(tupleDict)
	maxTuple = max(tupleDict, key=tupleDict.get)
	#print("The max tuple is " + max)
	tupleList = []
	tupleList.append(maxTuple)
	return(tupleList)
def FindXTuples(s,n,x):
	#s: input passage
	#n: frequency wanted
	#x how how the tuple
	tlist = []
	for i in range(0,len(s)-1,1):
		t=s[i:i+x] #builds a tuple of x length from spot i in the string
		
		#ADD if tuple is not already in the list,
		#occurs at least n times in the string, 
		#and is exactly x chars in length
		if((t not in tlist)and(s.count(t)>=n) and (len(t) == x)):
			tlist.append(t)
			#print(t,s.count(t))
	return(tlist)
	