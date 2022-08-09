from data_structures.binary_tree import BinaryTree, Node
from data_structures.stack_and_queue.queue import Queue

def breadth_first(tree):
    """
    Write a function called breadth_first
    Arguments: tree
    Return: list of all values in the tree, in the order they were encountered
    """
    breadth_queue = Queue()
    values = []
    
    if tree.root is not None:
        breadth_queue.enqueue(tree.root)
    else: 
        return

    while not breadth_queue.is_empty():
        front_node = breadth_queue.dequeue()
        values.append(front_node.value)
        
        if front_node.left:
            breadth_queue.enqueue(front_node.left)
        
        if front_node.right:
            breadth_queue.enqueue(front_node.right)
   


    return values
