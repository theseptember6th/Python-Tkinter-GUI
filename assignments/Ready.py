from tkinter import *

root=Tk()
root.geometry("500x400")

label=Label(text="Ready",bg="red",fg="white",padx=10,pady=5,justify=CENTER,relief=SUNKEN,font="Times 15 bold italic")
label.pack(fill=X,side=BOTTOM,anchor="center")


root.mainloop()