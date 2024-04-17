from tkinter import *
import sqlite3
import tkinter.messagebox
import datetime
import math

conn = sqlite3.connect("C:\\Users\\hp\\Desktop\\Supermarket_App_Gp1\\Database\\store.db")
c = conn.cursor()

# date
date=datetime.datetime.now().date()

#temporary list like session
product_list= []
product_price= []
product_quantity= []
product_id= []
class application:
    def __init__(self,master):
        self.master = master

        self.left = Frame(master, width=900, height= 768, bg='steelblue')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=700, height= 768, bg='white')
        self.right.pack(side=RIGHT)

        # App name and date
        self.heading = Label(self.left, text="Market Square", font=('arial 40 bold'), bg='steelblue', fg='white')
        self.heading.place(x=15, y=0)

        self.date_l = Label(self.right, text="Today's Date: " + str(date), font=('arial 12 bold'), bg='white', fg='steelblue')
        self.date_l.place(x=10, y=0)

        # Invoice Table
        self.tproduct = Label(self.right, text="Products", font=('arial 18 bold'), bg='white',fg='black' )
        self.tproduct.place(x=10, y=60)
        
        self.tquantity = Label(self.right, text="Quantity", font=('arial 18 bold'), bg='white',fg='black' )
        self.tquantity.place(x=300, y=60)

        self.tamount = Label(self.right, text="Amount", font=('arial 18 bold'), bg='white',fg='black' )
        self.tamount.place(x=470, y=60)

        # Creating product Id label and box....
        self.enterid = Label(self.left, text="Enter Product's ID",font=('arial 18 bold'), fg='black', bg='steelblue')
        self.enterid.place(x=20, y=80)

        self.enteride = Entry(self.left, width=25,font=('arial 18 bold'), bg='white')
        self.enteride.place(x=300, y=80)
        self.enteride.focus() #we use focus to set our curse at a particular place. with this our cursor will be blinking inside the id box


        #  search Button
        self.search_btn= Button(self.left, width=25, text= 'Search', height=2, bg='orange', command=self.find)
        self.search_btn.place(x=445, y=120)
        
        # items to appear once the search button is click
        self.productname=Label(self.left, text="", font=('arial 25 bold'), bg='steelblue', fg='white')
        self.productname.place(x=20, y=250)

        self.pprice=Label(self.left, text="", font=('arial 25 bold'), bg='steelblue', fg='white')
        self.pprice.place(x=20, y=290)

        # Total Label
        self.total_l = Label(self.right, text='', font=('arial 30 bold'), bg='white', fg='black')
        self.total_l.place(x=10, y=600)

    def find(self):
        # getting the product ID and filling it with label above 
        self.get_id = self.enteride.get()
        query = "SELECT * FROM inventory WHERE id =?"
        result= c.execute(query,(self.get_id, )) 
        for self.r in result:
            self.get_id= self.r[0]
            self.get_name= self.r[1]
            self.get_price= self.r[4]
            self.get_stock= self.r[2]
        self.productname.configure(text="Product Name: " + str(self.get_name))
        self.pprice.configure(text="Price: N" + str(self.get_price))

        # Quantity and Label

        self.quantity_l= Label(self.left, text='Enter Quantity', font=("arial 18 bold"), bg='steelblue', fg='black')
        self.quantity_l.place(x=20, y=370)

        self.quantity_e= Entry(self.left,width=25, font=("arial 18 bold"), bg='white')
        self.quantity_e.place(x=250, y=370)
        self.quantity_e.focus() 

        # Add to cart button

        self.add_to_cart_btn= Button(self.left, width=25, text= 'Add To Cart', height=2, bg='orange', command=self.add_to_cart)
        self.add_to_cart_btn.place(x=395, y=420)
        
        # generate bill and change button

        self.change_l= Label(self.left, text='Given Amount', font=("arial 18 bold"), bg='steelblue', fg='black')
        self.change_l.place(x=20, y=550)

        self.change_e= Entry(self.left,width=25, font=("arial 18 bold"), bg='white')
        self.change_e.place(x=250, y=550)

        self.change_btn= Button(self.left, width=25, text= 'Calculate Change', height=2, bg='orange', command=self.change_func)
        self.change_btn.place(x=395, y=600)

        # generate bill button 

        self.bill_btn= Button(self.left, width=80, text= 'Generate Bill', height=2, bg='brown', command=self.generate_bill)
        self.bill_btn.place(x=120, y=700)

    def add_to_cart(self):
        # get the quantity value from the database
        self.quantity_value=int(self.quantity_e.get())
        if self.quantity_value > int(self.get_stock):
            tkinter.messagebox.showinfo("Error","Insurficient product")
        else:
            # calculate the price
            self.final_price=float(self.quantity_value) * float(self.get_price)
            product_list.append(self.get_name)
            product_price.append(self.final_price)
            product_quantity.append(self.quantity_value)
            product_id.append(self.get_id)

            self.x_index =0
            self.y_index = 100
            self.counter = 0
            for self.p in product_list:
                self.tempname = Label(self.right, text=str(product_list[self.counter]), font=('arial 18 bold'), bg='white', fg='black')
                self.tempname.place(x=20, y=self.y_index)

                self.tempqty = Label(self.right, text=str(product_quantity[self.counter]), font=('arial 18 bold'), bg='white', fg='black')
                self.tempqty.place(x=310, y=self.y_index)

                self.tempprice = Label(self.right, text=str(product_price[self.counter]), font=('arial 18 bold'), bg='white', fg='black')
                self.tempprice.place(x=470, y=self.y_index)

                self.y_index += 40
                self.counter += 1

                #total configure
                self.total_l.configure(text="Total: N" + str(sum(product_price)))

    def change_func(self):
        # creating change function
        self.amount_given= float(self.change_e.get())
        self.our_total = float(sum(product_price))

        self.to_give = self.amount_given - self.our_total

        # Label for change
        self.c_amount= Label(self.left, text='Change: N' + str(self.to_give), font=("arial 18 bold"), bg='steelblue', fg='yellow')
        self.c_amount.place(x=20, y=650)

    def generate_bill(self):
        self.x=0
        # Decrease the stock from the db
        initial = "SELECT * FROM inventory WHERE id=?"
        result = c.execute(initial, (product_id[self.x],))
       
        for i in product_list:
            for r in result:
                self.old_stock= r[2]
            self.new_stock=int(self.old_stock) - product_quantity[self.x]

            sql= "UPDATE inventory SET stock=? WHERE id=?"
            c.execute(sql, (self.new_stock, product_id[self.x]))
            conn.commit()
            print('decrease')
            self.x += 1
            


root = Tk()
b = application(root)

root.geometry("1500x800+0+0")
root.mainloop()