import math
def isSquareInt(lst):
    ans = []
    for num in lst:
        if math.sqrt(num) == int(math.sqrt(num)):
            ans.append(num)
    return ans

lst = [int(item) for item in input().split()]
ans = isSquareInt(lst)
ans.sort()
print(ans)