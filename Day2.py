"""
Python Day 2 – Data Types, Operations & Tip Calculator
Author: Mohammed Saheeb

This single Python program demonstrates:
- String subscripting
- Core data types (String, Integer, Float, Boolean)
- Type checking and type conversion
- Mathematical operations
- Operator precedence (PEMDAS)
- Rounding numbers
- f-strings
- A complete Day-2 project: Tip Calculator
"""

# ---------------------------------------------------
# STRING SUBSCRIPTING
# ---------------------------------------------------

# Subscripting from first to last [0 to ...]
print("Hello"[0])        # Output: H

# Subscripting from last to first [-1 to ...]
print("Hello"[-5])       # Output: H


# ---------------------------------------------------
# DATA TYPES
# ---------------------------------------------------

# Integer
print(10 + 20)           # Output: 30

# Float (decimal values)
print(3.142)             # Output: 3.142

# Boolean values
print(True)              # Output: True
print(False)             # Output: False


# ---------------------------------------------------
# CHECKING DATA TYPES
# ---------------------------------------------------

print(type("Saheeb"))    # <class 'str'>
print(type(1234))        # <class 'int'>
print(type(3.14))        # <class 'float'>
print(type(True))        # <class 'bool'>


# ---------------------------------------------------
# TYPE CONVERSION
# ---------------------------------------------------

# String concatenation
print("123" + "456")     # Output: 123456

# Converting string to integer before addition
print(int("123") + int("456"))  # Output: 579


# ---------------------------------------------------
# CORRECTED INPUT + LENGTH CALCULATION
# ---------------------------------------------------

name_of_the_user = input("Enter your name: ")
length_of_name = len(name_of_the_user)
print("Number of letters in your name: " + str(length_of_name))


# ---------------------------------------------------
# MATHEMATICAL OPERATIONS
# ---------------------------------------------------

print(1 + 2)             # Addition → 3
print(2 - 1)             # Subtraction → 1
print(2 * 3)             # Multiplication → 6
print(4 / 2)             # Division (float) → 2.0
print(6 // 2)            # Division (integer) → 2
print(2 ** 2)            # Exponent → 4


# ---------------------------------------------------
# PEMDAS RULE
# Order: Parentheses, Exponents, Multiply, Divide, Add, Subtract
# Calculation happens left to right
# ---------------------------------------------------

print(3 * 3 + 3 / 3 - 3) # Output: 7


# ---------------------------------------------------
# ROUNDING NUMBERS
# ---------------------------------------------------

print(round(3.9))                # Output: 4
print(round(3.96825, 3))         # Output: 3.968


# ---------------------------------------------------
# F-STRINGS
# ---------------------------------------------------

age = input("Enter your Age: ")
print(f"I am {age} years old.")


# ---------------------------------------------------
# DAY 2 PROJECT – TIP CALCULATOR
# ---------------------------------------------------

print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? Rs: "))
tip = int(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))

# Calculate total bill including tip
total_bill_with_tip = bill * (1 + tip / 100)

# Calculate bill per person
bill_per_person = total_bill_with_tip / people

# Round the final amount to 2 decimal places
final_amount = round(bill_per_person, 2)

# Display result
print(f"Each person should pay: Rs {final_amount}")
