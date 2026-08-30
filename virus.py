from tkinter import *
from tkinter import messagebox
groot = Tk()
groot.geometry("200x200")
def msg():
    messagebox.askyesno("Confirm, are you sure?")
button = Button(groot, text= "messagebox", command= msg)
button.place(x=40, y=80)
groot.mainloop()