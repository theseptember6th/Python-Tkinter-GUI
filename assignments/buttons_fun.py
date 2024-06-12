"""
AUTHOR:KRISTAL SHRESTHA
DATE:6/12/2024
PURPOSE: LEARNING TKINTER'S BUTTON
"""



from tkinter import *


def hello():
    print("This is kristal's Tkinter")

def Name():
    print("Author name is Kristal Shrestha")

def Age():
    print("Author's age is 20")

def Help():
    print("contact shrestha@gmail.com")

root=Tk()
root.geometry("600x400")
frame1=Frame(root,borderwidth=6,bg="grey",relief=SUNKEN)
frame1.pack(side=LEFT,anchor="nw")

b1=Button(frame1,fg="red",text="Hello",command=hello)
b1.pack(side=LEFT,padx=10)
b2=Button(frame1,fg="red",text="AUTHORS NAME",command=Name)
b2.pack(side=LEFT,padx=10)
b3=Button(frame1,fg="red",text="AUTHORS AGE",command=Age)
b3.pack(side=LEFT,padx=10)
b4=Button(frame1,fg="red",text="HELP",command=Age)
b4.pack(side=LEFT,padx=10)


root.mainloop()