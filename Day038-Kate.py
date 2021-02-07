message = input()
vowel = ['a','e','i','o','u','A','E','I','O','U']
text1 = []
text2 = []
count1 = 0
count2 = 0

for i in range(int(len(message)/2)):
    text1.append(message[i])

for i in range(int(len(message)/2), len(message)):
    text2.append(message[i])

for item in text1:
    for check in vowel:
        if item == check:
            count1 += 1

for item in text2:
    for check in vowel:
        if item == check:
            count2 += 1

if count1 == count2:
    print("true")
else:
    print("false")