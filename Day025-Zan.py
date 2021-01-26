lstEven = []
lstOdd = []
for i in range(8):
    num = int(input())
    if num % 2 == 0:
        lstEven.append(num)
    else:
        lstOdd.append(num)

if(len(lstEven) > len(lstOdd)):
    print("Even")
else:
    print("Odd")

print(sum(lstEven))
print(sum(lstOdd))