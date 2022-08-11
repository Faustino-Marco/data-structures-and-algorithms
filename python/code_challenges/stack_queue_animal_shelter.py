from data_structures.queue import Queue
from data_structures.invalid_operation_error import InvalidOperationError

class AnimalShelter:
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()

    def enqueue(self, animal):
        if animal.animal_type == "dog":
            print("doggggggg")
            self.dogs.enqueue(animal)
        
        if animal.animal_type == "cat":
            self.cats.enqueue(animal)

        if not animal.animal_type:
            print("wtf")
            raise InvalidOperationError

    def dequeue(self, pref):
        if pref == "dog":
            return self.dogs.dequeue()
        
        if pref == "cat":
            return self.cats.dequeue()
        
        else:
            return None


class Dog:
    def __init__(self):
        self.animal_type = "dog"

class Cat:
    def __init__(self):
        self.animal_type = "cat"
       

