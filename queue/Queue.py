from abc import ABC, abstractmethod

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