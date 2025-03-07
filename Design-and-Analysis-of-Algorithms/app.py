from Data_Structures.array_structure import Array
from Data_Structures.ll_structure import List
from Data_Structures.stack_structure import Stack
from Data_Structures.queue_structure import Queue
from Data_Structures.bst_structure import BST

global_data_type = None
arr = Array(type=None)
myQueue = Queue()

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
        stack_menu()
    elif inp == 4:
        queue_menu()
    elif inp == 5:
        bst_menu()
    else:
        exit()

def array_menu():
    global arr, myQueue
    while True:  # Keeps the menu active
        print("\nArray Page\n\
        (1). Create Array\n\
        (2). Insert\n\
        (3). Delete\n\
        (4). Sort Asc\n\
        (5). Sort Des\n\
        (0). Main Menu")
        
        inp = int(input("Input: "))

        if inp == 1:
            data_type()  # Get data type
            if global_data_type is None:
                continue  # If no valid type, go back to menu

            arr = Array(global_data_type)

            if myQueue.size != 0:
                print("Old created arrays have been deleted.")
                while myQueue.size != 0:
                    myQueue.dequeue()

            myQueue.enqueue(arr)
            # print("Array successfully created!")

        elif inp == 2:
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
            print("Deleting data: \n")
            if global_data_type == 'i':
                inp = int(input("delete: "))
                arr.delete(inp)
            elif global_data_type == 'f':
                inp = arr.delete("delete: ")
                arr.delete(inp)
            else:
                inp = float(input("delete: "))
                arr.delete(inp)
        
        elif inp == 4:
            print("Sorting in Ascending order...")
            print(arr.sort())

        elif inp == 5:
            print("Sorting in Descending order...")
            # Implement sorting logic
            print(arr.sort(reversed=True))

        elif inp == 0:
            print("Returning to Main Menu...")
            print_menu()
            while myQueue.size != 0:
                myQueue.dequeue()
            break  # Exit the loop to return to main menu

        else:
            print("Invalid input! Please try again.")

def ll_menu():
    print("Linked List Page\n\
        (1). Create Linked List\n\
        (2). Insert\n\
        (3). Delete\n\
        (4). Reverse\n\
        (5). Remove Duplicates\n\
        (6). Display\n\
        (0). Main Menu")

def stack_menu():
    print("Stack Page\n\
        (1). Create Linked List\n\
        (2). Push\n\
        (3). Pop\n\
        (4). Modify\n\
        (5). Display\n\
        (0). Main Menu")

def queue_menu():
    print("Queue Menu\n\
          (1). Create Queue\n\
          (2). Enqueue\n\
          (3). Dequeue\n\
          (4). Check Front\n\
          (5). Check Rear\n\
          (6). Display the Queue\n\
          (0). Main Menu")
    
def bst_menu():
    print("Queue Menu\n\
          (1). Create BST\n\
          (2). Insert\n\
          (3). Delete\n\
          (4). Display\n\
          (5). Display Structure\n\
          (0). Main Menu")
    

def data_type():
    global global_data_type
    while True:
        inp = int(input("Selection:\n\
                        (1). int\n\
                        (2). float\n\
                        (3). char\n\
                        input: "))
        if inp == 1:
            print("An Array of type integer has been created!")
            global_data_type = 'i'
            break
        elif inp == 2:
            print("An Array of type float has been created!")
            global_data_type = 'f'
            break
        elif inp == 3:
            print("An Array of type char has been created!")
            global_data_type = 'u'
            break
        else:
            print("Invalid choice, please try again.")


print_menu()