"""
AUTHOR:KRISTAL SHRESTHA
DATE:6/12/2024
PURPOSE:Accepting user input in tkinter form
"""

from tkinter import *

def getvals():
    print("Submitting Form")

    print(f"{name_var.get()} {phone_var.get()} {gender_var.get()} {contact_var.get()} {payment_var.get()}")


    with open(r'C:\Users\Kristal\Desktop\Python-Tkinter-GUI\basics\log.txt','a') as f:
        f.write(f"{name_var.get()} ,{phone_var.get()} ,{gender_var.get()} {contact_var.get()} ,{payment_var.get()}\n")
  

root=Tk()
root.geometry("600x400")
root.title("Kristal Travels")

'''Tkinter does not support using multiple geometry managers on the same parent widget because they have conflicting layout instructions.
you should choose one geometry manager (either pack() or grid()) and use it consistently throughout your application'''

#heading
Label(root,text="WELCOME TO KRISTAL TRAVELS",font="comicsansms 13 bold",pady=15).grid(row=0,column=3)


#text for our form
name=Label(root,text="Name")
phone=Label(root,text="Phone")
gender=Label(root,text="Gender")
contact=Label(root,text="Emergency Contact")
payment=Label(root,text="Payment MOde")

#packed text using grid
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
contact.grid(row=4,column=2)
payment.grid(row=5,column=2)

#tkinter variable for storing values
name_var=StringVar()
phone_var=IntVar()
gender_var=StringVar()
contact_var=StringVar()
payment_var=StringVar()
foodservice_var=IntVar()

#entry for our form
name_entry=Entry(root,textvariable=name_var)
phone_entry=Entry(root,textvariable=phone_var)
gender_entry=Entry(root,textvariable=gender_var)
payment_entry=Entry(root,textvariable=contact_var)
foodservices_entry=Entry(root,textvariable=foodservice_var)

#packing the entries
name_entry.grid(row=1,column=3)
phone_entry.grid(row=2,column=3)
gender_entry.grid(row=3,column=3)
payment_entry.grid(row=4,column=3)
foodservices_entry.grid(row=5,column=3)

#checkbox & packing it
foodservice=Checkbutton(text="Want to book your meals?",variable=foodservice_var)
foodservice.grid(row=6,column=3)

#button and packing it and assigning it a command

Button(text="Submit to Kristal Travels",command=getvals).grid(row=7,column=3)



root.mainloop()