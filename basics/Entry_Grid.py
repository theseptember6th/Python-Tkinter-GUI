"""
AUTHOR:KRISTAL SHRESTHA
DATE:
PURPOSE:
"""
from tkinter import *

def getvals():
    print(f"Username: {uservalue.get()}")
    print(f"Username: {passvalue.get()}")
root=Tk()
root.geometry("600x400")

username=Label(root,text="username")
password=Label(root,text="password")
username.grid()
password.grid(row=1)
#variable classes in tkinter
# BooleanVar,DoubleVar,IntVar,StringVar
uservalue=StringVar()
passvalue=StringVar()

userentry=Entry(root,textvariable=uservalue)
passwordentry=Entry(root,textvariable=passvalue)

userentry.grid(row=0,column=1)
passwordentry.grid(row=1,column=1)

Button(text="Submit",command=getvals).grid()

root.mainloop()