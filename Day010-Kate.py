lst = []
n = int(input())
for i in range(0,n):
    lst.append(int(input()))

string = input()
if string == 'Max':
    lst.sort(reverse = True)
else:
    lst.sort()

for i in lst:
    print(i, end=" ")