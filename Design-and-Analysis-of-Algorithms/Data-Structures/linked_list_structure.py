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
    
    def display(self):
        if (self.head == None):
            print("Linked List is empty!")
        else:
            current_node = self.head
            while (current_node != None):
                print(current_node.data, end=" -> ")
                current_node = current_node.next
            print("None")

    def reverse(self):
        pass 

    def remove_duplicates(self, element):
        pass

    def delete(self, element):
        pass
    

if __name__ == '__main__':
    myLl = List()
    myLl.insert(2)
    myLl.insert(3)
    myLl.insert(1)
    myLl.insert(6)
    myLl.display()
