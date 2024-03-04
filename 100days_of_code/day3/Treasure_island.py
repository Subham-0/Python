

print("Welcome to Treasure Island \nYour mission is to find the treasure.")

choice1 = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"").lower()
if choice1 =="left":
    choice2 = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait fora boat. Type \"swim\" to swim across").lower()
    if choice2 =="wait":
        choice3 = input("You arive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game over.")
        elif choice3 == "yellow":
            print("You found the treasure! You win!")
        elif choice3 == "blue":
            print("You enrer a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't ecist. Game Over!")
    else:
        print("You got attacked by an angry trout. Game Over!")
else:
    print("you fell into a hole. Game Over!")
        

    




