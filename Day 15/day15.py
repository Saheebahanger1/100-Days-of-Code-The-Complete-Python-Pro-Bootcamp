"""
Coffee Machine Project
----------------------
This program simulates a simple coffee machine that serves espresso,
latte, and cappuccino.

The machine:
- Maintains available resources
- Accepts coin-based payments
- Checks resource availability
- Processes transactions
- Generates reports
- Allows the machine to be turned off

Concepts used:
- Dictionaries
- Functions
- Conditional statements
- Loops
- Global variables
"""

# Coffee machine ASCII logo
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

# Menu containing drink details
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Initial profit
profit = 0

# Initial machine resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    """
    Checks if the machine has enough resources to make the drink.
    Returns True if sufficient, otherwise False.
    """
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """
    Calculates the total value of coins inserted by the user.
    Returns the total amount.
    """
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """
    Checks if the payment is sufficient.
    Returns True if payment is successful, otherwise False.
    """
    global profit
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        profit += drink_cost
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """
    Deducts ingredients from resources and serves the drink.
    """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕️. Enjoy.")
    print(logo)

# Main program loop
is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_on = False

    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    elif choice in MENU:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print("Invalid selection. Please choose again.")