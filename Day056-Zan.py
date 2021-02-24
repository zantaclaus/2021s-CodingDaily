def findNotAlphabet(str1, str2):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lst1 = []
    lst2 = []
    for letter in str1:
        if letter not in alphabet:
            lst1.append(letter)
    for letter in str2:
        if letter not in alphabet:
            lst2.append(letter)
    if len(lst1) > len(lst2):
        return lst1
    return lst2

str1 = input()
str2 = input()
print(findNotAlphabet(str1,str2))