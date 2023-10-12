from ASCIIart import logoHLG, vs
import game_data
import random

# # Create point counter as variable named score
# #  Create head mechanism of game in function game where player choice
# #   that value is Higher or Lower. If answer is correct posB should be
# #   switch to posA and next random person can be assigned to posB.
# #  Create "VS" logo during comparsion import from ASCIIart module
# #  If answer was wrong game should display Your Score and exit the game.
# #   So player anser should be close in while loop.

# variable declaration

pointerA = 0
pointerB = 0
positionA = ""
positionB = ""
positionA_likes = 0
positionB_likes = 0
print(logoHLG)
data = game_data.data

print(positionB)

def creator_playerA(data):
    # pointer for table creating
    pointerA = random.randint(0, len(data) - 1)
    tempA = []
    for values in data[pointerA].values():
        tempA.append(values)

    positionA = f' {tempA[0]} as {tempA[2]} from {tempA[3]}'
    positionA_likes = tempA[1]
    creating_dataA = [positionA, positionA_likes]
    return creating_dataA


def creator_playerB(data):
    # pointer for table creating
    pointerB = random.randint(0, len(data) - 1)
    tempB = []
    for values in data[pointerB].values():
        tempB.append(values)

    positionB = f' {tempB[0]} as {tempB[2]} from {tempB[3]}'
    positionB_likes = tempB[1]
    creating_dataB = [positionB, positionB_likes]
    return creating_dataB

#
packageA = creator_playerA(data)
positionA = packageA[0]
positionA_likes = packageA[1]

packageB = creator_playerB(data)
positionB = packageB[0]
positionB_likes = packageB[1]
print(f'A:{positionA}\n {vs} \n B: {positionB}')

def game(data):
    points_cnt = 0
    packageA = creator_playerA(data)
    positionA = packageA[0]
    positionA_likes = packageA[1]


    while True:
        packageB = creator_playerB(data)
        positionB = packageB[0]
        def show_enemies():
            print(f'A:{positionA}\n {vs} \n B: {positionB}')
            print('________________________________________________________________________________')
        print(f'A: {positionA_likes}k likes')
        print(f'B: {positionB_likes}k likes')


        user_choice = str(input('Please Type who has a more followers : "a" or "b" \n')).lower()
        if user_choice == "a" and positionA_likes > positionB_likes or user_choice =="b" and positionB_likes > positionA_likes:

            print('TRUE')
            points_cnt += 1
            print(f'Your actual score is :{points_cnt}')
            positionA = positionB
            packageB =creator_playerB(data)
            print(positionB)

        else:
            print('FALSE')
            return points_cnt
        show_enemies()
    else:
        print('Something went wrong ... Please type correct position ')
    clear()




game_score = game(data)
print(f'Game over. Your Score is : {game_score}')
