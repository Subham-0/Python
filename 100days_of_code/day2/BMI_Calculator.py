height = float(input("Enter your height = "))
weight = float(input("Enter your weight = "))

#bmi = str(int(weight/(height**2)))
bmi = str(round(weight/(height**2),3))
print("Body mass index is "+bmi)



# Round up the value to three digits after the decimal
print(round(3.6666666),3)

#floor division
print(8//3)
# if we divide any number to any number it gets turn into a floating point number
#if we don't want that then use floor division it give a integer value
print(type(8//3))


# use shorthand
score = 0
score= score+1
score+=1
print(score)
# we can also use -= , *= , /=

#f-string
score = 0 
height=1.8
iswinning = True
# print("your score is "+ str(score) +" your height is  " +str(height )+" and you are winning is "+str(iswinning))
print(f"your score is {score} your height is {height } and you are winning is {iswinning}")