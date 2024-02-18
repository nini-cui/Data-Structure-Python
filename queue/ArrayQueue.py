from Queue import Queue

# first in first out -> [A, B, C] --> Queue

# last in first out --> Stack
# first in last out --> stack

# queue first in first out
# linked list: head is the first elements
# making a queue using linked list 

# create a new data structure using linkedlist - creating a queue using linkedlist

# queue: first in first out queue
# to do:
    # add elements: 
        # Queue 
        # check if queue is not full, if yes -> add element to the end of the queue
    # remove elements
    # peek element
    # get the length of the queue
    # check if queue is full/empty

# first in last out


class ArrayQueue(Queue):
    def __init__(self, obj, capacity):
        self.qSize = 0
        self.data = [obj for i in range(capacity)]
        self.front = 0
        self.rear = 0

    def size(self):
        return self.adjustIndex(self.rear + len(self.data) - self.front, len(self.data))
    

    def offer(self, elem):
        if self.isFull():
            raise Exception('Queue is full')
        
        self.data[self.rear] = elem
        self.rear += 1
        self.rear = self.adjustIndex(self.rear, len(self.data))

    
    def poll(self):
        if self.isEmpty():
            raise Exception('Queue is empty')
        
        self.front = self.adjustIndex(self.front, len(self.data))
        d = self.data[self.front]
        self.front += 1
        return d
    

    def peek(self):
        if self.isEmpty():
            raise Exception('Queue is empty')
        
        self.front = self.adjustIndex(self.front, len(self.data))
        return self.data[self.front]


    def isEmpty(self):
        return self.rear == self.front


    def isFull(self):
        return (self.front + len(self.data) - self.rear) % len(self.data) == 1
    

    def adjustIndex(self, index, size):
        return index - size if index >= size else index
    

if __name__ == '__main__':
    q = ArrayQueue(0, 6)

    q.offer(1);
    q.offer(2);
    q.offer(3);
    q.offer(4);
    q.offer(5);

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