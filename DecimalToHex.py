def rgb(r, g, b):
    digits = [r,g,b]
    hexadecimal = ''
    for i in range(0, len(digits)):
        if(digits[i] >= 17 and digits[i] <= 255):
            temp = hex(digits[i])
            hexadecimal += temp[2:len(temp)]
        elif (digits[i] < 0):
            hexadecimal += '00'
        elif (digits[i] > 255):
            hexadecimal += 'FF'
        elif digits[i] == 0:
            hexadecimal += '00'
        else:
            temp = hex(digits[i])
            hexadecimal += '0' +temp[2:len(temp)]
    return hexadecimal.upper()
    pass

# test = hex(255)
# print(test[2:len(test)])

print(rgb(1,3,5))