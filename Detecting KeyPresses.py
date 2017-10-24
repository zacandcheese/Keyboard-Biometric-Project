import win32api
import win32con
#-32768 is the value of a keypress according to win32api.GetAsyncKeyState(ord(char))
A = -32768;
B = -32768;
C = -32768;
D = -32768;
E = -32768;
F = -32768;
G = -32768;
H = -32768;
I = -32768;
J = -32768;
K = -32768;
L = -32768;
M = -32768;
N = -32768;
O = -32768;
P = -32768;
Q = -32768;
R = -32768;
S = -32768;
T = -32768;
U = -32768;
V = -32768;
W = -32768;
X = -32768;
Y = -32768;
Z = -32768;
SPACE = -32768;
BACKSPACE = -32768;

def setKey(char,value):
	global A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, SPACE, BACKSPACE, PERIOD
	
	if(char == 'A'):
		A = value;
	if(char == 'B'):
		B = value;
	if(char == 'C'):
		C = value;
	if(char == 'D'):
		D = value;
	if(char == 'E'):
		E = value;
	if(char == 'F'):
		F = value;
	if(char == 'G'):
		G = value;
	if(char == 'H'):
		H = value;
	if(char == 'I'):
		I = value;
	if(char == 'J'):
		J = value;
	if(char == 'K'):
		K = value;
	if(char == 'L'):
		L = value;
	if(char == 'M'):
		M = value;
	if(char == 'N'):
		N = value;
	if(char == 'O'):
		O = value;
	if(char == 'P'):
		P = value;
	if(char == 'Q'):
		Q = value;
	if(char == 'R'):
		R = value;
	if(char == 'S'):
		S = value;
	if(char == 'T'):
		T = value;
	if(char == 'U'):
		U = value;
	if(char == 'V'):
		V = value;
	if(char == 'W'):
		W = value;
	if(char == 'X'):
		X = value;
	if(char == 'Y'):
		Y = value;
	if(char == 'Z'):
		Z = value;
	if(char == ' '):
		SPACE = value;
	if(char == '\x08'):
		BACKSPACE =value;
		
def key(char,key):

	if(win32api.GetAsyncKeyState(ord(char))==key):
		if(key==-32768):
			print(char+"-On");
			setKey(char, 0)
			
		else:
			print(char+"-Off");
			setKey(char,-32768);
while(True):
	key('A',A)
	key('B',B)
	key('C',C)
	key('D',D)
	key('E',E)
	key('F',F)
	key('G',G)
	key('H',H)
	key('I',I)
	key('J',J)
	key('K',K)
	key('L',L)
	key('M',M)
	key('N',N)
	key('O',O)
	key('P',P)
	key('Q',Q)
	key('R',R)
	key('S',S)
	key('T',T)
	key('U',U)
	key('V',V)
	key('W',W)
	key('X',X)
	key('Y',Y)
	key('Z',Z)
	key(' ',SPACE)
	key('\x08',BACKSPACE)

