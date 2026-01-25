# Functions with Output.
def format_name(f_name, l_name):
    """
    Print the first and last name in title case.

    This function takes a first name and last name,
    converts both to title case, and prints them
    on separate lines.

    Args:
        f_name (str): The first name.
        l_name (str): The last name.

    Returns:
        None
    """
    print(f_name.title())
    print(l_name.title())


format_name(f_name="saheeb", l_name="ahanger")


def format_name(f_name, l_name):
    """
    Format and return the full name in title case.

    This function converts the first and last names
    to title case and returns them as a single
    formatted string.

    Args:
        f_name (str): The first name.
        l_name (str): The last name.

    Returns:
        str: The formatted full name.
    """
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name(f_name="saheeb", l_name="ahanger"))


output = len("saheeb")
"""
Stores the length of the string "saheeb".

Type:
    int
"""


def function_1(text):
    """
    Duplicate the given text.

    This function concatenates the input text
    with itself and returns the result.

    Args:
        text (str): Input text.

    Returns:
        str: The duplicated text.
    """
    return text + text


def function_2(text):
    """
    Convert text to title case.

    This function capitalizes the first letter
    of each word in the provided text.

    Args:
        text (str): Input text.

    Returns:
        str: The title-cased text.
    """
    return text.title()

output = function_2(function_1(" hello"))
print(output)


def format_name(f_name, l_name):
    """
    Format a first name and last name into title case.

    This function checks whether the provided first and last names
    are valid (non-empty). If either input is an empty string,
    an error message is returned. Otherwise, both names are
    converted to title case and returned as a formatted string.

    Args:
        f_name (str): The user's first name.
        l_name (str): The user's last name.

    Returns:
        str: A formatted string containing the title-cased first
        and last name, or an error message if inputs are invalid.
    """
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()



# The calculator project.
"""
Regular Calculator Program

This module implements a simple command-line calculator that performs
basic arithmetic operations: addition, subtraction, multiplication,
and division. The calculator supports continuous calculations and
allows restarting the calculation at any time.

The program displays an ASCII-art calculator logo and interacts with
the user through standard input/output.
"""

logo = """ 
           _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   

            _____________________
           |  _________________  |
           | | JO           0. | |
           | |_________________| |
           |  ___ ___ ___   ___  |
           | | 7 | 8 | 9 | | + | |
           | |___|___|___| |___| |
           | | 4 | 5 | 6 | | - | |
           | |___|___|___| |___| |
           | | 1 | 2 | 3 | | x | |
           | |___|___|___| |___| |
           | | . | 0 | = | | / | |
           | |___|___|___| |___| |
           |_____________________|

             (Regular Calculator)                                             
"""
print(logo)


def add(n1, n2):
    """
    Add two numbers.

    Args:
        n1 (float): The first number.
        n2 (float): The second number.

    Returns:
        float: The sum of n1 and n2.
    """
    return n1 + n2


def subtract(n1, n2):
    """
    Subtract the second number from the first number.

    Args:
        n1 (float): The first number.
        n2 (float): The second number.

    Returns:
        float: The result of n1 minus n2.
    """
    return n1 - n2


def multiply(n1, n2):
    """
    Multiply two numbers.

    Args:
        n1 (float): The first number.
        n2 (float): The second number.

    Returns:
        float: The product of n1 and n2.
    """
    return n1 * n2


def divide(n1, n2):
    """
    Divide the first number by the second number.

    Args:
        n1 (float): The dividend.
        n2 (float): The divisor.

    Returns:
        float: The result of dividing n1 by n2.

    Note:
        This function does not handle division by zero.
    """
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
"""
Dictionary mapping arithmetic operation symbols to their corresponding
function implementations.
"""


def calculator():
    """
    Run the calculator program.

    This function:
    - Displays the calculator logo
    - Prompts the user for numbers and an operation
    - Performs the selected calculation
    - Allows the user to continue calculating with the result
      or start a new calculation

    The function uses a loop for continuous calculations and recursion
    to restart the calculator when the user chooses to begin a new one.
    """
    print(logo)
    should_accumulate = True
    num1 = float(input("what is the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")
        num2 = float(input("what is the next number?: "))

        answer = operations[operation_symbol](n1=num1, n2=num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(
            f"Type 'y' to continue calculating with {answer} , "
            "or type 'n' to start a new calculation."
        )

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n * 30")
            calculator()


calculator()