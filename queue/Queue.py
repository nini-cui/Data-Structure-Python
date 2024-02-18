from abc import ABC, abstractmethod

# (1) Enqueue()
# (2) Dequeue()
# (3) front() peek the first element in the queue
# (4) Isempty() 
# Execution will take constant time O(1)
# Frist in First out

class Queue(ABC):

    @abstractmethod
    def offer(self, elem):
        pass

    @abstractmethod
    def poll(self):
        pass

    @abstractmethod
    def peek(self):
        pass

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def isEmpty(self):
        pass