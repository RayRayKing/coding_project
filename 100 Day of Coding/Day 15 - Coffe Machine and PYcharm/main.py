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


def check_resource(drink_type):
    """"Reports if enough resource to make drink.
    returns True if enough, otherwise false."""
    drink = MENU[drink_type]
    material = drink["ingredients"]
    for key, value in material.items():
        if resources[key] < value:
            print(f"Not enough {key}.")
            return False
        else:
            return True


def report():
    """Prints number of resource available"""
    print(f"Water: {resources['water']}ml\n"
          f"Milk: {resources['milk']}ml\n"
          f"Coffee: {resources['coffee']}g\n"
          f"Money: ${resources['money']}")


def check_coins(drink):
    """Check price against inserted coins."""
    price = MENU[drink]["cost"]
    if sum_coins > price:
        return True
    else:
        print("Sorry, that is not enough money. Money refunded.")
        return False


# to ask for input
resources['money'] = resources.get("money", 0)
is_on = True
while is_on:
    ans = input("What would you like to drink (espresso/latte/cappuccino)")
    if ans == "report":
        report()
    elif ans == "off":
        is_on = False
        exit()
    elif ans in MENU:
        # Ingredients check if enough
        pass_resource = check_resource(ans)
        milk_cost = MENU[ans]["ingredients"].get("milk", 0)
        water_cost = MENU[ans]["ingredients"].get("water", 0)
        coffee_cost = MENU[ans]["ingredients"].get("coffee", 0)
        money_cost = MENU[ans]["cost"]
        if pass_resource:
            # ask and check for coins
            print("Please insert coins.")
            quarter = int(input("How many quarters?: "))
            dime = int(input("How many dime?: "))
            nickle = int(input("How many nickle?: "))
            pennies = int(input("How many pennies?: "))
            sum_coins = (quarter * .25) + (dime * .10) + (nickle * .05) + (pennies * .01)
            pass_coins = check_coins(ans)

            # WRite function to process coins
            if pass_resource and pass_coins:
                resources["money"] += money_cost
                resources["water"] -= water_cost
                resources["milk"] -= milk_cost
                resources["coffee"] -= coffee_cost
                change = sum_coins - money_cost
                print(f"Here is ${round(change,2)} in change")
                print(f"Here is your {ans} ☕")
                