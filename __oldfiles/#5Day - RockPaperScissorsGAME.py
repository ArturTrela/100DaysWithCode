rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
import random

your_choice = int(input("what's your choice ? Rock - 0 , Paper - 1, Scissors- 2\n"))
if your_choice == 0:
    print(f'Your choice is {rock}')
if your_choice == 1:
    print(f'Your choice is {paper}')
if your_choice == 2:
    print(f'Your choice is {scissors}')

computer_choice = random.randint(0, 2)
print(computer_choice)
if computer_choice == 0:
    print(f"Computer choice is: " + (rock))
elif computer_choice == 1:
    print(f"Computer choice is " + (paper))
else:
    print(f"Computer choice is " + (scissors))

draw = "Draw, one again"
lose = "You lose..."
win = "You Win!!!"

# user choice -rock
if your_choice == 0 and computer_choice == 0:
    print(draw)
if your_choice == 0 and computer_choice == 1:
    print(lose)
if your_choice == 0 and computer_choice == 2:
    print(win)

# user choice paper
if your_choice == 1 and computer_choice == 0:
    print(win)
if your_choice == 1 and computer_choice == 1:
    print(draw)
if your_choice == 1 and computer_choice == 2:
    print(lose)

# user choice scissors
if your_choice == 2 and computer_choice == 0:
    print(lose)
if your_choice == 2 and computer_choice == 1:
    print(win)
if your_choice == 2 and computer_choice == 2:
    print(draw)