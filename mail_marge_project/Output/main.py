"""manually created file and structure cause source file from repo Udemy is in iOS coding"""

starting_letter = []
invite_names = []
final_letter = []
with open("../Input/Letters/starting_letter.txt", "r") as letters:
    for row in letters:
        starting_letter.append(row)


with open("../Input/Names/invited_names.txt", "r") as invited:
    for row in invited:
        invite_names.append(row)




for i in range(0 ,len(invite_names)-1):
    with open(f'invited_{invite_names[i]}.txt', "w") as final:
        final_letter = starting_letter
        header = final_letter[0].replace("[name]",invite_names[i])
        starting_letter.insert(0,header)
        starting_letter.pop(1)





print(header)
print(invite_names)
print(final_letter)