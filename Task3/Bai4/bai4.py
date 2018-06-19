import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
from mpl_toolkits.mplot3d import Axes3D
import math
import datetime

# Chuyen tu unixTime ve readData time
def conventUnixTime(unixTime):
    return datetime.datetime.fromtimestamp(
        float(unixTime)
    ).strftime('%Y-%m-%d')

# Đọc dữ liệu từ file, đưa các con ngựa vào từng dict (id , list tọa độ)
def readData(fileName):
    res = defaultdict(list)
    with open(fileName) as f:
        for x in f:
            horse = x.split(",")
            horse[0] = conventUnixTime(horse[0])        
            idHorse = horse[3]                             
            res[idHorse].append(horse)
    return res

# Tinh khoang cach gan nhat giua 2 ngay bat ki
def minIn2Day(day1, day2):
    res = 1000000000
    for data1 in day1:
        for data2 in day2:
            resTemp = float(math.hypot(float(data2[0]) - float(data1[0]), float(data2[1]) - float(data1[1])))
            if(resTemp < res): res = resTemp
    return res





# Tìm 2 ngày mà có khoảng cách ngắn nhất
def minOfHorse(horse):
    res = 1000000000
    day1, day2 = 0, 0
    key = list(horse.keys())
    for i in range(len(key)- 1):
        day1 = key[i]
        for j in range(1, len(key)):       
            day2 = key[j]
            resTemp = minIn2Day(horse[day1], horse[day2])
            if(resTemp < res): 
                res = resTemp
    return res, day1, day2     





# Tính khoảng cách của từng con ngựa
list_horse = readData("ZebraBotswana.txt")  
# print(list_horse['Z6399\n']) 
for key in list_horse:
    res = defaultdict(list)
    for horse in list_horse[key]:  
        viTri = [horse[1], horse[2]]
        time = horse[0]
        res[time].append(viTri)

    lengh, day1, day2 = minOfHorse(res)
    print("2 ngay co khoang cach gan nhau nhat cua id", key, "la ngay ", day1 , " va ngay ", day2, "\n",
    "Khoảng cách ngắn nhất là", lengh)




# Vẽ đường đi của ngựa


color = ['r','b','g','k','c','y','m']
index = -1
for key in list_horse.keys():
    x, y = [], []
    index += 1
    c =  color[index] 
    for i in list_horse[key]:
        x.append(float(i[1]))
        y.append(float(i[2]))    
    sorted(x)
    sorted(y)
    plt.plot(x, y, c = c, label = key)
    
plt.legend()
plt.xlabel('Vĩ độ')
plt.ylabel('Kinh độ')
plt.savefig("horse.png")  
# plt.show()

        


   

