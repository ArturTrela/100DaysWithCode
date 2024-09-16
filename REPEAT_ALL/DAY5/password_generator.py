import string
import random
print('Welcome in PyPassword Generator')
letters = list(string.ascii_letters)
chars = list('!@#$%^&*()_+-=[]{}|;:,.<>?/~`')
num = list(string.digits)
letters_to_pass =[]
chars_to_pass =[]
num_to_pass =[]
long = int(input('How letters will be your Password ?'))
chars_qty = int(input('How many special char ? '))
num_qty = int(input('how many numbers ?'))
your_pass=[]
for l in range(0,long):
    letters_to_pass.append(random.choice(letters))
for c in range(0,chars_qty):
    chars_to_pass.append(random.choice(chars))
for n in range(0,num_qty):
    num_to_pass.append(random.choice(num))

all_chars = num_to_pass + letters_to_pass + chars_to_pass
print(all_chars)
for x in range(0,len(all_chars)):
   your_pass.append(random.choice(all_chars))

password = ''.join(your_pass)
print(f'Your password is : {password}')