"""
AUTHOR: KRISTAL SHRESTHA
DATE: 6/12/2024
PURPOSE: NEWSPAPER EXERCISE
"""
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("KRISTAL's NEWSPAPER GUI")
root.geometry("800x600")

texts = []
photos = []

for i in range(0, 2):
    with open(f"C:\\Users\\Kristal\\Desktop\\Python-Tkinter-GUI\\Exercises\\Ex-1\\news_text\\{i+1}.txt", encoding='utf-8') as f:
        text = f.read()
        texts.append(text)

    image = Image.open(f"C:\\Users\\Kristal\\Desktop\\Python-Tkinter-GUI\\Exercises\\Ex-1\\news_images\\{i+1}.jpg")
    
    # Resize these images
    image = image.resize((225, 225), Image.LANCZOS)
    photos.append(ImageTk.PhotoImage(image))

f0 = Frame(root, width=400, height=70)
f0.pack()
Label(f0, text="KRISTAL NEWS", font="lucida 23 bold").pack()
Label(f0, text="JUNE 12, 2024", font="lucida 15 bold").pack()

f1 = Frame(root, width=800, height=250)
f1.pack(anchor="w", pady=10)
Label(f1, text=texts[0], padx=10, pady=10, wraplength=500, justify="left").pack(side="left")
Label(f1, image=photos[0]).pack(side="right", padx=10)

f2 = Frame(root, width=800, height=250)
f2.pack(anchor="w", pady=10)
Label(f2, text=texts[1], padx=10, pady=10, wraplength=500, justify="left").pack(side="left")
Label(f2, image=photos[1]).pack(side="right", padx=10)

root.mainloop()
