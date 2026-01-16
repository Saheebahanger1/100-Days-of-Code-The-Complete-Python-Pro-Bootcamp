"""
Python Day 1 Basics
Author: Mohammed Saheeb
Description:
This program demonstrates basic Python concepts such as:
- Printing to the console
- New line printing
- String concatenation
- Taking user input
- Variables
- Calculating string length
- A simple Band Name Generator project
"""


# Printing a simple message to the console
print("Hello Saheeb!")

# Output:
# Hello Saheeb!


# \n is used to move text to the next line
print("Hello Saheeb! \nHello World")

# Output:
# Hello Saheeb!
# Hello World


# Joining two strings using the + operator
print("Hello " + "Saheeb")

# Output:
# Hello Saheeb


# Asking the user to enter their name
input("What is your Name? ")

# Output (example):
# What is your Name? Saheeb


# Storing a value in a variable
Name = "Saheeb"

# Printing the value stored in the variable
print(Name)

# Output:
# Saheeb


# Assigning a string to a variable
Name = "Saheeb"

# Calculating and printing the length of the string
print(len(Name))

# Output:
# 6


# Taking name input from the user
username = input("What is your name? ")

# Calculating the length of the input
length = len(username)

# Printing the length
print(length)

# Output (example):
# What is your name? Saheeb
# 6


# Displaying welcome message
print("Welcome to the Band Name Generator.")

# Asking the user for city name
city = input("Which city did you grow up in?\n")

# Asking the user for pet name
pet = input("What is the name of a pet?\n")

# Generating and displaying the band name
print("Your band name could be: " + city + " " + pet)