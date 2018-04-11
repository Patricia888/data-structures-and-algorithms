from .node import Node


class AnimalShelter:
    def __init__(self, iterable=[]):
        self.front = None
        self.back = None
        self._size = 0
        if type(iterable) is not list:
            raise TypeError('Invalid iterable')
        for item in iterable:
            self.enqueue(item)

    def __repr__(self):
        return f'Oldest animal in the shelter is {self.front.val}'

    def enqueue(self, animal=None):
        if animal != 'dog' and animal != 'cat':
            raise ValueError('we are a biased shelter, only cats and dogs')

        node = Node(animal)
        self._size += 1
        if self.front is None:
            self.front = self.back = node
        self.back._next = node
        self.back = node
        return None
