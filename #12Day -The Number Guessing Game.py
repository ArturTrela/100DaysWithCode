from ASCIIart import logoNumberGuess
import random
#TODO correct display ASCII art LOGO or change type logo
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
condition = 1
while attempts_qty != 0:
      #TODO correct decrese value for attempts_qty
    def numberguess(inputValue, guessNumber, attempts_qty, condition):
          #TODO - remove additional print statments for clean code
          if attempts_qty > 0:
              inputValue = int(input(f'Make a guess :'))
              print(inputValue)
              if inputValue < guessNumber:
                  attempts_qty -= 1
                  print(guessNumber)
                  print(f'To low. Remaining ' + str(attempts_qty) + 'attempts')
              elif inputValue > guessNumber:
                  attempts_qty -= 1
                  print(guessNumber)
                  print(f'To high. Remaining ' + str(attempts_qty) + 'attempts')
              else:
                  print(f'Correct! This number is : ' + str(inputValue))
                  attempts_qty == 0
          else:
                #TODO - modified condition for while loop when guess number is correct - maybe use return from function or other\n
                # check documentation about return result from function
                condition = False

    numberguess(inputValue, guessNumber, attempts_qty,condition)
