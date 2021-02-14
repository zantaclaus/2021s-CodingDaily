def compareTypeInString(string):
    upperCase = 0
    lowerCase = 0
    number = 0
    for word in string:
        if word.isupper():
            upperCase += 1
        elif word.islower():
            lowerCase += 1
        elif word.isnumeric():
            number += 1
    if upperCase > lowerCase and upperCase > number:
        return 1
    if lowerCase > upperCase and lowerCase > number:
        return 2
    if number > lowerCase and number > upperCase:
        return 3
    return 4

string = input()
print(compareTypeInString(string))