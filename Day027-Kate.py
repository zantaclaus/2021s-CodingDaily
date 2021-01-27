lst1 = [int(item) for item in input().split()]
lst2 = [int(item) for item in input().split()]
point = [0, 0]
for i in range(len(lst1)):
    if lst1[i] > lst2[i]:
        point[0] += 1
    elif lst1[i] < lst2[i]:
        point[1] += 1

print(point)