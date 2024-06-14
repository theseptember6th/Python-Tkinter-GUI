"""
AUTHOR:KRISTAL SHRESTHA
DATE:6/14/2024
PURPOSE:OOP GUI
"""

from tkinter import *
import tkinter.messagebox

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
    
    def status(self):
        self.var=StringVar()
        self.var.set("Ready")
        self.statusbar=Label(self,textvar=self.var,relief=SUNKEN,anchor="w",padx=20,fg="red",font="Arial 10 bold")
        self.statusbar.pack(side=BOTTOM,fill=X)
    
    def click(self):
        print("button clicked")

    def createButton(self,inptext):
        Button(text=inptext,command=self.click).pack()
    


if __name__=="__main__":
    root=GUI()
    root.status()
    root.createButton("hello kristal")
    root.mainloop()