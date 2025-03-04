import array

class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class List:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, element, position = None):
        new_node = Node(element)
        if (position == None): # this is appending
            position = self.size

            if (self.head == None):
                self.head = new_node
                return None

            last_node = self.head
            while (last_node.next != None):
                last_node = last_node.next 
            last_node.next = new_node
            self.size += 1
            return None #?

        if (position < 0 or position > self.size):
            print("invalid position!")
            return None
        
        elif (position == 0):
            # Prepending
            temp_node, self.head = self.head, new_node
            self.head.next = temp_node
            self.size += 1
        else:
            # insert anywhere
            count = 0
            last_node = self.head
            while last_node is not None:
                if count == position - 1:
                    new_node.next = last_node.next
                    last_node.next = new_node
                    self.size += 1
                    return  # Stop after inserting
                last_node = last_node.next
                count += 1
    
    def display(self, head = None):
        if (head == None):
            head = self.head

        if (head == None):
            print("Linked List is empty!")
            return None
        
        else:
            current_node = head
            while (current_node != None):
                print(current_node.data, end=" -> ")
                current_node = current_node.next
            print("None")

    def reverse(self):
        if (self.head == None):
            print("No existing List")
            return None
        else:
            prev, curr = None, self.head
            while (curr != None):
                temp = curr.next
                curr.next = prev 
                prev = curr 
                curr = temp
        self.display(prev)


    def remove_duplicates(self, element):
        # I need type kapag array
        arr = array.array()  


    def delete(self, element):
        # if you want to delete you must remove the duplicates first
        if (self.head == None):
            print("No existing list!")
            return None 
        else:
            pass
    

if __name__ == '__main__':
    myLl = List()
    myLl.insert(1)
    myLl.insert(2)
    myLl.insert(3)
    myLl.insert(4)
    myLl.display()
    myLl.reverse()
