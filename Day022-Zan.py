string = input()
n = int(input())

count = 0
for item in string:
    count += 1
    print(item, end="")
    if count == n:
        count =  0
        print("")