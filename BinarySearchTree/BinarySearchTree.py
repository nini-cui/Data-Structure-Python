from enum import Enum, auto
from collections import deque

class TreeTraversalOrder(Enum):
    PRE_ORDER = auto()
    IN_ORDER = auto()
    POST_ORDER = auto()
    LEVEL_ORDER = auto()


class Node():
    def __init__(self, left, right, elem):
        self.data = elem
        self.left = left
        self.right = right


class BinarySearchTree():

    def __init__(self):
        self.nodeCount = 0
        self.root = None
        self.stackPreOrderIter = deque()


    def isEmpty(self):
        return self.size() == 0
    
    
    def size(self):
        return self.nodeCount
    

    def traverse(self, order):
        if order is TreeTraversalOrder.PRE_ORDER:
            return self.preOrderTraversal()
        if order is TreeTraversalOrder.IN_ORDER:
            return self.inOrderTraversal()
        if order is TreeTraversalOrder.POST_ORDER:
            return self.postOrderTraversal()
        if order is TreeTraversalOrder.LEVEL_ORDER:
            return self.levelOrderTraversal()
        
        return None
    

    # def __iter__(self):

    #     self.expectedNodeCount = self.nodeCount
    #     self.stackPreOrderIter.clear()
    #     self.stackPreOrderIter.append(self.root)
    #     return self
    

    # def __next__(self):
    #     if self.expectedNodeCount != self.nodeCount:
    #         raise Exception('ConcurrentModificationException')
        
    #     if self.root == None or len(self.stackPreOrdreIter) == 0:
    #         raise StopIteration
        
    #     node = self.stackPreOrderIter.popleft()
    #     if node.right != None:
    #         self.stackPreOrderIter.append(node.right)
    #     if node.left != None:
    #         self.stackPreOrderIter.append(node.left)
    #     return node.data


    def add(self, elem):
        if self.contains(elem):
            return False
        else:
            self.root = self.__add(self.root, elem)
            self.nodeCount += 1
            return True


    def __add(self, node, elem):
        if node == None:
            node = Node(None, None, elem)
        else:
            if elem < node.data:
                node.left = self.__add(node.left, elem)
            else:
                node.right = self.__add(node.right, elem)
        
        return node


    def contains(self, elem):
        return self.__contains(self.root, elem)
    
    
    def __contains(self, node, elem):
        if node == None:
            return False
        
        cmp = elem < node.data
        
        if node.data == elem:
            return True
        elif cmp is True:
            return self.__contains(node.left, elem)
        else:
            return self.__contains(node.right, elem) 
        

    def remove(self, elem):
        if self.contains(elem):
            self.root = self.__remove(self.root, elem)
            self.nodeCount -= 1
            return True
        
        return False
    
        
    def __remove(self, node, elem):
        if node == None:
            return False
        
        cmp = elem < node.data

        if elem == node.data:
            if node.left == None:
                rightChild = node.right

                node.data = None
                node = None

                return rightChild
            elif node.right == None:
                leftChild = node.left

                node.data = None
                node = None

                return leftChild
            else:
                tmp = self.findMin(node.right)

                node.data = tmp.data

                node.right = self.__remove(node.right, tmp.data)
        elif cmp is True:
            node.left = self.__remove(node.left, elem)
        elif cmp is False:
            node.right = self.__remove(node.right, elem)
        
        return node
    
    
    def findMin(self, node):
        while node.left is not None:
            node = node.left
        
        return node
    

    def findMax(self, node):
        while node.right is not None:
            node = node.right

        return node
    
    
    def height(self):
        return self.__height(self.root)
    
    
    def __height(self, node):
        if node == None:
            return 0
        
        left_tree_height = self.__height(node.left) + 1
        right_tree_height = self.__height(node.right) + 1
        get_max_value = max(left_tree_height, right_tree_height)
        return get_max_value
        
        # return max(self.__height(node.left), self.__height(node.right)) + 1
    
    
    def preOrderTraversal(self):
        if self.root == None:
            return None
        
        expectedNodeCount = self.nodeCount
        stack = deque()
        stack.append(self.root)

        while True:
            if self.root is None or len(stack) == 0:
                break

            node = stack.pop()
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
            
            yield node.data
        else:
            raise StopIteration
        
    
    def inOrderTraversal(self):
        
        expectedNodeCount = self.nodeCount
        stack = deque()
        stack.append(self.root)

        trav = self.root
        while True:
            if self.root == None or len(stack) == 0:
                break

            while trav != None and trav.left != None:
                stack.append(trav.left)
                trav = trav.left

            node = stack.pop()

            if node.right != None:
                stack.append(node.right)
                trav = node.right

            yield node.data
        else:
            raise StopIteration
        
    
    def postOrderTraversal(self):

        expectedNodeCount = self.nodeCount
        stack1 = deque()
        stack1.append(self.root)
        stack2 = deque()

        while len(stack1) != 0:
            node = stack1.pop()
            if node is not None:
                stack2.append(node)
            if node.left is not None:
                stack1.append(node.left)
            if node.right is not None:
                stack1.append(node.right)


        while True:
            if self.root == None or len(stack2) == 0:
                break

            node = stack2.pop()

            yield node.data
        else:
            raise StopIteration
        

    def levelOrderTraversal(self):
        expectedNodeCount = self.nodeCount
        queue = deque()
        queue.append(self.root)

        while True:
            if self.root == None or len(queue) == 0:
                break

            node = queue.popleft()
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

            yield node.data
        else:
            raise StopIteration
        

    





