import random
from art import logo

attempts=0
game_over=False

def number_between():
    '''
    Returns random number in the range of 1 to 100
    '''
    random_num=random.randint(1,100)
    return random_num

win_num=number_between()


def guess_num(num):
    '''
    this function takes user input for a number
    and accordingly genarates a result
    '''
    global attempts
    global game_over
    if num==win_num:
        print(f"You gussed it right, The answer is {num}")
        game_over=True

    if num>win_num:
        print("Too high")

    if num<win_num:
        print("Too low")

    if num>win_num or num<win_num:
        attempts-=1
        print(f"You have {attempts} attempts left")
        print("Guess Again!")

print(logo)
print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100")

def set_difficulty():
    global attempts
    level = input("Choose difficulty , Type 'easy' or 'hard' : ").lower()

    if level == "easy":
        attempts = 10
        print("You have 10 attempts to guess the number.")
    elif level == "hard":
        attempts = 5
        print("You have 5 attempts to guess the number.")
    else:
        print("Wrong input")
        game_over=True

set_difficulty()

while not game_over:
    guess=int(input("Make a guess : "))
    guess_num(guess)

    if attempts==0:
        print("You've run out of guesses.")
        game_over=True
