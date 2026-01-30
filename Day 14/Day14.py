from day14_data import game_data
import random

# Display art.
logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ '/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/    

"""
vs = """

 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

"""
print(logo)

def format_data(account):
    """Takes the account data and returns the prrintable format."""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"


def check_answer(user_guess, a_followers, b_followers):
    """Take a user"s guess and the follower counts and returns if they got it right."""
    if a_followers > b_followers and user_guess == "a":
        return  True
    elif a_followers > b_followers and user_guess == "b":
        return False
    elif a_followers < b_followers and user_guess == "b":
        return  True
    elif a_followers < b_followers and user_guess == "a":
        return False

score = 0
game_should_continue = True
account_b = random.choice(game_data)

# Make the game repeatable.
while game_should_continue:
    # Generate a random account from the game data.

    # Making accounts at position B become the next account at position A.
    account_a = account_b
    account_b = random.choice(game_data)

    if account_a == account_b:
        account_b = random.choice(game_data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")


    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Clear the Screen.
    print("\n" * 20)
    print(logo)

    # -Get follower count of each account.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    # Check if user is correct.
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give your feedback on their guess.
    # Score keeping.
    if is_correct:
        score += 1
        print(f"You're right! Current Score: {score}")
    else:
        print(f"Sorry that's wrong. Final Score: {score}")
        game_should_continue = False
