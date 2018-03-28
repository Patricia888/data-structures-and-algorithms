from node import Node


class LinkedList:
    """
    create a linked list
    """
    def __init__(self, iterable=[]):
        """Constructor for the LinkedList object"""
        self.head = None
        self._size = 0
        if type(iterable) is not list:
            raise TypeError('Invalid iterable')
        for item in iterable:
                self.insert(item)

    def __repr__(self):
        return f'<head> is {self.head.val}'

    def __str__(self):
        return self.__repr__

    def __len__(self):
        """Return the size of the linked list"""
        return self._size
