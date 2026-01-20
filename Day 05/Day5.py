"""
Day 05 – Beginner
Loops, Range Function, and Password Generator

This script demonstrates:
- For loops
- Working with lists
- Using built-in functions like sum() and max()
- Using range() in loops
- Generating passwords using random choices

Concepts covered:
- Iteration
- Accumulators
- Conditional logic
- Randomization
"""

import random

# --------------------------------------------------
# For Loop Example
# --------------------------------------------------
fruits = ["Apple", "Peach", "Mango"]
for fruit in fruits:
    print(fruit)  # Prints each fruit one by one

# --------------------------------------------------
# Sum using built-in sum() function
# --------------------------------------------------
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86]
total_exam_score = sum(student_scores)
print("Total score using sum():", total_exam_score)

# --------------------------------------------------
# Sum using a for loop
# --------------------------------------------------
total_score = 0
for score in student_scores:
    total_score += score
print("Total score using for loop:", total_score)

# --------------------------------------------------
# Find maximum score using built-in max()
# --------------------------------------------------
print("Maximum score using max():", max(student_scores))

# --------------------------------------------------
# Find maximum score using a for loop
# --------------------------------------------------
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print("Maximum score using for loop:", max_score)

# --------------------------------------------------
# For loop using range() function
# --------------------------------------------------
for num in range(1, 10):
    print(num)

# --------------------------------------------------
# Adding numbers from 1 to 100
# --------------------------------------------------
sum_numbers = 0
for num in range(1, 101):
    sum_numbers += num
print("Sum of numbers from 1 to 100:", sum_numbers)

# --------------------------------------------------
# PyPassword Generator
# --------------------------------------------------

letters = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "<", ">", "/", "?", "~", "`"]

print("\nWelcome to the PyPassword Generator!")

# User input for password requirements
req_letters = int(input("How many letters would you like in your password?\n"))
req_numbers = int(input("How many numbers would you like in your password?\n"))
req_symbols = int(input("How many symbols would you like in your password?\n"))

# --------------------------------------------------
# Easy Level Password Generator (not shuffled)
# --------------------------------------------------
password = ""

for _ in range(req_letters):
    password += random.choice(letters)

for _ in range(req_numbers):
    password += random.choice(numbers)

for _ in range(req_symbols):
    password += random.choice(symbols)

print("Easy password:", password)

# --------------------------------------------------
# Hard Level Password Generator (shuffled)
# --------------------------------------------------
password_list = []

for _ in range(req_letters):
    password_list.append(random.choice(letters))

for _ in range(req_numbers):
    password_list.append(random.choice(numbers))

for _ in range(req_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

# Convert list to string
hard_password = ""
for char in password_list:
    hard_password += char

print("Hard password:", hard_password)