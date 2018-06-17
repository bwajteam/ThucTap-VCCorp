import random
import numpy as np
from numpy import linalg as la

def writeFile(name, mode, data):
    with open(name, mode) as f:
        for a in data:
            f.write(str(a) + "\n")
    f.close()

matrix = []

for x in range(100):
    matrixTemp = []
    for i in range(100):
        temp = random.randrange(100)
        matrixTemp.append(temp)
    matrix.append(matrixTemp)


a = np.array(matrix)
b = a.transpose()
detA = la.det(a)
w, v = la.eig(a)

print("Ma trận chuyển vị")
print(b)

print("Định thức ma trận: ")
print(detA)

print("DS giá trị riêng: ")
print(w)

print("DS vector riêng: ")
print(v)

# print(matrix)
writeFile("output.txt", "w", matrix)






