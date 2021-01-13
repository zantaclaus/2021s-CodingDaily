lst = [int(item) for item in input().split()]
ans = []
value = 0
for item in lst:
    value = value + item
    ans.append(value)

print(ans)