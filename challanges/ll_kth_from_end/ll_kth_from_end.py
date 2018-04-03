from .node import Node


class LinkedList:
    """
    create a linked list
    """
    def __init__(self, iterable=[]):
        self.head = None
        self._size = 0
        if type(iterable) is not list:
            raise TypeError('Invalid iterable')

        for item in reversed(iter):
                self.insert(item)

    def __repr__(self):
        return '<head> => {}'.format(self.head.val)

    def __str__(self):
        return self.__repr__

    def __len__(self):
        return self._size

    def insert(self, val):
        node = Node(val)
        node._next = self.head
        self.head = node
        self._size += 1

    def find(self, val):
        current = self.head
        while current is not None:
            if current.val == val:
                return True
            current = current._next

        return False
