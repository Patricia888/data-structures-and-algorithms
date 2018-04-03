from .stack import Stack


class Queue:
    """queue that uses 2 stacks"""
    def __init__(self, iterable=[]):
        self._size = 0
        self.stack_one = Stack()
        self.stack_two = Stack()

        if type(iterable) is not list:
            raise TypeError('Invalid iterable')
        for item in iterable:
            self.enqueue(item)

    def enqueue(self, val):
        """put val in queue"""

    def dequeue(self):
        """take val out of queue"""