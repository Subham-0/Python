print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ")
name2 = input("What is their name? ")
combine_name = name1+name2
combine_name = combine_name.lower();
t = combine_name.count('t')
r = combine_name.count('r')
u = combine_name.count('u')
e = combine_name.count('e')
first_digit = t+u+r+e
l = combine_name.count('l')
o = combine_name.count('o')
v = combine_name.count('v')
e = combine_name.count('e')
second_digit = l+o+v+e
score = int(str(first_digit)+str(second_digit))
if(score <10) or (score>90):
    print(f"Your score is {score} , you go together like coke and mentos.")
elif(score>=40) and (score<=50):
    print(f"Your score is {score} , you are alright together.")
else:
    print(f"Your score is {score}")
    