"""
Day 06 – Beginner
Functions and While Loops

This script demonstrates:
- How to define and call functions
- How while loops work
- Using conditional logic inside loops
- Practical problem-solving with loops and functions
- Logic used in Reeborg's World challenges (Hurdles & Maze)

Note:
Some functions like turn_left(), move(), at_goal(), etc.
are built-in functions provided by Reeborg's World environment.
"""

# --------------------------------------------------
# Defining and Calling a Function
# --------------------------------------------------
def my_function():
    """
    This function prints two messages.
    It demonstrates how to define and call a function in Python.
    """
    print("Hello")
    print("Bye")

# Calling the function
my_function()


# --------------------------------------------------
# While Loop Example
# Check numbers from 1 to 10 for even or odd
# --------------------------------------------------
num = 1

while num <= 10:
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")
    num += 1  # Increment to avoid infinite loop


# --------------------------------------------------
# Hurdle 4 Game – Reeborg's World
# --------------------------------------------------
"""
This section solves the Hurdle 4 challenge in Reeborg's World.
The robot jumps over hurdles using functions and while loops.
"""

def turn_right():
    """
    Turns the robot right by calling turn_left() three times.
    """
    turn_left()
    turn_left()
    turn_left()

def jump():
    """
    Makes the robot jump over a hurdle by:
    - Turning left
    - Moving until the right side is clear
    - Crossing the hurdle
    - Returning to the original direction
    """
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

# Main loop to reach the goal
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()


# --------------------------------------------------
# Final Project – Day 6
# Escaping the Maze (Reeborg's World)
# --------------------------------------------------
"""
This section solves the Maze challenge using the
right-hand rule algorithm.

The robot:
1. Turns right if possible
2. Moves forward if the front is clear
3. Turns left if blocked
"""

def turn_right():
    """
    Turns the robot right using three left turns.
    """
    turn_left()
    turn_left()
    turn_left()

# Main loop continues until the robot reaches the goal
while not at_goal():
    if right_is_clear():
        # Priority 1: Turn right if possible
        turn_right()
        move()
    elif front_is_clear():
        # Priority 2: Move forward if path is clear
        move()
    else:
        # Priority 3: Turn left if blocked
        turn_left()