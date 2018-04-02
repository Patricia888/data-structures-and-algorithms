from .node import Node


class Queue:
    """create a queue"""
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
