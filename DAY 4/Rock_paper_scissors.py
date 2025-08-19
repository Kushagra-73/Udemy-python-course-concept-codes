# Rock paper scissors
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice=int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors :"))

if 0<=user_choice<=2:
    print(game_images[user_choice])

comp_choice=random.randint(0,2)
print("Computer choose :"
      )
print(game_images[comp_choice])

if user_choice<0 and user_choice>2:
    print("Invalid choice")

elif comp_choice==0 and user_choice==2:
    print("You loose")

elif comp_choice==2 and user_choice==0:
    print("You win")

elif comp_choice>user_choice:
    print("You loose")

elif comp_choice<user_choice:
    print("You win")

elif comp_choice==user_choice:
    print("Draw!")

