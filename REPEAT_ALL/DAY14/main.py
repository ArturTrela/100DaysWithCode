"""
1. Print report
2. Check resources sufficient
3. Process coins
4. Check transaction successful
5. Make Coffe """
# logo = """
#    _____       __  __            __  __            _     _
#   / ____|     / _|/ _|          |  \/  |          | |   (_)
#  | |     ___ | |_| |_ ___  ___  | \  / | __ _  ___| |__  _ _ __   ___
#  | |    / _ \|  _|  _/ _ \/ _ \ | |\/| |/ _` |/ __| '_ \| | '_ \ / _ |
#  | |___| (_) | | | ||  __/  __/ | |  | | (_| | (__| | | | | | | |  __/
#   \_____\___/|_| |_| \___|\___| |_|  |_|\__,_|\___|_| |_|_|_| |_|\___|
#
#
# """

# print(logo)

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
            "milk": 100,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappucino": {
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
profit = 0
def is_resource_sufficient(order_ingredients):
    """ Return True when order can be made , False if ingredients are not enough"""
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f'Sorry there not enough {item}')
            return False
    return True

def coin_process():
    """ Return total calculated coins as value"""
    print('Please insert the coins :')
    total = int(input('How many quarters ?:'))*0.25
    total += int(input('How many dimes ?:')) * 0.10
    total += int(input('How many nickles ?:')) * 0.05
    total += int(input('How many pennies ?:')) * 0.01
    return total


def report():
    print(f'Water: {resources['water']}ml')
    print(f'Milk: {resources['milk']}ml')
    print(f'Coffee: {resources['coffee']}g')
    print(f'Money: ${profit}')


def cashback():
    user_cashback = payment - drink["cost"]
    print(f'{user_cashback}$ This is your cashback')

def refill():
    resources["water"] = 500
    resources["milk"] = 500
    resources["coffee"] = 100
    print("Refilling complete ")

def sub_ingredients(order_ingredients):
    for i in order_ingredients:
        resources[i] -= order_ingredients[i]


is_on = True
while is_on:
    user_guess = input("What would you like ? espresso/latte/cappucino : ")
    # if user_guess in MENU or user_guess =="report" or user_guess =="off":
    #     is_on = False

    if user_guess == 'off':
        is_on = False
        print("Machine shutdown ....")
    elif user_guess == "report":
        report()
    elif user_guess =='refill':
        refill()
    else:
        drink = MENU[user_guess]
        if is_resource_sufficient(drink["ingredients"]):
            payment = coin_process()
            print(f'{payment}$')
            if payment > drink["cost"]:
                print('This is your coffee')
                cashback()
                profit += drink["cost"]
                sub_ingredients(drink["ingredients"])
                report()

            else:
                print('Not enough money')


