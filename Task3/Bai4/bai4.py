import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
from mpl_toolkits.mplot3d import Axes3D
import math

def readData(fileName):
    res = defaultdict(list)
    with open(fileName) as f:
        for x in f:
            horse = x.split(",")        
            idHorse = horse[3]                             
            res[idHorse].append(horse)
    return res


list_horse = readData("ZebraBotswana.txt")    
print(list_horse.keys()) 
for keyName in list_horse.keys():
    maxLen = 100000
    t1, t2 =0, 0
    for i in range(len(list_horse[keyName]) - 1):
        x1 = float(list_horse[keyName][i][2])
        y1 = float(list_horse[keyName][i][1])  
        tmpt1 = float(list_horse[keyName][i][0])
               
        x2 = float(list_horse[keyName][i+1][1])       
        y2 = float(list_horse[keyName][i+1][2])   
        tmpt2 = float(list_horse[keyName][i+1][0])    

        tempLen = float(math.hypot(x2 - x1, y2 - y1))
        # deltaTime = (t2 - t1) / 86400 
        # Cach 24h

        # if(tempLen < maxLen and deltaTime >= 1): 
        if(tempLen < maxLen): 
            maxLen = tempLen
            t1 = tmpt1
            t2 = tmpt2
            
    print("Hai thời điểm mà",keyName,"có khoảng cách nhỏ nhất: ",t1,t2)





# print(list_horse.keys())
# print(list_horse['Z3864\n'][-1][0])
fig = plt.figure()
ax = fig.add_subplot(111, projection = "3d")
x, y, z = [], [], []

color = ['r','b','g','k','c','y','m']
for key in list_horse.keys():
    index = -1
    for i in list_horse[key]:
        x.append(float(i[1]))
        y.append(float(i[2]))
        z.append(float(i[0]))
        
    ax.scatter(x, y, z, c= color[index + 1], marker='o', label =key)
    
plt.legend()
ax.set_xlabel('Vĩ độ')
ax.set_ylabel('Kinh độ')
ax.set_zlabel('Thời gian')
plt.savefig("horse.png")
plt.show()
        


   

