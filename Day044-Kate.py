def sortEvenOdd(arr):
    lst = []
    for num in arr:
        if num % 2 == 0:
            lst.append(num)
    for num in arr:
        if num % 2 != 0:
            lst.append(num)
    return lst

arr = [int(item) for item in input().split()]
print(sortEvenOdd(arr))