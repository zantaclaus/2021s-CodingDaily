n = int(input())
for i in range(1, n+1):
    for j in range(1, n+1):
        if (i+j < n/2 +1):        # Left Top
            print(" ", end = "")
        elif (j-i > n/2):         # Right Top
            print(" ", end = "")
        elif (i-j > n/2):         # Left Bottom
            print(" ", end = "")
        elif (i+j > n/2 + n+1):   # Right Bottom
            print(" ", end = "")
        else:
            print("*", end = "")
    print("")