from data_structures.stack_and_queue.queue import Queue


class KaryTree:
    def __init__(self, root=None):
        self.root = root


    def clone(self):
        if not self.root:
            return KaryTree()
        
        breadth = Queue()
        breadth.enqueue(self.root)
        clone_root = Node(self.root.value)
        while breadth: # is not empty
            front = breadth.dequeue()
            for child in front.children:
                breadth.enqueue(child)
                #create clone node
                clone_node = Node(child.value)
                clone_root.children.append(clone_node)
        
        return KaryTree(root=clone_root)


    def breadth_first(self):
        queue = Queue()

        collection = []

        queue.enqueue(self.root)

        while not queue.is_empty():
            node = queue.dequeue()

            #double odd
            if node.value % 2 == 1:
                node.value *= 2
            collection.append(node.value)
            for child in node.children:
                queue.enqueue(child)

        return collection


class Node:
    """K-Ary Tree Node"""

    def __init__(self, value):
        self.value = value
        self.children = []
