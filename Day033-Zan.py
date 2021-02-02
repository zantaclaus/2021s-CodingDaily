a = int(input())
b = int(input())
c = int(input())

if a + b == c:
    print("+")
elif a - b == c:
    print("-")
elif a * b == c:
    print("*")
elif int(a / b) == c:
    print("/")
else:
    print("%")
