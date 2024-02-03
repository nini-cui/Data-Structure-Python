import unittest
from collections import deque
import sys
import os
import random

# sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'BinarySearchTree'))

from BinarySearchTree.BinarySearchTree import BinarySearchTree
from BinarySearchTree.BinarySearchTree import TreeTraversalOrder

class TestTreeNode():
    def __init__(self, data, l, r):
        self.data = data
        self.right = r
        self.left = l


def addTestTreeNode(root, data):
    if root is None:
        root = TestTreeNode(data, None, None)
    else:
        if data < root.data:
            root.left = addTestTreeNode(root.left, data)
        else:
            root.right = addTestTreeNode(root.right, data)

    return root


def preOrderTestTreeNode(root):
    lst = []
    if root is None:
        return lst
    
    lst.append(root.data)
    if root.left is not None:
        lst.extend(preOrderTestTreeNode(root.left))
    if root.right is not None:
        lst.extend(preOrderTestTreeNode(root.right))

    return lst


def inOrderTestTreeNode(root):
    lst = []
    if root is None:
        return lst
    
    if root.left is not None:
        lst.extend(inOrderTestTreeNode(root.left))
    lst.append(root.data)
    if root.right is not None:
        lst.extend(inOrderTestTreeNode(root.right))

    return lst


def postOrderTestTreeNode(root):
    lst = []
    if root is None:
        return lst
    
    if root.left is not None:
        lst.extend(postOrderTestTreeNode(root.left))
    if root.right is not None:
        lst.extend(postOrderTestTreeNode(root.right))
    lst.append(root.data)

    return lst


def levelOrderTestTreeNode(root):
    lst = []
    q = deque()

    if root is not None:
        q.append(root)

    while len(q) != 0:
        root = q.popleft()
        lst.append(root.data)
        if root.left is not None:
            q.append(root.left)
        if root.right is not None:
            q.append(root.right)

    return lst


class BinarySearchTreeTest(unittest.TestCase):

    def test_IsEmpty(self):
        tree = BinarySearchTree()
        self.assertTrue(tree.isEmpty())

        tree.add("Hello World!")
        self.assertFalse(tree.isEmpty())


    def test_Size(self):
        tree = BinarySearchTree()
        self.assertEqual(tree.size(), 0)

        tree.add("Hello World!")
        self.assertEqual(tree.size(), 1)

    
    def test_Height(self):
        tree = BinarySearchTree()
        self.assertEqual(tree.height(), 0)

        tree.add("M")
        self.assertEqual(tree.height(), 1)

        tree.add("J")
        self.assertEqual(tree.height(), 2)
        tree.add("S")
        self.assertEqual(tree.height(), 2)

        tree.add("B")
        self.assertEqual(tree.height(), 3)
        tree.add("N")
        self.assertEqual(tree.height(), 3)
        tree.add("Z")
        self.assertEqual(tree.height(), 3)

        tree.add("A")
        self.assertEqual(tree.height(), 4)


    def test_Add(self):
        tree = BinarySearchTree()
        self.assertTrue(tree.add('A'))

        self.assertFalse(tree.add('A'))

        self.assertTrue(tree.add('B'))


    def test_Remove(self):
        tree = BinarySearchTree()
        tree.add('A')
        self.assertEqual(tree.size(), 1)
        self.assertFalse(tree.remove('B'))
        self.assertEqual(tree.size(), 1)

        tree.add("B")
        self.assertEqual(tree.size(), 2)
        self.assertTrue(tree.remove('B'))
        self.assertTrue(tree.size(), 1)
        self.assertEqual(tree.height(), 1)

        self.assertTrue(tree.remove('A'))
        self.assertEqual(tree.size(), 0)
        self.assertEqual(tree.height(), 0)


    def test_Contains(self):
        tree = BinarySearchTree()

        tree.add('B')
        tree.add('A')
        tree.add('C')

        self.assertFalse(tree.contains('D'))
        self.assertTrue(tree.contains('B'))
        self.assertTrue(tree.contains('A'))
        self.assertTrue(tree.contains('C'))


    def genRandList(self, sz):
        lst = [*range(0, sz, 1)]
        random.shuffle(lst)
        return lst
    

    def validateTreeTraversal(self, trav_order, input):
         
        out =[]
        expected = []

        testTree = None
        tree = BinarySearchTree()

        for value in input:
            testTree = addTestTreeNode(testTree, value)
            tree.add(value)

        # I am not sure if this iter will use iter & function
        for iter in tree.traverse(trav_order):
            out.append(iter)

        if trav_order == TreeTraversalOrder.PRE_ORDER:
            expected = preOrderTestTreeNode(testTree)
        elif trav_order == TreeTraversalOrder.IN_ORDER:
            expected = inOrderTestTreeNode(testTree)
        elif trav_order == TreeTraversalOrder.POST_ORDER:
            expected = postOrderTestTreeNode(testTree)
        elif trav_order == TreeTraversalOrder.LEVEL_ORDER:
            expected = levelOrderTestTreeNode(testTree)
        else:
            raise Exception('Invalid TreeTraversalOrder')
        
        if len(out) != len(expected):
            return False
        
        if expected != out:
            return False
        
        return True
    

    def test_PreOrderTraversal(self):
        input = self.genRandList(4)
        self.assertTrue(self.validateTreeTraversal(TreeTraversalOrder.PRE_ORDER, input))


    def test_InOrderTraversal(self):
        input = self.genRandList(4)
        self.assertTrue(self.validateTreeTraversal(TreeTraversalOrder.IN_ORDER, input))


    def test_PostOrderTraversal(self):
        input = self.genRandList(4)
        self.assertTrue(self.validateTreeTraversal(TreeTraversalOrder.POST_ORDER, input))

    
    def test_LevelOrderTraversal(self):
        input = self.genRandList(4)
        self.assertTrue(self.validateTreeTraversal(TreeTraversalOrder.LEVEL_ORDER, input))

if __name__ == '__main__':
    unittest.main()