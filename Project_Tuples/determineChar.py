import listOfAllKeys

def determineChar(i,stateDict,nameDict):

	char = nameDict[i]
	char2 = char
	if i<=57 and i>=48:#NUMBERS
		if stateDict["SHIFT"] == 0:
			char2 = nameDict[i-16]
		else:pass						
	elif (char == "SHIFT") or (stateDict["SHIFT"] == 0) or (char == '.'):#SHIFT KEY, PERIOD, or UPPERCASE
		pass
	else:#LOWERCASE
		try:
			char2 = nameDict[i+32]
		except KeyError:
			pass
		
	return char2