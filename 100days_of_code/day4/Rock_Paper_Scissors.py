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

game_image = [rock,paper,scissors]
user_choice = int(input("What do you choose? Typr 0 for Rock , 1 for Paper or 2 for Scissors"))

if user_choice >= 3 or user_choice <0:
    print("you typed an invalid number, you lose!")
else:
    print(game_image[user_choice])

computer_choice = random.randint(0,2)
print("Computer choise:")
print(game_image[computer_choice])

if user_choice ==0 and computer_choice ==2:
    print("You win!")
elif computer_choice == 0 and user_choice ==2:
    print("You Lose")
elif computer_choice > user_choice:
    print("You lose")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's Draw!")


                # OR

# while True:
#     user_choose = eval(input("What do you choose? Typr 0 for Rock , 1 for Paper or 2 for Scissors"))
#     if user_choose == 0:
#         print(f"user choose \n{rock}")
#         break
#     elif user_choose == 1:
#         print(f"user choose \n{paper}")       
#         break
#     elif user_choose == 2:
#         print(f"user choose \n{scissors}") 
#         break
#     else:
#         print("please enter a valid choose...")

# # computer_choise

# computer_choose = random.randint(0,2)
# if computer_choose == 0:
#         print(f"computer_choose \n{rock}")
# elif computer_choose == 1:
#         print(f"computer_choose\n{paper}")
# else:
#     print(f"computer_choose\n{scissors}")

# if user_choose == 0 :
#     if computer_choose == 0 :
#         print("Tie")
#     elif computer_choose == 1:
#         print("Computer Win!")
#     else:
#         print("You Win!")
# elif user_choose == 1:
#     if computer_choose == 0:
#          print("You Win!")
#     elif computer_choose == 1:
#          print("Tie")
#     else:
#          print("Computer Win!")
# else:
#     if computer_choose == 0:
#          print("Computer Win!")
#     elif computer_choose == 1:
#          print("You Win!")
#     else:
#          print("Tie")
    
     