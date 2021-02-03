height = int(input())
width = int(input())
if height <= 0 and width <= 0:
    print("invalid width and height")
elif height <= 0:
    print("invalid height")
elif width <= 0:
    print("invalid width")
else:
    print("%0.2f" % (height*width))
