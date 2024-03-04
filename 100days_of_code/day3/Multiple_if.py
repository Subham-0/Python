print("Welcome to the rollercoaster!")
height = int(input("what is your height in cm?"))
amount = 0
if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("enter your age"))
    if age<12:
        amount=5
        print(f"Child tickets are ₹{amount}")
    elif age<=18:
        amount=7
        print(f"Youth tickets are ₹{amount}")
    else:
        amount=12
        print(f"Adult tickets are ₹{amount}")
    take_photo = input("Do you want to take a photo? Y or N. ")
    if take_photo=="Y":
        amount+=3
        print(f"Your total amount is ₹{amount}")
    if take_photo=="N"
        print(f"Your total amount is ₹{amount}")
else:
    print("Sorry, you have grow taller before you can ride.")