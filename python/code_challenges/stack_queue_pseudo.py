from data_structures.stack_and_queue.stack import Stack

class PseudoQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.top = None
    
    def enqueue(self, value):
        storage_stack = Stack()

        current = self.top

        if not self.top:
            Stack.push(self, value)
            
        # else:
        #     while current:
        #         if 
        #         storage_stack.push(Stack.pop())

        #     old_rear = self.rear
        #     old_rear.next = new_rear
        #     self.rear = new_rear






        # stg_stk = Stack()
        # if Stack.is_empty() is not True:
        #     if self.top.next == None:
        #         self.top.next = value
        #         return
        #     else:
        #         stg_stk.push(Stack.pop())






    def dequeue(self):
        Stack.pop(self)
        # if not self.front:
        #     raise InvalidOperationError
        # else:
        #     # remove front
        #     # reset front
        #     # return value
        #     old_front = self.front
        #     self.front = self.front.next
        #     return old_front.value
        
    def is_empty(self):
        if not self.top:
            return True



class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

class InvalidOperationError(Exception):
    pass

