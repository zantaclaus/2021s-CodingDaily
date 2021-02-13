def sortString(string):
    ans = ""
    for letter in string:
        if letter.isupper():
            ans += letter
    for letter in string:
        if letter.islower():
            ans += letter
    return ans

string = input()
print(sortString(string))
    

