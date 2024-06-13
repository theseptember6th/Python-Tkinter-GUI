"""
AUTHOR: KRISTAL SHRESTHA
DATE: 6/13/2024
PURPOSE: Learning messagebox in tkinter GUI
"""

from tkinter import *
import tkinter.messagebox as tmsg

# Initialize the main application window
root = Tk()
root.geometry("600x400")
root.title("Kristal's GUI")

def rate_us():
    print("Rate Us")
    user_feedback = tmsg.askquestion(title="Please Rate Us", message="Was your experience good?")
    if user_feedback == 'yes':
        response_message = "Great, please rate us on our playstore."
    else:
        response_message = "Tell us what was wrong, we will solve the issue very soon."
    tmsg.showinfo("Experience", response_message)

def study_with_kristal():
    user_choice = tmsg.askretrycancel("Study with Kristal", "Kristal will not study with you.")
    if user_choice:
        tmsg.showerror("Error", "Even if you retry, Kristal won't study with you, okay?")
    else:
        tmsg.showinfo("Good", "Good that you gave up.")

def display_help():
    print("Help menu item clicked")
    help_message = tmsg.showinfo(title="Help", message="Kristal is a good boy.")
    print(help_message)

def continue_action():
    user_choice = tmsg.askyesnocancel("Question", "Do you want to continue?")
    if user_choice == True:
        tmsg.showinfo("Continue", "You chose to continue.")
    elif user_choice == False:
        tmsg.showinfo("Exit", "You can exit using the X button on the top right.")
    else:
        return

def display_warning():
    tmsg.showwarning("Warning", "This is a warning message!")

def display_error():
    tmsg.showerror("Error", "An unexpected error occurred!")

# Create the menu bar
menu_bar = Menu(root)

# Help menu
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Help", command=display_help)
help_menu.add_command(label="Rate Us", command=rate_us)
help_menu.add_command(label="Study with Kristal", command=study_with_kristal)
help_menu.add_command(label="Continue", command=continue_action)
help_menu.add_command(label="Warning", command=display_warning)
help_menu.add_command(label="Error", command=display_error)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Configure the menu bar
root.config(menu=menu_bar)

# Run the application
root.mainloop()
