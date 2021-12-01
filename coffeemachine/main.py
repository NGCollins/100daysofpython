from resources import MENU, resources


def coffee_machine():
    users_coffee_choice = input("What would you like? (espresso/latte/cappuccino):")
    if users_coffee_choice == "espresso":
        espresso_cost = MENU.get("cost")


    elif users_coffee_choice == "off":
        return
    elif users_coffee_choice == "report":
        water_amount = resources.get("water")
        print(water_amount)


coffee_machine()
