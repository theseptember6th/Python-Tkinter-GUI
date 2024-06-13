"""
AUTHOR:KRISTAL SHRESTHA
DATE:6/13/2024
PURPOSE:simple food review gui
"""

from tkinter import *
import tkinter.messagebox as tsmg


root=Tk()
root.geometry("600x400")
root.minsize(600,400)
root.maxsize(600,400)
root.title("KRISTAL'S GUI")
# root.config(bg="yellow")

def submit():
    print("you pressed submit button")
    value=Slider.get()
    if value >=0 and value<=4:
        tsmg.showinfo("FOOD REVIEW","Sorry for our bad services,please suggest us your changes")
    elif value >=8 and value<=10:
        tsmg.showinfo("FOOD REVIEW","Thank you for using our services")
    else:
        tsmg.showinfo("FOOD REVIEW","Thank you for using our services,we will keep on improving")

    with open("C:\\Users\\Kristal\\Desktop\\Python-Tkinter-GUI\\assignments\\Food review\\food-log.txt","a") as f:
        f.write(f"{str(value)}\n")

Label(root,text="How was your food experience?",borderwidth=5,relief=SUNKEN,justify=CENTER,font="comicsansm 20 bold").pack(padx=30,pady=40)
Slider=Scale(root,from_=0,to=10,resolution=1,length=200,tickinterval=5,orient=HORIZONTAL)
Slider.set(5)
Slider.pack()
Button(root,text="Submit",command=submit).pack()
root.mainloop()
