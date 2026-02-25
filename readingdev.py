from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext


root =Tk ()
root.title("dev")

def change1():
	text = textbox.get('1.0',END)
	with open("demofile.txt", "w") as f:
		f.write(text)

def change2():
	with open("demofile.txt","r") as f:
		content=f.read()
		textbox.insert('1.0',content)
		print(content)


 	

textbox=Text(root)
button1= Button(root, text=" Write to file", background='white', command=change1)
button2= Button(root, text=" Read from file", background='white', command=change2)




button1.grid(column=0,row=2)
button2.grid(column=0,row=1)
textbox.grid(column=0,row=0)

root.mainloop()
