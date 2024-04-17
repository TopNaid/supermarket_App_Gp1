from tkinter import *
import sqlite3
import tkinter.messagebox
import datetime
import math

conn = sqlite3.connect("C:\\Users\\hp\\Desktop\\Supermarket_App_Gp1\\Database\\store.db")
c = conn.cursor()

# date
date = datetime.datetime.now().date()

# temporary list like session
product_list = []
product_price = []
product_quantity = []
product_id = []

def find():
    # getting the product ID and filling it with label above
    get_id = enteride.get()
    query = "SELECT * FROM inventory WHERE id =?"
    result = c.execute(query, (get_id,))
    for r in result:
        get_id = r[0]
        get_name = r[1]
        get_price = r[4]
        get_stock = r[2]
    productname.configure(text="Product Name: " + str(get_name))
    pprice.configure(text="Price: N" + str(get_price))

    # Quantity and Label
    global quantity_l, quantity_e, add_to_cart_btn
    quantity_l = Label(left, text='Enter Quantity', font=("arial 18 bold"), bg='steelblue', fg='black')
    quantity_l.place(x=20, y=370)

    quantity_e = Entry(left, width=25, font=("arial 18 bold"), bg='white')
    quantity_e.place(x=250, y=370)
    quantity_e.focus()

    # Add to cart button
    add_to_cart_btn = Button(left, width=25, text='Add To Cart', height=2, bg='orange', command=add_to_cart)
    add_to_cart_btn.place(x=395, y=420)

    # generate bill and change
    global change_l, change_e, change_btn
    change_l = Label(left, text='Given Amount', font=("arial 18 bold"), bg='steelblue', fg='black')
    change_l.place(x=20, y=550)

    change_e = Entry(left, width=25, font=("arial 18 bold"), bg='white')
    change_e.place(x=250, y=550)

    change_btn = Button(left, width=25, text='Calculate Change', height=2, bg='orange', command=change_func)
    change_btn.place(x=395, y=600)

def add_to_cart():
    # get the quantity value from the database
    quantity_value = int(quantity_e.get())
    if quantity_value > int(get_stock):
        tkinter.messagebox.showinfo("Error", "Insufficient product")
    else:
        # calculate the price
        final_price = float(quantity_value) * float(get_price)
        product_list.append(get_name)
        product_price.append(final_price)
        product_quantity.append(quantity_value)
        product_id.append(get_id)

        x_index = 0
        y_index = 100
        counter = 0
        for p in product_list:
            tempname = Label(right, text=str(product_list[counter]), font=('arial 18 bold'), bg='white', fg='black')
            tempname.place(x=20, y=y_index)

            tempqty = Label(right, text=str(product_quantity[counter]), font=('arial 18 bold'), bg='white', fg='black')
            tempqty.place(x=310, y=y_index)

            tempprice = Label(right, text=str(product_price[counter]), font=('arial 18 bold'), bg='white', fg='black')
            tempprice.place(x=470, y=y_index)

            y_index += 40
            counter += 1

            # total configure
            total_l.configure(text="Total: N" + str(sum(product_price)))

def change_func():
    # creating change function
    amount_given = float(change_e.get())
    our_total = float(sum(product_price))

    to_give = amount_given - our_total

    # Label for change
    c_amount = Label(left, text='Change: N' + str(to_give), font=("arial 18 bold"), bg='steelblue', fg='red')
    c_amount.place(x=20, y=650)

root = Tk()

left = Frame(root, width=900, height=768, bg='steelblue')
left.pack(side=LEFT)

right = Frame(root, width=700, height=768, bg='white')
right.pack(side=RIGHT)

# App name and date
heading = Label(left, text="Market Square", font=('arial 40 bold'), bg='steelblue', fg='white')
heading.place(x=15, y=0)

date_l = Label(right, text="Today's Date: " + str(date), font=('arial 12 bold'), bg='white', fg='steelblue')
date_l.place(x=10, y=0)

# Invoice Table
tproduct = Label(right, text="Products", font=('arial 18 bold'), bg='white', fg='black')
tproduct.place(x=10, y=60)

tquantity = Label(right, text="Quantity", font=('arial 18 bold'), bg='white', fg='black')
tquantity.place(x=300, y=60)

tamount = Label(right, text="Amount", font=('arial 18 bold'), bg='white', fg='black')
tamount.place(x=470, y=60)

# Creating product Id label and box....
enterid = Label(left, text="Enter Product's ID", font=('arial 18 bold'), fg='black', bg='steelblue')
enterid.place(x=20, y=80)

enteride = Entry(left, width=25, font=('arial 18 bold'), bg='white')
enteride.place(x=300, y=80)
enteride.focus()

#  search Button
search_btn = Button(left, width=25, text='Search', height=2, bg='orange', command=find)
search_btn.place(x=445, y=120)

# items to appear once the search button is click
productname = Label(left, text="", font=('arial 25 bold'), bg='steelblue', fg='white')
productname.place(x=20, y=250)

pprice = Label(left, text="", font=('arial 25 bold'), bg='steelblue', fg='white')
pprice.place(x=20, y=290)

# Total Label
total_l = Label(right, text='', font=('arial 30 bold'), bg='white', fg='black')
total_l.place(x=10, y=600)

root.geometry("1500x800+0+0")
root.mainloop()
