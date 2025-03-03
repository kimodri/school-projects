from array_structure import Array
import array

class Stack(Array):
    def __init__(self, type, capacity):
        super().__init__(type)
        self.capacity = capacity
        self._array = array.array(self.type, [0] * self.capacity)

    def push(self, element):
        if (self.size == self.capacity):
           print("Stack Overflow!")
           return None
        else:
           self._array[self.size] = element
           self.size += 1

    def pop(self):
        if (self.size <= 0):
            print("Stack Underflow!")
        else:
            self.size -= 1

    def modify(self, element, position = None):
        
        if (position == None):
            position = self.size

        if (position < 0 or position > self.size):
            print("Invalid position!")
            return None 
        
        self._array[position] = element
        
        return self._array
