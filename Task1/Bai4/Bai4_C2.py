#!/usr/bin/python

import threading
import time

lock = threading.Lock()
summ = 0
threads = []

n = 1000
numOfThreads = 10

data = []

class my_thread (threading.Thread):
   def __init__(self,name,  data, lock):
        threading.Thread.__init__(self)
        self.name = name
        self.data = data
        self.lock = lock


   def run(self): 
        global summ 
        while len(self.data)> 0:
            lock.acquire()             
            n= self.data.pop()  
            lock.release()
            summ+= n                              
            print(self.name + " n = " + str(n) + " summ = "+ str(summ)) 
            time.sleep(0.01)                                                                                                

for i in range(1001):
    data.append(i)



for i in range(numOfThreads-1):
    thread = my_thread("Thread {}".format(i+1), data, lock)
    threads.append(thread)

thread = my_thread("Thread {}".format(i+1), data, lock)
threads.append(thread)

for t in threads:
    t.start()

for t in threads:
    t.join()


print(summ)
