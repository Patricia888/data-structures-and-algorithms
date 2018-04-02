from .node import Node


class Stack:
    """basic stack"""
    def __init__(self, iterable=[]):
        self.top = None
        self._size = 0
        if type(iterable) is not list:
            raise TypeError('Invalid iterable')
        for item in iterable:
            self.push(item)

    def __repr__(self):
        return f'Top of stack is {self.top.val}'

    def __str__(self):
        return f'Top of stack is {self.top.val}'

    def __len__(self):
        """Return the size of the stack"""
        return self._size
