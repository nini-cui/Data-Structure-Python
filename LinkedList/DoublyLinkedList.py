import ctypes

class Node(object):
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

    
    def __repr__(self):
        return str(self.data)
    

class DoublyLinkedList(object):

    def __init__(self):
        self.llSize = 0
        self.head = 0
        self.tail = 0
        self.travIter = 0


    def __len__(self):
        return self.llSize
    

    def size(self):
        return self.llSize
    

    def isEmpty(self):
        return self.size() == 0 
    

    def clear(self):

        trav = self.head
        while trav is not None:
            next = trav.next
            trav.prev = trav.next = None
            trav.data = None
            trav = next

        self.llSize = None
        self.head = None
        self.tail = None
        trav = None


    def add(self, elem):
        self.addLast(elem)


    def addLast(self, elem):
        if self.isEmpty():
            self.head = self.tail = Node(elem, None, None)
        else:
            self.tail.next = Node(elem, self.tail, None)
            self.tail = self.tail.next

        self.llSize += 1


    def addFirst(self, elem):
        if self.isEmpty():
            self.head = self.tail = Node(elem, None, None)
        else:
            self.head.prev = Node(elem, None, self.head)
            self.head = self.head.prev

        self.llSize += 1

    
    def addAt(self, index, data):
        if index < 0:
            raise Exception('index should not be negative. The value of index was {}'.format(index))
        
        if index == 0:
            self.addFirst(data)
            return
        
        if index == self.llSize:
            self.addLast(data)
            return
        
        temp = self.head
        for i in range(0, index - 1):
            temp = temp.next

        newNode = Node(data, temp, temp.next)
        temp.next.prev = newNode
        temp.next = newNode

        self.llSize += 1


    def peekFirst(self):
        if self.isEmpty():
            raise Exception('Empty list')
        return self.head.data
    

    def peekLast(self):
        if self.isEmpty():
            raise Exception('Empty list')
        return self.tail.data
    

    def removeFirst(self):
        if self.isEmpty():
            raise Exception('Empty list')
        
        data = self.head.data
        self.head = self.head.next
        self.llSize -= 1

        if self.isEmpty():
            self.tail = None
        else:
            self.head.prev = None


        return data
    

    def removeLast(self):
        if self.isEmpty():
            raise Exception('Empty list')
        
        data = self.tail.data
        self.tail = self.tail.prev
        self.llSize -= 1

        if self.isEmpty():
            self.head = None
        else:
            self.tail.next = None

        return data


    def __remove__(self, node):
        if node.prev == None:
            return self.removeFirst()
        if node.next == None:
            return self.removeLast()
        
        node.next.prev = node.prev
        node.prev.next = node.next

        data = node.data

        node.data = None
        node.prev = None
        node.next = None
        node = None

        self.llSize -= 1

        return data
    

    def removeAt(self, index):
        if index < 0 or index >= self.llSize:
            raise ValueError("wrong index")

        if index < self.llSize / 2:
            i = 0
            trav = self.head 
            while i != index:
                i += 1
                trav = trav.next
        else:
            i = self.llSize - 1
            trav = self.tail
            while i != index:
                i -= 1
                trav = trav.prev

        return self.__remove__(trav)
    

    def remove(self, obj):
        if obj == None:
            trav = self.head
            while trav is not None:
                if trav.data is None:
                    self.__remove__(trav)
                    return True
                trav = trav.next
        else:
            trav = self.head
            while trav is not None:
                if obj == trav.data:
                    self.__remove__(obj)
                    return True
                
                trav = trav.next

        return False
    

    def indexOf(self, obj):
        index = 0
        trav = self.head

        if obj is None:
            while trav is not None:
                if trav.data is None:
                    return index
                trav = trav.next
                index += 1
        else:
            while trav is not None:
                if trav.data == obj:
                    return index
                trav = trav.next
                index += 1

        return -1
    

    def contains(self, obj):
        return self.indexOd(obj) != -1
    

    def __iter__(self):
        self.travIter = self.head
        return self
    

    def __next__(self):
        if self.travIter is None:
            raise StopIteration
        
        data = self.travIter.data
        self.travIter = self.travIter.next

        return data
    

    def __repr__(self):
        sb = ""

        sb = sb + '[ '
        trav = self.head
        while trav is not None:
            sb = sb + str(trav.data)
            if trav.next is not None:
                sb = sb + ','
            trav = trav.next

        sb = sb = ' ]'

        return str(sb)