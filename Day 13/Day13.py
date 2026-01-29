"""
====================================================
DEBUGGING & LOGIC EXPLANATION – PYTHON DOCUMENTATION
====================================================

This script demonstrates common beginner mistakes in Python
and shows how to debug and fix them step by step.

Topics covered:
1. for-loop range issue
2. Conditional boundary errors
3. f-string formatting
4. Debugging using print statements
"""

# --------------------------------------------------
# Example 1: for-loop range issue
# --------------------------------------------------

def my_function():
    """
    This function runs a loop from 1 to 19.
    Since the range upper limit is exclusive,
    the value 20 will never be reached.
    """
    for i in range(1, 20):
        # i takes values from 1 to 19
        if i == 20:
            # This condition will NEVER be true
            print("you got it")

# Function call
my_function()


# --------------------------------------------------
# Debugged Version of Example 1
# --------------------------------------------------

def my_function():
    """
    This function fixes the issue by extending
    the range to include 20.
    """
    for i in range(1, 21):
        if i == 20:
            print("you got it")

# Function call
my_function()


# --------------------------------------------------
# Problem 1: Conditional boundary exclusion
# --------------------------------------------------

"""
Problem:
If the user enters 1994, no output is printed.
This happens because 1994 is excluded due to
the use of '<' and '>' operators.
"""

year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")


# --------------------------------------------------
# Solution to Problem 1
# --------------------------------------------------

"""
Solution:
The '=' operator is added to include 1994
in the millennial category.
"""

year = int(input("What's your year of birth?"))

if year > 1980 and year <= 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")


# --------------------------------------------------
# Problem 2: Missing f-string formatting
# --------------------------------------------------

age = int(input("How old are you?"))

if age > 18:
    """
    Problem:
    The variable 'age' is used inside a string
    without using an f-string, so it prints
    the literal text instead of the value.
    """
    print("You can drive at age {age}")


# --------------------------------------------------
# Solution to Problem 2
# --------------------------------------------------

age = int(input("How old are you?"))

if age > 18:
    """
    Solution:
    Using an f-string allows variable substitution
    inside the string.
    """
    print(f"You can drive at age {age}")


# --------------------------------------------------
# Problem 3: Debugging using print statements
# --------------------------------------------------

"""
Problem:
The variable 'words_per_page' is not updated
because '==' (comparison) is used instead of '='.
"""

words_per_page = 0
pages = int(input("Number of pages: "))

# Logical error: comparison instead of assignment
words_per_page == int(input("Number of words per page: "))

total_words = pages * words_per_page

# Debugging output
print(f"pages = {pages}")
print(f"words_per_page = {words_per_page}")
print(total_words)
print(2 * "\n")


# --------------------------------------------------
# Solution to Problem 3
# --------------------------------------------------

print("solution 3")

words_per_page = 0
pages = int(input("Number of pages: "))

# Correct assignment using +=
words_per_page += int(input("Number of words per page: "))

total_words = pages * words_per_page

# Debugging output
print(f"pages = {pages}")
print(f"words_per_page = {words_per_page}")
print(total_words)


# Use a Debugger
"""
Most IDE's such as (VS Code,Py Charm etc.),have built in tools for debugging.
"Debuggers allows us to peek into our code during 
execution and pause on chosen lines to figure out what
is the inner mechanism and where it's going wrong."
"""

