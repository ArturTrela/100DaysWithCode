import random
rock_asci = """
 
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
       """
paper_asci = '''         ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'   '''
scissors_asci = """
    _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\."""
z = [rock_asci,paper_asci,scissors_asci]
while True :
    user_guess = int(input('What you choose : 0 for rock , 1 for paper , 2 for scissors '))
    print(f' Your choice is : {z[user_guess]}')
    computer_choice = random.randint(0,2)
    print(f' Computer  choice is : {z[computer_choice]}')
    # if user_guess == 0 :
    #     print('Your choice is : ROCK')
    #     print(rock_asci)
    # elif user_guess == 1:
    #     print('Your choice is : PAPER')
    #     print(paper_asci)
    # elif user_guess == 2 :
    #     print('Your choice is : SCISSORS')
    #     print(scissors_asci)2

    if (user_guess == 0 and computer_choice == 0 ) or (user_guess == 1 and computer_choice == 1 )or (user_guess == 2 and computer_choice == 2):
        print('DRAW ! ')
    elif (user_guess == 0 and computer_choice ==2) or(user_guess==1 and computer_choice==0)or (user_guess==2 and computer_choice==1):
        print('You Win ')
    else:
        print('You loose')
