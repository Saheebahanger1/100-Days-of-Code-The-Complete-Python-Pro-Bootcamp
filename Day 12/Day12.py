"""
Demonstration: Local Scope in Python
-----------------------------------
A variable created inside a function has LOCAL scope.
It is accessible only within that function.
"""

def drink_potion():
    """
    Creates and prints a local variable.

    The variable `potion_strength` exists only
    inside this function and cannot be accessed
    from outside.
    """
    potion_strength = 2  # Local variable
    print(potion_strength)


# Function call
drink_potion()



"""
Demonstration: Global Scope in Python
------------------------------------
A variable declared outside all functions has GLOBAL scope.
It can be accessed from anywhere in the program, including
inside functions (read-only by default).
"""

# Global variable
player_health = 10


def drink_potion():
    """
    Prints the player's health.

    This function accesses a global variable without modifying it.
    Reading a global variable inside a function is allowed in Python.
    """
    print(player_health)


# Function call
drink_potion()



"""
Demonstration: There is NO Block Scope in Python
------------------------------------------------
Python does not have block-level scope for variables created inside
conditionals (if/for/while). Variables created inside these blocks
are accessible outside the block, as long as they are within the same
function or global scope.
"""

# Global variable
game_level = 10

# Global list
enemies = ["Alien", "Zombie", "Skeleton"]


def create_enemy():
    """
    Creates an enemy based on the current game level.

    This function demonstrates that variables declared inside
    an 'if' block are still accessible outside the block
    because Python does NOT have block scope.
    """

    # Variable declared in function scope
    new_enemy = ""

    # Conditional block (NOT a new scope in Python)
    if game_level < 5:
        new_enemy = enemies[0]

    # Accessible outside the 'if' block
    print(new_enemy)


# Function call
create_enemy()



"""
Number Guessing Game
--------------------
This program is a console-based number guessing game where the user
tries to guess a randomly generated number between 1 and 100.

The player chooses a difficulty level:
- Easy: 10 attempts
- Hard: 5 attempts

The program gives feedback after each guess and ends when the
user guesses correctly or runs out of attempts.
"""

from random import randint

# ASCII art logo displayed at the start of the game
logo = """
 _______           _______  _______  _______   _________          _______    _                 _______  ______   _______  _______ 
(  ____ \\|\\     /|(  ____ \\(  ____ \\(  ____ \\  \\__   __/|\\     /|(  ____ \\  ( (    /||\\     /|(       )(  ___ \\ (  ____ \\(  ____ )
| (    \\/| )   ( || (    \\/| (    \\/| (    \\/     ) (   | )   ( || (    \\/  |  \\  ( || )   ( || () () || (   ) )| (    \\/| (    )|
| |      | |   | || (__    | (_____ | (_____      | |   | (___) || (__      |   \\ | || |   | || || || || (__/ / | (__    | (____)|
| | ____ | |   | ||  __)   (_____  )(_____  )     | |   |  ___  ||  __)     | (\\ \\) || |   | || |(_)| ||  __ (  |  __)   |     __)
| | \\_  )| |   | || (            ) |      ) |     | |   | (   ) || (        | | \\   || |   | || |   | || (  \\ \\ | (      | (\\ (   
| (___) || (___) || (____/\\/\\____) |/\\____) |     | |   | )   ( || (____/\\  | )  \\  || (___) || )   ( || )___) )| (____/\\| ) \\ \\__
(_______)(_______)(_______/\\_______)\\_______)     )_(   |/     \\|(_______/  |/    )_)(_______)|/     \\||/ \\___/ (_______/|/   \\__/  
"""

# Constants defining number of attempts for each difficulty level
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(user_guess, actual_answer, turns):
    """
    Compares the user's guess with the actual answer.

    Parameters:
        user_guess (int): The number guessed by the user
        actual_answer (int): The randomly generated number
        turns (int): Remaining number of attempts

    Returns:
        int: Updated number of turns remaining
    """
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}.")
        return turns


def set_difficulty():
    """
    Asks the user to choose a difficulty level.

    Returns:
        int: Number of attempts allowed based on difficulty
    """
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    """
    Runs the main game loop.
    Handles number generation, user input, feedback,
    and win/loss conditions.
    """
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate random number
    answer = randint(1, 100)

    # Set difficulty
    turns = set_difficulty()

    guess = None

    # Game loop
    while guess != answer:
        print(f"\nYou have {turns} attempts remaining to guess the number.")

        # User input
        guess = int(input("Make a guess: "))

        # Check guess and update turns
        turns = check_answer(guess, answer, turns)

        # Check for loss condition
        if turns == 0:
            print("You've run out of guesses. You lose!")
            return
        elif guess != answer:
            print("Guess again.")


# Start the game
game()
