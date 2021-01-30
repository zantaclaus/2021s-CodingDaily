n = int(input())
count = 10000
for i in range(8):
    check = int(input())
    if abs(n-check) < count:
        count = abs(n-check)
        ans = check

print(ans)  