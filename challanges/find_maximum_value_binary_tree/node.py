class Node:
    """create a node"""
    def __init__(self, val, next=None):
        self.val = val
        self._next = next
        if val is None:
            raise TypeError('Must pass a value')

    def __repr__(self):
        return '{val}'.format(val=self.val)

    def __str__(self):
        return '{val}'.format(val=self.val)
