height = float(input("Enter your height = ")) #in meter
weight = int(input("Enter your weight = "))  # in kilogram


BMI = round(weight/(height**2),3)
print(f"Body mass index is {BMI}")

if BMI<18.5:
    print("your are under weight")
elif BMI<25.0:
    print("your have a normal weight")
elif BMI<30.0:
    print("your are slightly overweight")
elif BMI<35.0:
    print("your are obese")
else:
    print("your are clinically obese")