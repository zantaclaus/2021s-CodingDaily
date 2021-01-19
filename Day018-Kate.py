message = input()
checker = input()
ans = 0
for item1 in message:
    for item2 in checker:
        if item1 == item2:
            ans += 1

#print(ans)#