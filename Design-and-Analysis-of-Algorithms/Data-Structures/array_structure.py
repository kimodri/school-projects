import array

class Array():

    def __init__(self, type):
        self.type = type
        self._array = array.array(type)
        self.size = 0
        self.capacity = 4

    def resize(self):
        self.capacity *= 2
        new_array = array.array(self.type, [0] * self.capacity)
        for i in range(self.size):
            new_array[i] = self._array[i]
        self._array = new_array

    # insert an element
    def insert(self, element, position = None):
        if (position == None):
            position = self.size

        if (position < 0 or position > self.size):
            print("Invalid position!")
            return None 

        if (self.size == self.capacity):
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
 
    # Traverse to know if the element exists
    def search(self, element):
        if (self._array == None):
            return None
        else:
            for i in range(self.size):
                if (self._array[i] == element):
                    return i 
            return -1

    def delete(self, element):
        # Check if it exists
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

            # delete
            index = 0
            for el in left:
                decreasedArr[index] = el
                index += 1
            for el in right:
                decreasedArr[index] = el
                index += 1
            self._array = decreasedArr
            
            #check for duplicates, and only recurse if element exists.
            if self.search(element) != -1:
                self.delete(element)

        else:
            print("The element does not exist!")
            return None

    def sort(self, reversed = None):
        # copy the array so I won't have to change the unsorted array
        if (self.size == 0):
            print("Array is empty!")
            return None

        else:
            sorted_array = self._array[:]
            # bubble sort
            # ascending sort
            n = self.size
            if (reversed == None):
                for i in range(n):
                    swapped = False
                    for j in range(0, n - i - 1):
                        if sorted_array[j] > sorted_array[j + 1]:
                            sorted_array[j], sorted_array[j + 1] = sorted_array[j + 1], sorted_array[j]
                            swapped = True
                    if not swapped:
                        break
                return sorted_array

            # descending sort
            else:
                for i in range(n):
                    swapped = False  # Reset swapped here, before the inner loop.
                    for j in range(0, n - i - 1):
                        if sorted_array[j] < sorted_array[j + 1]:
                            sorted_array[j], sorted_array[j + 1] = sorted_array[j + 1], sorted_array[j]
                            swapped = True
                    if not swapped:
                        break
                return sorted_array
            


        # we should not use the sorted array because the index elements are not the representation
        # of the original array
        # sorted_array = self.sort()

        # if (sorted_array == None):
        #     return None 
        # else:
        #     left = 0
        #     right = self.size - 1
        #     while left <= right:
        #         mid = (left + right) // 2
        #         if sorted_array[mid] == element:
        #             return mid  
        #         elif sorted_array[mid] < element:
        #             left = mid + 1
        #         else:
        #             right = mid - 1
        #     return -1  # Element not found