import random

word_list = ["tiger" , "bear" , "cat"]
chosen_word = random.choice(word_list)

display  = []
word_lenght = len(chosen_word)
# for letter in chosen_word:
for letter in range(word_lenght):
    display +="_"
# print(display)

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter:").lower()

    

    for position in range(word_lenght):
        letter = chosen_word[position]
        if letter == guess:
            display[position]= letter
            
    print(display)
    if "_" not in display:
        end_of_game = True