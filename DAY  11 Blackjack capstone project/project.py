# if card number add more than 21 then "bust" which means you loose
# ace holds two values wither 1 or 11 which can be choosen as according to goal
# face cards hold value of 10
# when dealer's and our's score is same then it is draw


"""
Chose your difficulty
Normal 😎: Use all Hints below to complete the project.
Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
Expert 🤯: Only use Hint 1 to complete the project.
Our Blackjack Game House Rules
The deck is unlimited in size.
There are no jokers.
The Jack/Queen/King all count as 10.
The Ace can count as 11 or 1.
Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

The cards in the list have equal probability of being drawn.
Cards are not removed from the deck as they are drawn.
The computer is the dealer.
"""
import random as rd

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player = []
dealer = []

def deal_cards(random_pick):
    random_pick=rd.choice(cards)
    

play_again = True
while play_again:
    play = input("Do you want to play BLACKJACK CAPSTONE ? Type 'y' or 'n' :").lower()
    if play == "y":

        for card in range(0, 2):
            player_2_cards = rd.choice(cards)

            dealer_2_cards = rd.choice(cards)
            player.append(player_2_cards)
            dealer.append(dealer_2_cards)

    print(f"Your cards :{player}, current score : {sum(player)}")
    dealer_random=rd.randint(0,1)
    print(f"Computer's first card {dealer[dealer_random]}")


