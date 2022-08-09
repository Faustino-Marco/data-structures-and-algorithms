from data_structures.binary_tree import BinaryTree, Node


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
        """
        super().__init__() from ancestor BinaryTree class
        """
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

            if node_to_add.value < root.value:
                if root.left is None:
                    print("no root.left, adding now")
                    root.left = node_to_add
                else:
                    print("root.left taken, walking left")
                    walk(root.left, node_to_add)
            if node_to_add.value > root.value:
                if root.right is None:
                    print("no root.right, adding now")
                    root.right = node_to_add                 
                else:
                    print("root.right taken, walking right")
                    walk(root.right, node_to_add)

        walk(self.root, node)


    def contains(self, target):
        """
        Argument: value
        Returns: boolean indicating whether or not the value is in the tree at least once.
        """
        def walk(root):
            if root is None:
                return False

            if root.value == target:
                return True

            if target < root.value:
                return walk(root.left)
            else:
                return walk(root.right)

        return walk(self.root)


##### IMPORT NODE FROM BINARY TREE (SEE IMPORTS) #####
# class Node:
#     """
#     Instantiate a tree node with `Node(value)`

#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#     """
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None