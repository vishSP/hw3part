import unittest
from linked_list import *

n1 = Node(5, None)
n2 = Node('a', n1)

class TestLinkedList(unittest.TestCase):


    def test_Node(self):
        self.assertEqual(n1.data, 5)
        self.assertEqual(n2.data, 'a')
        self.assertEqual(n1.data, 5)
        self.assertEqual(n1.next, None)


    def test_LinkedList(self):
        ll = LinkedList()

        self.assertEqual(ll.insert_beginning({'id': 1}), None)
        self.assertEqual(ll.insert_at_end({'id': 2}), None)
        self.assertEqual(ll.insert_at_end({'id': 3}), None)
        self.assertEqual(ll.insert_beginning({'id': 0}), None)


if __name__ == '__main__':
    unittest.main()