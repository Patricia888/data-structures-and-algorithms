from queue import Queue


class Node:  # pragma: no cover
    """create a Node for a K-ary tree"""
    def __init__(self, val=None):
        self.val = val
        self.children = []

    def __repr__(self):
        return 'Node Val: {}'.format(self.val)

    def __str__(self):
        return f'Node value is {self.val}'
