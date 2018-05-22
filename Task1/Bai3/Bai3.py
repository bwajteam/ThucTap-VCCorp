from random import *
from Bai2 import writeFile

class point():
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
def check (p, listPoint):
    for x in listPoint:
        if(x.x == p.x and x.y == p.y):
            return False
    return True


# Sinh diem ngau nhien khong trung
def genaratoRandomPoint(numOfPoint):
    pointList = []
    # i = 0
    while len(pointList) != numOfPoint:
        x = (randrange(0, numOfPoint))
        y = (randrange(0, numOfPoint))
        p = point(x, y)
        if(check(p, pointList)):
            pointList.append(p)
    return pointList


# Main
pointList = genaratoRandomPoint(1000)
x = []
y = []
for i in pointList:
    x.append(i.x)
    y.append(i.y)
    
output = zip(x,y)
writeFile("output3.txt", "w", list(output))


