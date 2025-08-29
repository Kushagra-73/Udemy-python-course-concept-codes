import random
from art import logo

def deal_card():
    '''
    returns a random card from the deck
    '''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card

def calculate_score(cards):
    '''
    Take a list of cards and return the score calculated from the cards
    '''
    if sum(cards)==21 and len(cards)==2:
        return 0
    
    if 11 in cards and sum(cards)==21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(u_score,c_score):
    if u_score==c_score:                            #if elif run priority wise
        return "Draw "
    elif c_score==0:
        return "You Lose, Opponent has Blackjack"
    elif u_score==0:
        return "You win, You have the Blackjack "
    elif u_score>21:
        return "You went over, You lose"
    elif u_score>c_score:
        return "You win"
    else:
        return "You lose"


def play_game():
    print(logo)

    user_cards=[]
    computer_cards=[]
    user_score=-1           #As we defiend these variables earlier in the first while loop 
                            #We need to define it earlier to use in later code outside while
                            #loop otherwise the variable will be undefined
    computer_score=-1



    is_game_over=False

    for yc in range(0,2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
            
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)

        print(f"Your cards are : {user_cards}, current score = {user_score}")
        print (f"Dealer's First Card : {computer_cards[0]}")


        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            cont=input("Type 'y' to hit(another card) type 'n' to pass: ").lower()
            if cont=='y':
                user_cards.append(deal_card())
            else:
                is_game_over=True
        
    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)


    print(f"Your Final Hand :{user_cards}, final score: {user_score}")
    print(f"Dealer's Final Hand : {computer_cards}, final score:{computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want to play the game of Blackjack Type 'y' if yes or 'n' if no :  ")=="y":
    print("\n"*100)
    play_game()
       
        