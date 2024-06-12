"""
AUTHOR:KRISTAL SHRESTHA
DATE:6/12/2024
PURPOSE: LEARNING TKINTER'S BUTTON
"""



from tkinter import *


def hello():
    print("This is kristal's Tkinter")

root=Tk()
root.geometry("600x400")
frame1=Frame(root,borderwidth=6,bg="grey",relief=SUNKEN)
frame1.pack(side=LEFT,anchor="nw")

b1=Button(frame1,fg="red",text="Print Now",command=hello)
b1.pack(side=LEFT,padx=10)
b2=Button(frame1,fg="red",text="Print Now")
b2.pack(side=LEFT,padx=10)
b3=Button(frame1,fg="red",text="Print Now")
b3.pack(side=LEFT,padx=10)
b4=Button(frame1,fg="red",text="Print Now")
b4.pack(side=LEFT,padx=10)
b5=Button(frame1,fg="red",text="Print Now")
b5.pack(side=LEFT,padx=10)



root.mainloop()