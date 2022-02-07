"""
Eine Graphische Applikation um Bestellungen für ein Restaurant einzugeben und abzurufen.
"""
import csv
import tkinter as tk
from tkinter import ttk, CENTER, NO, Frame, Label, Button, Listbox, Entry

__author__ = "7775152, Usatenko, 7762091, Kanja"

class Order():
    """Die Klasse für eine Bestellung, mit den verschiedenen dingen die dort gespeichert werden."""
    def __init__(self, dishid, number, dishes):
        self.dishid = dishid
        self.number = number
        self.dishes = dishes
        self.payed = False

class Dish():
    """Klases für ein Gericht, auch nur mit den eingelesenen Variablen."""
    def __init__(self, dishid, name, dtype, category, price, customfeatures):
        self.dishid = dishid
        self.name = name
        self.dtype = dtype
        self.category = category
        self.price = price
        self.customfeatures = customfeatures

class Table():
    """Die verschiedenen Tische mit Nummer und Leuten,
     dort können dann Bestellungen aufgenommen werden."""
    def __init__(self, number, people):
        self.number = number
        self.people = people

    def createorder(self, dishid, dishes):
        """An einem Tisch können Bestellungen aufgenommen werden,
         diese werden unten weiter definiert."""
        print("Menu:")
        order = Order(dishid, self.number, dishes)
        return order

def createmenu(menue_file):
    """Das Menü mit den verschiedenen Gerichten, wird aus einer Datei eingelesen."""
    menu = []
    with open(menue_file, newline='', encoding="utf-8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        next(csvfile)
        i = 0
        for row in spamreader:
            dish = Dish(i, row[0], row[1], row[2], float(row[3].replace(',', '.')), [])
            menu.append(dish)
            i += 1
        return menu

def printmenu(menu):
    """Darstellung des Menüs das oben erstellt wurde."""
    dishtype = ""
    for dish in menu:
        if dish.dtype != dishtype:
            print("#"*10, dish.dtype, "#"*10)
            dishtype = dish.dtype
        print(str(dish.dishid)+")", dish.name, "("+ dish.category +")", "-", dish.price)


def openmenuwindow():
    """Die Hauptfunktion um vor allem die Graphischen Elemente vorzugeben
    und alles genauer zu beschreiben."""
    table = tablenumber.get()
    people = People.get()
    # save current table to all tables
    allables.append(Table(table, people))

    if (table.isnumeric()) & (people.isnumeric()):
        if (int(table) > 0) & (int(people) > 0):
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



            menu = createmenu('food.csv') # main list of all dishes
            for dish in menu:
                my_game.insert(parent='',index='end',iid=dish.dishid,text='',
                values=(dish.dishid,dish.name,dish.dtype, dish.category, dish.price))

            profit = tk.IntVar()
            def printchousendishes():
                """Anzeigen der Gerichte"""
                i = 0
                lb1.delete(0,'end')
                for dish in order:
                    lb1.insert(1, dish.name)
                    i += 1
            def adddish():
                """Diese Funktion ist für das hinzufügen eines Gerichtes
                zur Bestellung zuständig."""
                added = 0
                name = ""
                curitem = my_game.focus()
                chousendict = my_game.item(curitem).values()
                chousenid = list(chousendict)[2][0]
                for dish in menu:
                    if dish.dishid == chousenid:
                        name = dish.name
                        order.append(dish)
                        added = 1

                if added:
                    profit.set(name + " successfully added!")
                    printchousendishes()

                else:
                    profit.set("Sorry, dish with dishid " + str(chousenid) + " is not available")

            def deletedish():
                """Wenn etwas ausgewählt wurde, kann es mit dieser Funktion
                von der Bestellung entfernt werden."""
                selection = lb1.curselection()
                lb1.delete(selection[0]) # delete object from a list
                del order[-selection[0]] # delete this element from our order

            def addcustomfeature():
                """Funktion für extra Wünsche"""
                curitem = my_game.focus()
                chousendict = my_game.item(curitem).values()
                chousenid = list(chousendict)[2][0]
                added = 0
                for dish in menu:
                    if dish.dishid == chousenid:
                        dish.name = dish.name + " *"
                        dish.price += 1
                        dish.customfeatures.append(str(customfeature.get()))
                        added = 1
                if added:
                    printchousendishes()

            def makeorder():
                """Wenn die Bestellung fertig ist, kann sie hiermit
                zur allgemeinen Bestellliste hinzugefügt werden."""
                orderid = len(allorders)
                mainorder = Order(orderid, int(table), order)
                allorders.append(mainorder) # save this order
                ordersuccess.set("Thank you for your order! Now you can close this window")
        else:
            Error.set("Something went wrong!")
    else:
        Error.set("Something went wrong!")

    #Specifies looks of Buttons and Text

    Label(ws,
          text ="Choose id of dishes:",
          fg="#54BAB9",
          bg="#FBF8F1",
        ).pack()

    Button(ws, text='Add', command=adddish).pack()

    labelprofit = tk.Label(
        ws,
        textvariable=profit,
        fg="#54BAB9",
        bg="#FBF8F1",
        )
    labelprofit.pack()

    lb1 = Listbox(ws)
    lb1.pack()

    Button(ws, text='Delete', command=deletedish).pack()

    customfeature = Entry(ws)
    customfeature.pack()
    Button(ws, text='Customize', command=addcustomfeature).pack()

    Button(
        ws,
        text='Make order',
        width=15,
        height=1,
        command=makeorder,
    ).pack()

    ordersuccess = tk.IntVar()
    ordersuccess.set("")
    orderlabel = tk.Label(
        ws,
        textvariable=ordersuccess,
        fg="green",
        bg="#F7ECDE",
    )
    orderlabel.pack()


    my_game.pack()

def openorderswindow():
    """Anzeigen von der Liste aller Bestellungen und Funktionen dieser"""
    def orderdetails():
        """Zeigt die verschiedenen Bestellungen an und definiert wie das Fenster und alles darin
        auszusehen hat."""

        tk.Label(
            ws1,
            text="id: ",
            fg="#54BAB9",
            bg="#FBF8F1",
        ).pack()
        idvar = tk.IntVar()
        idvar.set("")
        idtext = tk.Label(
            ws1,
            textvariable=idvar,
            fg="#54BAB9",
            bg="#FBF8F1",
        )
        idtext.pack()

        tk.Label(
            ws1,
            text="Table: ",
            fg="#54BAB9",
            bg="#FBF8F1",
        ).pack()
        tablevar = tk.IntVar()
        tablevar.set("")
        tabletext = tk.Label(
            ws1,
            textvariable=tablevar,
            fg="#54BAB9",
            bg="#FBF8F1",
        )
        tabletext.pack()

        tk.Label(
            ws1,
            text="Dishes: ",
            fg="#54BAB9",
            bg="#FBF8F1",
        ).pack()

        disheslist = Listbox(ws1)
        disheslist.pack()

        tk.Label(
            ws1,
            text="Sum: ",
            fg="#54BAB9",
            bg="#FBF8F1",
        ).pack()
        sumvar = tk.IntVar()
        sumvar.set("")
        sumtext = tk.Label(
            ws1,
            textvariable=sumvar,
            fg="#54BAB9",
            bg="#FBF8F1",
        )
        sumtext.pack()

        # Set vars
        curitem = ordertable.focus()
        chousendict = ordertable.item(curitem).values()
        chousenid = list(chousendict)[2][0]
        idvar.set(chousenid)
        for order in allorders:
            if order.dishid == chousenid:
                tablevar.set(order.number)
                dishes = order.dishes

        disheslist.delete(0,'end')
        i = 0
        summ = 0
        for dish in dishes:
            disheslist.insert(1, dish.name)
            summ += dish.price
            i += 1

        sumvar.set(summ)






    ws1 = tk.Toplevel()
    ws1.geometry("500x600")
    ws1.configure(background='#FBF8F1')
    ws1.title("Orders")

    orderframe = Frame(ws1)
    orderframe.pack()

    style = ttk.Style()
    style.configure('Treeview',
        background="#F7ECDE",
        foreground="#54BAB9",
        fieldbackground="#F7ECDE")

    ordertable = ttk.Treeview(orderframe)
    ordertable['columns'] = ('Id', 'Table')

    ordertable.column("#0", width=0,  stretch=NO)
    ordertable.column("Id",anchor=CENTER, width=80)
    ordertable.column("Table",anchor=CENTER,width=150)

    ordertable.heading("#0",text="",anchor=CENTER)
    ordertable.heading("Id",text="Id",anchor=CENTER)
    ordertable.heading("Table",text="Table",anchor=CENTER)

    for order in allorders:
        ordertable.insert(parent='',index='end',iid=order.dishid,text='',
        values=(order.dishid,order.number))

    ordertable.pack()

    Button(
        ws1,
        text='Details',
        width=15,
        height=1,
        command=orderdetails,
    ).pack()




# Define all dishes
#menu = createmenu('food.csv') # main list of all dishes



#TEST SECTION#
# Our main lists

###############
allorders = []
allables = []
###############

root = tk.Tk()
root.geometry('600x400+50+50')
root.configure(background='#F7ECDE')
greeting = tk.Label(
    text="Welcome to simple_restaurant!",
    fg="#54BAB9",
    bg="#F7ECDE",
)
tabletext = tk.Label(
    text="Table: ",
    fg="#54BAB9",
    bg="#F7ECDE",
).pack()
tablenumber = Entry(root)
tablenumber.pack()
PEOPLETEXT = tk.Label(
    text="People: ",
    fg="#54BAB9",
    bg="#F7ECDE",
).pack()
People = Entry(root)
People.pack()
Error = tk.IntVar()
Error.set("")
labelerror = tk.Label(
        root,
        textvariable=Error,
        fg="red",
        bg="#F7ECDE",
    )
labelerror.pack()
main_text = tk.Label(
    text="We are happy to see you! Take a look at our Menu!",
    fg="#54BAB9",
    bg="#F7ECDE",
)
menubutton = tk.Button(
    text="Menu",
    width=25,
    height=5,
    bg="#E9DAC1",
    fg="#54BAB9",
    command = openmenuwindow
)
ordersbutton = tk.Button(
    text="Orders",
    width=15,
    height=1,
    bg="#E9DAC1",
    fg="#54BAB9",
    command = openorderswindow
)

greeting.pack()
main_text.pack(pady = 10)
menubutton.pack(pady = 10)
ordersbutton.pack(pady = 10)
root.mainloop()
