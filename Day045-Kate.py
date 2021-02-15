lowLimit = int(input())
highLimit = int(input())

box = [0]*(highLimit+1)
for i in range(lowLimit, highLimit+1):
    num = i
    total = 0
    while(num >= 1):
        digit = num % 10
        total += digit
        num = int(num/10)
    box[total] += 1

print(box)