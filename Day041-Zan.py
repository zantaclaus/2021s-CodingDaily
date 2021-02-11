consonant = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
check = [0]*52

string = input()
string = string.lower()

for item in string:
    for i in range(52):
        if item == consonant[i]:
            check[i] += 1

for i in range(52):
    if check[i] != 0:
        print(consonant[i] , "=", check[i])