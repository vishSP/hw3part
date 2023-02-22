from collections import deque


class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class Queue:
    """Узел Queue  """
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        """положить объекты в Queue"""
        node = Node(item)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next_node = node
            self.tail = node


