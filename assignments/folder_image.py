import os
from tkinter import *
from PIL import Image, ImageTk

# Function to load and display images
def display_images(folder_path):
    # Get a list of image files in the specified folder
    image_files = os.listdir(folder_path)

    # Loop through the image files and display them
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)

        label = Label(root, image=photo)
        label.image = photo  # Keep a reference to avoid garbage collection
        label.pack()

# Initialize the main Tkinter window
root = Tk()
root.geometry("800x600")  # Set the window size

# Specify the folder containing images
folder_path = r'C:\Users\Kristal\Desktop\Python-Tkinter-GUI\images'

# Display images from the specified folder
display_images(folder_path)

# Start the Tkinter main event loop
root.mainloop()
