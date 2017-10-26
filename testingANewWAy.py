import win32api
import os
#[port, char]
nameDict = dict([(65, 'A'),(97, 'a'), (66, 'B'),(98, 'b'), (32, ' '), (190,'.'), (13, '\n'),(8, "DELETE"),(16,"SHIFT"),
(48, '0'),(80,')'),(49, '1'),(81,'!')])
#[char, state]
stateDict = dict([('A',-32768),('B',-32768),('C',-32768),('D',-32768),('E',-32768),('F',-32768),('G',-32768),('H',-32768),('I',-32768),('J',-32768),
('K',-32768),('L',-32768),('M',-32768),('N',-32768),('O',-32768),('P',-32768),('Q',-32768),('R',-32768),('S',-32768),('T',-32768),('U',-32768),
('V',-32768),('W',-32768),('X',-32768),('Y',-32768),('Z',-32768)('.', -32768), ('\n', -32768),('0', -32768),("DELETE", -32768),
("SHIFT",-32768),('a',-32768),('b', -32768),('c',-32768),('d',-32768),('e',-32768),('f',-32768),('g',-32768),('h',-32768),('i',-32768),('j',-32768),
('k',-32768),('l',-32768),('m',-32768),('n',-32768),('o',-32768),('p',-32768),('q',-32768),('r',-32768),('s',-32768),('t',-32768),('u',-32768),
('v',-32768),('w',-32768),('x',-32768),('y',-32768),('z',-32768),('1',-32768),('!',-32768),(')',-32768)])
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
							pass

					print(passageTyped)
					stateDict[char] = 0
		except KeyError:
			pass
