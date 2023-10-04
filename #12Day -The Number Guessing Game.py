from ASCIIart import logoNumberGuess
import random

print(logoNumberGuess)
print(f"Welcome to the Number Guessing Game \n I'm thinking about number in range from 1 to 100 \n"
      f"Please choice your difficulty : 'easy' or 'hard' :")

difficulty = input('Your difficulty level is : ')
attempts_qty = 0
if difficulty == 'easy':
    attempts_qty = 10
    print(f'OK! Your level is ' + difficulty)
elif difficulty == 'hard':
    attempts_qty = 5
    print(f'OK! Your level is ' + difficulty)
else:
    print(f'Something went wrong . Please insert correct level name ')

guessNumber = random.randint(1, 100)
inputValue = 0
while True:

    def numberguess(inputValue, guessNumber, attempts_qty,):
        t = 0
        if attempts_qty  > 0 or t == 1:
            inputValue = int(input(f'Make a guess :'))
            print(inputValue)
            print(guessNumber)
            if inputValue < guessNumber:
                print(f'To low. Remaining ' + str(attempts_qty) + ' attempts')
            elif inputValue > guessNumber:
                print(f'To high. Remaining ' + str(attempts_qty) + ' attempts')
            else:
                inputValue == guessNumber
                print(f'Correct! This number is : ' + str(inputValue))
                attempts_qty == 0

    attempts_qty = attempts_qty - 1
    numberguess(inputValue, guessNumber, attempts_qty,)
    print(f'Attempts : ' + str(attempts_qty))


