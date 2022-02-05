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
    def __init__(self, dishId, name, type, category, price, customFeatures):
        self.dishId = dishId
        self.name = name
        self.type = type
        self.category = category
        self.price = price
        self.customFeatures = customFeatures

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
            dish = Dish(i, row[0], row[1], row[2], float(row[3].replace(',', '.')), [])
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
 

def openNewWindow():
    table = tableNumber.get()
    people = People.get()
    if((table.isnumeric()) & (people.isnumeric())):
        if ((int(table) > 0) & (int(people) > 0)):
            # Toplevel object which will
            # be treated as a new window
            order = [] # list of all dishes which customer chooses
            ws = tk.Toplevel()
            ws.geometry("500x600")
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

            profit = tk.IntVar()
            def printChousenDishes():
                i = 0
                Lb1.delete(0,'end')
                for dish in order:
                    Lb1.insert(1, dish.name)
                    i += 1
            def addDish():
                added = 0
                name = ""
                curItem = my_game.focus()
                chousenDict = my_game.item(curItem).values()
                chousenId = list(chousenDict)[2][0]
                for dish in menu:
                    if(dish.dishId == chousenId):
                        name = dish.name
                        order.append(dish)
                        added = 1
                        
                if(added):
                    profit.set(name + " successfully added!")
                    printChousenDishes()
                    
                else:
                    profit.set("Sorry, dish with id " + str(chousenId) + " is not available")
            
            def deleteDish():
                selection = Lb1.curselection()
                Lb1.delete(selection[0]) # delete object from a list
                del order[-selection[0]] # delete this element from our order

            def addCustomFeature():
                curItem = my_game.focus()
                chousenDict = my_game.item(curItem).values()
                chousenId = list(chousenDict)[2][0]
                added = 0
                for dish in menu:
                    if(dish.dishId == chousenId):
                        dish.name = dish.name + " *"
                        dish.price += 1
                        dish.customFeatures.append(str(customFeature.get()))
                        added = 1
                if added:
                    printChousenDishes()
            
            # def makeOrder():
            #     mainOrder = Order()
        else:
            Error.set("Something went wrong!")
    else:
        Error.set("Something went wrong!")



    Label(ws,
          text ="Choose id of dishes:",
          fg="#54BAB9",
          bg="#FBF8F1",
        ).pack()

    Button(ws, text='Add', command=addDish).pack()

    labelProfit = tk.Label(
        ws,
        textvariable=profit,
        fg="#54BAB9",
        bg="#FBF8F1",
        )
    labelProfit.pack()

    Lb1 = Listbox(ws)
    Lb1.pack()

    Button(ws, text='Delete', command=deleteDish).pack()

    CustomFeatureText = tk.Label(
        ws,
        text="Custom feature: ",
        fg="#54BAB9",
        bg="#FBF8F1",
        ).pack()

    customFeature = Entry(ws)
    customFeature.pack()
    Button(ws, text='Customize', command=addCustomFeature).pack()

    #Button(ws, text='Make order', command=makeOrder).pack()


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
tableText = tk.Label(
    text="Table: ",
    fg="#54BAB9",
    bg="#F7ECDE",
).pack()
tableNumber = Entry(root)
tableNumber.pack()
peopleText = tk.Label(
    text="People: ",
    fg="#54BAB9",
    bg="#F7ECDE",
).pack()
People = Entry(root)
People.pack()
Error = tk.IntVar()
Error.set("")
labelError = tk.Label(
        root,
        textvariable=Error,
        fg="red",
        bg="#F7ECDE",
    )
labelError.pack()
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

