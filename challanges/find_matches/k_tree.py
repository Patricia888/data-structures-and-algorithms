from .queue import Queue


class Node:
    """
    Creating nodes for use in data structures
    """
    def __init__(self, val=None):
        """
        method called upon creation of node
        """
        self.val = val
        self.children = []

    def __repr__(self):
        """
        string representation of node for dev
        """
        return 'Node.val = {}'.format(self.val)

    def __str__ (self):
        """
        string representation of node for user
        """
        return self.val


class KTree:
    """ 
    class for the k-ary tree 
    """
    def __init__(self):
        """ initialization of the k-ary tree """
        self.root = None
        self._size = 0
    
    def __repr__(self):
        """
        string representation of root for dev
        """
        return 'Node.val = {}'.format(self.root.val)
    
    def __str__ (self):
        """
        string representation of node for user
        """
        return self.root.val

    def insert(self, parent_node_val, val = None):
        """
        method for inserting new nodes into k-ary tree 
        """
        queue = Queue()
        traverse = []

        node = Node(val)
        if self.root is None:
            self.root = node
            self._size += 1
            return

        queue.enqueue(self.root)
        while len(queue) > 0:
            current = queue.dequeue()
            if current.val == parent_node_val:
                current.children.append(node)
                self._size += 1
                return
            traverse.append(current.val)
            for child in current.children:
                queue.enqueue(child)
        return traverse

    def pre_order_traversal(self, function_lambda):
        """
        defines a method for traversing a k-ary tree, perfomring
        operations on each node as it is first reached
        """
        def _walk(node = None):
            if node is None:
                return
            
            function_lambda(node)

            for child in node.children:
                    _walk(child)
            
        _walk(self.root)

    def post_order_traversal(self, function_lambda = None):
        """
        defines a method for traversing a k-ary tree, performing
        operations on each node as it is last passed by
        """
        def _walk(node = None):
            if node is None:
                return

            for child in node.children:
                _walk(child)
            
            function_lambda(node)
            
        _walk(self.root)
    
    def breadth_first_traversal(self, function_lambda):
        """ 
        defines a method for traversing a k-ary tree from shallowest 
        to deepest level
        """

        queue = Queue()
        traverse = []

        queue.enqueue(self.root)
        while len(queue) > 0:
            current = queue.dequeue()
            function_lambda(current)
            traverse.append(current.val)
            for child in current.children:
                queue.enqueue(child)
        return traverse
