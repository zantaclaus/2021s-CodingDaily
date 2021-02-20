def isSubset(list1, list2):
    count = 0
    for item in list1:
        if item in list2:
            count += 1
    if count == len(list1):
        return True
    count = 0
    for item in list2:
        if item in list1:
            count += 1
    if count == len(list2):
        return True
    return False

lst1 = [int(item) for item in input().split()]
lst2 = [int(item) for item in input().split()]
print(isSubset(lst1,lst2))