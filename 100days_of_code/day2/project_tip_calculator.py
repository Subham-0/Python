print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? ₹"))
percentage = float(input("what percentage tip would you like to give ? 10, 12 or 15 ?"))
tip = (total_bill*percentage)/100
total_bill+=tip
people = int(input("How many people to split the bill ? "))
per_person = total_bill/people
# amount = round(per_person,2)
amount = "{:.2f}".format(per_person)

print(f"Each person should pay: ₹{amount}" )

