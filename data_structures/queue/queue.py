from .node import Node


# a queue is only aware of 'the back'
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
        # print front of queue
        # current = self.back
        # while current._next:
        #     current = current._next

    def __str__(self):
        # print back
        # return 'Queue back: {}'.format(self.back.val)
        # print front
        return f'Front of queue is {self.front.val}'

    def __len__(self):
        return self._size

    def enqueue(self, val):
        self.back = Node(val, self.back)

    def dequeue(self):
        pass
