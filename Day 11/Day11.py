"""
Blackjack Game Project

This module implements a simple command-line Blackjack game where
a user plays against the computer. The game follows standard Blackjack
rules, including card dealing, score calculation, and win/lose conditions.
"""

logo = """
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                       _/ |                
                      |__/                 
        .------.------.------.------.
        |A_  _ |A /\  |A _   |A .   |
        |( \/ )| /  \ | ( )  | / \  |
        | \  / | \  / |(_x_) |(_,_) |
        |  \/ A|  \/ A|  Y  A|  I  A|
        `------^------^------'------'             
"""

import random


"""
Card Values:
- Cards from 2-10 have their face value.
- Jack, Queen, King have a value of 10.
- Ace has a value of 11 or 1 depending on the score.
"""


def deal_card():
    """
    Deal a random card from the deck.

    The deck includes:
    - One Ace (value 11)
    - Cards 2 through 10
    - Face cards (Jack, Queen, King) represented as 10

    Returns:
        int: The value of the randomly selected card.
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """
    Calculate the score of a hand of cards.

    Rules:
    - A Blackjack (Ace + 10-value card) returns a score of 0.
    - If the score exceeds 21 and an Ace (11) is present,
      the Ace is converted to 1.

    Args:
        cards (list[int]): A list of card values.

    Returns:
        int: The calculated score of the hand.
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    """
    Compare the user's score with the computer's score
    and determine the game outcome.

    Args:
        user_score (int): Final score of the user.
        computer_score (int): Final score of the computer.

    Returns:
        str: A message describing the result of the game.
    """
    if user_score == computer_score:
        return "Draw \n"
    elif computer_score == 21:
        return "Lose, opponent has a blackjack! \n"
    elif user_score == 21:
        return "You won with a blackjack! \n"
    elif user_score > 21:
        return "You went over. You Lose! \n"
    elif computer_score > 21:
        return "Opponent went over. You Win! \n"
    elif user_score > computer_score:
        return "You Win! \n"
    else:
        return "You Lose! \n"


def play_game():
    """
    Play a single game of Blackjack.

    This function:
    - Deals initial cards to the user and computer
    - Allows the user to draw additional cards
    - Automatically draws cards for the computer
    - Displays final hands and determines the winner
    """
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}\n")
        print(f"Computer's first card: {computer_cards[0]}\n")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input(
                "Type 'y' to get another card, type 'n' to pass: "
            ).lower()

            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, Final score: {user_score}\n")
    print(f"Computer's final hand: {computer_cards}, Final score: {computer_score}\n")
    print(compare(user_score, computer_score))


"""
Main game loop.

Continuously prompts the user to start a new game of Blackjack
until the user chooses not to continue.
"""
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()