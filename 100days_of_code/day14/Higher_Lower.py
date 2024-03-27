from art import logo,vs
from gamedata import data
import random
import os
def format_data(account):
    """Takes the account data and return the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_descr}, from {account_country}")

def check_answer(guess, a_follwer , b_follwer):
    """Takes the user guess and follower counts returns if they got it right."""
    if a_follwer >b_follwer:
        return guess == 'a'
    else:
        return guess == 'b'
             
    


#Display art
def game():
    print(logo)
    score = 0
    game_should_continue = True
    while game_should_continue:
        os.system('cls')
        #Generate a random account from game data
        account_a = random.choice(data)
        account_b = random.choice(data)
        
        # Make account at position B become the next account at position A
        account_a = account_b
        account_b = random.choice(data)

        while account_a == account_b:
            account_b = random.choice(data)
            
        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Against B: {format_data(account_b)}")

        # Ask user for a guess.
        guess = input("Who has more followers? 'A' or 'B':  " ).lower()

        # Check if user is correct.
        ## Get follower count.
        a_follwer_count  = account_a["follower_count"]
        b_follwer_count  = account_b["follower_count"]
        ## If Statement
        is_correct = check_answer(guess,a_follwer_count,b_follwer_count)

        # Feedback.
        if is_correct:
            score+=1
            print(f"You're right! Current score : {score}")
        else:
            game_should_continue = False
            print(f"Sorry! that's wrong.Final score : {score}")
game()
