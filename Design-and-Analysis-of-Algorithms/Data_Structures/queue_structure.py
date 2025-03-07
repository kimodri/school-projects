from Data_Structures.ll_structure import List

class Queue(List):
    def __init__(self):
        """
        Initializes a Queue object, inheriting from the List class.
        """
        super().__init__()

    def enqueue(self, element):
        """
        Adds an element to the rear of the queue.
        """
        super().insert(element, position=None)

    def dequeue(self):
        """
        Removes and returns the element from the front of the queue.
        """
        if self.head is None:
            print("No existing list!")
            return

        data = self.head
        self.head = self.head.next
        self.size -= 1
        return data

    def front(self):
        """
        Prints the element at the front of the queue.
        """
        if self.head:
            print(self.head.data)
        else:
            print("Queue is empty")

    def rear(self):
        """
        Prints the element at the rear of the queue.
        """
        last_node = self.head
        if last_node is None:
            print("No existing queue.")
            return

        while last_node.next:
            last_node = last_node.next
        print(last_node.data)
    
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
                print(current_node.data, end=" ")
                current_node = current_node.next
            print("\n")
            


# if __name__ == '__main__':
#     myQueue = Queue()
#     myQueue.enqueue(1)
#     myQueue.enqueue(2)
#     myQueue.enqueue(3)
#     myQueue.enqueue(4)
#     myQueue.enqueue(5)
#     myQueue.enqueue(4)

#     myQueue.display()

#     print(myQueue.dequeue())
#     myQueue.display()
#     myQueue.enqueue(69)
#     myQueue.display()
#     print(myQueue.dequeue())
#     myQueue.display()
#     print(myQueue.dequeue())
#     myQueue.display()

    