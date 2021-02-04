m, n = input().split()
sumM = 0
sumN = 0

countRound = 0
for i in range(1, int(m)+1, 2):
    sumM += i * ((-1)**countRound)
    countRound += 1

countRound = 0
i = 1
while i <= int(n):
    sumN += (i * ((-1) ** countRound))
    i *= 2
    countRound += 1

print(sumM * sumN)