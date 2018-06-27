"""
Created on Mon Jun 25 19:36:09 2018
A program that stores this book inforamtion:
Titlem, Author, Year, ISBN
"""

import tkinter
from backend import Database

database = Database("books.db")

def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    e1.delete(0,'end')    #to view the title, author, year, isbn in the entries
    e1.insert('end',selected_tuple[1])    
    e2.delete(0,'end')
    e2.insert('end',selected_tuple[2])
    e3.delete(0,'end')
    e3.insert('end',selected_tuple[3])
    e4.delete(0,'end')
    e4.insert('end',selected_tuple[4])
    

def view_command():
    list1.delete(0,'end')  #empty the Listbox
    for row in database.view():
        list1.insert('end', row)


def search_command():
    list1.delete(0,'end')
    for row in database.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert('end', row)


def add_command():
    database.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,'end')
    list1.insert('end',(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))


def delete_command():
    database.delete(selected_tuple[0])


def update_command():
    database.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    

window = tkinter.Tk()

window.wm_title("BookStore")

l1 = tkinter.Label(window, text='Title')
l1.grid(row=0, column=0)

l2 = tkinter.Label(window, text='Author')
l2.grid(row=0, column=2)
 
l3 = tkinter.Label(window, text='Year')
l3.grid(row=1, column=0)

l4 = tkinter.Label(window, text='ISBN')
l4.grid(row=1, column=2)

title_text = tkinter.StringVar()
e1 = tkinter.Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = tkinter.StringVar()
e2 = tkinter.Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = tkinter.StringVar()
e3 = tkinter.Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = tkinter.StringVar()
e4 = tkinter.Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

list1 = tkinter.Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = tkinter.Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = tkinter.Button(window, text='View all', width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = tkinter.Button(window, text='Search entry', width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = tkinter.Button(window, text='Add entry', width=12, command=add_command)
b3.grid(row=4, column=3)

b4 = tkinter.Button(window, text='Update selected', width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = tkinter.Button(window, text='Delete selected', width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = tkinter.Button(window, text='Close', width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
