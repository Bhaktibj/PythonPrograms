""" Write a Program DeckOfCards.java, to initialize deck of cards having suit
("Clubs", "Diamonds", "Hearts", "Spades") & Rank ("2", "3", "4", "5", "6", "7", "8", "9", "10",
"Jack", "Queen", "King", "Ace").

Shuffle the cards using Random method and then distribute 9 Cards to 4 Players and
Print the Cards the received by the 4 Players using 2D Array…
"""


import random
import itertools

# rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'king', 'queen', 'jack', 'ace']

# suit = ['clubs', 'diamonds', 'hearts', 'spades']

class Cards:
    def dack_of_cards(self):
        dack_of_card= list(
            itertools.product(['2','3','4','5','6','7','8','9','king','queen','jack','ace'],
                 ['clubs','diamond','hearts','spades']))
        print(dack_of_card)
        for number_of_player in range(1, 5): # This loop shuffle cards to 4 players
            random.shuffle(dack_of_card) # "random.shuffle" is used to shuffle the card
            print("\n")
            print("player:",number_of_player)
            # This loop is to distribute 9 cards to the players
            for number_of_cards in range(1, 10):
                    print(number_of_cards, dack_of_card[number_of_cards][0],
                          "of", dack_of_card[number_of_cards][1])
cards_obj = Cards()
if __name__ == '__main__':
    cards_obj.dack_of_cards()


