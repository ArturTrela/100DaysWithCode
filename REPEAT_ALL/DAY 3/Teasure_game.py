logo = """
         __________
        /\____;;___|
       | /         /
       `. ())oo() .
        |\(%()*^^()^|
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
      """
print(logo)
print('Welcome in Teasure Island -> Your mission is find teasure chest')
print('You are at crossroad type "R" if you want go to right side or type "L" if you want go to left side')
condition = True
user_guess = input("Where you go ? ").lower()
while condition:

    if user_guess == "l":
        print('You go to the left side')
        user_guess2 = input('Swim type "S" or "W" if you want wait').lower()
        if user_guess2 =="s":
            print('Attacked by trout.Game over')
            condition = False
        else:
            user_door = input('Wich door you choose : Red -"R" , Blue - "B" ,Yellow - "Y"')
            if user_door =="r":
                print('Burned in fire . Game over !')
                condition = False
            elif user_door =="b":
                print('Eaten by beast . Game over! ')
                condition = False
            elif user_door =="y":
                print("Congratulations You Won !")
            else:
                print('Game Over')
                condition = False
    elif user_guess == 'r':
        print('Fall into a hole . Game Over! ')
        condition =False
    else:
        print('Something went wrong -> Please type correct letter')