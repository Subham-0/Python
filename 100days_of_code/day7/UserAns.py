import random

word_list = ["tiger" , "bear" , "cat"]
chosen_word = random.choice(word_list)
guess = input("Guess a letter:").lower()
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")