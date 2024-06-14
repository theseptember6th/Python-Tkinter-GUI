"""
AUTHOR: KRISTAL SHRESTHA
DATE: 6/14/2024
PURPOSE: Implement a scrollbar in a Tkinter GUI
"""

from tkinter import *

# Initialize the main application window
root = Tk()
root.geometry("600x400")
root.title("KRISTAL GUI")

# Create a vertical scrollbar and pack it to the right side of the window
scrollbar = Scrollbar(root)
scrollbar.pack(fill=Y, side=RIGHT)


# Create a Listbox widget and link it to the scrollbar
# listbox_widget = Listbox(root, yscrollcommand=scrollbar.set)
# for i in range(344):
#     listbox_widget.insert(END, f"item {i}")
# listbox_widget.pack(fill='both', padx=22, pady=10)
# Configure the scrollbar to control the y-view of the Listbox widget
# scrollbar.config(command=listbox_widget.yview)

# Create a Text widget and link it to the scrollbar
text_widget = Text(root, yscrollcommand=scrollbar.set)
text_widget.pack(fill='both', expand=True)

# Configure the scrollbar to control the y-view of the Text widget
scrollbar.config(command=text_widget.yview)

# Start the main event loop
root.mainloop()
