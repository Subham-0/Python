from art import logo
import random

def run():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 to 100.")
   
    number = random.randint(1,100)
    #print(number)
    level = input("Choose a difficulty .Type 'easy' or 'hard':  ")
    def game_level(num):
        attempt = num
        while attempt != 0:
            print(f"You have {attempt} left to guess the number")
            guess_number = int(input("make a guess : "))
            if guess_number > number:
                print("Too High.")
                print("Guess again")
            elif guess_number<number:
                print("Too Low")
                print("Guess Again")
            attempt-=1
            if guess_number == number:
                print(f"You got it! The answer was {number}")
                attempt = 0
            if guess_number<number or guess_number>number:
                if attempt == 0:
                    print(f"The number is {number}")
                    print("You've run out of guesses. You lose!")
                
            
             
    if level == "easy":
        game_level(10)
    elif level == 'hard':
        game_level(5)
    else:
        print("please enter a valid level")
    dis = input("Do you want to play again? 'y' or 'n'")   
    if dis == 'y' or 'n':
        run()
    else:
        print("Thank you for playing!")      
            
    
run()


# or

# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5

# #Function to check user's guess against actual answer.
# def check_answer(guess, answer, turns):
#   """checks answer against guess. Returns the number of turns remaining."""
#   if guess > answer:
#     print("Too high.")
#     return turns - 1
#   elif guess < answer:
#     print("Too low.")
#     return turns - 1
#   else:
#     print(f"You got it! The answer was {answer}.")

# #Make function to set difficulty.
# def set_difficulty():
#   level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#   if level == "easy":
#     return EASY_LEVEL_TURNS
#   else:
#     return HARD_LEVEL_TURNS

# def game():
#   print(logo)
#   #Choosing a random number between 1 and 100.
#   print("Welcome to the Number Guessing Game!")
#   print("I'm thinking of a number between 1 and 100.")
#   answer = random.randint(1, 100)
#   print(f"Pssst, the correct answer is {answer}") 

#   turns = set_difficulty()
#   #Repeat the guessing functionality if they get it wrong.
#   guess = 0
#   while guess != answer:
#     print(f"You have {turns} attempts remaining to guess the number.")

#     #Let the user guess a number.
#     guess = int(input("Make a guess: "))

#     #Track the number of turns and reduce by 1 if they get it wrong.
#     turns = check_answer(guess, answer, turns)
#     if turns == 0:
#       print("You've run out of guesses, you lose.")
#       return
#     elif guess != answer:
#       print("Guess again.")


# game()
