import win32api
import os
#[port, char]
nameDict = dict([(65, 'A'),(66, 'B'),(67, 'C'),(68, 'D'), (69, 'E'), (70, 'F'),(71,'G'), (72,'H'),(73,'I'),(74,'J'),(75,'K'),(76, 'L'),(77, 'M'),
(78,'N'),(79,'O'),(80,'P'),(81,'Q'),(82,'R'),(83,'S'),(84,'T'),(85,'U'),(86,'V'),(87,'W'),(88,'X'),(89,'Y'),(90,'Z'),
(97, 'a'), (98, 'b'),(99,'c'),(100,'d'),(101,'e'),(102,'f'),(103,'g'),(104,'h'),(105,'i'),(106,'j'),(107,'k'),(108,'l'),(109,'m'),
(110,'n'),(111,'q'),(112,'r'),(113,'s'),(114,'t'),(115,'u'),(116,'v'),(117,'w'),(118,'x'),(119,'y'),(120,'z'),
(32, ' '), (190,'.'), (13, '\n'),(8, "DELETE"),(16,"SHIFT"),
(48, '0'),(49, '1'),(50,'2'),(51,'3'),(52,'4'),(53,'5'),(54,'6'),(55,'7'),(56,'8'),(57,'9'),(80,')'),(81,'!')])

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