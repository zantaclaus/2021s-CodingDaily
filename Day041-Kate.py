def selfDiving(start, end):
    for i in range(start, end + 1):
        check = False
        num = i
        while(num >= 1):
            digit = num % 10
            if digit < 1 or i % digit != 0:
                check = True
                break
            num = int(num / 10)
        if check:
            continue
        print(i)

selfDiving(1, 22)