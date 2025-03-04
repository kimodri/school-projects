from linked_list_structure import *

class Queue(List):
    def __init__(self):
        super().__init__()

    def enqueue(self, element):
        super().insert(element, position = self.size)

    def dequeue(self):
        if (self.head == None):
            print("No existing list!")
            return 
        
        self.head = self.head.next
        self.size -= 1
        return

    def front(self):
        print(self.head.data, 0)

    def rear(self):
        last_node = self.head
        while last_node:
            last_node = last_node.next
        print(last_node, self.size)

if __name__ == '__main__':
    myQueue = Queue()
    myQueue.enqueue(1)
    myQueue.enqueue(2)
    myQueue.enqueue(3)
    myQueue.enqueue(4)
    myQueue.enqueue(5)
    myQueue.enqueue(4)

    myQueue.display()

    myQueue.dequeue()
    myQueue.display()
    myQueue.enqueue(69)
    myQueue.display()
    myQueue.dequeue()
    myQueue.display()
    myQueue.dequeue()
    myQueue.display()

    