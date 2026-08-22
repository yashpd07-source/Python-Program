from tkinter import *
from datetime import date
root = Tk()
root.title('Getting started with widgets')
root.geometry('500x500')
lb1 = Label(text="Hey there!", fg = "white", bg="#072F5F", height = 1, width = 300)
name_lb1 = Label(text = "Full Name", bg="#3895D3")
name_entry = Entry()
def display():
    name = name_entry.get()
    global Message
    Message = "Welcome to the application! \nToday's Date is: "
    greet = "Hello "+name+"\n"
    text_box.insert(END, greet)
    text_box.insert(END, Message)
    text_box.insert(END, date.today())
text_box = Text(height=3)
btn = Button(text="Begin", command=display, height=1, bg="#1261A0", fg='white')
lb1.pack()
name_lb1.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()