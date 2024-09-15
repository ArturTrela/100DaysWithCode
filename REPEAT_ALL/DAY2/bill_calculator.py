print('Welcome in bill calculator')
bill = float(input('What was a total bill $'))
tip = int(input("How many tip You would like to give 10 12 or 15? "))
people = int(input("how many people split bill ? "))

cost = (bill + (bill*tip/100))/people

print (f'Each person should pay {cost} $')