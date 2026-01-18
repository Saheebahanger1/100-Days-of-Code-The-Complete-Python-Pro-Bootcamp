"""
Treasure Island Game
--------------------
A text-based adventure game where the player makes choices to find the treasure.
This program demonstrates the use of control flow, conditional statements,
user input handling, and string manipulation in Python.
"""

# Display ASCII art for game introduction
print('''
**********************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
*******************************************************************************
''')

# Welcome message and game objective
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.\n")

# Stage 1: Crossroad decision
stage_1 = input(
    "You're at a cross road. Where do you want to go?\n"
    "Type 'left' or 'right': "
).lower()

if stage_1 == "left":

    # Stage 2: Lake decision
    stage_2 = input(
        "\nYou've come to a lake. There is an island in the middle of the lake.\n"
        "Type 'wait' to wait for a boat or 'swim' to swim across: "
    ).lower()

    if stage_2 == "wait":

        # Stage 3: Door selection
        stage_3 = input(
            "\nYou arrive at the island safely. There is a house with three doors:\n"
            "One yellow, one blue, and one red.\n"
            "Which color do you choose? "
        ).lower()

        if stage_3 == "yellow":
            print("\nYou found the treasure. You win!")
        elif stage_3 == "red":
            print("\nIt is a room full of fire. Game over.")
        elif stage_3 == "blue":
            print("\nIt is a room full of snakes. Game over.")
        else:
            print("\nInvalid choice. Game over.")

    else:
        print("\nYou were attacked by an alligator. Game over.")

else:
    print("\nYou fell into a hole. Game over.")




    

                                                      # <----------Day 3 Completed----------> #
