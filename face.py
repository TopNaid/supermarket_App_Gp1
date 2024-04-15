from tkinter import *
import sqlite3
import tkinter.messagebox
import datetime

# date
date=datetime.datetime.now().date()
class application:
    def __init__(self,master):
        self.master = master

        self.left = Frame(master, width=900, height= 768, bg='steelblue')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=466, height= 768, bg='white')
        self.right.pack(side=RIGHT)

        # component
        self.heading = Label(self.left, text="Market Square", font=('arial 40 bold'), bg='steelblue', fg='white')
        self.heading.place(x=0, y=0)

        self.date_l = Label
        
root = Tk()
b = application(root)

root.geometry("1366x786+0+0")
root.mainloop()