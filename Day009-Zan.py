a = int(input())
b = int(input())
c = int(input())
for i in range (a*b*c+1, 2, -1):
    if a%i==0 and b%i==0 and c%i==0:
        print("GCD: ", end="")
        print(i)
        break


    