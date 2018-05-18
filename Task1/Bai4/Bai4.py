#!/usr/bin/python

import threading
import time
from datetime import datetime

class myThread (threading.Thread):
   def __init__(self, name, x, y, output):
      threading.Thread.__init__(self)
      self.name = name
      self.x = x
      self.y = y
      self.output = output
   def run(self):
    print("Starting " + self.name + "  Time  " + str(datetime.now()))
      # Get lock to synchronize threads
    threadLock.acquire()
    self.output.append(sumCal(self.name, self.x, self.y))
    print("Output of " +self.name +" = "+ str(self.output) + "  Time  " + str(datetime.now()))
    time.sleep(5)
      # Free lock to release next thread
    threadLock.release()

def sumCal(threadName, x, y):
    sum = 0
    for value in range(x, y):
        sum += value
    return sum

n = 1000
numOfThreads = 10
output = []
sum = 0

threadLock = threading.Lock()
threads = []

for i in range(0, numOfThreads - 1):
    threads.append(myThread("Thread-{}".format(i+1), i*int((n/numOfThreads)), i*int((n/numOfThreads)) + int(n/numOfThreads), output))
threads.append(myThread("Thread-{}".format(numOfThreads), (numOfThreads-1)*int(n/numOfThreads), n, output))


for t in threads:
    t.start()
    time.sleep(5)


for t in threads:
    t.join()

for x in output:
    sum += x

print(sum)
