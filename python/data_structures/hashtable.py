from data_structures.linked_list import LinkedList

class Hashtable:
    """
    Put docstring here
    """

    def __init__(self, size):
        # initialization here
        self.size = size

    def get(self, key):
        # method body here
        pass

    def set(self, key, value):
        index = self.hash(key)
        bucket = self.buckets[index]
        if not bucket:
            bucket = LinkedList()
            self.buckets[index] = bucket
        kvp = (key, value)
        bucket.insert(kvp)

    def contains(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]
        if not bucket:
            return False

        current = bucket.head
        while current:
            kvp = current.value
            if kvp[0] == key:
                return True
            current = current.next
        
        return False

    def keys(self):
        gathered_keys = []
        for bucket in self.buckets:
            if bucket:
                current = bucket.head
                while current:
                    kvp = current.value
                    gathered_keys.append(kvp[0])
        return gathered_keys


    def hash(self, key):
        # add ascii values of each char together
        ascii_values = [ord(char) for char in key]
        ascii_sum = sum(ascii_values)

        primed = ascii_sum * 599
        index = primed % self.size

        return index # in range aka between 0 and the size - 1


