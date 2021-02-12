lst = [int(item) for item in input().split()] 
n = int(input())

for i in range(len(lst)):
    if lst[i] == n:
        print(i + 1, end = " ")