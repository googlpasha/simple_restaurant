import csv

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

# Define all dishes
menu = createMenu('food.csv') # main list of all dishes



#TEST SECTION#

table1 = Table(1, 2)
printMenu(menu)
order1 = table1.createOrder(0, ["soup", "pasta", "vine"])
print(order1.id)

