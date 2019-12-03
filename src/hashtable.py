# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0
        self.grown = False


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.
        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return self._hash_djb2(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash
        OPTIONAL STRETCH: Research and implement DJB2
        '''
        hash_value = 5381
    
        for char in key:
            hash_value = ((hash_value << 5)+hash_value) + ord(char)
        return hash_value


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def _update_size(self):
        ratio = self.count/self.capacity
        if ratio>.7:
            self.resize()
            self.grown = True
        elif ratio<.2 and self.grown:
            self.resize(.5)
        else:
            return

    def insert(self, key, value, cache=None, resize = False):
        '''
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Fill this in.
        '''
        if cache == None:
            cache = self.storage
            
        index = self._hash_mod(key)
        pair = LinkedPair(key, value)
        
        if cache[index] != None:
            # Add next handling
            cur_pair = cache[index]
            if cur_pair.key ==key:
                cur_pair.value=value
                return
            while cur_pair.next != None:
                cur_pair = cur_pair.next
                if cur_pair.key==key:
                    cur_pair.value=value
                    return
            
            cur_pair.next = pair
        else:
            cache[index] = pair
            
        self.count += 1
        if not resize:    
            self._update_size()


    def remove(self, key):
            '''
            Remove the value stored with the given key.
            Print a warning if the key is not found.
            Fill this in.
            '''
            index = self._hash_mod(key)
            if self.storage[index] == None:
                print("Error: nothing at that index")
                return
            elif self.storage[index].key == key:
                self.storage[index] = self.storage[index].next
                self.count-=1
                self._update_size()
                return
            else:
                cur_pair = self.storage[index]
                while cur_pair.next:
                    if cur_pair.next.key == key:
                        cur_pair.next = cur_pair.next.next
                        self.count-=1
                        self._update_size()
                        return
                    else:
                        cur_pair = cur_pair.next
            print("Error: that key does not exist")


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Fill this in.
        '''
        
        index = self._hash_mod(key)
        if self.storage[index] == None:
            return None
        
        elif self.storage[index].key != key:
            cur_pair = self.storage[index]
            while cur_pair.next is not None:
                cur_pair = cur_pair.next
                if cur_pair.key == key:
                    return cur_pair.value
            return None
        else:
            return self.storage[index].value


    def resize(self, factor=2):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Fill this in.
        '''
        temp = float(self.capacity)
        self.capacity= int(temp*factor)
        new_storage = [None]*self.capacity
        self.count = 0
        for head in self.storage:
            if head:
                self.insert(head.key, head.value, new_storage, True)
                while head.next:
                    head = head.next
                    self.insert(head.key, head.value, new_storage, True)
        self.storage = new_storage



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")
    print(ht._hash_djb2("Adam"))
    # print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
