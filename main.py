from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money = MoneyMachine()
menu = Menu()
coffe_maker = CoffeeMaker()

done = True
while done:
    drinks = menu.get_items()
    choice = input(f"what would u have?{drinks}")
    if choice == "off":
        done = False
    elif choice == "report":
        coffe_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffe_maker.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffe_maker.make_coffee(drink)



