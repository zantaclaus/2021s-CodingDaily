string = input()
check = False

for char in string:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' :
        check = True
        
if check:
    print("Vowel")
else:    
    print("NO Vowel")