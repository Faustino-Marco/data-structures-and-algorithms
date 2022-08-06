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
        # method body here

        # will build up alues in pre-order style
        values = []



        def walk(root):

            # don't be a space case, remember the base case

            if root is None:
                return 
            # root - left - right

            # do the root (aka whatever job you're doing)
            values.append(root.value_)

            # left
            walk(root.left)

            # right 
            walk(root.right)

        walk(self.root)


            return values

        return walk(self.root)


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


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

