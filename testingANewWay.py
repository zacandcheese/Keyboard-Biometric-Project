import win32api
import os
import moduleForCreatingAPassword
import listOfAllKeys
stateDict = listOfAllKeys.stateDict
nameDict = listOfAllKeys.nameDict
passageTyped = ""

#FIXME MATRIX OF TIMES

passage = moduleForCreatingAPassword.Create("Story", 20)
print(passage)
end = True
while end:
	for i in range(0,256):
		try:
			if(win32api.GetAsyncKeyState(i) == stateDict[nameDict[i]]):
				char = nameDict[i]
				if char == "SHIFT":
					pass
					#Uppercase
				if stateDict[char] == 0:#Released
					#FIXME END TIMER
					#FIXME START TIMER
					stateDict[char] = -32768
					
				else:#Pressed
					#FIXME END TIMER
					#FIXME START TIMER
					os.system('cls')
					if char == '\n':#Enter
						end = False
					if char == "DELETE":#DELETE
						passageTyped = passageTyped[:-1]
					elif i<=57 and i>=48:#NUMBERS
						if stateDict["SHIFT"] == 0:
							passageTyped += nameDict[i-16]
						else:passageTyped += char
					elif char == "SHIFT":#SHIFT
						pass
					elif stateDict["SHIFT"] == 0:#UPPERCASE
						passageTyped += char
					elif char == '.':
						passageTyped+='.'
					else:#lowercase
						try:
							passageTyped += nameDict[i+32]
						except KeyError:
							pass
							passageTyped += nameDict[i]
					print(passage)
					print(passageTyped)
					stateDict[char] = 0
		except KeyError:
			pass
#ADD SOMETHING WHICH PRINTS ARRAYS TO ANOTHER TXT FILE