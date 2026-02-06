"""
Day 16 – Beginner to Intermediate
Understanding Python Classes, Objects, Attributes, and OOP Projects

This script demonstrates:
1. Using built-in and external Python classes
2. Working with object attributes and methods
3. Creating tables using PrettyTable
4. Implementing an Object-Oriented Coffee Machine project

Author: Mohammad Saheb
Course: 100 Days of Code – The Complete Python Pro Bootcamp
"""

# --------------------------------------------------
# SECTION 1: Turtle Graphics (Working with Classes)
# --------------------------------------------------

from turtle import Turtle, Screen

# Creating a Turtle object
jimmy = Turtle()
print(jimmy)

# Modifying object attributes
jimmy.shape("turtle")
jimmy.color("green")
jimmy.forward(100)

# Creating a Screen object
my_screen = Screen()

# Accessing object attributes
print(my_screen.canvheight)
print(my_screen.canvwidth)

# Exit on mouse click
my_screen.exitonclick()


# --------------------------------------------------
# SECTION 2: PrettyTable (Using External Packages)
# --------------------------------------------------

from prettytable import PrettyTable

# Creating a table object
table = PrettyTable()

# Adding columns to the table
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# Aligning table text to the left
table.align = "l"

# Printing the table
print(table)


# --------------------------------------------------
# SECTION 3: Coffee Machine Project (OOP)
# --------------------------------------------------

"""
This project uses Object-Oriented Programming concepts.
Each responsibility is handled by a separate class:
- Menu: Handles drink options
- CoffeeMaker: Manages resources
- MoneyMachine: Handles payments
"""

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Coffee Machine ASCII Logo
logo = """
                             ______________________
                            (___________           |
                              [XXXXX]   |          |
                         __  /~~~~~~~\\  |          |
       CT               /  \\|@@@@@@@@@\\ |          |
         )              \\   |@@@@@@@@@@||          |
        (                   \\@@@@@@@@@@||  ______  |
       __)__                 \\@@@@@@@@/ | |on|off| |
    C\\|     \\               __\\@@@@@@/__|  ~~~~~~  |
      \\     /              (____________|__________|
       \\___/               |_______________________|
"""

print(logo)

# Creating objects from classes
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# Main program loop
is_on = True

while is_on:
    # Display available options
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")

    if choice == "off":
        # Turn off the machine
        is_on = False

    elif choice == "report":
        # Print resource and money reports
        coffee_maker.report()
        money_machine.report()

    else:
        # Process drink order
        drink = menu.find_drink(choice)

        if drink:
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
                print(logo)