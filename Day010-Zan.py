string = []
lst = []
for i in range(0,3):
    string.append(input())
    lst.append(len(string[i]))

lst.sort(reverse = True)
for i in range(0,3):
    for j in range(0,3):
        if lst[i] == len(string[j]):
            print("Lenght" , lst[i] , ":" , string[j])

