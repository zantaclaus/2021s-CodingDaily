lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while(True):
    n = int(input())
    if n < 0 or n >= 10:
        break
    lst[n] += 1

for i in range(len(lst)):
    print(i,"=",lst[i])    