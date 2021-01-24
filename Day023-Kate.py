lst = [1, 2, 3 ,4] # pair 1-2 ---> [2]*1  | pair 3-4 --->[4]*3  ---> output [2, 4, 4, 4]
ans = []
for i in range(0, len(lst), 2):
    print("time", i)
    for j in range(i+1):
        ans.append(lst[i+1])

print(ans)