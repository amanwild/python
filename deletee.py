from tkinter import *
from tkinter import ttk


project = Tk()

f1=Frame(project,bg ="red",relief= SUNKEN)
f1.pack(fill= "both")

project.title("Object Detection")
project.geometry("800x600")
project.minsize(400,300)

label = Label(f1,text="This GUI is created by Aman Sahu",font="comicsansms 15 bold",bg = "black",fg = "white" )
label.pack(side = TOP , fill = "both", padx=2, pady= 2)




project.mainloop()
