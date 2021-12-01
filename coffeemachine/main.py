MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

COINS = {"quarter": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}


def resource_check(resource_order, resource_stock, resource):
    if resource_order < resource_stock:
        print(f"Sorry, there is no a not {resource}")


# TODO number 2 check resources sufficient to make drink order

def coffee_machine():
    water_amount_left = resources['water']
    milk_amount_left = MENU['milk']
    coffee_amount_left = MENU['coffee']
    money_amount_collected = 0
    money_amount_inserted = 0
    users_coffee_choice = input("What would you like? (espresso/latte/cappuccino):")
    # TODO need generic function for that handles whatever drink
    if users_coffee_choice == "espresso":
        espresso_cost = MENU['espresso']["cost"]
        print(espresso_cost)
        # TODO  number 3 make a check resource function
        coffee_requirements = MENU['espresso']["ingredients"]['coffee']
        water_requirements = MENU['espresso']["ingredients"]['water']
        print(f"{coffee_requirements} {water_requirements}")
        resource_check(coffee_requirements, coffee_amount_left, "Coffee")
        resource_check(water_requirements, water_amount_left, "Water")
        if money_amount_inserted < espresso_cost:
            print(f"Sorry that's not enough money. Money refunded.")
        else:
            # TODO make function that handles subtracting order from stock
            water_amount_left = -water_requirements
            coffee_amount_left = - coffee_requirements
            money_amount_collected = + money_amount_inserted
            print("here is you drink please enjoy")
            if money_amount_inserted > espresso_cost:
                # TODO need to implement feature for figuring out which coins to return using modula
                print("Please take your change.")


    elif users_coffee_choice == "off":
        return
    elif users_coffee_choice == "report":

        print(
            f"Water: {water_amount_left}ml\nMilk: {milk_amount_left}ml\nCoffee: {coffee_amount_left}g\nMoney: ${money_amount_collected}")


coffee_machine()
