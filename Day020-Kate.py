print("s = ", end="")
s = input()
print("indices = ", end="")
indices = [int(item) for item in input().split()]

ans = []
for item in indices:
    for index in range(len(s)):
        if item == index:
            ans.append(s[index])
    
print(ans)