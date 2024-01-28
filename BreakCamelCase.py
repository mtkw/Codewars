import re
def solution(s):
    new_string = ''
    for i in range(0, len(s)):
        if re.search('[A-Z]', s[i]) and i != 0:
            new_string += ' ' + s[i]
        else:
            new_string += s[i]
    return new_string

print(solution("TestString"))