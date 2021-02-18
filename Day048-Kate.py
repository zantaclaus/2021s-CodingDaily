def checkPosition(string):
    sumX = 0
    sumY = 0
    for letter in string:
        if letter == 'U':
            sumY += 1
        elif letter == 'D':
            sumY -= 1
        elif letter == 'R':
            sumX += 1
        else:
            sumX -= 1
    if sumX == 0 and sumY == 0:
        return True
    return False

print(checkPosition("LFRRLRUULR"))