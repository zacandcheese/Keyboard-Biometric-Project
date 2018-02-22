__version__ = '1.0'
__author__ = 'Zachary Nowak'
"""STANDARD LIBRARY IMPORTS"""
import platform
if(platform.system() == "Darwin"):
   from Tkinter import *
if(platform.system() == "Windows"):
   from tkinter import *
   
import time


"""THIRD PARTY LIBRARY IMPORTS"""

"""LOCAL LIBRARY IMPORTS"""

"""LOCAL LIBRARY VARIABLES"""



pressTimeLine = []
pressCharTimeLine = []
releaseTimeLine = []
releaseCharTimeLine = []
i = 0


def start_recording(passage):
	#METHODS TO DEAL WITH KEYBOARD EVENTS
	def keydown(e):
		global i
		pressTimeLine.append(time.time())
		if(e.char == '\x08' or e.keycode == 3342463):#Fixes Backspace
			pressCharTimeLine.append("@")
		elif(e.char == '\r' or e.keycode == 2359309):#Fixes Enter
			pressCharTimeLine.append("\n")
		elif(e.char == '\b'):#Fixes Backspace
			pressCharTimeLine.append("@")
		else:
			pressCharTimeLine.append(e.char)
      
	
		if(e.keycode == 13 or e.keycode == 2359309):
			if(i == len(passage)-1):
				text.destroy()

			else:
				text.delete('1.0', END)
				i += 1 #MAKES IT EVERY OTHER WITH TWO
				if(passage[i]=='\n'):
					i+=1
				text.insert(INSERT, (passage[i].lower()+".\n"))

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
	text.insert(INSERT, passage[i].lower()+".\n")
	text.bind("<KeyPress>", keydown)
	text.bind("<KeyRelease>",keyrelease)
	text.pack()
	
	frame = Frame(root, width=100, height=100)
	frame.pack()
	frame.focus_set()
	
	"""}"""

	root.mainloop()

	return(pressTimeLine,pressCharTimeLine,releaseTimeLine,releaseCharTimeLine)