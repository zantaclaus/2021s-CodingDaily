def insert_end(str):
    char1 = str[len(str) - 2]
    char2 = str[len(str) - 1]
    for i in range(4):
        print(char1+char2, end="")

#insert_end("Python")