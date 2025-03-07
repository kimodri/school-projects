# Import the structures
from Data_Structures.array_structure import Array
from Data_Structures.bst_structure import BST
from Data_Structures.ll_structure import List
from Data_Structures.stack_structure import Stack
from Data_Structures.queue_structure import Queue

global_data_type = None

# myQueue = Queue()

arr = Array(type='i')
list = List()
stack = Stack('i', 4)
queue = Queue()
bst = BST()

def print_menu():
    print("Menu Page\n\
        (1). Array\n\
        (2). Linked List\n\
        (3). Stack\n\
        (4). Queue\n\
        (5). BST\n\
        (6). Exit")
    
    inp = int(input("Selection: "))
    if inp == 1:
        array_menu()
    elif inp == 2:
        ll_menu()
    elif inp == 3:
        pass
        stack_menu()
    elif inp == 4:
        queue_menu()
    elif inp == 5:
        bst_menu()
    else:
        exit()

def array_menu():
    global arr
    created = False

    while True:  # Keeps the menu active
        print("\nArray Page\n\
        (1). Create Array\n\
        (2). Insert\n\
        (3). Delete\n\
        (4). Sort Asc\n\
        (5). Sort Des\n\
        (0). Main Menu")
        
        inp = int(input("input: "))

        if inp == 1:
            created = True
            data_type()  
            arr = Array(global_data_type)

        elif inp == 2:
            if created == False:
                print("There is no existing array.")
                continue
            else:
                print("Inserting data: \n")
                if global_data_type == 'i':
                    inp = int(input("insert: "))
                    arr.insert(inp)
                elif global_data_type == 'f':
                    inp = float(input("insert: "))
                    arr.insert(inp)
                else:
                    inp = input("insert: ")
                    arr.insert(inp)

        elif inp == 3:
            if created == False:
                print("There is no existing array.")
                continue
            else:
                print("Deleting data... \n")
                if global_data_type == 'i':
                    inp = int(input("delete: "))
                    arr.delete(inp)
                elif global_data_type == 'f':
                    inp = float(input("delete: "))
                    arr.delete(inp)
                # else:
                #     inp = input("delete: ")
                #     arr.delete(inp)
        
        elif inp == 4:
            print("Sorting in Ascending order...")
            arr.sort()

        elif inp == 5:
            print("Sorting in Descending order...")
            # Implement sorting logic
            arr.sort(reversed=True)

        elif inp == 0:
            print("Returning to Main Menu...")
            print_menu()
            break  

        else:
            print("Invalid input! Please try again.")
            continue

def ll_menu():
    global list
    created = False

    while True:
        print("Linked List Page\n\
            (1). Create Linked List\n\
            (2). Insert\n\
            (3). Delete\n\
            (4). Reverse\n\
            (5). Remove Duplicates\n\
            (6). Display\n\
            (0). Main Menu")
        inp = int(input("input: "))

        if inp == 1:
          created = True
          list = List()
          print("Linked List has been created!")

        elif inp == 2:
           if created == False:
                print("There is no existing linked list.")
                continue
           else:
                print("Inserting data... \n")
                inp = input("insert: ")
                list.insert(inp)

        elif inp == 3:
            if created == False:
                print("There is no existing linked list.")
                continue
            else:
                print("Deleting data... \n")
                inp = input("delete: ")
                list.delete(inp)
        
        elif inp == 4:
            if created == False:
                print("There is no existing linked list.")
                continue
            else:
                print("Displaying the reversed... \n")
                list.reverse_copy_and_display()

        elif inp == 5:
            if created == False:
                print("There is no existing linked list.")
                continue
            else:
                print("Removing the duplicates...\n")
                list.remove_duplicates()
        
        elif inp == 6:
            if created == False:
                print("There is no existing linked list.")
                continue
            else:
                print("Displaying the list...\n")
                list.display()

        elif inp == 0:
            print("Returning to Main Menu...")
            print_menu()
            break  
            
        else:
            print("Invalid input! Please try again.")
            continue

def stack_menu():
    global stack
    created = False

    while True:
        print("Stack Page\n\
            (1). Create Stack\n\
            (2). Push\n\
            (3). Pop\n\
            (4). Modify\n\
            (5). Display\n\
            (0). Main Menu")
        inp = int(input("input: "))

        if inp == 1:
          created = True
          data_type()  
          size = int(input("Input the size of the stack: "))
          stack = Stack(global_data_type, size)

        elif inp == 2:
            if created == False:
                print("There is no existing stack.")
                continue
            else:
                print("Inserting data... \n")
                if global_data_type == 'i':
                    inp = int(input("insert: "))
                    stack.push(inp)
                elif global_data_type == 'f':
                    inp = float(input("insert: "))
                    stack.push(inp)

        elif inp == 3:
            if created == False:
                print("There is no existing stack.")
                continue
            else:
                print("Popping data... \n")
                stack.pop()
        
        
        elif inp == 4:
            if created == False:
                print("There is no existing stack.")
                continue
            else:
                print("Modifying a data...\n")
                if global_data_type == 'i':
                    element = int(input("Input element to subsitute: "))
                    position = int(input("Input the position to substitute it to: "))
                stack.modify(element, position)
        
        elif inp == 5:
            print("Displaying the stack...\n")
            stack.display()

        elif inp == 0:
            print("Returning to Main Menu...")
            print_menu()
            break 
            
        else:
            print("Invalid input! Please try again.")
            continue

def queue_menu():
    created = False
    global queue

    while True:
        print("Queue Menu\n\
            (1). Create Queue\n\
            (2). Enqueue\n\
            (3). Dequeue\n\
            (4). Check Front\n\
            (5). Check Rear\n\
            (6). Display the Queue\n\
            (0). Main Menu")
            
        inp = int(input("input: "))
        if inp == 1:
            print("Queue has been created!")
            created = True
            queue = Queue()

        elif inp == 2:
            if created == False:
                print("No queue exists.")
            else:
                print("Enqueuing a data...\n")
                inp = input("enqueue: ")
                queue.enqueue(inp)

        elif inp == 3:
            if created == False:
                print("No queue exists.")
            else:
                print("Dequeuing a data...\n")
                queue.dequeue()
            
        elif inp == 4:
            if created == False:
                print("No queue exists.")
            else:
                print("Accessing the front...\n")
                queue.front()

        elif inp == 5:
            if created == False:
                print("No queue exists.")
            else:
                print("Accessing the rear...\n")
                queue.rear()
    
        elif inp == 6:
            if created == False:
                print("No queue exists.")
            else:
                print("Displaying the queue...\n")
                queue.display()

        elif inp == 0:
            print("Returning to Main Menu...")
            print_menu()
            break  #
                
        else:
            print("Invalid input! Please try again.")
    
def bst_menu():
    global bst
    created = False

    while True:
        print("BST Menu\n\
            (1). Create BST\n\
            (2). Insert\n\
            (3). Delete\n\
            (4). Display\n\
            (5). Display Structure\n\
            (0). Main Menu")
        inp = int(input("input: "))

        if inp == 1:
            print("A Binary Search Tree has been created.")
            created = True
            bst = BST()

        elif inp == 2:
            if created == False:
                print("No BST exists.")
            else:
                print("Inserting...\n")
                inp = input("insert: ")
                bst.insert(inp)

        elif inp == 3:
            if created == False:
                print("No BST exists.")
            else:
                print("Deleting...\n")
                inp = input("delete: ")
                bst.delete(inp)
            
        elif inp == 4:
            if created == False:
                print("No BST exists.")
            else:
                print("Displaying...\n")
                print("Selection:\n\
                  (1). Inorder\n\
                  (2). Preorder\n\
                  (3). Postorder")
                inp = 0
                while inp > 3 or inp <= 0:
                    inp = int(input("input: "))
                    if inp == 1:
                        bst.inorder().display()
                    elif inp == 2:
                        bst.preorder().display()
                    elif inp == 3:
                        bst.postorder().display()
                    else:
                        print("Not in the options, try again.")
        elif inp == 5:
            if created == False:
                print("No BST exists.")
            else:
                print("Displaying the structure...\n")
                bst.printTree()

        elif inp == 0:
            print("Returning to Main Menu...")
            print_menu()
            break  
                
        else:
            print("Invalid input! Please try again.")

def data_type():
    global global_data_type
    while True:
        inp = int(input("Selection:\n\
                        (1). int\n\
                        (2). float\n\
                        input: "))
                        # (3). char\n\
        if inp == 1:
            print("An Array/Stack of type integer has been created!")
            global_data_type = 'i'
            break
        elif inp == 2:
            print("An Array/Stack of type float has been created!")
            global_data_type = 'f'
            break
        # elif inp == 3:
        #     print("An Array of type char has been created!")
        #     global_data_type = 'u'
        #     break
        else:
            print("Invalid choice, please try again.")

print_menu()

