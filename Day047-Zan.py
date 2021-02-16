def factorial(lst):
    ans = []
    for num in lst:
        value = 1
        for i in range(1, num+1):
            value *= i
        ans.append(value)
    return ans

lst = [int(item) for item in input().split()]
print(factorial(lst))