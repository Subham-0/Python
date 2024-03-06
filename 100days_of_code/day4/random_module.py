import random
random_number = random.randint(1,10)
print(random_number)

# what is a python module ?
# Python Module is a file that contains built-in functions, classes,its and variables


random_float = random.random()
print(random_float) #It actually print a long floating point value between 0.0 - 1.0

#how to create a random decimal number between 0 and 5?
print(random_float*5) 

love_score = random.randint(1,100)
if(love_score <10) or (love_score>90):
    print(f"Your score is {love_score} , you go together like coke and mentos.")
elif(love_score>=40) and (love_score<=50):
    print(f"Your score is {love_score} , you are alright together.")
else:
    print(f"Your score is {love_score}")




# can we make our own module?
# yes
# # here i create a file my_module i want use it in this random file 
import my_module
print(my_module.ower)
print(my_module.description)
