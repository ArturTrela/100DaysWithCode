"""manualy created file and structure cause source file from repo Udemy is in iOS coding"""

starting_letter = []
invite_names = []

with open("../Input/Letters/starting_letter.txt", "r") as letters:
    for row in letters:
        starting_letter.append(row)

print(starting_letter)

with open("../Input/Names/invited_names.txt", "r") as invited:
    for row in invited:
        invite_names.append(row)

# print(invite_names)
# print(starting_letter)
