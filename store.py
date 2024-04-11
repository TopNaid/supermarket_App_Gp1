from tkinter import *
from store_base import look
from store_base import find_price


window = Tk()

window.geometry("550x330")
window.resizable(0, 0)

window.title("Group 1 Supermart")



# def search():
#     query = entry.get()  
#     results = look(query)
#     # Clear the Listbox
#     listbox.delete(0, END)

#     # Insert each result into the Listbox
#     for result in results:
#         listbox.insert(END, result)
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
entry.grid(row=0, column=0, padx= 11, pady=7)


button = Button(window, text="Search", command= search,width=10, height=1, bd=0, bg='lightblue', cursor='hand2',)  
button.grid(row=0, column=1, padx=10) 

listbox = Listbox(window,width= 60, cursor='hand2')
listbox.grid(row=1, column=0, columnspan=2, padx=16, pady=10)

price_entry = Entry(window)
price_entry.grid(row=1, column=3, padx=5, pady=0)

quantity_entry = Entry(window)
quantity_entry.grid(row=2, column=3, padx=5, pady=0)

add_button = Button(window, text="Add")
add_button.grid(row=3, column=3, padx=5, pady=0)


window.mainloop()