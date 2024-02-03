import unittest
from LinkedList.DoublyLinkedList import DoublyLinkedList

class LinkedListTest(unittest.TestCase):

    def setUp(self) -> None:
        self.lnkList = DoublyLinkedList()


    def testaddAt(self):
        self.lnkList.addAt(0, 1)
        self.assertEqual(self.lnkList.size(), 1)
        self.lnkList.addAt(1, 2)
        self.assertEqual(self.lnkList.size(), 2)
        self.lnkList.addAt(1, 3)
        self.assertEqual(self.lnkList.size(), 3)
        self.lnkList.addAt(2, 4)
        self.assertEqual(self.lnkList.size(), 4)
        self.lnkList.addAt(1, 8)
        self.assertEqual(self.lnkList.size(), 5)

if __name__ == '__main__':
    unittest.main()