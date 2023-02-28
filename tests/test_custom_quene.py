import unittest
from custom_queue import *

"""тесты"""
n1 = Node(5, None)
n2 = Node('a', n1)

queue = Queue()
queue.enqueue('data1')
queue.enqueue('data2')
queue.enqueue('data3')


class TestMain(unittest.TestCase):

    def test_Node(self):
        self.assertEqual(n1.data, 5)
        self.assertEqual(n2.data, 'a')
        self.assertEqual(n1.data, 5)
        self.assertEqual(n1.next_node, None)

    def test_enqueue(self):
        self.assertEqual(queue.head.data, "data1")
        self.assertEqual(queue.head.next_node.data, "data2")
        self.assertEqual(queue.tail.data, "data3")
        self.assertEqual(queue.tail.next_node, None)

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')

        self.assertEqual(queue.dequeue(), "data1")
        self.assertEqual(queue.dequeue(), "data2")
        self.assertEqual(queue.dequeue(), "data3")
        self.assertEqual(queue.dequeue(), None)
