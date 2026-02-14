"""
Turtle Graphics Practice Program 🐢🎨

This script contains multiple Turtle Graphics challenges implemented step by step.
Each section demonstrates a different concept such as loops, functions, randomization,
RGB colors, and geometric patterns using Python's turtle module.

Author: Mohammed Saheeb
"""

# --------------------------------------------------
# BASIC SETUP
# --------------------------------------------------
from turtle import Turtle, Screen
import random

# Create turtle object
luffy = Turtle()
luffy.shape("turtle")
luffy.speed("fastest")


# --------------------------------------------------
# Challenge 1: Draw a Square
# --------------------------------------------------
# Draws a square using a for loop
for _ in range(4):
    luffy.forward(100)
    luffy.right(90)


# --------------------------------------------------
# Challenge 2: Draw a Dashed Line
# --------------------------------------------------
# Creates a dashed line by alternating pen up and pen down
for _ in range(50):
    luffy.pendown()
    luffy.forward(10)
    luffy.penup()
    luffy.forward(10)


# --------------------------------------------------
# Challenge 3: Drawing Different Shapes
# --------------------------------------------------
# Import random module (used for colors)
import random

# List of colors
colours = ["red", "blue", "green", "purple", "orange", "black", "pink", "brown"]

def draw_shapes(num_sides):
    """
    Draws a regular polygon with the given number of sides.
    """
    luffy.pensize(3)
    angle = 360 / num_sides
    for _ in range(num_sides):
        luffy.forward(100)
        luffy.right(angle)

# Draw shapes from triangle (3 sides) to decagon (10 sides)
for shape_side_n in range(3, 11):
    luffy.color(random.choice(colours))
    draw_shapes(shape_side_n)


# --------------------------------------------------
# Challenge 4: Draw a Random Walk
# --------------------------------------------------
# Random walk using fixed directions and random colors
import random

colours = ["red", "blue", "green", "purple", "orange", "black", "pink", "brown"]
directions = [0, 90, 180, 270]
luffy.pensize(5)

for _ in range(300):
    luffy.color(random.choice(colours))
    luffy.forward(50)
    luffy.setheading(random.choice(directions))


# --------------------------------------------------
# Generate Random RGB Colors (Random Walk)
# --------------------------------------------------
# Re-import turtle module as luffy
import turtle as luffy
import random

# Set turtle speed and color mode
luffy.speed("fastest")
luffy.colormode(255)

def random_color():
    """
    Generates and returns a random RGB color tuple.
    """
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

directions = [0, 90, 180, 270]
luffy.pensize(5)

for _ in range(200):
    luffy.color(random_color())
    luffy.forward(30)
    luffy.setheading(random.choice(directions))


# --------------------------------------------------
# Challenge 5: Draw a Spirograph
# --------------------------------------------------
import turtle as luffy

# Enable RGB color mode
luffy.colormode(255)

def random_color():
    """
    Generates and returns a random RGB color tuple.
    """
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

# Draw an initial circle
luffy.circle(100)

def draw_spirograph(size_of_gap):
    """
    Draws a spirograph using circles rotated by a fixed gap angle.
    """
    for _ in range(int(360 / size_of_gap)):
        luffy.color(random_color())
        luffy.speed("fastest")
        current_heading = luffy.heading()
        luffy.setheading(current_heading + size_of_gap)
        luffy.circle(100)

# Call spirograph function
draw_spirograph(5)


# --------------------------------------------------
# Exit on Click
# --------------------------------------------------
screen = Screen()
screen.exitonclick()
