from node import node


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

    # 3 ways to Insert (at start)
    def insert(self, val):
        # node = Node(val, self.head)
        # self.head = node

        node = Node(val)
        node.next = self.head
        self.head = node
