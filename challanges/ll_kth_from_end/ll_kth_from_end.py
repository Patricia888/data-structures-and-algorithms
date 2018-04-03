from .node import Node


class LinkedList:
    """
    create a linked list
    """
    def __init__(self, iterable=[]):
        self.head = None
        self._size = 0
        if type(iterable) is not list:
            raise TypeError('Invalid iterable')

        for item in reversed(iter):
                self.insert(item)

    def __repr__(self):
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

    def append(self, val):
        if self.head is None:
            self.insert(val)
        else:
            current = self.head
            while current is not None:
                if current._next is None:
                    current._next = Node(val)
                    self._size += 1
                    break
                current = current._next

    def insert_before(self, val, newVal):
        current = self.head
        previous = None
        while current:
            if current.val == val:
                if previous is None:
                    self.insert(newVal)
                else:
                    new_node = Node(newVal)
                    new_node._next = current
                    previous._next = new_node
                    self._size += 1
                break
            previous = current
            current = current._next

    def insert_after(self, val, newVal):
        current = self.head
        while current:
            if current.val == val:
                position = current._next
                current._next = Node(newVal)
                current._next._next = position
                self._size += 1
                break
            current = current._next
