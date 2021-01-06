n = int(input())
if n%2 == 1:
    print("Weird")
else:
    if (n>=2 and n<=5) or n>20:
        print("Not Weird")
    elif n>=5 and n<=20:
        print("Weird");