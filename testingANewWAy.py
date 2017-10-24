import win32api
import os
#[port, char]
nameDict = dict([(65, 'A'),(97, 'a'), (66, 'B'),(98, 'b'), (32, ' '), (190,'.'), (13, '\n'),(8, "DELETE"),(16,"SHIFT"),
(48, '0'),(80,')'),(49, '1'),(81,'!')])
#[char, state]
stateDict = dict([('A',-32768),('B',-32768),(' ', -32768),('.', -32768), ('\n', -32768),('0', -32768),("DELETE", -32768),("SHIFT",-32768),('a',-32768),('b', -32768),
('1',-32768),('!',-32768),(')',-32768)])
passageTyped = ""
while True:
	for i in range(0,257):
		try:
			if(win32api.GetAsyncKeyState(i) == stateDict[nameDict[i]]):
				char = nameDict[i]
				if char == "SHIFT":
					pass
					#Uppercase
				
				if stateDict[char] == 0:#Released
					stateDict[char] = -32768
				else:#Pressed
					os.system('cls')
					if char == "DELETE":#DELETE
						passageTyped = passageTyped[:-1]
					elif i<=57 and i>=48:#NUMBERS
						if stateDict["SHIFT"] == 0:
							passageTyped += nameDict[i+32]
						else:passageTyped += char
					elif char == "SHIFT":#SHIFT
						pass
					elif stateDict["SHIFT"] == 0:#UPPERCASE
						passageTyped += char
					else:#lowercase
						try:
							passageTyped += nameDict[i+32]
						except KeyError:
							passageTyped += nameDict[i]
							
					print(passageTyped)
					stateDict[char] = 0
		except KeyError:
			pass