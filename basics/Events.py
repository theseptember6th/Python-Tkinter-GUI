"""
AUTHOR:KRISTAL SHRESTHA
DATE:6/12/2024
PURPOSE:LEARNING EVENTS TKINTER
"""

from tkinter import *

def kristal(event):
    print(f"You clicked on the button at {event.x},{event.y}")
root=Tk()
root.geometry("600x400")
root.title("KRISTAL GUI")

widget=Button(root,text="Click me Please")
widget.pack()

widget.bind('<Button-1>',kristal)
widget.bind('<Double-1>',quit)
root.mainloop()