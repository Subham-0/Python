import random

name_string ="Subham Ajit Hari Komal"
name = name_string.split(" ")  # put the names in to a list
total_name = len(name)
random_number = random.randint(0,total_name-1)
random_name = name[random_number]
# print(random_name)
print(f"{random_name} is going to buy the meal today")