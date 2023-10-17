# Pizza order Exercise

print('Welcome to Pizza Delivery')
size = input("Please choice your pizza size : S , M , L ")
add_pepperoni = input("Do you want pepperoni ? Y/N")
add_cheese = input("Do you want extra cheese  ? Y/N")
bill = 0
small_pizza_price = 15
medium_pizza_price = 20
large_pizza_price = 25
small_pizza_pepperoni = 2
med_larg_pizza_pepperoni = 3
extra_cheese = 1


if size.upper() == "S":
    bill = bill + small_pizza_price

    if add_pepperoni.upper() == "Y":
        bill = bill + small_pizza_pepperoni

    if add_cheese.upper() == "Y":
        bill = bill + extra_cheese


if size.upper() == "M":
    bill = bill + medium_pizza_price

    if add_pepperoni.upper() == "Y":
        bill = bill + med_larg_pizza_pepperoni

    if add_cheese.upper() == "Y":
        bill = bill + extra_cheese


if size.upper() == "L":
    bill = bill + large_pizza_price

    if add_pepperoni.upper() == "Y":
        bill = bill + med_larg_pizza_pepperoni

    if add_cheese.upper() == "Y":
        bill = bill + extra_cheese


print(f'Your final bill is: $ {bill}.')
