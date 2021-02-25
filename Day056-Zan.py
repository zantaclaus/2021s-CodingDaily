def isSort(lst):
    ans = True
    check = []
    for item in lst:  
        check.append(item)
    check.sort()
    for i in range(len(lst)):
        if lst[i] != check[i]:
            ans = False
    if ans:
        print("First one")
        return True

    ans = True
    check.sort(reverse = True)
    for i in range(len(lst)):
        if lst[i] != check[i]:
            print(lst[i])
            ans = False
    return ans
    
print(isSort([5,4,3]))