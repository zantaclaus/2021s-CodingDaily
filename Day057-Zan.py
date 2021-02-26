import math
def checkSquare(lst):
    ans = []
    for num in lst:
        if float(math.sqrt(num)) == int(math.sqrt(num)):
            ans.append(num)
    return ans

lst = [int(item) for item in input().split()]
print(checkSquare(lst))