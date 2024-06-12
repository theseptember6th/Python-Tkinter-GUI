from tkinter import *

# Initialize the main window
root = Tk()
root.geometry("400x300")  # Set the size of the window

# Create the first frame with internal padding (inside widget)
f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN, padx=10, pady=10)
f1.pack(side=LEFT, fill="y", anchor="nw")

# Create the second frame with external padding (outside widget)
f2 = Frame(root, bg="purple", borderwidth=6, relief=SUNKEN)
f2.pack(side=TOP, fill="x", pady=20, padx=20)

# Add a label to the first frame with internal padding
l1 = Label(f1, text="Label 1", bg="red", padx=10, pady=10)
l1.pack(pady=20, padx=20)

# Add a label to the second frame with external padding
l2 = Label(f2, text="Label 2", bg="orange",font="Helvetica 16 bold",fg="red")
l2.pack(pady=20, padx=20)

# Start the Tkinter event loop
root.mainloop()
