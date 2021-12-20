from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# drinks_menu = Menu.get_items()
# menu_items = MenuItem.find_drink("")
money_machine = MoneyMachine()
my_menu = Menu()
coffee_machine = CoffeeMaker()
is_on = True

while is_on:
    options = my_menu.get_items()
    drinks_choice = str(input(f"Would you like a: {options}?"))
    if drinks_choice == "off":
        is_on = False
    elif drinks_choice == "report":
        coffee_machine.report()
        money_machine.report()
    elif my_menu.find_drink(drinks_choice) is None:
        print('\033[31mError. Please choose an available option.\033[m')
    else:
        beverage = my_menu.find_drink(drinks_choice)  # Encapsulates the result
        sufficient_resources = coffee_machine.is_resource_sufficient(beverage)  # TrueFalse result
        sufficient_money = money_machine.make_payment(beverage.cost)
        if sufficient_resources and sufficient_money:
            print('Done! Allow us to make your beverage now.')
            coffee_machine.make_coffee(beverage)
