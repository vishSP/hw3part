class Node:
    """Узел нод для с двумя атрибутами"""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    """ Узел для хранения односвязного списка"""
    def __init__(self):
        self.head = None
        self.nail = None

    def insert_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print_ll(self):
        ll_string = ''
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next

        ll_string += ' None'
        print(ll_string)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

