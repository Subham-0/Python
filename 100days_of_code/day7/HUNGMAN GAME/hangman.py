import random
import os
from hungman_word import word_list
from hungman_art import stages,logo




chosen_word = random.choice(word_list)

print(logo)

word_lenght = len(chosen_word)
lives = 6
display  = []
for letter in range(word_lenght):
    display +="_"


end_of_game = False

while not end_of_game:
    guess = input("Guess a letter:").lower()
    
    os.system('cls')
    
    if guess in display:
        print(f"You've already aguessed {guess}")

    for position in range(word_lenght):
        letter = chosen_word[position]
        if letter == guess:
            display[position]= letter
       
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives =lives-1
      
    if lives == 0:
      end_of_game = True
      print("You Lose!")
        
                
    print(display)
    print(stages[lives])
    
    if "_" not in display:
        end_of_game = True
        print("You win!")
    
    
if  "_"  in display:
        print(f"The word is {chosen_word}")    