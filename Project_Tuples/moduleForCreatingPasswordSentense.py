#Module for creating a sentence with a tuple
import nltk
import random



from nltk.corpus import brown

tupleList = ["ca", "that", "th"]

def Noun(NN):
	return NN[random.randint(0, len(NN)-1)]
def Verb(VB):
	return VB[random.randint(0, len(VB)-1)]
def Adjective(ADJ):
	return ADJ[random.randint(0, len(ADJ)-1)]
def Proper(NNP):
	return(NNP[random.randint(0, len(NNP)-1)])
	
def makeSentence(tupleList):
	NN = []
	VB = []
	ADJ = []
	NNP = []
	for word in brown.tagged_words():
		for tuple in tupleList:
			if((tuple.lower() in word[0].lower()) and (word[1] == "NN") and (word[0].lower() not in NN)):
				NN.append(word[0])
			if((tuple.lower() in word[0].lower()) and (word[1] == "VB") and (word[0].lower() not in VB)):
				VB.append(word[0])
			if((tuple.lower() in word[0].lower()) and (word[1] == "JJ") and (word[0].lower() not in ADJ)):
				ADJ.append(word[0])
			if((tuple.lower() in word[0].lower()) and (word[1] == "NNP") and (word[0].lower() not in NNP)):
				NNP.append(word[0])	
				
	print("A vacation is when you take a trip to some " +Adjective(ADJ)+" place "+
	"with your "+ Adjective(ADJ)+" family. Usually you go to some place "+
	"that is near a/an "+ Noun(NN) + " or up on a/an "+ Noun(NN)+"."+ 
	"A good vacation place is one where you can ride "+ Noun(NN)+"s"+
	"or play "+ Noun(NN)+" or go hunting for " +Noun(NN)+"." )
	
makeSentence(tupleList)
