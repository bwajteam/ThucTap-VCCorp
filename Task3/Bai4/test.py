import matplotlib.pyplot as plt
import math

i=0
l=[]#lưu thông tin của tất cả các con ngựa
ds=[]# lưu id của tất cả các con ngựa 

with open("ZebraBotswana.txt") as f:
    for line in f:
        x=line.split(',')
        x[3]=x[3].split('\n')[0]
        l.append(x)
        ds.append(x[3])
l.sort()

m=0
n=list(set(ds))#loại bỏ các id con ngựa trùng lặp(có tất cả 7 con ngựa)
while m<len(n):
	dsl=[]#tạo danh sách tách mỗi con ngựa ra theo id
	for i in range(0,len(l)):
		if(l[i][3]==n[m]):
			dsl.append(l[i])

	min=100#gán khoảng cách min=100
	# biến lưu 2 ngày có khoảng cách vị trí nhỏ nhất
	t1=""
	t2=""
	for i in range(0,len(dsl)-1):
		for j in range(i+1, len(dsl)):
			if (i != j):
				#khoảng cách giữa 2 con ngựa
				b=math.sqrt((float(dsl[i][1])-float(dsl[j][1]))*(float(dsl[i][1])-float(dsl[j][1]))+(float(dsl[i][2])-float(dsl[j][2]))*(float(dsl[i][2])-float(dsl[j][2])))
				if b < min:
					min=b
					t1= dsl[i][0]
					t2= dsl[j][0]

	print("Hai thời điểm mà",n[m],"có khoảng cách nhỏ nhất: ",t1,t2)
	m+=1

#hiển thị đường đi của các con ngựa trên đồ thị

while m<len(n):
	lx=[]
	ly=[]
	for k in l:
		if(k[3]==n[m]):
			lx.append(float(k[1]))
			ly.append(float(k[2]))
	plt.plot(lx,ly)
	m+=1
plt.show()