from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_mechine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

money_mechine.report()
coffee_maker.report()

while is_on:
    option = menu.get_items()
    choice = input(f"What would you like?{option}")
    
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_mechine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and print(money_mechine.make_payment(drink.cost)):
            coffee_maker.make_coffee(drink)
        
