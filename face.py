from tkinter import *
import sqlite3
import tkinter.messagebox
import datetime

conn = sqlite3.connect("C:\\Users\\hp\\Desktop\\Supermarket_App_Gp1\\Database\\store.db")
c = conn.cursor()

# date
date=datetime.datetime.now().date()
class application:
    def __init__(self,master):
        self.master = master

        self.left = Frame(master, width=800, height= 768, bg='steelblue')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=566, height= 768, bg='white')
        self.right.pack(side=RIGHT)

        # component
        self.heading = Label(self.left, text="Market Square", font=('arial 40 bold'), bg='steelblue', fg='white')
        self.heading.place(x=10, y=0)

        self.date_l = Label(self.right, text="Today's Date: " + str(date), font=('arial 12 bold'), bg='white', fg='steelblue')
        self.date_l.place(x=10, y=0)

        # Table invoice
        self.tproduct = Label(self.right, text="Products", font=('arial 18 bold'), bg='white',fg='black' )
        self.tproduct.place(x=10, y=60)
        
        self.tquantity = Label(self.right, text="Quantity", font=('arial 18 bold'), bg='white',fg='black' )
        self.tquantity.place(x=300, y=60)

        self.tamount = Label(self.right, text="Amount", font=('arial 18 bold'), bg='white',fg='black' )
        self.tamount.place(x=450, y=60)

        # Enter items....
        self.enterid = Label(self.left, text="Enter Product's ID",font=('arial 18 bold'), fg='white', bg='steelblue')
        self.enterid.place(x=10, y=80)

        self.enteride = Entry(self.left, width=25,font=('arial 18 bold'), bg='white')
        self.enteride.place(x=250, y=80)

        # search Button
        self.search_btn= Button(self.left, width=25, text= 'Search', height=2, bg='orange', command=self.find)
        self.search_btn.place(x=395, y=120)
        
        # items to appear once the search button is click
        self.productname=Label(self.left, text="", font=('arial 25 bold'), bg='steelblue', fg='white')
        self.productname.place(x=20, y=250)

        self.pprice=Label(self.left, text="", font=('arial 25 bold'), bg='steelblue', fg='white')
        self.pprice.place(x=20, y=290)

    def find(self):
        # getting the product ID and filling it with label above 
        self.get_id = self.enteride.get()
        query = "SELECT product_name,selling_price FROM inventory WHERE id =?"
        result= c.execute(query,(self.get_id, )) 
        for self.r in result:
            self.get_name= self.r[0]
            self.get_price= self.r[1]
        self.productname.configure(text="Product Name: " + str(self.get_name))
        self.pprice.configure(text="Price: N" + str(self.get_price))

        # qty and discount Label

        self.quantity_l= Label(self.left, text='Enter Quantity', font=("arial 18 bold"), bg='steelblue', fg='black')
        self.quantity_l.place(x=20, y=370)

        self.quantity_e= Entry(self.left,width=25, font=("arial 18 bold"), bg='white')
        self.quantity_e.place(x=225, y=370)

        # Add to cart button

        self.add_to_cart_btn= Button(self.left, width=25, text= 'Add To Cart', height=2, bg='orange', command=self.find)
        self.add_to_cart_btn.place(x=395, y=450)
        
        # generate bill and change


root = Tk()
b = application(root)

root.geometry("1366x786+0+0")
root.mainloop()