import random
life0= '''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
_____|___
'''
life1 = '''
   _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
_____|___
'''
life2 = '''
   _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
_____|___
'''
life3 ='''
   _______
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
_____|___
'''
life4 = '''
   _______
     |/      |
     |      (_)
     |      \|
     |       
     |      
     |
_____|___
'''
life5 = '''
   _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
_____|___
'''
life6 =
letters =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

word=str(input("Tell me any word: ... \n")).lower()
long_word = len(word)
word_to_check = []

for x in range(0,long_word):
    word_to_check.append(word[x])

your_letter