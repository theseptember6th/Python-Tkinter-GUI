"""
AUTHOR: KRISTAL SHRESTHA
DATE: 6/13/2024
PURPOSE: Learning sliders using Scale()
"""

from tkinter import *
import tkinter.messagebox as tsmg

root = Tk()
root.title("Kristal GUI")
root.geometry("600x400")

def credit_dollars():
    amount = dollar_slider.get()
    print(f"We have credited {amount} dollars to your bank account")
    tsmg.showinfo("Kristal Bank", f"We have credited {amount} dollars to your bank account")

# Horizontal slider
Label(root, text="How many dollars do you want?").pack()
dollar_slider = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=50, length=300, resolution=10)
dollar_slider.set(34)
dollar_slider.pack()

Button(root, text="Get dollars!", pady=10, command=credit_dollars).pack()

root.mainloop()
