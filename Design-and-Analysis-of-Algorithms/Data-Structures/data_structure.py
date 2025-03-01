import array

class Array():

    def __init__(self, type):
        self._array = array.array('type')
        self.size = 0

    # insert an element
    def insert(self, element, position=None):
        ''' Need to modify this to move the element and input validation try catch maybe sa GUI?'''

        if (position > self.size + 1 or position < 0):
            print("Invalid position!")
        
        # Add the element
        elif (position == None):
            self._array[self.size] = element
            self.size += 1 
        
        # Add the element
        else:
            self._array[position] = element
            self.size += 1
            # move the elements, slice the array




    # Traverse to know if the element exists
    def search(self, element):
        sortedArray = self.sort()
        left = 0
        right = self.size - 1
        while left <= right:
            mid = (left + right) // 2
            if sortedArray[mid] == element:
                return mid  # Element found, return its index immediately
            elif sortedArray[mid] < element:
                left = mid + 1
            else:
                right = mid - 1
        return -1  # Element not found


    def delete(self, element):
        # Check if it exists
        index = self.search(element)

        if (index != -1):
            #  Will these be arrays or lists?
            left = self._array[0:index]
            right = self._array[-1:index:-1]  

            # delete
            for i in range(self.size - 1):
                # decreased_arr[i] = 
                # decreased_arr is not gonna be an array but rather a list I think. 
                pass 

        else:
            pass
            # return a message that you cannot delete

    def sort(self, reversed = None):
        
        # copy the array so I won't have to change the unsorted array
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



