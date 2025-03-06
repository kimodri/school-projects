import tkinter as tk
from Data_Structures.array_structure import *
from Data_Structures.ll_structure import *
from Data_Structures.stack_structure import *
from Data_Structures.queue_structure import *
from Data_Structures.bst_structure import *


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Menu")
        self.geometry("420x260")

        # container frame 
        # self is just an instanced of tl.Tk (window)
        self.container = tk.Frame(self)
        self.container.pack(fill = 'both', expand = True)

        self.frames = {}

        for F in (MenuFrame, arrayFrame, llFrame,\
                   stackFrame, queueFrame, bstFrame):
            page_name = F.__name__
            frame = F(parent = self.container, controller = self)
            self.frames[page_name] = frame
            frame.grid(row = 0, column = 0, sticky='nsew')
        
        self.show_frame("MenuFrame")

    def show_frame(self, page_name):
        """Bring the given frame to the front"""
        frame = self.frames[page_name]
        if page_name == 'arrayFrame':
            self.myArr = Array()
        elif page_name == 'llFrame':
            self.myLl = List()
        elif page_name == 'stackFrame':
            self.myStack = Stack()
        elif page_name == 'queueFrame':
            self.myQueue = Queue()
        else:
            self.myBst = BST()
        frame.tkraise()


class MenuFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller 
    
        left_frame = tk.Frame(self, bg="lightblue", width=210)
        left_frame.grid(row=0, column=0, sticky="ns")

        right_frame = tk.Frame(self, bg="lightgreen", width=100)
        right_frame.grid(row=0, column=1, sticky="ns")
        
        array_frame = tk.Frame(left_frame, borderwidth=2, relief="groove")
        array_frame.grid(row=0, column= 0, padx = 20, pady = 10)
        datatype_label = tk.Label(array_frame, text="Select Data Type:")
        datatype_label.pack()
        # Variable to store selected datatype
        self.array_datatype_var = tk.StringVar(value="int")  # Default value
        # Create radio buttons for datatypes
        datatypes = ["int", "float", "char"]
        for dtype in datatypes:
            tk.Radiobutton(array_frame, text=dtype, variable=self.array_datatype_var, value=dtype).pack(anchor="w")
        # Create a button to create an array
        array_button = tk.Button(array_frame, text="Create Array", command=lambda: controller.show_frame("arrayFrame"))
        array_button.pack(pady=10)

        stack_frame = tk.Frame(left_frame, borderwidth=2, relief="groove")
        stack_frame.grid(row=0, column= 1, padx = 10, pady = 25)
        datatype_label = tk.Label(stack_frame, text="Select Data Type:")
        datatype_label.pack()
        self.stack_datatype_var = tk.StringVar(value="int")
        datatypes = ["int", "float", "char"]
        for dtype in datatypes:
            tk.Radiobutton(stack_frame, text=dtype, variable=self.stack_datatype_var, value=dtype).pack(anchor="w")
        # Create a button to create an array
        stack_button = tk.Button(stack_frame, text="Create Stack", command=lambda: controller.show_frame("stackFrame"))
        stack_button.pack(pady=10)


        linkedList_frame = tk.Frame(right_frame, borderwidth=2, relief="groove")
        linkedList_frame.grid(row=0, column=0, padx = 10, pady = 5)
        linkedList_button = tk.Button(linkedList_frame, text = "Create Linked List", command=lambda: controller.show_frame("llFrame"), width=15)
        linkedList_button.pack(pady = 5, padx = 5)

        queue_frame = tk.Frame(right_frame, borderwidth=2, relief="groove")
        queue_frame.grid(row=1, column= 0, padx = 10, pady = 5)
        queue_button = tk.Button(queue_frame, text = "Create Queue", command=lambda: controller.show_frame("queueFrame"), width=15)
        queue_button.pack(pady = 5, padx = 5)

        bst_frame = tk.Frame(right_frame, borderwidth=2, relief="groove")
        bst_frame.grid(row=2, column= 0, padx = 10, pady = 5)
        bst_button = tk.Button(bst_frame, text = "Create BST", command=lambda: controller.show_frame("bstFrame"), width=15)
        bst_button.pack(pady = 5, padx = 5)

        menu_frame = tk.Frame(right_frame, borderwidth=2, relief="groove")
        menu_frame.grid(row=3, column= 0, padx = 10, pady = 5)
        menu_button = tk.Button(menu_frame, text = "Menu", command=lambda: controller.show_frame("MenuFrame"), width=15)
        menu_button.pack(pady = 5, padx = 5)
        


class arrayFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        left_frame = tk.Frame(self, bg="lightblue")
        left_frame.grid(row=0, column=0, sticky="ns")

        right_frame = tk.Frame(self, bg="lightgreen")
        right_frame.grid(row=0, column=1, sticky="ns")
        
        input_frame = tk.LabelFrame(left_frame, borderwidth=2, relief="groove", text="Input:")
        input_frame.grid(row=0, column=0, padx=10, pady=5)

        self.input_entry = tk.Entry(input_frame, width=40)  # Single-line input
        self.input_entry.grid(row=0, column=0, padx=5, pady=5)

        # Output Frame
        output_frame = tk.LabelFrame(left_frame, borderwidth=2, relief="groove", text="Output:")
        output_frame.grid(row=1, column=0, padx=10, pady=5)

        self.output_text = tk.Text(output_frame, height=10, width=30)  # Multi-line output
        self.output_text.grid(row=0, column=0, padx=5, pady=5)
        
        # Right side
        insert_frame = tk.Frame(right_frame, borderwidth=2, relief="groove")
        insert_frame.grid(row=0, column=0, padx = 10, pady = 5)
        insert_button = tk.Button(insert_frame, text = "Insert", command = self.insert_arr(), width=15) # lagay rito yung nasa text field
        insert_button.pack(pady = 5, padx = 5)

        delete_frame = tk.Frame(right_frame, borderwidth=2, relief="groove")
        delete_frame.grid(row=1, column= 0, padx = 10, pady = 5)
        delete_button = tk.Button(delete_frame, text = "Delete", command = List, width=15)
        delete_button.pack(pady = 5, padx = 5)

        sort_asc_frame = tk.Frame(right_frame, borderwidth=2, relief="groove")
        sort_asc_frame.grid(row=2, column= 0, padx = 10, pady = 5)
        sort_asc_button = tk.Button(sort_asc_frame, text = "Sort asc", command = List, width=15)
        sort_asc_button.pack(pady = 5, padx = 5)

        sort_des_frame = tk.Frame(right_frame, borderwidth=2, relief="groove")
        sort_des_frame.grid(row=2, column= 0, padx = 10, pady = 5)
        sort_des_button = tk.Button(sort_des_frame, text = "Sort des", command = List, width=15)
        sort_des_button.pack(pady = 5, padx = 5)

        menu_frame = tk.Frame(right_frame, borderwidth=2, relief="groove")
        menu_frame.grid(row=3, column= 0, padx = 10, pady = 5)
        menu_button = tk.Button(menu_frame, text = "Menu", command=lambda: controller.show_frame("MenuFrame"), width=15, )
        menu_button.pack(pady = 5, padx = 5)

    def insert_arr(self, data):
        self.controller.myArr.insert(data) # lagay dito yung nasa text field
        # print na inserted yung data

        

class llFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        left_frame = tk.Frame(self, bg="lightblue")
        left_frame.grid(row=0, column=0, sticky="ns")

        right_frame = tk.Frame(self, bg="lightgreen")
        right_frame.grid(row=0, column=1, sticky="ns")
        
        input_frame = tk.LabelFrame(left_frame, borderwidth=2, relief="groove", text="Input:")
        input_frame.grid(row=0, column=0, padx=10, pady=5)

        self.input_entry = tk.Entry(input_frame, width=40)  # Single-line input
        self.input_entry.grid(row=0, column=0, padx=5, pady=5)

        # Output Frame
        output_frame = tk.LabelFrame(left_frame, borderwidth=2, relief="groove", text="Output:")
        output_frame.grid(row=1, column=0, padx=10, pady=5)

        self.output_text = tk.Text(output_frame, height=10, width=30)  # Multi-line output
        self.output_text.grid(row=0, column=0, padx=5, pady=5)


        insert_frame = tk.Frame(right_frame, borderwidth=2, relief="groove")
        insert_frame.grid(row=0, column=0, padx = 10, pady = 5)
        insert_button = tk.Button(insert_frame, text = "Insert", command = List, width=15)
        insert_button.pack(pady = 5, padx = 5)

        delete_frame = tk.Frame(right_frame, borderwidth=2, relief="groove")
        delete_frame.grid(row=1, column= 0, padx = 10, pady = 5)
        delete_button = tk.Button(delete_frame, text = "Delete", command = List, width=15)
        delete_button.pack(pady = 5, padx = 5)

        reverse_frame = tk.Frame(right_frame, borderwidth=2, relief="groove")
        reverse_frame.grid(row=2, column= 0, padx = 10, pady = 5)
        reverse_button = tk.Button(reverse_frame, text = "Reverse", command = List, width=15)
        reverse_button.pack(pady = 5, padx = 5)

        rem_dup_frame = tk.Frame(right_frame, borderwidth=2, relief="groove")
        rem_dup_frame.grid(row=2, column= 0, padx = 10, pady = 5)
        rem_dup_button = tk.Button(rem_dup_frame, text = "Remove duplicates", command = List, width=15)
        rem_dup_button.pack(pady = 5, padx = 5)

        menu_frame = tk.Frame(right_frame, borderwidth=2, relief="groove")
        menu_frame.grid(row=3, column= 0, padx = 10, pady = 5)
        menu_button = tk.Button(menu_frame, text = "Menu", command=lambda: controller.show_frame("MenuFrame"), width=15)
        menu_button.pack(pady = 5, padx = 5)

class stackFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        left_frame = tk.Frame(self, bg="lightblue")
        left_frame.grid(row=0, column=0, sticky="ns")

        right_frame = tk.Frame(self, bg="lightgreen")
        right_frame.grid(row=0, column=1, sticky="ns")
        
        input_frame = tk.LabelFrame(left_frame, borderwidth=2, relief="groove", text="Input:")
        input_frame.grid(row=0, column=0, padx=10, pady=5)

        self.input_entry = tk.Entry(input_frame, width=40)  # Single-line input
        self.input_entry.grid(row=0, column=0, padx=5, pady=5)

        # Output Frame
        output_frame = tk.LabelFrame(left_frame, borderwidth=2, relief="groove", text="Output:")
        output_frame.grid(row=1, column=0, padx=10, pady=5)

        self.output_text = tk.Text(output_frame, height=10, width=30)  # Multi-line output
        self.output_text.grid(row=0, column=0, padx=5, pady=5)


        insert_frame = tk.Frame(right_frame, borderwidth=2, relief="groove")
        insert_frame.grid(row=0, column=0, padx = 10, pady = 5)
        insert_button = tk.Button(insert_frame, text = "Push", command = List, width=15)
        insert_button.pack(pady = 5, padx = 5)

        delete_frame = tk.Frame(right_frame, borderwidth=2, relief="groove")
        delete_frame.grid(row=1, column= 0, padx = 10, pady = 5)
        delete_button = tk.Button(delete_frame, text = "Pop", command = List, width=15)
        delete_button.pack(pady = 5, padx = 5)

        modify_frame = tk.Frame(right_frame, borderwidth=2, relief="groove")
        modify_frame.grid(row=2, column= 0, padx = 10, pady = 5)
        modify_button = tk.Button(modify_frame, text = "Modify", command = List, width=15)
        modify_button.pack(pady = 5, padx = 5)

        display_frame = tk.Frame(right_frame, borderwidth=2, relief="groove")
        display_frame.grid(row=2, column= 0, padx = 10, pady = 5)
        display_button = tk.Button(display_frame, text = "Display", command = List, width=15)
        display_button.pack(pady = 5, padx = 5)

        menu_frame = tk.Frame(right_frame, borderwidth=2, relief="groove")
        menu_frame.grid(row=3, column= 0, padx = 10, pady = 5)
        menu_button = tk.Button(menu_frame, text = "Menu", command=lambda: controller.show_frame("MenuFrame"), width=15)
        menu_button.pack(pady = 5, padx = 5)
        

class queueFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        left_frame = tk.Frame(self, bg="lightblue")
        left_frame.grid(row=0, column=0, sticky="ns")

        right_frame = tk.Frame(self, bg="lightgreen")
        right_frame.grid(row=0, column=1, sticky="ns")
        
        input_frame = tk.LabelFrame(left_frame, borderwidth=2, relief="groove", text="Input:")
        input_frame.grid(row=0, column=0, padx=10, pady=5)

        self.input_entry = tk.Entry(input_frame, width=40)  # Single-line input
        self.input_entry.grid(row=0, column=0, padx=5, pady=5)

        # Output Frame
        output_frame = tk.LabelFrame(left_frame, borderwidth=2, relief="groove", text="Output:")
        output_frame.grid(row=1, column=0, padx=10, pady=5)

        self.output_text = tk.Text(output_frame, height=10, width=30)  # Multi-line output
        self.output_text.grid(row=0, column=0, padx=5, pady=5)

        # Right side
        insert_frame = tk.Frame(right_frame, borderwidth=2, relief="groove")
        insert_frame.grid(row=0, column=0, padx = 10, pady = 5)
        insert_button = tk.Button(insert_frame, text = "Enqueue", command = List, width=15)
        insert_button.pack(pady = 5, padx = 5)

        delete_frame = tk.Frame(right_frame, borderwidth=2, relief="groove")
        delete_frame.grid(row=1, column= 0, padx = 10, pady = 5)
        delete_button = tk.Button(delete_frame, text = "Dequeue", command = List, width=15)
        delete_button.pack(pady = 5, padx = 5)

        front_frame = tk.Frame(right_frame, borderwidth=2, relief="groove")
        front_frame.grid(row=2, column= 0, padx = 10, pady = 5)
        front_button = tk.Button(front_frame, text = "Front", command = List, width=15)
        front_button.pack(pady = 5, padx = 5)

        rear_frame = tk.Frame(right_frame, borderwidth=2, relief="groove")
        rear_frame.grid(row=2, column= 0, padx = 10, pady = 5)
        rear_button = tk.Button(rear_frame, text = "Rear", command = List, width=15)
        rear_button.pack(pady = 5, padx = 5)

        display_frame = tk.Frame(right_frame, borderwidth=2, relief="groove")
        display_frame.grid(row=2, column= 0, padx = 10, pady = 5)
        display_button = tk.Button(display_frame, text = "Display", command = List, width=15)
        display_button.pack(pady = 5, padx = 5)

        menu_frame = tk.Frame(right_frame, borderwidth=2, relief="groove")
        menu_frame.grid(row=3, column= 0, padx = 10, pady = 5)
        menu_button = tk.Button(menu_frame, text = "Menu", command=lambda: controller.show_frame("MenuFrame"), width=15)
        menu_button.pack(pady = 5, padx = 5)

class bstFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        left_frame = tk.Frame(self, bg="lightblue")
        left_frame.grid(row=0, column=0, sticky="ns")

        right_frame = tk.Frame(self, bg="lightgreen")
        right_frame.grid(row=0, column=1, sticky="ns")
        
        input_frame = tk.LabelFrame(left_frame, borderwidth=2, relief="groove", text="Input:")
        input_frame.grid(row=0, column=0, padx=10, pady=5)

        self.input_entry = tk.Entry(input_frame, width=40)  # Single-line input
        self.input_entry.grid(row=0, column=0, padx=5, pady=5)

        # Output Frame
        output_frame = tk.LabelFrame(left_frame, borderwidth=2, relief="groove", text="Output:")
        output_frame.grid(row=1, column=0, padx=10, pady=5)

        self.output_text = tk.Text(output_frame, height=10, width=30)  # Multi-line output
        self.output_text.grid(row=0, column=0, padx=5, pady=5)

        # Right side
        insert_frame = tk.Frame(right_frame, borderwidth=2, relief="groove")
        insert_frame.grid(row=0, column=0, padx = 10, pady = 5)
        insert_button = tk.Button(insert_frame, text = "Enqueue", command = List, width=15)
        insert_button.pack(pady = 5, padx = 5)

        delete_frame = tk.Frame(right_frame, borderwidth=2, relief="groove")
        delete_frame.grid(row=1, column= 0, padx = 10, pady = 5)
        delete_button = tk.Button(delete_frame, text = "Dequeue", command = List, width=15)
        delete_button.pack(pady = 5, padx = 5)

        front_frame = tk.Frame(right_frame, borderwidth=2, relief="groove")
        front_frame.grid(row=2, column= 0, padx = 10, pady = 5)
        front_button = tk.Button(front_frame, text = "Front", command = List, width=15)
        front_button.pack(pady = 5, padx = 5)

        rear_frame = tk.Frame(right_frame, borderwidth=2, relief="groove")
        rear_frame.grid(row=2, column= 0, padx = 10, pady = 5)
        rear_button = tk.Button(rear_frame, text = "Rear", command = List, width=15)
        rear_button.pack(pady = 5, padx = 5)

        display_frame = tk.Frame(right_frame, borderwidth=2, relief="groove")
        display_frame.grid(row=2, column= 0, padx = 10, pady = 5)
        display_button = tk.Button(display_frame, text = "Display", command = List, width=15)
        display_button.pack(pady = 5, padx = 5)

        menu_frame = tk.Frame(right_frame, borderwidth=2, relief="groove")
        menu_frame.grid(row=3, column= 0, padx = 10, pady = 5)
        menu_button = tk.Button(menu_frame, text = "Menu", command=lambda: controller.show_frame("MenuFrame"), width=15)
        menu_button.pack(pady = 5, padx = 5)



# Run the application
if __name__ == "__main__":
    app = App()
    app.mainloop()
