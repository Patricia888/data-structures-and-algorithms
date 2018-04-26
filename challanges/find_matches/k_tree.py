from .queue import Queue


class Node:  #pragma: no cover
    """create a Node"""
    def __init__(self, val=None):
        self.val = val
        self.children = []

    def __repr__(self):
        return 'Node Val: {}'.format(self.val)

    def __str__(self):
        return f'Node value is {self.val}'


class KTree:  #pragma: no cover
    """create a K-ary tree"""
    def __init__(self):
        self.root = None

    def __repr__(self):
        return '<Tree Root {}>'.format(self.root.val)

    def __str__(self):
        return f'Tree root value is {self.root.val}'

    def pre_order_traversal(self, operation):
        """Pre-order traversal"""
        def _walk(node=None):
            if node is None:
                return

            operation(node)

            for child in node.children:
                _walk(child)

        _walk(self.root)

    def post_order_traversal(self, operation):
        """Post-order traversal"""
        def _walk(node=None):
            if node is None:
                return

            for child in node.children:
                _walk(child)

            operation(node)

        _walk(self.root)

    def breadth_first_traversal(self):
        """Return breadth-first-traversal"""
        queue = Queue()
        traverse = []

        queue.enqueue(self.root)
        while len(queue) > 0:
            current = queue.dequeue()
            traverse.append(current.val)
            for child in current.children:
                queue.enqueue(child)
        return traverse

    def insert(self, val, parent):
        """Insert node into K-ary tree"""
        node = Node(val)
        current = self.root

        if parent is None:
            if self.root is None:
                self.root = node
                return node
            raise ValueError('Parent value not found')

        def _walk(current=None):
            if current.val == parent:
                current.children.append(node)
                return node
            for child in current.children:
                inserted = _walk(child)
                if inserted:
                    return inserted

        node = _walk(self.root)
        if node is None:
            raise ValueError('Parent value not found')
        return node
