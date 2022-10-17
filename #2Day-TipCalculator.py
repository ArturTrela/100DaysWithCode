# BMI Calculator

# Input value code below

print('Welcome to the tip calculator.')
bill = float(input('What was the total bill ? $'))
people = int(input('How many people to split the bill?'))
percent_tip = int(input('What percent tip would you like to give? 10,12, or 15 '))

# Math part of code

tip_as_percent = bill * percent_tip/100
tip_as_percent_head = tip_as_percent / people
to_pay = round((bill + tip_as_percent) / people, 2)
total_bill = bill + tip_as_percent
# Return value for user code

print(F"Each preson should pay : ${to_pay} , included tip {tip_as_percent_head}")
print(f'Total bill is {total_bill}, and included tip {tip_as_percent}')