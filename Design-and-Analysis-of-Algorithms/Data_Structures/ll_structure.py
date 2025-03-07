class Node:
    def __init__(self, data):
        """
        Initializes a Node object.
        """
        self.data = data
        self.left = None
        self.right = None
        self.next = None

class List:
    def __init__(self):
        """
        Initializes a List object.
        """
        self.head = None
        self.size = 0

    def insert(self, element, position=None):
        """
        Inserts an element into the list at a specified position.
        """
        new_node = Node(element)

        # Appending
        if position is None:
            position = self.size

            if self.head is None:
                self.head = new_node
                return None
            
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = new_node
            self.size += 1
            return None

        if position < 0 or position > self.size:
            print("invalid position!")
            return None

        # Prepending
        elif position == 0:
            temp_node, self.head = self.head, new_node
            self.head.next = temp_node
            self.size += 1
        
        # Specified Position
        else:
            count = 0
            last_node = self.head
            while last_node is not None:
                if count == position - 1:
                    new_node.next = last_node.next
                    last_node.next = new_node
                    self.size += 1
                    return
                last_node = last_node.next
                count += 1

    def display(self, head=None):
        """
        Displays the elements of the list.
        """
        if head is None:
            head = self.head

        if head is None:
            print("Linked List is empty!")
            return None

        else:
            current_node = head
            while current_node is not None:
                print(current_node.data, end=" -> ")
                current_node = current_node.next
            print("None")

    def copy_list(self):
        """
        Creates and returns a copy of the list
        """
        if self.head is None:
            return None

        # Create the new head with the same data as the original head
        new_head = Node(self.head.data)
        new_current = new_head
        current = self.head.next

        # Copy each node
        while current:
            new_node = Node(current.data)
            new_current.next = new_node
            new_current = new_node
            current = current.next

        return new_head

    def reverse_copy_and_display(self):
        """
        Reverses a copy of the list and displays it
        """
        copy_head = self.copy_list()
        if copy_head is None:
            print("Linked List is empty!")
            return

        prev, curr = None, copy_head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        self.display(prev)

    def remove_duplicates(self):
        """
        Removes duplicate elements from the list.
        """
        if self.head is None:
            print("No existing list!")
            return None
        current = self.head

        while current:
            runner = current
            while runner.next:
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next

    def search(self, element):
        """
        Searches for an element in the list.
        """
        if self.head is None:
            print("No list exists!")
            return
        if self.head.data == element:
            return True
        last_node = self.head
        while last_node:
            if last_node.data == element:
                return True
            last_node = last_node.next
        return False

    def delete(self, element):
        """
        Deletes an element from the list.
        """
        if self.head is None:
            print("No existing list!")
            return
        if self.search(element):
            if self.head.data == element:
                self.head = self.head.next
                self.size -= 1
                return
            last_node = self.head
            while last_node.next:
                if last_node.next.data == element:
                    last_node.next = last_node.next.next
                    self.size -= 1
                    if self.search(element) is not False:
                        self.delete(element)
                    else:
                        return
                last_node = last_node.next

# if __name__ == '__main__':
#     myLl = List()
#     myLl.insert(1)
#     myLl.insert(2)
#     myLl.insert(3)
#     myLl.insert(4)
#     myLl.insert(5)
#     myLl.insert(6)
#     myLl.insert(7)
#     myLl.insert(8)
#     myLl.insert(9)
#     myLl.insert(0)

#     myLl.display()
#     myLl.reverse_copy_and_display()

#     myLl.display()
#     myLl.reverse_copy_and_display()