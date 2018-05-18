from random import *
from Bai2 import writeFile

# Sinh diem ngau nhien khong trung
def genaratoRandomPoint(numOfPoint):
    pointList = {}
    # i = 0
    while len(pointList) != numOfPoint:
        x = (randrange(0, numOfPoint*2))
        y = (randrange(0, numOfPoint))
        pointList[x] = y
        # i += 1
    x = list(sorted(pointList.keys()))
    y = list(pointList.values())
    ziped = zip(x ,y)
    # print(i)

    return list(ziped)

# Main
pointList = genaratoRandomPoint(1000)
writeFile("output3.txt", "w", pointList)


