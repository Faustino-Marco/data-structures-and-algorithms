class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.head = None

    def __str__(self):

        txt = ""

        #start at head
        current = self.head

        #loop while current exists
        while current:
            # do something
            txt += f"{{ {current.value} }} -> "
        
            current = current.next

        return txt + "NULL"

    def includes(self, target):
        current = self.head
        while current:
            if current.value == target:
                return True
            current = current.next
        
        return False

    def insert(self, value):
        """
        create a node with given value
        set new node's next to be the list's head
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

class Node:
    def __init__(self, value, next=None):
        self.value = value
        

class TargetError:
    pass
