from data_structures.binary_tree import BinaryTree


class BinarySearchTree(BinaryTree):
    """
    This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods: 

    - Add
        - Arguments: value
        - Return: nothing
        - Adds a new node with that value in the correct location in the binary search tree.

    - Contains
        - Argument: value
        - Returns: boolean indicating whether or not the value is in the tree at least once.
    """

    def __init__(self):
        # initialization here
        super().__init__()

    def add(self, value):
        """
        Arguments: value
        Return: nothing
        Adds a new node with that value in the correct location in the binary search tree.
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