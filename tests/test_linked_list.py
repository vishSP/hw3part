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

    def test_to_list(self):
        ll = LinkedList()

        self.assertEqual(ll.insert_beginning({'id': 1, 'username': 'lazzy508509'}), None)
        self.assertEqual(ll.insert_at_end({'id': 2, 'username': 'mik.roz'}), None)
        self.assertEqual(ll.insert_at_end({'id': 3, 'username': 'mosh_s'}), None)
        self.assertEqual(ll.insert_beginning({'id': 0, 'username': 'serebro'}), None)

        lst = ll.to_list()
        for item in lst: print(item)

    def test_data_by_id(self):
        ll = LinkedList()

        user_data = ll.get_data_by_id(3)
        self.assertEqual(user_data, None)
        print(user_data)

    def test_try(self):
        ll = LinkedList()
        self.assertEqual(ll.insert_beginning({'id': 1, 'username': 'lazzy508509'}),None)
        self.assertEqual(ll.insert_at_end('idusername'),None)
        self.assertEqual(ll.insert_at_end([1, 2, 3]),None)
        self.assertEqual(ll.insert_at_end({'id': 2, 'username': 'mosh_s'}),None)

        user_data = ll.get_data_by_id(2)
        self.assertEqual(user_data, {'id': 2, 'username': 'mosh_s'})





if __name__ == '__main__':
    unittest.main()
