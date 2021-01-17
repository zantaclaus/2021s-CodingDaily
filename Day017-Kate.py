n = int(input())
lst = [int(item) for item in input().split()]
lst.sort(reverse=True)
print(lst[0] * lst[1])