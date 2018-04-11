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
        if val is None:
            raise TypeError('Invalid value')
        self.stack_one.push(val)
        self._size += 1
        return self

    def dequeue(self):
        if len(self.stack_one) == 0:
            raise IndexError('Empty')

        current1 = self.stack_one.top
        while current1:
            self.stack_two.push(self.stack_one.pop())
            current1 = current1._next

        removed = self.stack_two.pop()

        current2 = self.stack_two.top
        while current2:
            self.stack_one.push(self.stack_two.pop())
            current2 = current2._next

        self._size -= 1
        return removed
