"""Project Coffee Machine from Udemy course #100DaysWithPython"""

# """Dodać aktualizację zasobów w maszynie po wykonaniu kawy"""
# """Poprawić błąd z próbą przypisania nastepnych składników gdy użyte jest off lub report"""

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
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
    "money": 0,
}
powerOn = 1


def report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]
    print(f'In machine remaining ... \nWater: {water} ml\nMilk: {milk} ml\nCoffee: {coffee} g\nMoney: $ {money}')


def spend_coins(user_coins, drink_cost):
    to_spend = user_coins - drink_cost
    print(f'Your rest of coins is {to_spend} PLN ')

    check_ingredients(resources)


def check_ingredients(resources):
    """Water , Milk , Coffee checking..."""
    next_water_amount = next_drink_ingredients['water']
    print(f' Your drink contains  {next_water_amount} ml of water ')

    next_coffee_amount = next_drink_ingredients['coffee']
    print(f' Your drink contains  {next_coffee_amount} g of coffee ')

    if operation_type(request) != 'espresso':
        next_milk_amount = next_drink_ingredients['milk']
        print(f' Your drink contains  {next_milk_amount} ml of milk ')

        if (resources['water'] > next_water_amount and resources['milk'] > next_milk_amount and resources['coffee'] >
                next_coffee_amount):
            print(f'Your coffee is preparing ! Please Wait')
            update_resources(next_water_amount , next_milk_amount , next_coffee_amount)

    elif resources['water'] > next_water_amount and resources['coffee'] > next_coffee_amount:

        next_milk_amount = 0
        print(f'Your coffee is preparing ! Please Wait')
        update_resources(next_water_amount , next_milk_amount , next_coffee_amount)

    else:
        print(f' Not enough ingredients to prepare your coffee ... ')
        print("Return coins... ")

    next_amount = [next_water_amount, next_milk_amount, next_coffee_amount]
    return next_amount


def coin_process(drink_cost):
    correct_cost = 0
    while not correct_cost:

        print('Please prepare coins to insert into machine ... ')

        dziesiec_groszy = int(input("How many 0.1PLN you have?  ")) * 0.1
        dwadziescia_groszy = int(input("How many 0.2PLN you have?   ")) * 0.2
        piecdziesiat_groszy = int(input("How many 0.5PLN you have?  ")) * 0.5
        zlotowka = int(input("How many 1 PLN you have?  ")) * 1.0
        dwa_zlote = int(input("How many 2 PLN you have? ")) * 2.0
        piec_zlotych = int(input("How many 5 PLN you have?  ")) * 5.0

        total_coins = dziesiec_groszy + dwadziescia_groszy + piecdziesiat_groszy + zlotowka + dwa_zlote + piec_zlotych
        print(f' You insert into machine : {total_coins} PLN')
        print(f' Your drink cost is : {drink_cost} PLN')

        if drink_cost == total_coins:
            correct_cost = 0
            check_ingredients(resources)
            return "ok"
        if drink_cost <= total_coins:
            correct_cost = 0
            spend_coins(total_coins, drink_cost)
            return "high"
        if drink_cost >= total_coins:
            print(f'Coins value to low please insert coins again ...')
        else:
            return "Counting cost still process .. "

    return total_coins


def update_resources(water, milk, coffee, ):

    resources['milk'] -= milk
    resources['water'] -= water
    resources['coffee'] -= coffee
    resources['money'] += MENU[to_make]['cost']
    print(resources)


while powerOn:
    request = input("What would you like? (espresso -Type 'e'/latte - Type 'l' /cappuccino - Type - 'c')\n ").lower()


    def operation_type(user_choice):
        """Take a coffee type from user."""

        if user_choice == 'e':
            # print('Espresso ...')
            return 'espresso'
        elif user_choice == 'l':
            # print('Latte ...')
            return 'latte'
        elif user_choice == 'c':
            # print('Cappuccino...')
            return 'cappuccino'
        elif user_choice == 'r':
            report()
            return 'report'
        elif user_choice == 'off':
            print('Shutdown ... preparing and report printing')
            report()
        # elif user_choice == 't':
        #     check_ingredients(resources)
        #     return 'test'
        else:
            print('Something went wrong ! Please type correct operation  type ')


    to_make = operation_type(request)
    if to_make == 'report' and to_make == 'off':
        print("Service statement")

    else:
        next_drink_ingredients = MENU[to_make]['ingredients']
        next_drink_cost = MENU[to_make]['cost']
        print(next_drink_ingredients)
        print(next_drink_cost)

    if operation_type(request) != "":
        coin_process(next_drink_cost)
