import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

number = ['0','1','2','3','4','5','6','7','8','9',]
symbol = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the Subham Password generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_number = int(input("How many numbers would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))

# password = ""
# for n in range(1,nr_letters+1):
#     random_letter = random.choice(letters)
#     password+=random_letter
# for n in range(1,nr_number+1):
#     random_number = random.choice(number)
#     password+=random_number
# for n in range(1,nr_symbols+1):
#     random_symbol = random.choice(symbol)
#     password+=random_symbol
# print(password)   

password_list = []
for n in range(1,nr_letters+1):
    random_letter = random.choice(letters)
    password_list.append(random_letter)
for n in range(1,nr_number+1):
    random_number = random.choice(number)
    password_list.append(random_number)
for n in range(1,nr_symbols+1):
    random_symbol = random.choice(symbol)
    password_list.append(random_symbol)
    
random.shuffle(password_list)
# print(password_list)   

password = ""
for char in password_list:
    password+=char
print(f"Your password is : {password}")