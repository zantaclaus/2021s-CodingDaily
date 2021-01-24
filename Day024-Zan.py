lst = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
print(lst[0], end=" ")
for i in range(1, len(lst)):
    if lst[i] != lst[i-1]:
        print(lst[i], end=" ")