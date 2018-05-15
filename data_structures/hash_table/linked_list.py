class Node:
    def __init__(self, val, next=None):
        self.val = val
        self._next = next
    
    def __repr__(self):
        return '{val}'.format(val=self.val)


class LinkedList:
    def __init__(self, iter=[]):
        self._current = None
        self.head = None
        self._size = 0
        if type(iter) is not list:
            raise TypeError('Invalid iterable')
        for item in reversed(iter):
            self.insert(item)

    def __repr__(self):
        return '<head> => {}'.format(self.head.val)

    def __len__(self):
        return self._size

    def insert(self, val):
        self.head = Node(val, self.head)
        self._size += 1
        return self.head

    def find(self, val):
        temp = self.head
        while(temp):
            if temp.val == val:
                return temp
            temp = temp._next
        return False

    def append(self, val):
        """
        appends a value at the end of the linked list
        """
        temp = self.head
        while temp:
            temp = temp._next
        self.insert(val)
        self._size += 1
        return self._size

    def insert_before(self, val, newVal):
        """
        Add a new node with the given newValue immediately before the first value node
        """
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

    def remove(self, val):
        """Remove a node."""
        current = self.head
        previous = None
        while current:
            if current.val == val:
                if previous is None:
                    self.head = current._next
                    return current.val
                else:
                    previous._next = current._next
                    return current.val
            previous = current
            current = current._next
        return False

    def insert_after(self, value, newVal):
        """inserts a node after a specified node"""
        temp = self.head
        while temp:
            if temp.val == value:
                temp._next = Node('X', temp._next)
                self._size += 1
                return self._size
            temp = temp._next
        # if temp._next is None:
        #     raise ValueError("Data not in list")

    def kth_from_end(self, k):
        """
        takes in a value k and returns in the reverse 
        index position of that element in the array
        """
        if k <= self._size:
            r = self._size - k - 1
            temp = self.head
            while r > 0:
                temp = temp._next
                r -= 1
            return temp
        else:
            raise AttributeError('Your input value is larger than the linked list')
