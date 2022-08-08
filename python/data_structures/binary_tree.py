from platform import node


class BinaryTree:
    """
                a
        b               c
    d       e       f       g
    """

    def __init__(self):
        # initialization here
        self.root = None

    def pre_order(self):
        # root - left - right

        # will build up values in pre-order style
        values = []

        def walk(root):

            # don't B a space case, remember the base case
            if root is None:
                return 

            # do the root (aka whatever job you're doing)
            values.append(root.value)

            # left
            walk(root.left)

            # right 
            walk(root.right)

            return values

        # walk(self.root)

        return walk(self.root)

    def in_order(self):
        # left - root - right

        # value storage
        values = []

        #walkthrough method
        def walk(root):

            #don't B a space case
            if root is None:
                return

            # left
            walk(root.left)

            # root
            values.append(root.value)

            # right
            walk(root.right)

        walk(self.root)

        return values
    

    def post_order(self):
        values = []

        def walk(root):
            if root is None:
                return
            
            # left
            walk(root.left)

            # right
            walk(root.right)

            # root
            values.append(root.value)

        walk(self.root)

        return values


    def add(self, value):
        """
        wrap the value in a Node and add it at the correcet spot
        """

        node = Node(value)

        if not self.root:
            self.root = node
        
        def walk(root, node_to_add):
            if root is None:
                return 
        def walk(root, node_to_add):
            pass
            
        walk(self.root, node)


    def contains(self):
        """
        Argument: value
        Returns: boolean indicating whether or not the value is in the tree at least once.
        """
        pass


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

