"""
Author: Zachary Nowak 
Date:10/31/2017

Program Description: This program finds the "port"
used to connect a key to the computer.
"""
import win32api

while True:
	for i in range(0,256):#0-256 is the range of all ports
		if(win32api.GetAsyncKeyState(i) != 0):
			print(i, chr(i))