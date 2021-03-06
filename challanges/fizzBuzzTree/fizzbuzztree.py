class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

    def __repr__(self):
        return self.val, self.right.val, self.left.val

    def __str__(self):
        return self.val


class BST:
    def __init__(self, iterable=[]):
        self.root = None
        if type(iterable) is not list:
            raise TypeError
        for item in iterable:
            self.insert(item)

    def __repr__(self):
        return '<BST Root {}>'.format(self.root.val)

    def __str__(self):
        return self.root.val

    def in_order(self, operation):
        def _walk(node=None):
            if node is None:
                return

            if node.left is not None:
                _walk(node.left)

            operation(node)

            if node.right is not None:
                _walk(node.right)

        _walk(self.root)

    def insert(self, val):
        node = Node(val)
        current = self.root

        if self.root is None:
            self.root = node
            return node

        while current:
            if val >= current.val:
                if current.right is not None:
                    current = current.right
                else:
                    current.right = node
                    break

            elif val < current.val:
                if current.left is not None:
                    current = current.left
                else:
                    current.left = node
                    break

        return node

    def pre_order(self, operation):
        def _walk(node=None):
            if node is None:
                return

            operation(node)

            if node.left is not None:
                _walk(node.left)

            if node.right is not None:
                _walk(node.right)

        _walk(self.root)

    def post_order(self, operation):
        def _walk(node=None):
            if node is None:
                return

            if node.left is not None:
                _walk(node.left)

            if node.right is not None:
                _walk(node.right)

            operation(node)

        _walk(self.root)


def fizzbuzztree(tree):
    '''conduct fizzbuzz on all appropriate tree nodes'''
    tree.in_order(replace)
    return tree


def replace(node):
    if type(node.val) is int:
        if node.val % 3 == 0 and node.val % 5 == 0:
            node.val = 'fizz buzz'
        elif node.val % 3 == 0:
            node.val = 'fizz'
        elif node.val % 5 == 0:
            node.val = 'buzz'
    return
