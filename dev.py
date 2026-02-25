from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
import random
root =Tk ()
root.title("aris texteditor!")

def change1():
	label1.config(text="UPDATED 1!")

def change2():
	label2.config(text="UPDATED 2!")

def change3():
	label3.config(text="UPDATED 3!")

def rand():
	number=random.randint(0,2)
	if number==0:
		label1.config(text="randomly picked")
	if number==1:
		label2.config(text="randomly picked")
	if number==2:
		label3.config(text="randomly picked")


button1= Button(root, text=" Button 1!", background='white', command=change1)
button2= Button(root, text=" Button 2!", background='white', command=change2)
button3= Button(root, text=" Button 3!", background='white', command= change3)
gandom = Button(root, text=" Random Button!", background='white',command=rand)

label1= Label(root,text="Label 1", height=5, width=30,fg="black")
label2= Label(root,text="Label 2", height=5, width=30,fg="black")
label3= Label(root,text="Label 3", height=5, width=30,fg="black")

button1.grid(column=0,row=0)
button2.grid(column=0,row=1)
button3.grid(column=0,row=2)

gandom.grid(column=1,row=3)

label1.grid(column=2,row=0)
label2.grid(column=2,row=1)
label3.grid(column=2,row=2)

root.mainloop()