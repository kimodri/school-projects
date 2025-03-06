import array
class Array:
    def __init__(self, type):
        """
        Initializes an Array object.
        """
        self.type = type
        self._array = array.array(type)
        self.size = 0
        self.capacity = 4

    def resize(self):
        """
        Resizes the underlying array by doubling its capacity.
        """
        self.capacity *= 2
        new_array = array.array(self.type, [0] * self.capacity)
        for i in range(self.size):
            new_array[i] = self._array[i]
        self._array = new_array

    def insert(self, element, position=None):
        """
        Inserts an element into the array at a specified position.
        """
        if position is None:
            position = self.size

        if position < 0 or position > self.size:
            print("Invalid position!")
            return None

        if self.size == self.capacity:
            self.resize()

        new_array = array.array(self.type, [0] * self.capacity)

        for i in range(position):
            new_array[i] = self._array[i]

        new_array[position] = element

        for i in range(position, self.size):
            new_array[i + 1] = self._array[i]

        self.size += 1

        perfect_array = array.array('i', [0] * self.size)

        for i in range(self.size):
            perfect_array[i] = new_array[i]

        self._array = perfect_array

        return self._array

    def search(self, element):
        """
        Searches for an element in the array.
        """
        if self._array is None:
            return None
        else:
            for i in range(self.size):
                if self._array[i] == element:
                    return i
            return -1

    def delete(self, element):
        """
        Deletes an element from the array.
        """
        index = self.search(element)

        if index is None:
            if self.size == 0:
                print("Array is empty")
            return None
        elif index != -1:
            left = self._array[0:index]
            right = self._array[index + 1:]
            self.size -= 1
            decreasedArr = array.array("i", [0] * self.size)

            index = 0
            for el in left:
                decreasedArr[index] = el
                index += 1
            for el in right:
                decreasedArr[index] = el
                index += 1
            self._array = decreasedArr

            if self.search(element) != -1:
                self.delete(element)

        else:
            print("The element does not exist!")
            return None

    def sort(self, reversed=None):
        """
        Sorts the array in ascending or descending order using bubble sort.
        """
        if self.size == 0:
            print("Array is empty!")
            return None
        else:
            sorted_array = self._array[:]
            n = self.size
            if reversed is None:
                for i in range(n):
                    swapped = False
                    for j in range(0, n - i - 1):
                        if sorted_array[j] > sorted_array[j + 1]:
                            sorted_array[j], sorted_array[j + 1] = sorted_array[j + 1], sorted_array[j]
                            swapped = True
                    if not swapped:
                        break
                return sorted_array
            else:
                for i in range(n):
                    swapped = False
                    for j in range(0, n - i - 1):
                        if sorted_array[j] < sorted_array[j + 1]:
                            sorted_array[j], sorted_array[j + 1] = sorted_array[j + 1], sorted_array[j]
                            swapped = True
                    if not swapped:
                        break
                return sorted_array

    def display(self):
        """
        Displays the elements of the array.
        """
        print([self._array[i] for i in range(self.size)])
