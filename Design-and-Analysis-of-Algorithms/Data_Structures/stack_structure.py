from array_structure import Array # Assuming array_structure.py contains the Array class
import array

class Stack(Array):
    def __init__(self, type, capacity):
        """
        Initializes a Stack object, inheriting from the Array class.
        """
        super().__init__(type)
        self.capacity = capacity
        self._array = array.array(self.type, [0] * self.capacity)

    def push(self, element):
        """
        Pushes an element onto the top of the stack.
        """
        if self.size == self.capacity:
            print("Stack Overflow!")
            return None
        else:
            self._array[self.size] = element
            self.size += 1

    def pop(self):
        """
        Pops the element from the top of the stack.
        """
        if self.size <= 0:
            print("Stack Underflow!")
        else:
            self.size -= 1

    def modify(self, element, position=None):
        """
        Modifies an element at a specified position in the stack.
        """
        if position is None:
            position = self.size

        if position < 0 or position > self.size:
            print("Invalid position!")
            return None

        self._array[position] = element

        return self._array