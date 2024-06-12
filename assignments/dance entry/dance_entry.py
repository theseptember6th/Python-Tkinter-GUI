"""
AUTHOR:KRISTAL SHRESTHA
DATE:
PURPOSE:
"""

from tkinter import *


def entryfile():
    with open(r"C:\Users\Kristal\Desktop\Python-Tkinter-GUI\assignments\dance entry\dance-log.txt","a") as f:
        f.write(f"Username: {username_var.get()}\t")
        f.write(f"Age: {age_var.get()}\t")
        f.write(f"Mail: {mail_var.get()}\n")
    
    pass

root=Tk()
root.geometry("600x500")
root.maxsize(600,500)
root.minsize(600,500)

username_var=StringVar()
username=Label(root,text="Username:")
username.grid()
username_input=Entry(root,textvariable=username_var)
username_input.grid(row=0,column=1)

age_var=IntVar()
age=Label(root,text="Age:")
age.grid(row=1)
Age_input=Entry(root,textvariable=age_var)
Age_input.grid(row=1,column=1)

mail_var=StringVar()
mail=Label(root,text="Mail:")
mail.grid(row=2)
Mail_input=Entry(root,textvariable=mail_var)
Mail_input.grid(row=2,column=1)

Button(text="Submit",command=entryfile).grid()


root.mainloop()