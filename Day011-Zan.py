n = int(input())
lst = []
ans = 0;
for i in range(0, n):
    lst.append(int(input()))
    ans += lst[i]

print(lst, "=", ans)
