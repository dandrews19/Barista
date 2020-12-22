# Dylan Andrews, dmandrew@usc.edu
# ITP 115, Fall 2020
# Lab 12

from Coffee import Coffee

# create a class to simulate a barista
class Barista():

    MAX_ORDERS = 5

    # creates name and orders
    def __init__(self, nameParam):
        self.name = nameParam
        self.orders = []

    # gets order from user input and adds it to list
    def takeOrder(self):
        drinkInput = input("What drink do you want?")
        sizeInput = input("What size would you like?")
        nameInput = input("What is your name?")
        coffeeObject = Coffee(sizeInput, drinkInput, nameInput)
        self.orders.append(coffeeObject)
        print(coffeeObject)
        print()

    # checks if max number of orders has been reached
    def isAcceptingOrders(self):
        if len(self.orders) < Barista.MAX_ORDERS:
            return True
        else:
            return False

    # sets every drink in orders to be complete
    def makeDrinks(self):
        for order in self.orders:
            order.setCompleted()
            print("\t", order)


        self.orders = []

    # displays barista name
    def __str__(self):
        msg = "Barista: " + self.name
        return msg
