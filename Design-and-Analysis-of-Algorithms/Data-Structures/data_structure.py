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
        pass 


        # ''' Need to modify this to move the element and input validation try catch maybe sa GUI?'''

        # # Modification with dynamic array this time

        # if (position == None):
        #     position = self.size

        #     self._array[self.size] = element
        #     self.size += 1 

        # elif (position > self.size + 1 or position < 0):
        #     print("Invalid position!")
        #     return None
        
        # # Add the element
        # else:
        #     #  Bago mo iinsert move mo muna by slicing
        #     left = self._array[0:position]
        #     right = self._array[position:]

        #     addedArray = array.array('i', [])
            
        #     index = 0
        #     for element in left:
        #         addedArray[index] = element
        #         index += 1

        #     addedArray[position] = element
        #     index += 1
            
        #     for element in right:
        #         addedArray[index] = element
        #         index += 1

        #     self._array[position] = element
        #     self.size += 1
    
    # Traverse to know if the element exists
    def search(self, element):
        sortedArray = self.sort()

        if (sortedArray == None):
            return None 
        else:
            left = 0
            right = self.size - 1
            while left <= right:
                mid = (left + right) // 2
                if sortedArray[mid] == element:
                    return mid  
                elif sortedArray[mid] < element:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1  # Element not found


    def delete(self, element):

        # Needs modification if there is a duplicate
        # Check if it exists
        index = self.search(element)

        if (index == None):
            # return None
            print("Array is empty") #?

        elif (index != -1):
            left = self._array[0:index]
            right = self._array[index + 1:]  

            decreasedArr = array.array("i", [])                  
           
           # delete
            index = 0
            for element in left:
                decreasedArr[index] = element
                index += 1
            for element in right:
                decreasedArr[index] = element
                index += 1
        else:
            print("The element does not exist!")
            

    def sort(self, reversed = None):
        
        # copy the array so I won't have to change the unsorted array
        if (self.size == 0):
            print("Array is empty!")
            return None

        else:
            copiedArray = self._array[:]
            # bubble sort
            # ascending sort
            n = self.size
            if (reversed == None):
                for i in range(n):
                    swapped = False
                    for j in range(0, n - i - 1):
                        if copiedArray[j] > copiedArray[j + 1]:
                            copiedArray[j], copiedArray[j + 1] = copiedArray[j + 1], copiedArray[j]
                            swapped = True
                    if not swapped:
                        break
                return copiedArray

            # descending sort
            else:
                for i in range(n):
                    swapped = False
                    for j in range(0, n - i - 1):
                        if copiedArray[j] < copiedArray[j + 1]:
                            copiedArray[j], copiedArray[j + 1] = copiedArray[j + 1], copiedArray[j]
                            swapped = True
                        if not swapped:
                            break
                return copiedArray



