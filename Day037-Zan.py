n = int(input())
lst = [int(item) for item in input().split()]
lst.sort()

print(lst[0], end=" ")
for i in range(1, len(lst)):
    if(lst[i] != lst[i-1]):
        print(lst[i], end=" ")
