def searchIndex(lst, n):
    index = 0
    for item in lst:
        if item == n:
            return index
        index += 1
    return -1

lst = [1,2,3,4,5]
n = 5
print(searchIndex(lst,n))