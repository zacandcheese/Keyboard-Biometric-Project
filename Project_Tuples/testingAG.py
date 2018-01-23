from tkinter import *

def onclick():
   pass
   
def keydown(e):
	if(e.keycode == 13):
		text.destroy()

	
root = Tk()
text = Text(root)
text.insert(INSERT, "")
text.bind("<KeyPress>", keydown)
text.pack()

frame = Frame(root, width=100, height=100)
frame.pack()
frame.focus_set()


root.mainloop()