"""
AUTHOR:KRISTAL SHRESTHA
DATE:6/12/2024
PURPOSE:LEARNING CANVAS WIDGET
"""
from tkinter import *

canvas_width=600
canvas_height=400

root=Tk()
root.title("Kristal GUI")
root.geometry(f"{canvas_width}x{canvas_height}")
canvas_widget=Canvas(root,width=canvas_width,height=canvas_height)
canvas_widget.pack()

#The line goes from the point x1,y1 to x2,y2
canvas_widget.create_line(0,400,600,0,fill="red") #same concept as computer graphics
canvas_widget.create_line(0,0,600,400,fill="blue")


#for rectangle specify parameters in the order - coordinates of topleft and coordinates of topright

canvas_widget.create_rectangle(10,10,550,350,fill="yellow")


canvas_widget.create_text(300,200,text="KRISTAL'S GUI")


canvas_widget.create_oval(0,0,600,400)
canvas_widget.create_oval(0,0,300,300)


root.mainloop()
