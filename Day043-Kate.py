import math

num = int(input())
nDigit = []

while(num >= 1):
    digit = num % 10
    nDigit.append(digit)
    num = int(num / 10)

print(math.prod(nDigit) - sum(nDigit))