# Day4 - LOVE Calculator

name1 = input('What is your name ? : \n').lower()
name2 = input('What is their name ? : \n ').lower()

combined_names = name1 + name2
t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")

true_sum = t + r + u + e

l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e1 = combined_names.count("e")

love_sum = l + o + v + e1
love_score = str(true_sum) + str(love_sum)
new_love_score = int(love_score)

print(f'Love Score {new_love_score}')

if new_love_score < 10 and new_love_score > 90 :
    print(f'Your score is{new_love_score} , you go togehter like cola and mentos.')
elif new_love_score >= 40 and new_love_score <= 50 :
    print(f'Your score is {new_love_score} , you are alright togehter.')
else:
    print(f'Your score is {new_love_score}.')