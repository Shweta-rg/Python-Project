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


# Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.
def calculate_score(card_list):
    if 11 in card_list and 10 in card_list:
        sum_cards = 0
        # game_ends=True
        return 0

    if sum(card_list) > 21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)
        sum_cards = sum(card_list)

    return sum(card_list)


while (game_ends != True):
    user_score = calculate_score(user_cards)
    print(user_score)
    computer_score = calculate_score(computer_cards)
    print(computer_score)

    if user_score == 0 or computer_score == 0 or user_score > 21:
        game_ends = True
    else:

        input_choice = (
            input("Do you want to choose another card, Y/N")).upper()
        if (input_choice == 'Y'):
            user_cards.append(deal_card())
            print(user_cards)
            calculate_score(user_cards)

        else:
            game_ends = True
