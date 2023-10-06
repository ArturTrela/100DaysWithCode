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
def_answer = 0


def numberguess(guessNumber, attempts_qty, ):
    """ Head function of this game where input user's number is compare with
    hidden number choice from range 1 to 100 """
    while attempts_qty != 0:
        inputValue = int(input(f'Make a guess :'))
        # print(inputValue)
        # print(guessNumber)
        if inputValue < guessNumber:
            print(f'To low.')
        elif inputValue > guessNumber:
            print(f'To high.')
        else:
            inputValue == guessNumber
            print(f'Correct! This number is : ' + str(inputValue))
            attempts_qty == 0
            return
        attempts_qty = attempts_qty - 1
        print(f'Remaining attempts : {attempts_qty}')

        if attempts_qty == 0:
            print("You lose. Try again ")

numberguess(guessNumber, attempts_qty,)


