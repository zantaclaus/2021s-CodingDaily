value = 0
count = 0
lst = [int(item) for item in input().split()]
for item in lst:  
    value += item

for item in lst:
    if value - item > item:
        count += 1

if(count == len(lst)):
    print("True")
else:
    print("False")