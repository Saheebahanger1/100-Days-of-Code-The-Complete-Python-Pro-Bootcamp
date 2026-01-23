#Functions
def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice?")

greet()

#Funcions with Input.
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("Saheeb")

#Function with more Than 1 input.
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

#Positional argument
greet_with("Saheeb" , "Baramulla")  #(name,location)

#Keyword arguments
greet_with(location="Baramulla",name="Saheeb")


# Cipher Cypher Project.
print("""                                                                  
                                                                  
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88                                                                                                                                                                                              
                                   88                                 
                                   88                                 
                                   88                                 
 ,adPPYba, 8b       d8 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" `8b     d8' 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b          `8b   d8'  88       d8 88       88 8PP""""""" 88          
"8a,   ,aa   `8b,d8'   88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"'     Y88'    88`YbbdP"'  88       88  `"Ybbd8"' 88          
               d8'     88                                             
              d8'      88                                             
""")
# Define the reference alphabet for shifting
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

def ceaser(original_text, shift_amount, encode_or_decode):
    """
    Encrypts or decrypts a text by shifting letters by a specified amount.
    :param original_text: The string to be transformed.
    :param shift_amount: Integer representing how many positions to shift.
    :param encode_or_decode: String 'encode' to encrypt or 'decode' to decrypt.
    """

    output_text = ""

    # If decoding, reverse the shift direction
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:

        # Check if the character is a letter in our alphabet list
        if letter not in alphabet:
            # Keep symbols, numbers, and spaces as they are
            output_text += letter
        else:
            # Find current position and calculate new position            
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is {encode_or_decode}d result: {output_text}")

# Main program loop
should_continue = True

while should_continue:
    # Gather user input
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type shift number:\n"))

    # Execute the transformation logic
    ceaser(encode_or_decode= direction, original_text= text, shift_amount= shift )

    # Ask the user if they want to run the program again 
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Good Bye!")