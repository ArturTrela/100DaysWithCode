# Keyword method with iterrows()
# {new_key:new_value for (index,row) in df.iterrows() }
import pandas

with open("nato_phonetic_alphabet.csv") as data:
    nato = pandas.read_csv(data)
    nato_dict = nato.to_dict()

phonetic = {row.letter: row.code for (index, row) in nato.iterrows()}


def generate_phonetic():
    user_letter = input('Tell me any sentence \n ').upper()

    try:
        user_letter_list = [phonetic[l] for l in user_letter]
    except KeyError:
        print("Only letters in alphabet \n")
        generate_phonetic()
    else:
        print(user_letter_list)


generate_phonetic()
