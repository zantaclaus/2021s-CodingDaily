n = int(input())
positive_max = n
positive_min = n
for i in range(7):
    n = int(input())
    if n > 0:
        if n > positive_max:
            positive_max = n
        if n < positive_min:
            positive_min = n

print(positive_max)
print(positive_min)