# Keyword method with iterrows()
# {new_key:new_value for (index,row) in df.iterrows() }
import pandas
with open("nato_phonetic_alphabet.csv") as data:
    nato = pandas.read_csv(data)
    nato_dict = nato.to_dict()
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

phonetic = {row.letter:row.code for (index,row) in nato.iterrows()}

print(phonetic)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_letter = input('Tell me any sentence \n ' ).upper()

print(user_letter)
