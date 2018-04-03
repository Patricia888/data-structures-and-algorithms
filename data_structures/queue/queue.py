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
        node = Node(val)

        if self._size == 0:
            self.front = self.back = node
            self._size += 1
            return node

        self.back.next = self.back = node
        self._size += 1
        return node


        # # put in queue

        # # takes care of an empty list or list of 1
        # # don't need else
        # # if true will automatically break out of the if statement
        # if self.front is None:
        #     self.front = self.back = Node(val)
        #     self._size += 1
        #     return self.back

        # # takes care of a list that has more than 1 value
        # self.back = Node(val, self.back)
        # self._size += 1
        # return self.back

    def dequeue(self):
        if self._size == 0:
            raise IndexError('List is empty')

        temp = self.front
        self.front = temp.next
        self._size -= 1
        return temp



        # # remove from queue

        # current = self.back
        # while current._next:
        #     prev = current
        #     current = current._next

        # prev._next = None
        # return current

        # # do it with front:

