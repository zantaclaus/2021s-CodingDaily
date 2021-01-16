def compareList(lstA, lstB):
    lstA.sort()
    lstB.sort()

    if(len(lstA) != len(lstB)):
        return False
    for i in range(len(lstA)):
        if lstA[i] != lstB[i]:
            return False
    return True

A = [1, 2, 3, 4, 5]
B = [5, 3, 1, 2, 4, 20]
print(compareList(A, B))
