

from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
root =Tk ()
root.title("aris texteditor!")

text_area = scrolledtext.ScrolledText(root,
                                      wrap = WORD, 
                                      width = 40, 
                                      height = 10, 
                                      font = ("Times New Roman",
                                              15))

label= Label(root,text="aris text editor", height=5, width=30,fg="pink")

#buttons
plus= Button(root, text="+", background='white')
save= Button(root, text="save", background='white')
pen= Button(root, text=" pen", background='white')
mail= Button(root, text="mail", background='white')
erase= Button(root, text="erase", background='white')
#textbox



text_area.grid(row=3, column=0,columnspan=6)
plus.grid(row=2,column=1)
save.grid(row=2,column=5)
pen.grid(row=2,column=2)
mail.grid(row=2,column=4)
erase.grid(row=2,column=3)
label.grid(row=0,column=0, columnspan=6)


root.mainloop()







