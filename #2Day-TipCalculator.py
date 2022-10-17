# BMI Calculator

# Input value code below

print('Welcome to the tip calculator.')
bill = float(input('What was the total bill ? $'))
people = int(input('How many people to split the bill?'))
percent = int(input('What percent tip would you like to give? 10,12, or 15 '))

# Math part of code

tip = bill % percent
to_pay = (bill + tip) / people

# Return value for user code

print(F"Each preson should pay : ${to_pay} , included tip {tip}")