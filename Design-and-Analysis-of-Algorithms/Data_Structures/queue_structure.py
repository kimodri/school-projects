from linked_list_structure import * # Assuming linked_list_structure.py contains the List class

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
        super().insert(element, position=self.size)

    def dequeue(self):
        """
        Removes and returns the element from the front of the queue.
        """
        if self.head is None:
            print("No existing list!")
            return

        self.head = self.head.next
        self.size -= 1
        return

    def front(self):
        """
        Prints the element at the front of the queue.
        """
        if self.head:
            print(self.head.data, 0)
        else:
            print("Queue is empty")

    def rear(self):
        """
        Prints the element at the rear of the queue.
        """
        last_node = self.head
        if last_node is None:
            print(None, self.size)
            return

        while last_node.next:
            last_node = last_node.next
        print(last_node.data if last_node else None, self.size)

# if __name__ == '__main__':
#     myQueue = Queue()
#     myQueue.enqueue(1)
#     myQueue.enqueue(2)
#     myQueue.enqueue(3)
#     myQueue.enqueue(4)
#     myQueue.enqueue(5)
#     myQueue.enqueue(4)

#     myQueue.display()

#     myQueue.dequeue()
#     myQueue.display()
#     myQueue.enqueue(69)
#     myQueue.display()
#     myQueue.dequeue()
#     myQueue.display()
#     myQueue.dequeue()
#     myQueue.display()

    