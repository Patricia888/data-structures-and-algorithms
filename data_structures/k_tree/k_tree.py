from .queue import Queue


class Node:
    """Node for the k-ary tree"""
    def __init__(self, val=None):
        self.val = val
        self.children = []

    def __repr__(self):
        return 'Node Val: {}'.format(self.val)

    def __str__(self):
        return f'Node value is {self.val}'


class KTree:
    """Create a K-ary tree"""
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
        """Breadth-first traversal"""
        queue = Queue()
        traverse = []

        queue.enqueue(self.root)
        while len(queue) > 0:
            current = queue.dequeue()
            traverse.append(current.val)
            for child in current.children:
                queue.enqueue(child)
        return traverse

    def breadth_first_traversal_op(self, operation):
        """Breadth-first traversal"""
        queue = Queue()

        queue.enqueue(self.root)
        while len(queue) > 0:
            current = queue.dequeue()
            operation(current)
            for child in current.children:
                queue.enqueue(child)

    def insert(self, val, parent):
        """
        A node is inserted into the K-ary tree at the first instance of the indicated parent value
        """
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

    def insert_all(self, val, parent):
        """
        A node is inserted into the K-ary tree at all instances of the indicated parent value
        """
        node = Node(val)
        queue = Queue()

        if parent is None:
            if self.root is None:
                self.root = node
                return f'{val} inserted at root'
            raise ValueError('Parent value not found')

        current = self.root
        queue.enqueue(self.root)
        count = 0

        while queue:
            current = queue.dequeue()
            if current.val == parent:
                current.children.append(node)
                count += 1
            for child in current.children:
                queue.enqueue(child)
        if count == 0:
            raise ValueError('Parent value not found')
        return f'{val} inserted {count} times'
