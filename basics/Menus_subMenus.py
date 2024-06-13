"""
AUTHOR:KRISTAL SHRESTHA
DATE:6/13/2024
PURPOSE:Learning menus submenus in tkinter gui
"""

from tkinter import *

root=Tk()
root.geometry("600x400")
root.title("Kristal Gui")

def myfun():
    print("you clicked file")
#Use these to create non dropdown menu
# myMenu=Menu(root)
# myMenu.add_command(label="File",command=myfun)
# myMenu.add_command(label="Exit",command=quit)

# root.config(menu=myMenu)


menu1=Menu(root)
sub_menu1=Menu(menu1,tearoff=0)
sub_menu1.add_command(label="Save",command=myfun)
sub_menu1.add_command(label="Save as",command=myfun)
sub_menu1.add_separator()
sub_menu1.add_command(label="New",command=myfun)

menu1.add_cascade(label="file",menu=sub_menu1)


sub_menu2=Menu(menu1,tearoff=0)
sub_menu2.add_command(label="cut",command=myfun)
sub_menu2.add_command(label="copy",command=myfun)
sub_menu2.add_separator()
sub_menu2.add_command(label="paste",command=myfun)

menu1.add_cascade(label="Edit",menu=sub_menu2)
root.config(menu=menu1)

root.mainloop()