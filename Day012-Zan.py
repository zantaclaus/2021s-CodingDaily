# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())
# value = a + b + c + d + e

# check = 0
# lenght = 0
# lst = []
# for i in range(0, 5):
#     lst.append(int(input()))
#     value = value + lst[i]
#     lenght += 1

# for i in range(0,5):
#     if(value - lst[i] > 0):
#         check += 1
# if(check == lenght):
#     print("True")
# else:
#     print("False")
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