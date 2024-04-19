from tkinter import *
import sqlite3
import tkinter.messagebox
import datetime

# Initialize the Tkinter window
root = Tk()

# Establish database connection
conn = sqlite3.connect("C:\\Users\\hp\\Desktop\\Supermarket_App_Gp1\\Database\\store.db")
c = conn.cursor()

# Date
date = datetime.datetime.now().date()

# Temporary lists
product_list = []
product_price = []
product_quantity = []
product_id = []

# Function to search for a product
def find(enteride, productname, pprice, quantity_e, left):
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
    quantity_l = Label(left, text='Enter Quantity', font=("arial 18 bold"), bg='steelblue', fg='black')
    quantity_l.place(x=20, y=370)
    quantity_e = Entry(left, width=25, font=("arial 18 bold"), bg='white')
    quantity_e.place(x=250, y=370)
    quantity_e.focus()

    # Add to cart button
    add_to_cart_btn = Button(left, width=25, text='Add To Cart', height=2, bg='orange', command=lambda: add_to_cart(get_name, get_price, quantity_e, right))
    add_to_cart_btn.place(x=395, y=420)

    # Generate bill and change button
    change_l = Label(left, text='Given Amount', font=("arial 18 bold"), bg='steelblue', fg='black')
    change_l.place(x=20, y=550)
    change_e = Entry(left, width=25, font=("arial 18 bold"), bg='white')
    change_e.place(x=250, y=550)
    change_btn = Button(left, width=25, text='Calculate Change', height=2, bg='orange', command=lambda: change_func(change_e))
    change_btn.place(x=395, y=600)

    # Generate bill button
    bill_btn = Button(left, width=80, text='Generate Bill', height=2, bg='brown', command=generate_bill)
    bill_btn.place(x=120, y=700)

# Function to add a product to the cart
def add_to_cart(get_name, get_price, quantity_e, right):
    quantity_value = int(quantity_e.get())
    product_list.append(get_name)
    product_price.append(get_price * quantity_value)
    product_quantity.append(quantity_value)
    # Display added product in the cart
    for i in range(len(product_list)):
        Label(right, text=str(product_list[i]), font=('arial 18 bold'), bg='white', fg='black').place(x=20, y=100 + 40 * i)
        Label(right, text=str(product_quantity[i]), font=('arial 18 bold'), bg='white', fg='black').place(x=310, y=100 + 40 * i)
        Label(right, text=str(product_price[i]), font=('arial 18 bold'), bg='white', fg='black').place(x=470, y=100 + 40 * i)
    total_l.configure(text="Total: N" + str(sum(product_price)))

# Function to calculate change
def change_func(change_e):
    amount_given = float(change_e.get())
    our_total = float(sum(product_price))
    to_give = amount_given - our_total
    c_amount = Label(left, text='Change: N' + str(to_give), font=("arial 18 bold"), bg='steelblue', fg='yellow')
    c_amount.place(x=20, y=650)

# Function to generate bill
def generate_bill():
    initial = "SELECT * FROM inventory WHERE id=?"
    for i in range(len(product_list)):
        result = c.execute(initial, (product_id[i],))
        for r in result:
            old_stock = r[2]
        new_stock = int(old_stock) - product_quantity[i]
        sql = "UPDATE inventory SET stock=? WHERE id=?"
        c.execute(sql, (new_stock, product_id[i]))
        conn.commit()

# Left Frame
left = Frame(root, width=900, height=800, bg='steelblue')
left.pack(side=LEFT)

# Right Frame
right = Frame(root, width=700, height=800, bg='white')
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
tquantity.place(x=310, y=60)
tamount = Label(right, text="Amount", font=('arial 18 bold'), bg='white', fg='black')
tamount.place(x=470, y=60)

# Creating product Id label and box
enterid = Label(left, text="Enter Product ID", font=('arial 18 bold'), fg='black', bg='steelblue')
enterid.place(x=20, y=80)
enteride = Entry(left, width=25, font=('arial 18 bold'), bg='white')
enteride.place(x=300, y=80)
enteride.focus()

# Search Button
search_btn = Button(left, width=25, text='Search', height=2, bg='#008B8B', command=lambda: find(enteride, productname, pprice, quantity_e, left))
search_btn.place(x=445, y=120)

# Items to appear once the search button is clicked
productname = Label(left, text="", font=('arial 25 bold'), bg='steelblue', fg='white')
productname.place(x=20, y=250)
pprice = Label(left, text="", font=('arial 25 bold'), bg='steelblue', fg='white')
pprice.place(x=20, y=290)

# Quantity Entry
quantity_l = Label(left, text='Enter Quantity', font=("arial 18 bold"), bg='steelblue', fg='black')
quantity_l.place(x=20, y=370)
quantity_e = Entry(left, width=25, font=("arial 18 bold"), bg='white')
quantity_e.place(x=250, y=370)

# Total Label
total_l = Label(right, text='', font=('arial 30 bold'), bg='white', fg='black')
total_l.place(x=10, y=600)

# Run the GUI
root.geometry("1500x800+0+0")
root.mainloop()
