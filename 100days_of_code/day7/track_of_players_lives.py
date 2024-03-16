import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = ["tiger" , "bear" , "cat"]
chosen_word = random.choice(word_list)


word_lenght = len(chosen_word)
lives = 6
display  = []
for letter in range(word_lenght):
    display +="_"


end_of_game = False

while not end_of_game:
    guess = input("Guess a letter:").lower()

    for position in range(word_lenght):
        letter = chosen_word[position]
        if letter == guess:
            display[position]= letter
       
    if guess not in chosen_word:
      lives =lives-1
    if lives == 0:
      end_of_game = True
      print("You Lose!")
        
                
    print(display)
    print(stages[lives])
    if "_" not in display:
        end_of_game = True
        print("You win!")
    
   