from data_structures.binary_tree import BinaryTree, Node
from data_structures.stack_and_queue.queue import Queue

def breadth_first(tree):
    """
    Write a function called breadth_first
    Arguments: tree
    Return: list of all values in the tree, in the order they were encountered
    """
    
    print('hello world')
    breadth_queue = Queue()
    values = []
    
    if tree.root is not None:
        print(tree.root.value)  
        breadth_queue.enqueue(tree.root)
        print(breadth_queue.front.value.value)

    if not tree.root: 
        return values

    while not breadth_queue.is_empty():

        values.append(breadth_queue.front.value.value)

        front_node = breadth_queue.front.value

        if front_node.left:
            
            breadth_queue.enqueue(front_node.left)

        if front_node.right:
            
            breadth_queue.enqueue(front_node.right)
   
        breadth_queue.dequeue()
        # front_node = breadth_queue.front

    return values
