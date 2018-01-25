__version__ = '1.0'
__author__ = 'Zachary Nowak'
"""STANDARD LIBRARY IMPORTS"""
from tkinter import *
import time

"""THIRD PARTY LIBRARY IMPORTS"""

"""LOCAL LIBRARY IMPORTS"""

"""LOCAL LIBRARY VARIABLES"""
word = open("textGoldenBird.txt","r")
passage = word.readlines()


pressTimeLine = []
pressCharTimeLine = []
releaseTimeLine = []
releaseCharTimeLine = []

i = 0
name = input("What is your name: ")
def start_recording():
	#METHODS TO DEAL WITH KEYBOARD EVENTS
	def keydown(e):
		global i
		pressTimeLine.append(time.time())
		if(e.char == '\x08'):#Fixes Backspace
			pressCharTimeLine.append("@")
		elif(e.char == '\r'):#Fixes Backspace
			pressCharTimeLine.append("\n")
		elif(e.char == '\b'):#Fixes Backspace
			pressCharTimeLine.append("@")
		elif(e.char == '\r'):
			None
		else:
			pressCharTimeLine.append(e.char)
	
		if(e.keycode == 13):
			if(i == len(passage)-1):
				text.destroy()

			else:
				text.delete('1.0', END)
				i += 2
				text.insert(INSERT, passage[i].lower())

	def keyrelease(e):
		releaseTimeLine.append(time.time())
		if(e.char == '\x08'):#Fixes Backspace
			releaseCharTimeLine.append("@")
		if(e.char == '\r'):#Fixes Backspace
			releaseCharTimeLine.append("\n")
		else:
			releaseCharTimeLine.append(e.char)
		
	#INIT	
	
	
	
	#SETTING UP THE GUIs
	"""IT LOOPS THIS
	{"""
	
	root = Tk()
	text = Text(root)
	text.config(font=("Times", 20))
	text.insert(INSERT, passage[i])
	text.bind("<KeyPress>", keydown)
	text.bind("<KeyRelease>",keyrelease)
	text.pack()
	
	frame = Frame(root, width=100, height=100)
	frame.pack()
	frame.focus_set()
	
	"""}"""

	root.mainloop()

	return(pressTimeLine,pressCharTimeLine,releaseTimeLine,releaseCharTimeLine, name)