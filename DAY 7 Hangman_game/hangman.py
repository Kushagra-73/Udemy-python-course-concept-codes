import random


# import hangman_words  #METHOD 1

from hangman_words import words_list   #METHOD 2
from hangman_art import stages,logo


lives = 6


print(logo)

# chosen_word = random.choice(hangman_words.word_list)   #METHOD 1
chosen_word=random.choice(words_list)


placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

   
    print(f"**************************** {lives}/6 LIVES LEFT****************************")
   
    guess = input("Guess a letter: ").lower()

    
    if guess in correct_letters:
        print(f"You have already guessed {guess}")
    
    display = ""

    for letter in chosen_word:
        if letter == guess:                        #For if letter                  
            display += letter
            correct_letters.append(guess)
        
        elif letter in correct_letters:            #For if letter already exists in user input string
            display += letter

        else:
            display += "_"


    print("Word to guess: " + display)



    if guess not in chosen_word:      #Losing life and game block
        lives -= 1
        print(f"You guessed <{guess}> ,a wrong letter, You lose a life")

        if lives == 0:
            game_over = True

            
            print(f"***********************YOU LOSE**********************")
            print(f"The correct word is {chosen_word} ")

    if "_" not in display:            #Wining game block
        game_over = True
        print("****************************YOU WIN****************************")

   
    print(stages[lives])
