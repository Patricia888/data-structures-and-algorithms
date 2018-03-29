from node import Node


# can pass in a collection of elements
class LinkedList:
    """
    Single linked list
    """
    def __init__(self, iter=[]):
        # below will use later
        # self._current = None
        self.head = None
        self._size = 0 # or length

    # l = LinkedList([1, 2, 3, 4])
    for item in reversed(iter):
        self.insert(item)
    # l.head => 1 => 2 => 3 => 4
    # puts in front, instead of end

    def __repr__(self):
        # assuming head will have a val
        return '<head> => {}'.format(self.head.val)

    def __len__(self):
        return self._size
