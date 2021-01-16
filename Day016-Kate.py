#lst = [1, 1, 1, 1]
lst = [int(num) for num in input().split()]
count = 0
for i in range(len(lst)):
    for j in range(len(lst)):
        if(lst[i] == lst[j]) and (i < j):
            count += 1
print(count)