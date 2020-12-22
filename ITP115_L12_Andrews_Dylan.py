# Dylan Andrews, dmandrew@usc.edu
# ITP 115, Fall 2020
# Lab 12

"""
Main program
    - creates a Barista
    - Barista takes orders
    - when the barista is done taking orders, make the drinks
    - Continue taking orders until user chooses to exit
"""

# from Barista.py file import the Barista class
from Barista import Barista

# define main
def main():
    name = input("Please enter your name: ")
    barista = Barista(name)
    print("\n~ Welcome to the Coffee Shop! ~\n")

    cont = True
    while cont:
        # Take 5 orders
        while barista.isAcceptingOrders():
            print("Hello, my name is " + barista.name + ", and I am your barista.")
            barista.takeOrder()
        # Make drinks
        barista.makeDrinks()

        # Ask to continue
        response = input("Would you like to continue (y/n)? ")
        while response.lower() != "y" and response.lower() != "n":
            print("*Invalid input, please try again!")
            response = input("Would you like to continue (y/n)? ")
        cont = (response.lower() == "y")

    print("Goodbye, please come again!")

# call main
main()
