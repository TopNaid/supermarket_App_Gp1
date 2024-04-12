from tkinter import *
from store_base import look
from store_base import find_price


window = Tk()

window.configure(bg="#CDB79E")
window.geometry("550x330")
window.resizable(0, 0)

window.title("Group 1 Supermart")



def search():
    query = entry.get()  
    results = look(query)
    listbox.delete(0, END)

    for result in results:
        product, price = result
        listbox.insert(END, product)

def on_select(event):
    # Get selected line index
    index = listbox.curselection()[0]
    # Get the line's text
    selected_item = listbox.get(index)
    # Find the price of the selected item
    price = find_price(selected_item)
    # Display the price in the price box
    price_entry.delete(0, END)
    price_entry.insert(END, price)

    listbox.bind('<<ListboxSelect>>', on_select)


entry = Entry(window, width=30, bg="#fff", fg="#000",font=('arial', 11),bd=1)
entry.grid(row=0, column=0, padx= 15, pady=7, sticky="w")


button = Button(window, text="Search", command= search,width=10, height=1, bd=0, bg='lightblue', cursor='hand2',)  
button.grid(row=0, column=0, padx=53, sticky="e") 

listbox = Listbox(window,width= 60, cursor='hand2')
listbox.grid(row=1, column=0, rowspan=4, padx=16, pady=10)

world = Label(text='Price')
world.grid(row=1, column=1,rowspan=2, padx= 0, pady=45, sticky="n")
price_entry = Entry(window)
price_entry.grid(row=1, column=1, padx=5, pady=0, sticky="w")


word = Label(text='Quantity')
word.grid(row=0, column=1,rowspan=2, padx= 0, pady=25, sticky="n")
quantity_entry = Entry(window)
quantity_entry.grid(row=2, column=1, padx=5, pady=0,sticky="w")



add_button = Button(window, text="Add",width=10, height=1)
add_button.grid(row=3, column=1, padx=20, pady=0, sticky="w")

pay_button = Button(window, text="Payment", width=20, height=1)
pay_button.grid(row=6, column=0, padx=10, pady=65, sticky="s")


window.mainloop()