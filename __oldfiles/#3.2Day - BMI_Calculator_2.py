#BMI CALCULATOR V2.0

weight=float(input("Write your weight in kg"))
height=float(input('Write your height in m '))

bmi = (weight / (height**2))
new_bmi = int(round(bmi ,0))


# < 18.5 they are underweight
# > 18.5 < 25 they are normal weight
# > 25 < 30 they are overweight
# > 30 < 35 they are obese
# > 35 they are clinically obese

if new_bmi < 18.5:
    print(f'Your BMI is {new_bmi}, you are underweight.')
elif new_bmi < 25:
    print(f'Your BMI is {new_bmi}, you have a normal weight.')
elif new_bmi < 30:
    print(f'Your BMI is {new_bmi}, you are slightly overweight.')
elif new_bmi < 35:
    print(f'Your BMI is {new_bmi}, you are obese.')
else:
    print(f'Your BMI is {new_bmi}, you are clinically obese')