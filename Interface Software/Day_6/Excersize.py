initial_amount = int(input("Enter the initial amount: "))

spend = {
    "rice": 120,
    "dal": 234,
    "fruits": 334,
}
def  addfun():
        key = input("enter the item name ")
        value  = int(input("Enter the amount"))
        spend[key] = value
while True:
    add = input("do you want to buy more? (y or n)")
    if add=="y":
        addfun()
    else:
        break
    

        
    
keys_str = ",".join(spend.keys())
print("You spend in this items : ", keys_str)

dis = True


while dis:
    decision = input("Do you want to see an item? (y or n): ")
    if decision.lower() == "y":
        item = input("Enter the item: ")
        if item in spend:
            print(f"{item} : {spend[item]}")
        else:
            print("Enter a valid item.")
    else:
        break

spend_list_keys = list(spend.keys())
spend_list_values = list(spend.values())

# print(spend_list_keys)
# print(spend_list_values)
total=0
for total in spend_list_values:
    thing = spend_list_values.pop()
    total+=thing
print("Total Spent:", total)
rest_amount = initial_amount - total

if rest_amount < 0:
    print("You spent more than your initial amount.")
    spend.
else:
    see_receipt = input("Do you want to see your receipt? (y or n): ")
    if see_receipt.lower() == "y":
        print("Receipt:")
        for item, price in spend.items():
            print(f"{item} : {price}")

