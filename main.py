from collections import deque


class Node:
    """Узел нод для с двумя атрибутами"""

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:
    """Узел стак """

    def __init__(self):
        self.top = None

    def push(self, value):
        """Добавление данных в стак"""
        new_node = Node(data=value)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        """Удаление элемента из стака и вывод последнего аргумента"""
        remove = self.top
        self.top = self.top.next_node
        return remove.data
