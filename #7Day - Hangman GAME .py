import random

title = '''

_                                            

| |                                           

| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __ 

| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \

| | | | (_| | | | | (_| | | | | | | (_| | | | |

|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|

                    __/ |                     

                   |___/   



'''

life_0 = '''

      _______

     |/      |

     |      (_)

     |      \|/

     |       |

     |      / \

     |

____|___

'''

life_1 = '''

      _______

     |/      |

     |      (_)

     |      \|/

     |       |

     |      /

     |

____|___

'''

life_2 = '''

      _______

     |/      |

     |      (_)

     |      \|/

     |       |

     |     

     |

____|___

'''

life_3 = '''

      _______

     |/      |

     |      (_)

     |      \|/

     |     

     |     

     |

____|___

'''

life_4 = '''

      _______

     |/      |

     |      (_)

     |      \|

     |      

     |     

     |

____|___

'''

life_5 = '''

      _______

     |/      |

     |      (_)

     |       |

     |      

     |     

     |

____|___

'''

life_6 = '''

      _______

     |/      |

     |      (_)

     |     

     |      

     |     

     |

____|___

'''

life_7 = '''

      _______

     |/      |

     |     

     |     

     |      

     |     

     |

____|___

'''


def actual_life_visualisation():
    if life_qty == 7:
        print(life_7)

    if life_qty == 6:
        print(life_6)

    if life_qty == 5:
        print(life_5)

    if life_qty == 4:
        print(life_4)

    if life_qty == 3:
        print(life_3)

    if life_qty == 2:
        print(life_2)

    if life_qty == 1:
        print(life_1)

    if life_qty == 0:
        print(life_0)


random_word = ['słońce,', 'chmura', 'deszcz', 'pokój', 'dom', 'automatyk', 'mistrz', 'mechanik', ]
qty_words = len(random_word)
hiden_word_pointer = random.randint(0, qty_words - 1)
check_word = random_word[hiden_word_pointer]
qty_letters = len(check_word)
blank_word = []
your_letter = ""
check_word_elements = []
life_qty = 8
empty_slot = 0
letter_not_exist = 0

for x in range(0, qty_letters):
    check_word_elements.append(check_word[x])
    blank_word.append("X")

empty_slot = blank_word.count("X")

print(title)
print(f'Word for you :\n {blank_word}\n')
condition = True

if empty_slot == 0 or life_qty == 0:
    condition = False
# Input user letter

while condition:
    your_letter = str(input('Your letter is : \n')).lower()
    letter_not_exist = 0
    for y in range(0, qty_letters):
        if your_letter == check_word_elements[y]:
            blank_word.pop(y)
            blank_word.insert(y, your_letter)
            empty_slot -= 1
        else:
            letter_not_exist += 1
        if letter_not_exist == qty_letters:
            print('Ta litera nie występuje , tracisz życie :')
            life_qty -= 1

    user_letters = []
    actual_life_visualisation()

    # print(f'if letter_not_exist {letter_not_exist} == qty_letters:{qty_letters}')

    print(blank_word)

    if empty_slot == 0 and life_qty != 0:
        print("YOU WIN !!!")

    if empty_slot != 0 and life_qty == 0:
        print("You LOSE ...")
        condition = False