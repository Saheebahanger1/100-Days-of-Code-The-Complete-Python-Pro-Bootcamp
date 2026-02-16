# ==============================
#      Turtle Race Project
# ==============================

from turtle import Turtle, Screen
import random

is_race_on = False

# Screen setup
screen = Screen()
screen.setup(width=500, height=400)

# Ask user for bet
user_bet = screen.textinput(
    title="Make Your Bet!",
    prompt="Which Turtle will win the race? Enter a Color: "
)

# Turtle properties
colors = ["red", "yellow", "green", "orange", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# Create and position turtles
for turtle_index in range(len(y_positions)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index]) 
    all_turtles.append(new_turtle)

# Start race if user placed a bet
if user_bet:
    is_race_on = True

# Race loop
while is_race_on:
    for turtle in all_turtles:
        # Move each turtle randomly
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        
        # Check if turtle crossed finish line
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            
            # Announce result
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

# Exit on click
screen.exitonclick()


# ==============================
#      Etch-A-Sketch App
# ==============================

# Create a new turtle for drawing
new_turtle = Turtle(shape= "turtle")
new_turtle.speed("fastest")

# Movement functions
def move_forward():
    """Move turtle forward"""
    new_turtle.forward(20)

def move_backward():
    """Move turtle backward"""
    new_turtle.backward(20)

def turn_clockwise():
    """Turn turtle right"""
    new_turtle.right(10)

def turn_anti_clockwise():
    """Turn turtle left"""
    new_turtle.left(10)

def clear_drawing():
    """Clear screen and reset turtle"""
    new_turtle.clear()
    new_turtle.penup()
    new_turtle.home()
    new_turtle.pendown()

# Keyboard bindings
screen.listen()
screen.onkey(key = "f" , fun = move_forward)
screen.onkey(key = "b" , fun = move_backward)
screen.onkey(key = "r" , fun = turn_clockwise)
screen.onkey(key = "l" , fun = turn_anti_clockwise)
screen.onkey(key = "space" , fun = clear_drawing)

# Exit on click
screen.exitonclick()