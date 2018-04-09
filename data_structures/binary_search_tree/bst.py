class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

    def __repr__(self):
        return #
            self.val, self.right.val, self.left.val)

    def __str__(self):
        return self.val


class BST:
    def __init__(self):
        self.root = None

    def __repr__():
        return '<BST Root {}>'.format(self.root.val)

    def __str__():
        return self.root.val

    def in_order(self, operation):
        def _walk(node=None):
            if node is None:
                return

            if node.left is not None:
                _walk(node.left)

            # in order, operation goes here
            # this is our lambda
            # can call it anything
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


            # else:


        return node
