"""
AUTHOR: KRISTAL SHRESTHA
DATE: 6/14/2024
PURPOSE: Learning RadioButtons
"""

from tkinter import *
import tkinter.messagebox as tmsg

# Initialize the main application window
root = Tk()
root.geometry("600x400")
root.title("KRISTAL'S GUI")

# Function to handle the order button click
def place_order():
    tmsg.showinfo("Order", f"You have ordered {selected_item.get()}.\nThank you for ordering!")

# Create a StringVar to store the selected value of the RadioButtons
selected_item = StringVar()
selected_item.set("Momo")  # Set default value

# Create and pack the label asking the user what they would like to have
Label(root, text="What would you like to have sir?", font="lucida 19 bold", justify=LEFT, padx=14).pack()

# Create and pack the RadioButtons for each menu item
Radiobutton(root, text="Momo", padx=14, variable=selected_item, value="Momo").pack(anchor="w")
Radiobutton(root, text="Chowmein", padx=14, variable=selected_item, value="Chowmein").pack(anchor="w")
Radiobutton(root, text="Pizza", padx=14, variable=selected_item, value="Pizza").pack(anchor="w")
Radiobutton(root, text="Roast", padx=14, variable=selected_item, value="Roast").pack(anchor="w")

# Create and pack the order button
Button(root, text="Order now", pady=10, command=place_order).pack()

# Run the main event loop
root.mainloop()
