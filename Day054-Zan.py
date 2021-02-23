def prime(lst):
    ans = []
    for item in lst:
        isPrime = True
        for i in range(2,item):
            if item % i == 0:
                isPrime = False
                break
        if isPrime and item != 1:
            ans.append(item)
    if len(ans) == 0:
        return [0]
    return ans

lst = [int(item) for item in input().split()]
print(prime(lst))