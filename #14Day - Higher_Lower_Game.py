from ASCIIart import logoHLG, vs
import game_data
from random import randint

print(logoHLG)
posA = 0
posB = 0
first_position_pointer = 0
second_position_pointer = 0
pointer_range = len(game_data.data)

###  Use random modul to choice second person to fight (maybe good practice will be close this  in function) ###

first_position_pointer = randint(0, pointer_range)
second_position_pointer = randint(0, pointer_range)
if first_position_pointer == second_position_pointer:
    second_position_pointer = second_position_pointer + randint(0, pointer_range)
elif second_position_pointer > len(game_data.data):
    second_position_pointer = 50

# HELPING PRINT TO SHOW ACTUAL POINTERS VALUE
print(first_position_pointer)
print(second_position_pointer)

 ### Create description about person located on posA or posB ###
for i in range(0, len(game_data.data)):
    if i == first_position_pointer:
        values = [game_data.data[i].values()]
        print(values)
for k in range(0, len(game_data.data)):
    if k == second_position_pointer:
        values2 = [game_data.data[k].values()]
        print(values2)



# Create point counter as variable named score
#  Create head mechanism of game in function game where player choice
#   that value is Higher or Lower. If answer is correct posB should be
#   switch to posA and next random person can be assigned to posB.
#  Create "VS" logo during comparsion import from ASCIIart module
#  If answer was wrong game should display Your Score and exit the game.
#   So player anser should be close in while loop.
