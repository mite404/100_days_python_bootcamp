import random
import hangman_words
from hangman_art import logo, stages
# import os

end_of_game = False
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

LIVES = 6

# testing code
print(logo)

print(f"Pssst, the solution is {chosen_word}")

# create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:

    guess = input("Guess a letter: ").lower()

    # if os.name == 'nt':
    #     os.system('cls')
    # else:
    #     os.system('clear')

    # if the user has entered a letter they've already guessed, print it
    if guess in display:
        print(f"You've already guessed {guess}")

    # check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n"
        #       f"Current letter: {letter}\n"
        #       f"Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. -1 life bitch\n"
              f"you have {LIVES} lives left...")
        LIVES -= 1
        if LIVES == 0:
            end_of_game = True
            print("You fuckin' looser")

    # join all the elements in the list and turn it into a string
    print(f"{' '.join(display)}")

    # check if user has guessed all letters
    if "_" not in display:
        end_of_game = True
        print("You Win!")

    print(stages[LIVES])
