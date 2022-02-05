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
 

def openMenuWindow():
    table = tableNumber.get()
    people = People.get()
    # save current table to all tables
    allTables.append(Table(table, people))

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
            
            def makeOrder():
                orderId = len(allOrders)
                mainOrder = Order(orderId, int(table), order)
                allOrders.append(mainOrder) # save this order
                OrderSuccess.set("Thank you for your order! Now you can close this window")
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

    Button(
        ws,
        text='Make order',
        width=15,
        height=1,
        command=makeOrder,
    ).pack()

    OrderSuccess = tk.IntVar()
    OrderSuccess.set("")
    OrderLabel = tk.Label(
        ws,
        textvariable=OrderSuccess,
        fg="green",
        bg="#F7ECDE",
    )
    OrderLabel.pack()


    my_game.pack()

def openOrdersWindow():
    def orderDetails():

        tk.Label(
            ws1,
            text="id: ",
            fg="#54BAB9",
            bg="#FBF8F1",
        ).pack()
        idVar = tk.IntVar()
        idVar.set("")
        idText = tk.Label(
            ws1,
            textvariable=idVar,
            fg="#54BAB9",
            bg="#FBF8F1",
        )
        idText.pack()

        tk.Label(
            ws1,
            text="Table: ",
            fg="#54BAB9",
            bg="#FBF8F1",
        ).pack()
        tableVar = tk.IntVar()
        tableVar.set("")
        tableText = tk.Label(
            ws1,
            textvariable=tableVar,
            fg="#54BAB9",
            bg="#FBF8F1",
        )
        tableText.pack()

        tk.Label(
            ws1,
            text="Dishes: ",
            fg="#54BAB9",
            bg="#FBF8F1",
        ).pack()

        DishesList = Listbox(ws1)
        DishesList.pack()

        tk.Label(
            ws1,
            text="Sum: ",
            fg="#54BAB9",
            bg="#FBF8F1",
        ).pack()
        SumVar = tk.IntVar()
        SumVar.set("")
        SumText = tk.Label(
            ws1,
            textvariable=SumVar,
            fg="#54BAB9",
            bg="#FBF8F1",
        )
        SumText.pack()

        # Set vars
        curItem = orderTable.focus()
        chousenDict = orderTable.item(curItem).values()
        chousenId = list(chousenDict)[2][0]
        idVar.set(chousenId)
        for order in allOrders:
            if order.id == chousenId:
                tableVar.set(order.number)
                dishes = order.dishes

        DishesList.delete(0,'end')
        i = 0
        summ = 0
        for dish in dishes:
            DishesList.insert(1, dish.name)
            summ += dish.price
            i += 1

        SumVar.set(summ)



        

    
    ws1 = tk.Toplevel()
    ws1.geometry("500x600")
    ws1.configure(background='#FBF8F1')
    ws1.title("Orders")

    orderFrame = Frame(ws1)
    orderFrame.pack()

    style = ttk.Style()
    style.configure('Treeview',
        background="#F7ECDE",
        foreground="#54BAB9",
        fieldbackground="#F7ECDE")

    orderTable = ttk.Treeview(orderFrame)
    orderTable['columns'] = ('Id', 'Table')

    orderTable.column("#0", width=0,  stretch=NO)
    orderTable.column("Id",anchor=CENTER, width=80)
    orderTable.column("Table",anchor=CENTER,width=150)

    orderTable.heading("#0",text="",anchor=CENTER)
    orderTable.heading("Id",text="Id",anchor=CENTER)
    orderTable.heading("Table",text="Table",anchor=CENTER)

    for order in allOrders:
        orderTable.insert(parent='',index='end',iid=order.id,text='',
        values=(order.id,order.number))
    
    orderTable.pack()

    Button(
        ws1,
        text='Details',
        width=15,
        height=1,
        command=orderDetails,
    ).pack()
    



# Define all dishes
#menu = createMenu('food.csv') # main list of all dishes



#TEST SECTION#
# Our main lists

###############
allOrders = []
allTables = []
###############

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
MenuButton = tk.Button(
    text="Menu",
    width=25,
    height=5,
    bg="#E9DAC1",
    fg="#54BAB9",
    command = openMenuWindow
)
OrdersButton = tk.Button(
    text="Orders",
    width=15,
    height=1,
    bg="#E9DAC1",
    fg="#54BAB9",
    command = openOrdersWindow
)

greeting.pack()
main_text.pack(pady = 10)
MenuButton.pack(pady = 10)
OrdersButton.pack(pady = 10)
root.mainloop()

