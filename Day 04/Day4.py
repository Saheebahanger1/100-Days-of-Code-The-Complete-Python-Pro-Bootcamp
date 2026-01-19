"""
Rock Paper Scissors Game
------------------------
This is a simple command-line implementation of the classic
Rock, Paper, Scissors game.

The player selects one option, the computer randomly selects
another option, and the winner is decided based on the rules
of the game.

Concepts used:
- Lists
- User input
- Random module
- Conditional statements
"""

import random


# ASCII art representations of the game choices
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Store all choices in a list
choices = [rock, paper, scissors]

# Get player's choice
player_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors:\n")
)

# Display player's choice
print("\nYou chose:")
print(choices[player_choice])

# Generate computer's choice
computer_choice = random.randint(0, 2)

# Display computer's choice
print("Computer chose:")
print(choices[computer_choice])

# Determine the result of the game
if player_choice == computer_choice:
    print("This is a tie.")
elif player_choice == 0 and computer_choice == 2:
    print("You win.")
elif player_choice == 2 and computer_choice == 1:
    print("You win.")
elif player_choice == 1 and computer_choice == 0:
    print("You win.")
else:
    print("You lose.")