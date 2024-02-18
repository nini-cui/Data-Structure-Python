from Queue import Queue
from LinkedList import DoublyLinkedList

class LinkedQueue(Queue):
    def __init__(self):
        self.list = DoublyLinkedList()
        self.iterList = iter(self.list)


    def size(self):
        return self.list.size()
    
    
    def isEmpty(self):
        return self.size() == 0
    
    
    def peek(self):
        if self.isEmpty():
            raise Exception('Queue Empty')
        return self.list.peekFirst()
    
    
    def poll(self):
        if self.isEmpty():
            raise Exception('Queue Empty')
        return self.list.removeFirst()
    

    def offer(self, elem):
        self.list.addLast(elem)

    
    def __iter__(self):
        self.iterList = iter(self.list)
        return self
    
    
    def __next__(self):
        return next(self.iterList)
    

if __name__ == '__main__':
    q = LinkedQueue()


