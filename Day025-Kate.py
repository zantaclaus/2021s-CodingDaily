def nPalindrome(number):
    count = 0
    i = 0
    while(1):
        i += 1
        string = str(i)
        if string == string[::-1]:
            count += 1
        if count == number:
            return i

resault = nPalindrome(432)
print(resault)