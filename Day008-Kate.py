def checkList():
    n = int(input())
    lst = [int(item) for item in input().split()]
    check = int(input())

    for item in lst:
        if check == item:
            return 1
    return 0


ans = checkList()
if(ans):
    print("Yes")
else:
    print("No")
