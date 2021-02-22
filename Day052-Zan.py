def isTen(start, end):
    ans = []
    for i in range(start, end + 1):
        sum = 0
        lst = list(str(i))
        for item in lst:
            sum += int(item)
        if sum == 10:
            ans.append(i)

    return ans
start = int(input())
end = int(input())
print(isTen(start, end))
