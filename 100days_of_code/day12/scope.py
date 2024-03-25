        # Scope
from turtle import position


enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")
    
increase_enemies()
print(f"enemies outside function: {enemies}")

#Local Scope

def drink_potion():
    potion_strength  = 2 
    print(potion_strength)
    
drink_potion()
#print(potion_strength) #NameError: name 'potion_strength' is not defined

# new variable or function inside a funtion it can only access inside that function because it has local scope

# Global scope
player_health = 19 

def game():
    def drink_potion():
        player_health = 32
        print(player_health)
        
    drink_potion()
    
print(player_health)

game()

#Modifying Global Scope

gadgets = 1 

def increase_gadgets():
    global gadgets  #  explicitly tell Python to use the global variable
    gadgets += 5
    print(f"gadgets inside function: {gadgets}")
    
increase_gadgets()
print(f"gadgets outside function {gadgets}")    