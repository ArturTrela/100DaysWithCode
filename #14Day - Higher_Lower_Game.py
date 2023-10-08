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


def creator_playerA(data):
    # pointer for table creating
    pointerA = random.randint(0, len(data) - 1)
    tempA = []
    for values in data[pointerA].values():
        tempA.append(values)

    positionA = f'A: {tempA[0]} as {tempA[2]} from {tempA[3]}'
    positionA_likes = tempA[1]
    creating_dataA = [positionA, positionA_likes]
    return creating_dataA


def creator_playerB(data):
    # pointer for table creating
    pointerB = random.randint(0, len(data) - 1)
    tempB = []
    for values in data[pointerB].values():
        tempB.append(values)

    positionB = f'B: {tempB[0]} as {tempB[2]} from {tempB[3]}'
    positionB_likes = tempB[1]
    creating_dataB = [positionB, positionB_likes]
    return creating_dataB


packageA = creator_playerA(data)
positionA = packageA[0]
positionA_likes = packageA[1]

packageB = creator_playerB(data)
positionB = packageB[0]
positionB_likes = packageB[1]


def game(positionA, positionB, data):

    condition = 1
    points_cnt = 0
    while condition == 1:
        positionB = packageB[0]
        print(f'{positionA}\n {vs} \n {positionB}')
        print('________________________________________________________________________________')

        user_choice = str(input('Please Type who has a more followers : "a" or "b" \n'))
        if user_choice == "a":
            print(f'Your choice is {user_choice}-> {positionA}')
            if positionA_likes > positionB_likes:
                print('TRUE')
                points_cnt += 1
                print(f'Your actual score is :{points_cnt}')
                positionA = positionB
                positionB = packageB[0]

        elif user_choice == "b":
            print(f'Your choice is {user_choice}->{positionB}')
            if positionB_likes > positionA_likes:
                print('TRUE')
                points_cnt += 1
                print(f'Your actual score is :{points_cnt}')
            else:
                print('FALSE')
                return points_cnt
        else:
            print('Something went wrong ... Please type correct position ')
            return

        print(f'{positionA_likes}k likes')
        print(f'{positionB_likes}k likes')


game_score = game(positionA, positionB, data)
# game()
print(f'Game over. Your Score is : {game_score}')
