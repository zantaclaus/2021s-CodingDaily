nums = [0, 1, 2, 3, 4]
indexs = [0, 1, 2, 2, 1]
ans = []

i = 0
j = -1
for index in indexs:
    if(index > j):
        
    ans.append(nums[i])
    i += 1

print(ans)
