class Node:
    """Node class definition."""

    def __init__(self, val=None):
        """Create an instance of Node object."""
        self.val = val
        self.children = []
        self._next = next

    def __repr__(self):
        """Node class representation."""
        return '<Node Val: {}>'.format(self.val)

    def __str__(self):
        """Node class string printout."""
        return 'Node Val: {}'.format(self.val)

class Queue:
    def __init__(self, iter=[]):
        self.front = None
        self.back = None
        self._length = 0

        if not isinstance(iter, (list, dict, tuple)):
            """ check for iterable """
            raise TypeError('It is not iterable.')
        for i in iter:
            self.enqueue(i)

    def enqueue(self, val):
        """ add a value, increase size by 1"""
        node = Node(val)
        if self._length == 0:
            self.front = self.back = node
            self._length += 1
            return node
        self.back.next = node
        self.back = node
        self._length += 1
        return node

    def dequeue(self):
        """ remove node from the front of queue """
        if self._length == 0:
            raise IndexError('You cannot dequeue() when front is empty')

        temp = self.front
        self.front = temp.next
        self._length -= 1
        return temp
    
class KTree:
    """Ktree class definition."""

    def __init__(self):
        """Create an instance of KTree object."""
        self.root = None

    def __repr__(self):
        """Ktree class representation."""
        return '<KTree Root Val: {}>'.format(self.root.val)

    def __str__(self):
        """Ktree class string printout."""
        return 'KTree Root Val: {}'.format(self.root.val)

    def pre_order(self, operation):
        """Ktree pre_order traversal."""
        def _walk(node=None):
            if node is None:
                return

            operation(node)

            for child in node.children:
                _walk(child)

        _walk(self.root)

    def post_order(self, operation):
        """Ktree post_order traversal."""
        def _walk(node=None):
            if node is None:
                return

            for child in node.children:
                _walk(child)

            operation(node)

        _walk(self.root)

    def breadth_first_traversal(self, operation):
        """Ktree breadth_first_traversal."""
        queue = Queue()
        queue.enqueue(self.root)
        while queue._length > 0:
            current = queue.dequeue()
            operation(current)
            for child in current.children:
                queue.enqueue(child)

    def insert(self, val, parent=None):
        """Insert a value at first instance of given parent."""
        if parent is None:
            if self.root is None:
                self.root = Node(val)
                return self.root
            raise ValueError('parent node is none.')

        node = Node(val)

        def _walk(curr=None):
            if curr is None:
                return

            if curr.val == parent:
                curr.children.append(node)
                return

            for child in curr.children:
                _walk(child)
                if node in child.children:
                    return
        _walk(self.root)