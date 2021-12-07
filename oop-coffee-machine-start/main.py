import coffee_maker
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# drinks_menu = Menu.get_items()
# menu_items = MenuItem.find_drink("")
money_machine = MoneyMachine()
my_menu = Menu()
# my_menu_items = MenuItem()
my_coffee_machine = CoffeeMaker()
is_on = True


while is_on:
    options = my_menu.get_items()
    drinks_choice = input(f"Would you like a: + {options}?")
    if drinks_choice == "off":
        is_on = False
    elif drinks_choice == "report":
        my_coffee_machine.report()
        money_machine.report()
    else:
        drink = my_menu.find_drink(drinks_choice)
        if my_coffee_machine.is_resource_sufficient(drink):
            my_coffee_machine.make_coffee()
            money_machine.make_payment()







