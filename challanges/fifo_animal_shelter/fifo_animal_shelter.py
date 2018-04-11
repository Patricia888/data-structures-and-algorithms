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


def dequeue(self, pref=None):
        if self._size == 0:
            raise IndexError('animal shelter is empty')

        if pref is None or self.front.val == pref:
            removed_animal = self.front
            self.front = self.front._next
            self._size -= 1
            return removed_animal.val

        if type(pref) is not str:
            raise TypeError('must be a string dude')

        if pref != 'dog' and pref != 'cat':
            raise ValueError('we are a biased shelter, only cats and dogs')

        current = self.front._next
        temp = self.front
        while current:
            if current.val == pref:
                removed_animal = current
                temp._next = current._next
                self._size -= 1
                return removed_animal.val
            current = current._next
            temp = temp._next
