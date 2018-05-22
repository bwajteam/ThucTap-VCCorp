
import math
n = int(input("Nhap n "))
def ktSNT(n):
    # if(n == 2): return True
    for i in range(2, int(math.sqrt(n))+1):
        if(n%i == 0):
            return False
    return True

for i in range(2, n+1):
    if(ktSNT(i)):
        print(i)

