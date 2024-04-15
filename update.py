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
        self.heading = Label(master, text='Update the database',font=('arial 40 bold'), fg='black')
        self.heading.place(x=400, y=0)

        # label and entry for id
        self.id_ie = Label(master, text='Enter Id', font=('arial 18 bold'))
        self.id_ie.place(x=0, y=70)

        self.id_ieb = Entry(master, font=('arial 18 bold'), width=10)
        self.id_ieb.place(x=380, y=70)

        self.btn_search= Button(master, text='Search', width=15, height=1, bg='steelblue', command=self.search)
        self.btn_search.place(x=550, y=70)

        # labels for the window
        self.name_l = Label(master, text="Enter Product Name",font=('arial 18 bold'))
        self.name_l.place(x=0, y=120)

        self.stock_l = Label(master, text="Enter Stocks",font=('arial 18 bold'))
        self.stock_l.place(x=0, y=170)

        self.cp_l = Label(master, text="Enter Cost Price",font=('arial 18 bold'))
        self.cp_l.place(x=0, y=220)

        self.sp_l = Label(master, text="Enter Selling Price",font=('arial 18 bold'))
        self.sp_l.place(x=0, y=270)

        self.totalcp_l = Label(master, text="Enter Total Cost Price",font=('arial 18 bold'))
        self.totalcp_l.place(x=0, y=320)
        
        self.totalsp_l = Label(master, text="Enter Total Selling Price",font=('arial 18 bold'))
        self.totalsp_l.place(x=0, y=370)

        self.assumed_profit_l = Label(master, text="Enter Assumed Profit",font=('arial 18 bold'))
        self.assumed_profit_l.place(x=0, y=420)

        self.vendor_l = Label(master, text="Enter Vendor Name",font=('arial 18 bold'))
        self.vendor_l.place(x=0, y=470)

        self.vendor_phone_l = Label(master, text="Enter Vendor Phone Number",font=('arial 18 bold'))
        self.vendor_phone_l.place(x=0, y=520)

        # Entries for the labels
        self.name_g = Entry(master, width=25,font=('arial 18 bold'))
        self.name_g.place(x= 380, y=120)

        self.stock_g = Entry(master, width=25,font=('arial 18 bold'))
        self.stock_g.place(x= 380, y=170)

        self.cp_g = Entry(master, width=25,font=('arial 18 bold'))
        self.cp_g.place(x= 380, y=220)

        self.sp_g = Entry(master, width=25,font=('arial 18 bold'))
        self.sp_g.place(x= 380, y=270)

        self.totalcp_g = Entry(master, width=25,font=('arial 18 bold'))
        self.totalcp_g.place(x= 380, y=320)

        self.totalsp_g = Entry(master, width=25,font=('arial 18 bold'))
        self.totalsp_g.place(x= 380, y=370)

        self.assumed_profit_g = Entry(master, width=25,font=('arial 18 bold'))
        self.assumed_profit_g.place(x= 380, y=420)

        self.vendor_g = Entry(master, width=25,font=('arial 18 bold'))
        self.vendor_g.place(x= 380, y=470)

        self.vendor_phone_g = Entry(master, width=25,font=('arial 18 bold'))
        self.vendor_phone_g.place(x= 380, y=520)
        
        # Buttons to db
        self.btn_add = Button(master, text="Update Database", width=25, height=2, bg="brown", fg="white", command=self.update)
        self.btn_add.place(x=520, y=570)


        # text box for the logs
        self.tBox = Text(master, width=60, height=18)
        self.tBox.place(x=750, y=70)
        self.tBox.insert(END, "ID has reached upto: " + str(id))
    
    def search(self):
        sql = "SELECT * FROM inventory WHERE id=?"
        result= c.execute(sql, (self.id_ieb.get(), ))
        for r in result:
            self.n1 = r[1] #name
            self.n2 = r[2] #stock
            self.n3 = r[3] #cp
            self.n4 = r[4] #sp
            self.n5 = r[5] #totalcp
            self.n6 = r[6] #totalsp 
            self.n7 = r[7] #assumed_profit
            self.n8 = r[8] #vendor 
            self.n9 = r[9] #vendor_phone 
        conn.commit()

        # insert into the entries to update
        self.name_g.delete(0, END)
        self.name_g.insert(0, str(self.n1))

        self.stock_g.delete(0, END)
        self.stock_g.insert(0, str(self.n2))

        self.cp_g.delete(0, END)
        self.cp_g.insert(0, str(self.n3))

        self.sp_g.delete(0, END)
        self.sp_g.insert(0, str(self.n4))

        self.totalcp_g.delete(0, END)
        self.totalcp_g.insert(0, str(self.n5))

        self.totalsp_g.delete(0, END)
        self.totalsp_g.insert(0, str(self.n6))

        self.assumed_profit_g.delete(0, END)
        self.assumed_profit_g.insert(0, str(self.n7))
    
        self.vendor_g.delete(0, END)
        self.vendor_g.insert(0, str(self.n8))

        self.vendor_phone_g.delete(0, END)
        self.vendor_phone_g.insert(0, str(self.n9)) 

    def update(self):
        # get all updated values
        self.u1 = self.name_g.get()
        self.u2 = self.stock_g.get()
        self.u3 = self.cp_g.get()
        self.u4 = self.sp_g.get()
        self.u5 = self.totalcp_g.get()
        self.u6 = self.totalsp_g.get()
        self.u7 = self.assumed_profit_g.get()
        self.u8 = self.vendor_g.get()
        self.u9 = self.vendor_phone_g.get()
        
        query = "UPDATE inventory SET product_name=?, stock=?, cost_price=?, selling_price=?, total_cp=?, total_sp=?, assumed_profit=?, vendor=?, vendor_phoneno=? WHERE id=?"
        c.execute(query, (self.u1, self.u2, self.u3, self.u4, self.u5, self.u6, self.u7, self.u8, self.u9, self.id_ieb.get()))
        conn.commit()
        tkinter.messagebox.showinfo('Success', 'update database successful')









root = Tk()

b = Database(root)

root.geometry('1366x768+0+0')
root.title('update the database')


root.mainloop()