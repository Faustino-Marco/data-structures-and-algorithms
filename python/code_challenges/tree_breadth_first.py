from data_structures.binary_tree import BinaryTree, Node
from data_structures.stack_and_queue.queue import Queue

def breadth_first(tree):
    """
    Write a function called breadth_first
    Arguments: tree
    Return: list of all values in the tree, in the order they were encountered
    """
    breadth_queue = Queue()
    breadth_queue.enqueue(tree.root)

    
    values = []

    def walk(root):
        values.append(root.value)

    return values
