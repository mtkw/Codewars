# Move the first letter of each word to the end of it,
# then add "ay" to the end of the word. Leave punctuation marks untouched.

def pig_it(text):
    words = text.split(' ')
    sufix = 'ay'
    new_word = ''
    final_sent = ''
    counter = 0
    for word in words:
        if len(word) >= 1 and word != '?' and word != '!':
            first_letter = word[0]
            new_word += word[1:len(word)] + first_letter + sufix
        elif len(word) == 1:
            new_word += word
        new_word += ' '
        final_sent = new_word[0:len(new_word) -1]

    return final_sent


print(pig_it("Dura lex sed lex"))

