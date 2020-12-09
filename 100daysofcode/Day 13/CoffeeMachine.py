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

on = True
ingredient_sufficient = True
earned_money = 0.0
while on == True:
    print("Welcome to the Coffee Machine!")
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == "off":
        on = False
        break;
    elif user_input == "report":
        for resource in resources:
            print(f"{resource}: {resources[resource]}")
        print(f"money: ${earned_money}")
    else:
        coffee = MENU[user_input]
        for ingredient in coffee["ingredients"]:
            if resources[ingredient] < coffee["ingredients"][ingredient]:
                print(f"Sorry, there is not enough {ingredient}. Money refunded.")
                ingredient_sufficient = False
                break;
        if ingredient_sufficient:
            print(f"The {user_input} is ${coffee['cost']}. Insert coins.")
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickels = int(input("How many nickels?"))
            cents = int(input("How many cents?"))
            received_money = quarters*0.25 + dimes*0.1 + nickels*0.05 + cents*0.01;
            print(f"Received ${received_money}.")
            if received_money < coffee["cost"]:
                print("Sorry, that is not enough money; money refunded.")
            else:
                for ingredient in coffee["ingredients"]:
                    resources[ingredient] -= coffee["ingredients"][ingredient]
                earned_money += coffee["cost"]
                print(f"Here is your {user_input}.")
                if received_money > coffee["cost"]:
                    print(f"Here is your change ${round((received_money - coffee['cost']),2)}")

