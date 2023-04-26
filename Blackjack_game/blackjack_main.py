############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.
# Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
import random


def deal_card():
    # cards = [11, 10]
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card


game_ends = False
user_cards = []
computer_cards = []
user_cards.append(deal_card())
user_cards.append(deal_card())

print(user_cards)
computer_cards.append(deal_card())
computer_cards.append(deal_card())
print(computer_cards)
