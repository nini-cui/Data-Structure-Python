import unittest
from LinkedList.DoublyLinkedList import DoublyLinkedList

class LinkedListTest(unittest.TestCase):

    def setUp(self):
        self.lnkList = DoublyLinkedList()


    def tearDown(self):
        self.lnkList.clear()


    def test_EmptyList(self):
        self.assertTrue(self.lnkList.isEmpty())
        self.assertEqual(self.lnkList.size(), 0)

    
    def test_RemoveFirstOfEmpty(self):
        with self.assertRaises(Exception):
            self.lnkList.removeFirst()


    def test_RemoveLastofEmpty(self):
        with self.assertRaises(Exception):
            self.lnkList.removeLast()


    def test_PeekFirstOfEmpty(self):
        with self.assertRaises(Exception):
            self.lnkList.peekFirst()


    def test_PeekLastOfEmpty(self):
        with self.assertRaises(Exception):
            self.lnkList.peekLast()

        
    def test_AddFirst(self):
        self.lnkList.addFirst(3)
        self.assertEqual(self.lnkList.size(), 1)
        self.lnkList.addFirst(5)
        self.assertEqual(self.lnkList.size(), 2)


    def test_AddLast(self):
        self.lnkList.addLast(3)
        self.assertEqual(self.lnkList.size(), 1)
        self.lnkList.addLast(5)
        self.assertEqual(self.lnkList.size(), 2)


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


    def test_RemoveFirst(self):
        self.lnkList.addFirst(3)
        self.assertTrue(self.lnkList.removeFirst() == 3)
        self.assertTrue(self.lnkList.isEmpty())

    
    def test_removeLast(self):
        self.lnkList.addLast(4)
        self.assertTrue(self.lnkList.removeLast() == 4)
        self.assertTrue(self.lnkList.isEmpty())


    def test_PeekFirst(self):
        self.lnkList.addFirst(4)
        self.assertTrue(self.lnkList.peekFirst() == 4)
        self.assertEqual(self.lnkList.size(), 1)


    def test_PeekLast(self):
        self.lnkList.addLast(4)
        self.assertTrue(self.lnkList.peekLast() == 4)
        self.assertEqual(self.lnkList.size(), 1)


    def test_Peeking(self):
        # 5
        self.lnkList.addFirst(5)
        self.assertTrue(self.lnkList.peekFirst() == 5)
        self.assertTrue(self.lnkList.peekLast() == 5)

        # 6 - 5
        self.lnkList.addFirst(6);
        self.assertTrue(self.lnkList.peekFirst() == 6);
        self.assertTrue(self.lnkList.peekLast() == 5);

        # 7 - 6 - 5
        self.lnkList.addFirst(7)
        self.assertTrue(self.lnkList.peekFirst() == 7)
        self.assertTrue(self.lnkList.peekLast() == 5)

        # 7 - 6 - 5 - 8
        self.lnkList.addLast(8)
        self.assertTrue(self.lnkList.peekFirst() == 7)
        self.assertTrue(self.lnkList.peekLast() == 8)

        # 7 - 6 - 5
        self.lnkList.removeLast()
        self.assertTrue(self.lnkList.peekFirst() == 7)
        self.assertTrue(self.lnkList.peekLast() == 5)

        # 7 - 6
        self.lnkList.removeLast()
        self.assertTrue(self.lnkList.peekFirst() == 7)
        self.assertTrue(self.lnkList.peekLast() == 6)

        # 6
        self.lnkList.removeFirst()
        self.assertTrue(self.lnkList.peekFirst() == 6)
        self.assertTrue(self.lnkList.peekLast() == 6)

    def test_Removing(self):
        strs = DoublyLinkedList()
        strs.add("a")
        strs.add("b")
        strs.add("c")
        strs.add("d")
        strs.add("e")
        strs.add("f")
        strs.remove("b")
        strs.remove("a")
        strs.remove("d")
        strs.remove("e")
        strs.remove("c")
        strs.remove("f")
        self.assertEqual(0, strs.size())
        strs.clear()

    
    def test_RemoveAt(self):
        self.lnkList.add(1)
        self.lnkList.add(2)
        self.lnkList.add(3)
        self.lnkList.add(4)
        self.lnkList.removeAt(0)
        self.lnkList.removeAt(2)
        print(self.lnkList.peekFirst())
        self.assertTrue(self.lnkList.peekFirst() == 2)
        self.assertTrue(self.lnkList.peekLast() == 3)
        self.lnkList.removeAt(1)
        self.lnkList.removeAt(0)
        self.assertEqual(self.lnkList.size(), 0)

    
    def test_Clear(self):
        self.lnkList.add(22)
        self.lnkList.add(33)
        self.lnkList.add(44)
        self.assertEqual(self.lnkList.size(), 3)
        self.lnkList.clear()
        self.assertEqual(self.lnkList.size(), 0)
        self.lnkList.add(22)
        self.lnkList.add(33)
        self.lnkList.add(44)
        self.assertEqual(self.lnkList.size(), 3)
        self.lnkList.clear()
        self.assertEqual(self.lnkList.size(), 0)


    def testToString(self):
        strs = DoublyLinkedList()
        self.assertEqual(str(strs), "[  ]")
        strs.add("a")
        self.assertEqual(str(strs), "[ a ]")
        strs.add("b")
        self.assertEqual(str(strs), "[ a, b ]")
        strs.add("c")
        strs.add("d")
        strs.add("e")
        strs.add("f")
        self.assertEqual(str(strs), "[ a, b, c, d, e, f ]")


if __name__ == '__main__':
    unittest.main()