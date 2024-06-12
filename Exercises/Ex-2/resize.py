"""
AUTHOR:KRISTAL SHRESTHA
DATE:6/12/2024
PURPOSE:Windows Resizer GUI
"""

from tkinter import *

def changeGeometry():
    height = height_var.get()
    width = width_var.get()
    root.geometry(f"{width}x{height}")

height = 400
width = 600
root = Tk()
root.geometry(f"{width}x{height}")
root.title("KRISTAL'S RESIZER GUI")

Label(root, text="Width:").grid(row=0, column=0)
Label(root, text="Height:").grid(row=1, column=0)

height_var = IntVar()
width_var = IntVar()

width_input = Entry(root, textvariable=width_var)
height_input = Entry(root, textvariable=height_var)

width_input.grid(row=0, column=1)
height_input.grid(row=1, column=1)

Button(root, text="Apply", command=changeGeometry).grid(row=2, column=0, columnspan=2)

root.mainloop()
