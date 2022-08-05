from data_structures.stack_and_queue.queue import Queue
from data_structures.invalid_operation_error import InvalidOperationError

class AnimalShelter:
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()

    def enqueue(self, animal):
        if animal.animal_type == "dog":
            self.dogs.enqueue(animal)
        
        elif animal.animal_type == "cat":
            self.cats.enqueue(animal)

        else:
            raise InvalidOperationError()

    def dequeue(self, pref):
        if pref == "dog":
            return self.dogs.dequeue()
        
        if pref == "cat":
            return self.cats.dequeue()
        
        else:
            return None


class Dog:
    def __init__(self, next_=None):
        self.animal_type = "Dog"

class Cat:
    def __init__(self, next_=None):
        self.animal_type = "Cat"
       

