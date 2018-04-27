class Node:
    def __init__(self, val, next=None):
        self.val = val
        self._next = next

    def __repr__(self):
        return '{val}'.format(val=self.val)

    def __str__(self):
        return self.__repr__


class LinkedList:
    """Singly linked list"""
    def __init__(self, iter=[]):
        # self._current = None
        self.head = None
        self._size = 0  # or length
        if type(iter) is not list:
            raise TypeError('Invalid iterable')

        for item in reversed(iter):
            self.insert(item)

    def __repr__(self):
        # assuming head will have a val
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
