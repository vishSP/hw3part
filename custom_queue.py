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

    def dequeue(self):
        """убрать объекты из Queue"""
        if self.head is None:
            return None
        else:
            to_return = self.head.data
            self.head = self.head.next_node
            return to_return


queue = Queue()
queue.enqueue('data1')
queue.enqueue('data2')
queue.enqueue('data3')
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
