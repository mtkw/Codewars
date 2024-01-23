# WORK IN PROGRESS

decode = {".-": "A",
          "-...": "B",
          "-.-.": "C",
          "-..": "D",
          ".": "E",
          "..-.": "F",
          "--.": "G",
          "....": "H",
          "..": "I",
          ".---": "J",
          "-.-": "K",
          ".-..": "L",
          "--": "M",
          "-.": "N",
          "---": "O",
          ".--.": "P",
          "--.-": "Q",
          ".-.": "R",
          "...": "S",
          "-": "T",
          "..-": "U",
          "...-": "V",
          ".--": "W",
          "-..-": "X",
          "-.--": "Y",
          "--..": "Z",
          "-----": "0",
          ".----": "1",
          "..---": "2",
          "...--": "3",
          "....-": "4",
          ".....": "5",
          "-....": "6",
          "--...": "7",
          "---..": "8",
          "----.": "9",
          "--..--": ",",
          ".-.-.-": ".",
          "..--..": "?",
          "-..-.": "/",
          "-....-": "-",
          "-.--.": "(",
          "-.--.-": ")",
          "---...": ":",
          "...---...": "SOS",
          "... --- ...": "SOS",
          "-.-.--": "!",
          ".-...": "&",
          "...-..-": "$",
          "-.-.-.": ";",
          "-...-": "=",
          ".--.-.": "@",
          ".-..-.": '"',
          ".-.-.": "+",
          ".----.": "'",
          "..--.-": "_"
}

def decode_morse(morse_code):
    chars = morse_code.split(" ")
    natural_language = ''
    final_sentence = ''
    only_one_space = False
    for letter in chars:
        if len(letter) != 0:
            for key in decode:
                if letter == key:
                    natural_language += decode.get(key)
            only_one_space = True
        elif len(letter) == 0 and only_one_space == True:
            natural_language += " "
            only_one_space = False
    if natural_language[len(natural_language) - 1] == " ":
        final_sentence = natural_language[:-1]
        return final_sentence
    else:
        final_sentence = natural_language
        return final_sentence
    pass

test_word = "Sprawdzam możliwość dzielenia za pomocą spacji"
test_morse_code = '      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  '
# test_morse_code = '.-... ---...   -..-. --...'
print(decode_morse(test_morse_code))


