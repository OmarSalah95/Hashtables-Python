

class dynamic_array:

    def __init__(self, capacity=8):
        self.count = 0
        self.capacity = capacity
        self.storage = [None] * self.capacity # Allocates memeory
        
    def delete(self, index):
        if index >= self.count:
            print("Error: Out of range")
        for i in range(index, self.count-1, 1):
            self.storage[i] =self.storage[i+1]    
        self.count -= 1
            
    def insert(self, index, value):
        if self.count > self.capacity:
            #TODO : Make the array re-size
            print("Error: The array is full")
            return
        
        if index >= self.count:
            print("Error: out of range.")
        # Shift everything over to the right
        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i - 1]
        
        self.storage[index] = value
        self.count += 1
        
    def append(self, value):    
        self.insert(self.count, value)
        
    def prepend(self, value):
            self.insert(0, value)
            

    def double_size(self):
        self.capacity *= 2
        new_storage = [None] * self.capacity
        for i in range(self.count):
            new_storage[i] = self.storage[i]
        self.storage = new_storage        

my_new_array = dynamic_array(3)
my_new_array.insert(0, 7)
my_new_array.insert(1, 3)
my_new_array.insert(2, 8)
print(my_new_array.storage)
my_new_array.delete(2)
my_new_array.insert(0, 2)
print(my_new_array.storage)

