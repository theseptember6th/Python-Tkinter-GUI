"""
AUTHOR: KRISTAL SHRESTHA
DATE: 6/14/2024
PURPOSE: Listbox Example with Tkinter
"""

from tkinter import *
import tkinter.messagebox as tmsg

def add_item():
    global item_count
    listbox.insert(ACTIVE, f"Item {item_count}")
    item_count += 1

# Initialize the main window
root = Tk()
root.geometry("600x400")
root.title("KRISTAL GUI")

# Initial count for list items
item_count = 1

# Configure and create the Listbox widget
listbox = Listbox(root, bg='lightgrey', fg='black', bd=2, font=("Arial", 12))
listbox.pack()
listbox.insert(END, "First item of our listbox")

# Add button to add items to the listbox
add_button = Button(root, text="Add Item", command=add_item)
add_button.pack()

# Main loop to run the GUI
root.mainloop()
