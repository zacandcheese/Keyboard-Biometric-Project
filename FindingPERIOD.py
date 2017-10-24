import win32api
import win32con
while True:
	for i in range(0,257):
		if(win32api.GetAsyncKeyState(i) != 0):
			print(i, chr(i))