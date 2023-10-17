from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


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

is_On = True
""" Creating object from Class"""
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

""" Check resources  sufficient """
while is_On:
    options = menu.get_items()
    choice = input(f"What would you like? {options}")
    if choice == 'off':
        is_On = False
    elif choice == 'report':
        """Printing reports from object """
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            # money_machine.make_payment(drink.cost)
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

