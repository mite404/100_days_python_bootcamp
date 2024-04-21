import os
import random
from art import logo, vs
# import art
from game_data import data


def clear():
    # Clear screen for Windows
    if os.name == "nt":
        os.system("cls")
    # Clear screen for Linux/macOS
    else:
        os.system("clear")


def format_data(account):
    """Format the account data into printable format"""
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f"{account_name} a {account_descr} from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Take user guess and follower counts and returns if guess is correct"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# print comparisons
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    # print(times_right)
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print("Please pick the thing with more followers...")
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # get user guess
    guess = input("Who has more followers? (a/b)").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear()
    print(logo)

    if is_correct:
        score += 1
        print(f"Spot on!! Current score: {score}")
        # game()
    else:
        game_should_continue = False
        print(f"Wrong! Game Over SUCKERRR!! Final score: {score}")
        # play_again = input("Play again (y/n) ? ")
        # if play_again == 'y':
        #     game()


# game()  # call game function to start
