import string

def rot13(message):
    english_lower = 'abcdefghijklmnopqrstuvwxyz'
    english_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    english_letters_lower = {}
    letters_position_lower = {}
    english_letters_upper = {}
    letters_position_upper = {}
    hash_string = ''

    for counter, value in enumerate(english_lower):
        english_letters_lower[value] = counter
        letters_position_lower[counter] = value
    for counter, value in enumerate(english_upper):
        english_letters_upper[value] = counter
        letters_position_upper[counter] = value

    for i in range(len(message)):
        letter = message[i]
        if letter in english_letters_lower:
            position = english_letters_lower.get(letter) + 13
            if(position >= len(english_letters_lower)):
                absolute_position = position - len(english_letters_lower)
                hash_string += letters_position_lower.get(absolute_position)
            else:
                hash_string += letters_position_lower.get(position)
        elif letter in english_letters_upper:
            position = english_letters_upper.get(letter) + 13
            if (position >= len(english_letters_upper)):
                absolute_position = position - len(english_letters_upper)
                hash_string += letters_position_upper.get(absolute_position)
            else:
                hash_string += letters_position_upper.get(position)
        else:
            hash_string += message[i]

    return hash_string




print(rot13("aA bB zZ 1234 *!?%"))

