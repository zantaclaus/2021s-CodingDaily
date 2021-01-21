def func(num):
    if num % 2 == 0:
        return  num / 2
    return num - 1

count = 0
num = int(input())
while(num != 0):
    num = func(num)
    count += 1

print(count)

