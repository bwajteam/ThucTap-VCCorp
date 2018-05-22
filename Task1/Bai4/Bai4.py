#!/usr/bin/python

import threading

n = 1000
numOfThreads = 10
range_size = int(n/numOfThreads)
summ = 0
threads = []

def sum_cal(start,end):
    global summ
    for i in range(start,end):
        summ += i


for i in range(numOfThreads-1):
    thread = threading.Thread(target=sum_cal, args=(i*range_size, (i+1)* range_size, ))
    threads.append(thread)

thread = threading.Thread(target=sum_cal, args=(9*range_size, n+1, ))
threads.append(thread)

for t in threads:
    t.start()

for t in threads:
    t.join()

print(summ)
