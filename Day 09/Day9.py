# 1. Defining a Dictionary
# Dictionaries store data in key:value pairs. 
# As of 2026, they remain the standard for mapped data in Python.

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Bug"])

# 2. Accessing and Adding Items
# Accessing via key: programming_dictionary["Bug"]
# Adding a new entry:
programming_dictionary["loop"] = "The action of doing something over and over again."

# Empty Dictionary
empty_dictionary = {}


# wipe an existing dictionary.
programming_dictionary = {}
print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

# Loop through a dictionary.
for key in programming_dictionary:
    print(key)
    print((programming_dictionary[key]))

"""
Dictionary Nesting and Indexing Module
--------------------------------------
This script demonstrates the usage of a dictionary where values are stored 
as lists. It illustrates how to perform 'chained indexing' to retrieve 
specific items from a nested data structure.
"""

# The 'country' variable is a dictionary mapping strings (Country names) 
# to lists of strings (States/Cities).
# Type Hint: dict[str, list[str]]
country = {
 "India" : ["Delhi", "Jammu & Kashmir"],
 "Austrailia" : ["Sydney", "Melbourne" ]
}
print(country["India"][1])


"""
Nested List Indexing Demonstration
----------------------------------
This script illustrates the concept of a multi-dimensional list (a list within a list).
It demonstrates how to use chained indexing to access an element inside a nested 
data structure.
"""

# nested_list is a list containing strings and another list.
# Structure: Index 0: "A", Index 1: "B", Index 2: ["C", "D"]
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])



"""
Deeply Nested Dictionary and List Indexing Demonstration
-------------------------------------------------------
This script showcases complex data structuring using dictionaries nested 
within dictionaries, which themselves contain lists. This pattern is 
highly common in modern JSON APIs.

It demonstrates how to use multiple levels of chained indexing to reach 
a deeply embedded data point.
"""

# The 'country' variable is a deeply nested data structure.
# Type Hint (2026 Standard): dict[str, dict[str, list[str]]]
country = {
    "India" : {
         "states" :["Delhi", "Jammu & Kashmir"]
    },
    "Austrailia" : {
        "states" : ["Sydney", "Melbourne"]
    }
}

print(country["Austrailia"]["states"][1])




"""
Blind Auction Module
--------------------
A command-line application that facilitates a secret bidding process.
Users enter their names and bids, and the program determines the winner
after clearing the screen to maintain privacy between entries.
"""

# ASCII Art represents the auction trophy
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)


def find_highest_bidder(bidding_dictionary):
    """
    Iterates through a dictionary of bids to identify and print the winner.

    Args:
        bidding_dictionary: A dictionary where keys are bidder names (str) 
                            and values are bid amounts (int).
    
    Returns:
        None: Prints the winner's name and bid amount to the console.
    """
    winner = ""
    highest_bid = 0
    max(bidding_dictionary)
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}.")

bids = {}
continue_bidding = True


"""
Main execution loop for the auction. Handles user input, 
screen clearing, and data storage.
"""
while continue_bidding:
    name = input("What is your name: ")

        # Note: In a production environment, wrap this in a try-except block 
        # to handle non-integer inputs.
    bid = int(input("what is your bid: "))

    bids[name] = bid

    should_continue = input("Are there any other bidders? Type 'yes' or 'no' \n").lower()
    
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":

        # Clears the terminal view by scrolling
        print ("\n" * 100)
