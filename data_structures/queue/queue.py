from .node import Node


class Queue:
    """basic queue"""
    def __init__(self, iterable=[]):
        self.front = None
        self.back = None
        self._size = 0
        if type(iterable) is not list:
            raise TypeError('Invalid iterable')
        for item in iterable:
            self.enqueue(item)

    def __repr__(self):
        return f'Front of queue is {self.front.val}'

    def __str__(self):
        return f'Front of queue is {self.front.val}'

    def __len__(self):
        return self._size

    def enqueue(self, val):
        try:
            node = Node(val)
        except TypeError:
            return self.back
        self._size += 1
        if self.front is None:
            self.front = node
            self.back = node
        self.back._next = node
        self.back = node
        return self.front


    def dequeue(self):
        if self._size == 0:
            raise IndexError('List is empty')
        removed_node = self.front
        self.front = self.front._next
        self._size -= 1
        return removed_node.val
