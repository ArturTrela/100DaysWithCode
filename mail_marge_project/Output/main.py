"""manualy created file and structure cause source file from repo Udemy is in iOS coding"""

final_letter = []
new_names = []

with open("../Input/Names/invited_names.txt", "r") as invited:
    invite_names = invited.readlines()
    for name in invite_names:
        striped_name = name.strip()
        new_names.append(striped_name)
for name in new_names:
    with open("../Input/Letters/starting_letter.txt", "r") as letters:
        starting_letter = letters.read()

        final_letter = starting_letter.replace("[name]", name)
        print(final_letter)
        with open(f'./ReadyToSend/letter_for_{name}.txt', "w") as final:
            final.writelines(final_letter)
