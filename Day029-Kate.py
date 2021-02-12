word1 = [item for item in input().split()]
word2 = [item for item in input().split()]

lst1 = []
lst2 = []
for word in word1:
    for char in word:
        lst1.append(char)

for word in word2:
    for char in word:
        lst2.append(char)

if(lst1 == lst2):
    print("true")
else:
    print("false")