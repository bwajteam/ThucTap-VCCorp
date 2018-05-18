
import math
n = int(input("Nhap n "))
def ktSNT(n):
    for i in range(2, int(math.sqrt(n))+1):
        if(n%i == 0):
            return False
    return True

for i in range(2, n):
    if(ktSNT(i)):
        print(i)

