def isSame(number):
    lst = list(str(number))
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j:
                if lst[i] == lst[j]:
                    return True
    return False

n = int(input())
print(isSame(n))