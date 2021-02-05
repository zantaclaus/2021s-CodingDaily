n = int(input())
lst = [int(item) for item in input().split()]
# ans = []
# for i in range(len(lst) , -1, -1):
#     ans.append(lst[i])

k = -1
for i in range(n):
    for j in range(i+1):
        print(lst[k], end="")
    print("")
    k -= 1
