class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.head = None
        self.tail = None

    def __str__(self):

        txt = ""

        #start at head
        current = self.head

        #loop while current exists
        while current:
            # do something
            txt += f"{{ {current.value} }} -> "
            print(txt)
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

    def append(self, value):
        # new_node = Node(value)

        # self.tail.next = new_node
        # self.tail = new_node

        new_node = Node(value)

        # start at head
        current = self.head
        # while current exists
        while current:
            # if current has no next
            if not current.next:
                # change current.next to new node
                current.next = new_node

                break
            else:
                # proceed to next node
                current = current.next


    def insert_before(self, search_val, value):
        new_node = Node(value)

        if not self.head:
            raise TargetError

        if self.head.value == search_val:
            self.insert(value)
            return

        # start at head
        current = self.head
        # while head exists
        while current and current.next:
            # if current node's next has value in input
            if current.next.value == search_val:
                # change new node next to current next
                new_node.next = current.next
                # change current next to new node
                current.next = new_node
                # get out of loop
                return
                #DANGER!!
            # otherwise keep looking
            else:
                current = current.next
        raise TargetError


    def insert_after(self, search_val, value):
        # new_node = Node(value)

        #start at head
        current = self.head
        if not self.head:
            raise TargetError

        # if head exists
        while current:
            # if current value is our search val
            if current.value == search_val:
                self.insert_before(current.next.value, value)
                return
            else:
                current = current.next
        raise TargetError

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class TargetError(Exception):
    pass
