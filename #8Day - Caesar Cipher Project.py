alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

text = input('Write text to encryption : \n').lower()
shift = int(input('Write how many time shift : \n'))
direction = input("Type 'enco' if you want encryption or 'deco' if decryption : ").lower()


def ceasar_cipers(text, shift, direction):
    temp_word = ''
    for letter in text:
        position = alphabet.index(letter)
        if direction == "enco":
            new_position = int(position) + shift
            temp_word += alphabet[new_position]
        #   print(f'Your text after encryption is :\n {temp_word}')

        elif direction == "deco":
            new_position = int(position) - shift
            temp_word += alphabet[new_position]
        #   print(f'Your text after decryption is :\n {decryption_word}')

    print(f'Your {direction} new word is : {temp_word}')

ceasar_cipers(text=text, shift=shift, direction=direction)