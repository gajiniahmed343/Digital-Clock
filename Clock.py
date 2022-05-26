from tkinter import *
from tkinter.ttk import *

from time import strftime

root=Tk()
root.title("Clock")


def time():
    string=strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000,time)


label = Label(root,font=("ds-digital",100),background="black",foreground="blue")
label.pack(padx=15,pady=15,anchor="center")
time()

mainloop()
