"""
AUTHOR:KRISTAL SHRESTHA
DATE:6/14/2024
PURPOSE:Status bar 
"""

from tkinter import *
import time

root=Tk()
root.geometry("600x400")
root.title("KRISTAL GUI")

def upload():
    status_bar_var.set("busy")
    status_bar_widget.update()
    #import time
    time.sleep(2)
    status_bar_var.set("ready now")


status_bar_var=StringVar()
status_bar_var.set("Ready")
status_bar_widget=Label(root,textvariable=status_bar_var,relief=SUNKEN,anchor="w",padx=10)
status_bar_widget.pack(side=BOTTOM,fill=X)
Button(root,text="Upload",command=upload).pack()
root.mainloop()