from data_structures.linked_list import LinkedList

class Hashtable:
    """
    set
        - Arguments: key, value
        - Returns: nothing
        This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
        Should a given key already exist, replace its value from the value argument given to this method.
    
    get
        - Arguments: key
        - Returns: Value associated with that key in the table
    
    has
        - Arguments: key
        - Returns: Boolean, indicating if the key exists in the table already.
    
    keys
        - Returns: Collection of keys
    
    hash
        - Arguments: key
        - Returns: Index in the collection for that key
    """

    def __init__(self, size=1024):
        # initialization here
        self.size = size
        self.buckets = [None] * size

    def get(self, key):
        # method body here
        values = []
        idx = self.hash(key)
        bucket = self.buckets[idx]
        if not bucket:
            return None
        current = bucket.head
        while current:
            if key == current.value[0]
                values.append(current.value[1])
            current = current.next
        if len(values) == 1:
            return values[0]
        if len(values) > 1:
            return tuple(values)
        return None

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


