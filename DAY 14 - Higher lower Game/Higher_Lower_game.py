# Importing Modules and components for the game
from celebi import data
from art import logo,vs
import random

def acc_data(account):
    """
    Format the account data into printable format
    """
    account_name=account["name"]
    account_description=account["description"]
    account_country=account["country"]
    return f"{account_name}, {account_description}, from {account_country}"

def check_ans(user_guess,a_followers,b_followers):
    """
    Take a user's guess and the follower counts and returns if they got it right.
    """
    if a_followers > b_followers:
        return user_guess=="A"
    
    else:
        return user_guess=="B"
        

#Display the art
print(logo)
score=0
game_should_continue=True

account_b=random.choice(data)

while game_should_continue:


    # Generate a random account from the data
    account_a=account_b
    account_b=random.choice(data)
    

    if account_a==account_b:
        account_b=random.choice(data)


    print(f"Compare A: {acc_data(account_a)}")
    print(vs)
    print(f"Against B: {acc_data(account_b)}")

    # Ask user to guess
    guess=input("Who has more followers? Type 'A' or 'B': ").upper()

    print("\n"*50)
    print(logo)

    # Check if user is correct
    ## Get follower count of each account
    a_follower_account=account_a["follower_count"]
    b_follower_account=account_b["follower_count"]

    ## Use if statement to check if user is correct
    is_correct=check_ans(guess,a_follower_account,b_follower_account)

    # Give user feedback on their guess
    if is_correct:
        score+=1
        print(f"You're Right! Current Score : {score}")
    else:
        print(f"Sorry You're Wrong, Final Score : {score}")
        game_should_continue=False