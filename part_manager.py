# author stihiyahya2016@gmail.com

from tkinter import *
from tkinter import messagebox
from db import Database


db = Database('store.db')


def populate_list():
    part_list.delete(0, END)
    for row in db.fetch():
        part_list.insert(END, row)


def add_item():
    if part_text.get()=='' or customer_text.get()=='' or retailer_text.get()=='' or price_text.get()=='':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(part_text.get(), customer_text.get(), retailer_text.get(), price_text.get())
    part_list.delete(0, END)
    part_list.insert(END, (part_text.get(), customer_text.get(), retailer_text.get(), price_text.get()))
    populate_list()
    clear_text()

def select_item(event):
    try:
        global selected_item
        index = part_list.curselection()[0]
        selected_item = part_list.get(index)
        print(selected_item)

        part_entry.delete(0, END)
        part_entry.insert(END, selected_item[1])
        customer_entry.delete(0, END)
        customer_entry.insert(END, selected_item[2])
        retailer_entry.delete(0, END)
        retailer_entry.insert(END, selected_item[3])
        price_entry.delete(0, END)
        price_entry.insert(END, selected_item[4])
    except:
        pass

def update_item():
    db.update(selected_item[0], part_text.get(), customer_text.get(), retailer_text.get(), price_text.get())
    populate_list()

def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()

def clear_text():
    part_entry.delete(0, END)
    customer_entry.delete(0, END)
    retailer_entry.delete(0, END)
    price_entry.delete(0, END)

#creat window

app = Tk()
app.title('Part Manager')
app.geometry('640x350')

#author
author_text = StringVar()
author_label = Label(app, text='stihiyahya2016@gmail.com', font=('bold',8))
author_label.place(x=500, y=330)


# part
part_text = StringVar()
part_label = Label(app, text=' part name', font=('bold', 14), pady=20)
part_label.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, textvariable=part_text, font=('bold', 12))
part_entry.grid(row=0, column=1)

# customer
customer_text = StringVar()
customer_label = Label(app, text='customer name', font=('bold', 14))
customer_label.grid(row=0, column=2, sticky=W)
customer_entry = Entry(app, textvariable=customer_text, font=('bold', 12))
customer_entry.grid(row=0, column=3)

# retailer
retailer_text = StringVar()
retailer_label = Label(app, text=' retailer name', font=('bold', 14))
retailer_label.grid(row=1, column=0, sticky=W)
retailer_entry = Entry(app, textvariable=retailer_text, font=('bold', 12))
retailer_entry.grid(row=1, column=1)

# price
price_text = StringVar()
price_label = Label(app, text=' '*17+'price', font=('bold', 14))
price_label.grid(row=1, column=2, sticky=W)
price_entry = Entry(app, textvariable=price_text, font=('bold', 12))
price_entry.grid(row=1, column=3)

# part list
part_list = Listbox(app, height=6, width=50, border=5)
part_list.grid(row=3, column=0, columnspan=3, rowspan=6, ipady=30, ipadx=20)

# scrollbar
scrollbar = Scrollbar(app)
scrollbar.place(x=400, y=160)
#set scroll to listbox
part_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=part_list.yview)
#bind select
part_list.bind('<<ListboxSelect>>', select_item)
#buttons

add_btn = Button(app, text='Add Part', width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(app, text='Remove Part', width=12, command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn = Button(app, text='Update Part', width=12, command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text='Clear', width=12, command=clear_text)
clear_btn.grid(row=2, column=3)


#import image
from PIL import Image, ImageTk
import tkinter
img = ImageTk.PhotoImage(Image.open('python.png'))
panel = tkinter.Label(app, image=img).place(x=450, y=170)


# populate list
populate_list()
#start app
app.mainloop()

#pyinstaller.exe --onefile --icon=myicon.ico main.py
