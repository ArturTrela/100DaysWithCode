# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password_long = nr_letters + nr_symbols + nr_numbers
password = []

for char in range(0, password_long):
    if char in range(0, nr_letters):
        random_letter = random.randint(0, len(letters)-1)
        password.append(letters[random_letter])

    elif char in range(nr_letters, nr_letters+nr_numbers):
        random_number = random.randint(0, len(numbers)-1)
        password.append((numbers[random_number]))

    elif char in range(nr_letters+nr_numbers, password_long):
        random_symbol = random.randint(0, len(symbols)-1)
        password.append(symbols[random_symbol])

print(f'Your new password is :'+''.join(password))


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

new_password_hard: random.shuffle(password)
print(f'ZAMIESZAJMY TROCHĘ:' + ''.join(password))