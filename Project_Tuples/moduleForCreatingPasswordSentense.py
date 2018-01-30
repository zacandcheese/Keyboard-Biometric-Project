#Module for creating a sentence with a tuple
WORDS_DICTIONARY = []
for word in open("WORDS_DICTIONARY.txt",'r').readlines():
	WORDS_DICTIONARY.append(word)
	
def makeSentence(tuple):
	for word in WORDS_DICTIONARY:
		if tuple in word:
			print(word)

makeSentence("ca")
