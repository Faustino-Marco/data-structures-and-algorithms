from platform import node


class BinaryTree:
    """
    According to fixture in "test_binary_tree.py":
    ____________________________
                a
        b               c
    d       e       f       g
    ____________________________

    Methods:
    - pre_order()
        - Returns tree values in 'root-left-right' order

    - in_order()
        - Returns tree values in 'left-root-right' order

    - post_order()
        - Returns tree values in 'left-right-root' order
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


class Node:
    """
    Instantiate a tree node with `Node(value)`

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

