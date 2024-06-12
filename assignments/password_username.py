"""
AUTHOR:KRISTAL SHRESTHA
DATE:6/12/2024
PURPOSE:Simple password username setup
"""



from tkinter import *
def send():
    if policy_var.get()==1:
        print("form has been submitted")
    else:
        print("checkbox was not clicked")

root=Tk()
root.geometry("600x400")
root.minsize(600,400)
root.maxsize(600,400)

Label(root,text="WELCOME TO PERSONAL DATA FORM",fg="Red",font="comicsansms 14 bold",pady=15).grid(row=0,column=3)


username_label=Label(root,text="Username: ")
password_label=Label(root,text="Password")

username_label.grid(row=1,column=1)
password_label.grid(row=2,column=1)

username_var=StringVar()
password_var=StringVar()
policy_var=IntVar()

username_input=Entry(root,textvariable=username_var)
password_input=Entry(root,textvariable=password_var)

username_input.grid(row=1,column=2)
password_input.grid(row=2,column=2)

Policy=Checkbutton(text="I agree to all the policies",variable=policy_var)
Policy.grid(row=3,column=2)

Button(text="Submit",command=send).grid(row=4,column=2)

root.mainloop()