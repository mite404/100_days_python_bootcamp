############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   https://appbrewery.github.io/python-day11-demo/

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and
# return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove
# the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's
# score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then
# use the deal_card() function to add another card to the user_cards List. If no, then the game
# has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9
# need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep
# drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the
# computer and user both have the same score, then it's a draw. If the computer has a blackjack
# (0), then the user loses. If the user has a blackjack (0), then the user wins. If the
# user_score is over 21, then the user loses. If the computer_score is over 21, then the computer
# loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console
# and start a new game of blackjack and show the logo from art.py.

import random


def deal_card():
    """
    Returns a random card from the deck.
    """
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random.shuffle(deck)
    card = random.choice(deck)
    return card


def calculate_score(cards):
    """
    Take a list of cards & return score.
    :param cards:
    :return:
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


user_cards = []
dealer_cards = []
is_game_over = False

for _ in range(2):
    user_cards.append(deal_card())
    dealer_cards.append(deal_card())

while not is_game_over:
    user_score = calculate_score(user_cards)
    dealer_score = calculate_score(dealer_cards)

    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Dealer's first card: {dealer_cards[0]}")

    if user_score == 0 or dealer_score == 0 or user_score > 21:
        print("Busssst!")
        is_game_over = True
    else:
        draw_again = input("Type 'y' to get another card, type 'n' to pass:")
        if draw_again == "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True

while dealer_score != 0 and dealer_score < 17:
    dealer_cards.append(deal_card())
    dealer_score = calculate_score(dealer_cards)







# TODO 3 - If computer gets blackjack, then the user loses (even if the user also has a
#  blackjack). If the user gets a blackjack, then they win (unless the computer also has a
#  blackjack).

# TODO 4 - Calculate the user's and computer's scores based on their card values.

# TODO 5 - If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1
#  instead.

# TODO 6 - Reveal computer's first card to the user.

# TODO 7 - Game ends immediately when user score goes over 21 or if the user or computer gets a
#  blackjack.

# TODO 8 - Ask the user if they want to get another card.

# TODO 9 - Once the user is done and no longer wants to draw any more cards, let the computer
#  play. The computer should keep drawing cards unless their score goes over 16.

# TODO 10 - Compare user and computer scores and see if it's a win, loss, or draw.

# TODO 11 - Print out the player's and computer's final hand and their scores at the end of the
#  game.

# TODO 12 - After the game ends, ask the user if they'd like to play again. Clear the console
#  for a fresh start.