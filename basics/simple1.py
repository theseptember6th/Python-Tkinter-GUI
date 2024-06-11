from tkinter import *
from PIL import Image, ImageTk

root = Tk()

# gui logic

# width x height
root.geometry("444x330")

# width, height
root.minsize(200, 100)
root.maxsize(1000, 1000)

kristalshrestha = Label(text="Kristal is a good boy")
kristalshrestha.pack()

# Load the image using Pillow

image = Image.open(r'C:\Users\Kristal\Desktop\Python-Tkinter-GUI\lords.png')
photo = ImageTk.PhotoImage(image)

label = Label(image=photo)
label.pack()


root.mainloop()
