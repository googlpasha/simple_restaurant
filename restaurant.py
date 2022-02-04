import csv
import tkinter as tk
from tkinter import ttk
from tkinter import *

__author__ = "7775152, Usatenko"

class Order():
    def __init__(self, id, number, dishes, payed = False):
        self.id = id
        self.number = number
        self.dishes = dishes
        self.payed = False

class Dish():
    def __init__(self, dishId, name, type, category, price):
        self.dishId = dishId
        self.name = name
        self.type = type
        self.category = category
        self.price = price

class Table():
    def __init__(self, number, people):
        self.number = number
        self.people = people

    def createOrder(self, id, dishes):
        print("Menu:")
        order = Order(id, self.number, dishes, payed = False)
        return order

def createMenu(menue_file):
    menu = []
    with open(menue_file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        header = next(csvfile)
        i = 0
        for row in spamreader:
            dish = Dish(i, row[0], row[1], row[2], row[3])
            menu.append(dish)
            i += 1
        return menu

def printMenu(menu):
    dishType = ""
    for dish in menu:
        if(dish.type != dishType):
            print("#"*10, dish.type, "#"*10)
            dishType = dish.type
        print(str(dish.dishId)+")", dish.name, "("+ dish.category +")", "-", dish.price)

def printtext(e1):
    text = e1.get() 
    print(text)   

def openNewWindow():
    # Toplevel object which will
    # be treated as a new window
    ws = tk.Toplevel()
    ws.geometry("500x500")
    ws.configure(background='#FBF8F1')
    ws.title("Menu")

    game_frame = Frame(ws)
    game_frame.pack()

    style = ttk.Style()
    style.configure('Treeview',
        background="#F7ECDE",
        foreground="#54BAB9",
        fieldbackground="#F7ECDE"

    )
    my_game = ttk.Treeview(game_frame)

    my_game['columns'] = ('Id', 'Name', 'Type', 'Category', 'Price')

    my_game.column("#0", width=0,  stretch=NO)
    my_game.column("Id",anchor=CENTER, width=80)
    my_game.column("Name",anchor=CENTER,width=150)
    my_game.column("Type",anchor=CENTER,width=80)
    my_game.column("Category",anchor=CENTER,width=80)
    my_game.column("Price",anchor=CENTER,width=80)

    my_game.heading("#0",text="",anchor=CENTER)
    my_game.heading("Id",text="Id",anchor=CENTER)
    my_game.heading("Name",text="Name",anchor=CENTER)
    my_game.heading("Type",text="Type",anchor=CENTER)
    my_game.heading("Category",text="Category",anchor=CENTER)
    my_game.heading("Price",text="Price",anchor=CENTER)


    
    menu = createMenu('food.csv') # main list of all dishes
    for dish in menu:
        my_game.insert(parent='',index='end',iid=dish.dishId,text='',
        values=(dish.dishId,dish.name,dish.type, dish.category, dish.price))


    Label(ws,
          text ="Choose id of dishes:",
          fg="#54BAB9",
          bg="#FBF8F1",
        ).pack()

    e1 = Entry(ws)
    e1.pack()
    Button(ws, text='Show', command=printtext(e1)).pack()

    my_game.pack()



# Define all dishes
#menu = createMenu('food.csv') # main list of all dishes



#TEST SECTION#

table1 = Table(1, 2)
#printMenu(menu)
order1 = table1.createOrder(0, ["soup", "pasta", "vine"])
#print(order1.id)
root = tk.Tk()
root.geometry('600x400+50+50')
root.configure(background='#F7ECDE')
greeting = tk.Label(
    text="Welcome to simple_restaurant!",
    fg="#54BAB9",
    bg="#F7ECDE",
)
main_text = tk.Label(
    text="We are happy to see you! Take a look at our Menu!",
    fg="#54BAB9",
    bg="#F7ECDE",
)
button = tk.Button(
    text="Menu",
    width=25,
    height=5,
    bg="#E9DAC1",
    fg="#54BAB9",
    command = openNewWindow
)

greeting.pack()
main_text.pack(pady = 10)
button.pack(pady = 10)
root.mainloop()

