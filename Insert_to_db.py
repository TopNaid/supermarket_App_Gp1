from tkinter import *
import sqlite3
import tkinter.messagebox

conn = sqlite3.connect("C:\\Users\\hp\\Desktop\\Supermarket_App_Gp1\\Database\\store.db")
c = conn.cursor()

result= c.execute("SELECT max(id) from inventory")
for r in result:
    id = r[0]
class Database:
    def __init__(self,master):
        self.master = master
        self.heading = Label(master, text='Add to the database',font=('arial 40 bold'), fg='steelblue')
        self.heading.place(x=400, y=0)

        self.name_l = Label(master, text="Enter Product Name",font=('arial 18 bold'))
        self.name_l.place(x=10, y=70)

        self.stock_l = Label(master, text="Enter Stocks",font=('arial 18 bold'))
        self.stock_l.place(x=10, y=120)

        self.cp_l = Label(master, text="Enter Cost Price",font=('arial 18 bold'))
        self.cp_l.place(x=10, y=170)

        self.sp_l = Label(master, text="Enter Selling Price",font=('arial 18 bold'))
        self.sp_l.place(x=10, y=220)

        self.vendor_l = Label(master, text="Enter Vendor Name",font=('arial 18 bold'))
        self.vendor_l.place(x=10, y=270)

        self.vendor_phone_l = Label(master, text="Enter Vendor Phone Number",font=('arial 18 bold'))
        self.vendor_phone_l.place(x=10, y=320)

        self.id_l = Label(master, text="Enter ID",font=('arial 18 bold'))
        self.id_l.place(x=10, y=370)
        # Entries for the labels

        self.name_g = Entry(master, width=25,font=('arial 18 bold'))
        self.name_g.place(x= 380, y=70)

        self.stock_g = Entry(master, width=25,font=('arial 18 bold'))
        self.stock_g.place(x= 380, y=120)

        self.cp_g = Entry(master, width=25,font=('arial 18 bold'))
        self.cp_g.place(x= 380, y=170)

        self.sp_g = Entry(master, width=25,font=('arial 18 bold'))
        self.sp_g.place(x= 380, y=220)

        self.vendor_g = Entry(master, width=25,font=('arial 18 bold'))
        self.vendor_g.place(x= 380, y=270)

        self.vendor_phone_g = Entry(master, width=25,font=('arial 18 bold'))
        self.vendor_phone_g.place(x= 380, y=320)

        self.id_g = Entry(master, width=25,font=('arial 18 bold'))
        self.id_g.place(x= 380, y=370)
        # Buttons to db
        self.btn_add = Button(master, text="Add to Database", width=25, height=2, bg="brown", fg="white", command=self.get_items)
        self.btn_add.place(x=520, y=420)

        self.btn_clear = Button(master, text="Clear all fileds", width=20, height=2, bg='gray', fg='white', command=self.clear_all)
        self.btn_clear.place(x=350, y=420)


        # text box for the logs
        self.tBox = Text(master, width=60, height=18)
        self.tBox.place(x=750, y=70)
        self.tBox.insert(END, "ID has reached upto: " + str(id))

        # self.master.bind('<Return>',self.get_items())
        # self.master.bind('<Up>',self.clear_all())

    def get_items(self):
        # get from entries
        self.name = self.name_g.get()
        self.stock = self.stock_g.get()
        self.cp = self.cp_g.get()
        self.sp = self.sp_g.get()
        self.vendor = self.vendor_g.get()
        self.vendor_phone = self.vendor_phone_g.get()

        # Entries cals
        self.totalcp = float(self.cp) * float(self.stock) 
        self.totalsp = float(self.sp) * float(self.stock) 
        self.assumed_profit = float(self.totalsp-self.totalcp)
        if self.name == '' or self.stock == '' or self.cp == '' or self.sp == '' or self.vendor == '' or self.vendor_phone == '': 
             tkinter.messagebox.showinfo('Error', "Please fill all the entries")
        else:
            sql = "INSERT INTO inventory(product_name,stock,cost_price,selling_price,total_cp,total_sp,assumed_profit,vendor,vendor_phoneno) VALUES(?,?,?,?,?,?,?,?,?)"
            c.execute(sql,(self.name, self.stock, self.cp, self.sp, self.totalcp, self.totalsp, self.assumed_profit, self.vendor, self.vendor_phone))
            conn.commit()

            # textbox.insert
            self.tBox.insert(END, '\n\nInserted ' + str(self.name) + " into the database with code " + str(self.id_g.get()))
            tkinter.messagebox.showinfo("Success", "successfully added to the database")
        
    def clear_all(self, *args, **kwargs):
        self.name_g.delete(0, END)
        self.stock_g.delete(0, END)
        self.cp_g.delete(0, END)
        self.sp_g.delete(0, END)
        self.vendor_g.delete(0, END)
        self.vendor_phone_g.delete(0, END)
        self.id_g.delete(0, END)


        
root = Tk()

b = Database(root)

root.geometry('1366x768+0+0')
root.title('Add to the database')


root.mainloop()