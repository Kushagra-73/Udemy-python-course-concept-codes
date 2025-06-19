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

# rps=int(input("""
#             Type 0 to choose rock
#             Type 1 to choose scissors
#             Type 2 to choose Paper
              
#               """))

# if rps==0:
#     print(f"Rock {rock}")
#     a=random.choice([rock,paper,scissors])
#     print("Computer chose",a)
#     if a==rock:
#         print("Tie")
#     elif a==scissors:
#         print("You win")
#     else:
#         print("You lose")

# if rps==1:
#     print("Scissors",scissors)
#     a=random.choice([rock,paper,scissors])
#     print("Computer chose",a)
#     if a==scissors:
#         print("Tie")
#     elif a==paper:
#         print("You win")
#     else:
#         print("You lose")

# if rps==2:
#     print("Paper",paper)
#     a=random.choice([rock,paper,scissors])
#     print("Computer chose",a)
#     if a==paper:
#         print("Tie")
#     elif a==rock:
#         print("You win")
#     else:
#         print("You lose")


# OR 

game_images = [rock, paper, scissors]

# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# # Note: it's worth checking if the user has made a valid choice before the next line of code.
# # If the user typed somthing other than 0, 1 or 2 the next line will give you an error.
# # You could for example write:
# if user_choice >= 0 and user_choice <= 2:
#     print(game_images[user_choice])

# computer_choice = random.randint(0, 2)
# print("Computer chose:")
# print(game_images[computer_choice])

# if user_choice >= 3 or user_choice < 0:
#     print("You typed an invalid number. You lose!")
# elif user_choice == 0 and computer_choice == 2:
#     print("You win!")
# elif computer_choice == 0 and user_choice == 2:
#     print("You lose!")
# elif computer_choice > user_choice:
#     print("You lose!")
# elif user_choice > computer_choice:
#     print("You win!")
# elif computer_choice == user_choice:
#     print("It's a draw!")


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

