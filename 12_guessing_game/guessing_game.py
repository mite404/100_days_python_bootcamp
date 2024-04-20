from random import randint
import os
from art import logo

# Clear screen for Windows
if os.name == "nt":
    os.system("cls")
# Clear screen for Linux/macOS (might require modification on some systems)
else:
    os.system("clear")

print(logo)
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
    """
    Check player's answer against randomly chosen number, returns turns remaining.
    """
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")
        input(print("Play again? (y/n): "))
        if input() == "y":
            game()
        else:
            return


def set_difficulty():
    # ask user for easy/hard mode 10/5 LIVES
    level = input("Choose a difficulty. Type 'easy or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS

    else:
        return HARD_LEVEL_TURNS


def game():
    # Choose a random number b/t 1-100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()
    # Repeat the guessing functionality if they get it wrong
    guess = 0
    while guess != answer:
        print(f"{turns} attempts remaining.")
        # Let player guess
        guess = int(input("Make a guess: "))
        # Track number of turns and reduce by 1 if wrong
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses. GAME OVER SUCKERRrrr!!")
            input(print("Play again? (y/n): "))
            if input() == "y":
                game()
            else:
                return


game()
