def isJoin(string):
    checker = "abcdefghijklmnopqrstuvwxyz"
    index = checker.find(string[0].lower())
    for letter in string:
        if letter.lower() != checker[index]:
            return False
        index += 1
    return True
    
string = input()
print(isJoin(string))