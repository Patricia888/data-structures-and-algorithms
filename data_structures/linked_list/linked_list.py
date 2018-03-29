from node import Node


class LinkedList:
    """
    Singly linked list
    """
    def __init__(self, iter=[]):
        # self._current = None
        self.head = None
        self._size = 0  # or length
        if type(iterable) is not list:
            raise TypeError('Invalid iterable')
        for item in iterable:
                self.insert(item)

    def __repr__(self):
        # assuming head will have a val
        return f'<head> is {self.head.val}'

    def __str__(self):
        return self.__repr__

    def __len__(self):
        return self._size

    def insert(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node
        self._size += 1

    def find(self, val):
        current = self.head
        while current:
            if current.val == val:
                return True
            current = current._next

        return False
