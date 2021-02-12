startTime = [9,8,7,6,5,4,3,2,1]
endTime = [10]*9
queryTime = 5

count = 0
for i in range(len(startTime)):
    if queryTime >= startTime[i] and queryTime <= endTime[i]:
        count += 1

print(count)