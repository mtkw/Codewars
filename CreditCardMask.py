#Usually when you buy something, you're asked whether your credit card number,
# phone number or answer to your most secret question is still correct. However,
# since someone could look over your shoulder, you don't want that shown on your screen.
# Instead, we mask it.

# Your task is to write a function maskify, which changes all but the
# last four characters into '#'.

def maskify(cc):
    new_word = ''
    if len(cc) == 0:
        return new_word
    elif len(cc) > 0 and len(cc) <= 4:
        for char in cc:
            new_word += char
        return new_word
    else:
        for char in range(0, len(cc)):
            if char < len(cc) - 4:
                new_word += '#'
            else:
                new_word += cc[char]
        return new_word
    pass


print(maskify('ghost'))

