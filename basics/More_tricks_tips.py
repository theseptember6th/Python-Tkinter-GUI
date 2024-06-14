"""
AUTHOR:KRISTAL SHRESTHA
DATE:6/14/2024
PURPOSE:more tricks and tips on tkinter gui
"""

from tkinter import *
root=Tk()
root.geometry("600x400")
root.title("Kristal GUI")
root.wm_iconbitmap(r"C:\Users\Kristal\Desktop\Python-Tkinter-GUI\basics\notes.ico")
root.configure(background="grey")
width=root.winfo_screenwidth()
height=root.winfo_screenheight()
print(f"{width}X{height}")
Button(text="Close",command=root.destroy).pack()
root.mainloop()