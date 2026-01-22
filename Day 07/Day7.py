"""
HANGMAN GAME (Console Based)

This program implements a simple Hangman game where:
- A random word is selected from a predefined list
- The player guesses letters one by one
- The player has limited lives
- Incorrect guesses reduce lives and draw the hangman
- The game ends when the word is guessed or lives reach zero
"""

import random

# -------------------------------
# ASCII Art Logo
# -------------------------------
print(''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/  
''')

# -------------------------------
# Hangman stages (based on lives)
# -------------------------------
stages = [
    '''
      +---+
      |   |
      O   |
     /|\\  |    # Lives = 0
     / \\  |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\\  |     # Lives Remained = 1
     /    |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\\  |     # Lives Remained = 2
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |      # Lives Remained = 3
     /|   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |     
      O   |      # Lives Remained = 4
      |   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |    
      O   |      # Lives Remained = 5
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |      # Lives Remained = 6
          |
          |
          |
          |
    =========
    '''
]

# -------------------------------
# Word selection
# -------------------------------
word_list = ['microsoft', 'google', 'python', 'intelligence', 'programming',
             'blockchain', 'kubernetes', 'serverless', 'latency', 'firmware',
             'cryptography', 'virtualization', 'middleware','mainframe',
             'refactoring', 'api', 'frontend', 'backend', 'containerization']

chosen_word = random.choice(word_list)

# -------------------------------
# Game variables
# -------------------------------
lives = 6
game_over = False
correct_letters = []

# -------------------------------
# Create placeholder for word
# -------------------------------
display = "_" * len(chosen_word)
print("Word to guess:", display)

# -------------------------------
# Game loop
# -------------------------------
while not game_over:
    guess = input("\nGuess a letter: ").lower()

    new_display = ""

    # Check each letter in the chosen word
    for letter in chosen_word:
        if letter == guess:
            new_display += letter
            if guess not in correct_letters:
                correct_letters.append(guess)
        elif letter in correct_letters:
            new_display += letter
        else:
            new_display += "_"

    display = new_display
    print("Current word:", display)

    # If guessed letter is wrong
    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong guess! Lives remaining: {lives}")

        if lives == 0:
            game_over = True
            print("\nYou Lose!")
            print("The word was:", chosen_word)

    # If all letters are guessed
    if "_" not in display:
        game_over = True
        print("\nYou Win!")

    # Show hangman stage
    print(stages[lives])

