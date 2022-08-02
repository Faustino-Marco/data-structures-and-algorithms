from data_structures.stack_and_queue.stack import Stack

class PseudoQueue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, value):
        new_rear = Node(value)
        if not self.rear:
            self.rear = new_rear
            self.front = new_rear
        else:
            old_rear = self.rear
            old_rear.next = new_rear
            self.rear = new_rear

    def dequeue(self):
        if not self.front:
            raise InvalidOperationError
        else:
            # remove front
            # reset front
            # return value
            old_front = self.front
            self.front = self.front.next
            return old_front.value

class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

class InvalidOperationError(Exception):
    pass
