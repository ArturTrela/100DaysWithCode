# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
import random

# print(names)
qty_names = len(names)

# print(f'Actual qty elemnets {qty_names}')
who_pay_index = random.randint(0, qty_names-1)
print(f'{names[who_pay_index]}, paying the bill')




