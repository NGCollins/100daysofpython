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

COINS = {"quarters": 0.25, "dimes": 0.10, "nickels": 0.05, "pennies": 0.01}


def remove_resouces(resource_key,drink):
    resources[resource_key] =-MENU[drink]["ingredients"][resource_key]



def resource_check(drink):
    for keys in MENU[drink]["ingredients"].keys():
        if MENU[drink]["ingredients"][keys] <= resources[keys]:
            remove_resources(keys,drink)
            return True
        else:
            print(f"Sorry, there is not enough {keys}")


def take_money(drink):
    money_amount_collected = 0
    money_amount_inserted = 0
    quarters_amount = input("How many Quarters?") * COINS["quarters"]
    nickels_amount = input("How many Nickels?")  * COINS["nickels"]
    dimes_amount = input("How many Dimes?") * COINS["dimes"]
    pennies_amount = input("How many Pennies?") * COINS["pennies"]
    money_amount_inserted = quarters_amount + dimes_amount + nickels_amount + pennies_amount
    drink_cost = MENU[drink]["cost"]
    if resource_check(drink):
        if money_amount_inserted < drink_cost:
            print(f"Sorry that's not enough money. Money refunded.")
        else:
            money_amount_collected =+ money_amount_inserted
            print("here is you espresso please enjoy! ☕")

            if money_amount_inserted > drink_cost:
                # TODO need to implement feature for figuring out which coins to return using modula
                change = money_amount_inserted - drink_cost
                print(f"Please take your change. {change}")


def make_drink(drink):
    print("Please insert coins.")
    coffee_requirements = MENU[drink]["ingredients"]['coffee']
    water_requirements = MENU[drink]["ingredients"]['water']
    if drink == "espresso":
        milk_requirements = 0
    else:
        milk_requirements = MENU[drink]["ingredients"]['milk']
    take_money(drink)


# TODO number 2 check resources sufficient to make drink order

def coffee_machine():
    water_amount_left = resources['water']
    milk_amount_left = resources['milk']
    coffee_amount_left = resources['coffee']
    money_amount_collected = 0
    money_amount_inserted = 0
    users_coffee_choice = input("What would you like? (espresso/latte/cappuccino):")
    # TODO need generic function for that handles whatever drink
    if users_coffee_choice == "espresso":
        espresso_cost = MENU['espresso']["cost"]
        print("Please insert coins.")
        # TODO  number 3 make a check resource function
        coffee_requirements = MENU['espresso']["ingredients"]['coffee']
        water_requirements = MENU['espresso']["ingredients"]['water']
        milk_requirements = MENU['espresso']["ingredients"]['milk']
        # if milk_requirements is not None:
        #     print(f"{milk_requirements}")
        # else:
            milk_requirements = 0
        quarters_amount = input("How many Quarters?")
        nickels_amount = input("How many Nickels?")
        dimes_amount = input("How many Dimes?")
        pennies_amount = input("How many Pennies?")
        money_amount_inserted = quarters_amount + dimes_amount + nickels_amount + pennies_amount
        resource_check(coffee_requirements, coffee_amount_left, "Coffee")
        resource_check(water_requirements, water_amount_left, "Water")
        if money_amount_inserted < espresso_cost:
            print(f"Sorry that's not enough money. Money refunded.")
        elif money_amount_inserted == espresso_cost:
            print("here is you espresso please enjoy! ☕")
        else:
            # TODO make function that handles subtracting order from stock
            water_amount_left = -water_requirements
            coffee_amount_left = - coffee_requirements
            money_amount_collected = + money_amount_inserted
            print("here is you espresso please enjoy! ☕")
            if money_amount_inserted > espresso_cost:
                # TODO need to implement feature for figuring out which coins to return using modula
                change = money_amount_inserted - espresso_cost
                print(f"Please take your change. {change}")


    elif users_coffee_choice == "off":
        return
    elif users_coffee_choice == "report":

        print(
            f"Water: {water_amount_left}ml\nMilk: {milk_amount_left}ml\nCoffee: {coffee_amount_left}g\nMoney: ${money_amount_collected}")


coffee_machine()
