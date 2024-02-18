import time 
from array import array as arr
from collections import deque
from Queue import Queue

# to do list
# add list tasks
# complete a task 
# figure out whats the next task

class IntQueue(Queue):
    def __init__(self, maxSize):
        self.front = 0 
        self.end = 0
        self.qSize = 0
        self.data = arr('i', (0 for i in range(maxSize)))


    def isEmpty(self):
        return self.qSize == 0
    

    def size(self):
        return self.qSize
    

    def peek(self):
        if self.isEmpty():
            raise Exception('Queue is empty')
        
        self.front = self.front % len(self.data)
        return self.data[self.front]
    

    def isFull(self):
        return self.qSize == len(self.data)
    

    def offer(self, value):
        if self.isFull():
            raise Exception('Queue is full')
        
        self.data[self.end] = value
        self.end += 1
        self.qSize += 1
        self.end = self.end % len(self.data)


    def poll(self):
        if self.isEmpty():
            raise Exception('Queue is empty')
        
        self.qSize -= 1
        self.front = self.front % len(self.data)
        d = self.data[self.front]
        self.front += 1
        return d
    

if __name__ == '__main__':
    q = IntQueue(5)

    q.offer(1)
    q.offer(2)
    q.offer(3)
    q.offer(4)
    q.offer(5)

    q.poll()
    q.poll()
    q.poll()
    q.poll()

    q.offer(1)
    q.offer(2)
    q.offer(3)

    q.poll()
    q.poll()
    q.poll()
    q.poll()
