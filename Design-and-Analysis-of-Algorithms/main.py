from Data_Structures.array_structure import Array
from Data_Structures.linked_list_structure import *


import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("GUI Navigation")
        self.geometry("400x300")

        # Create a container frame
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        # Dictionary to hold frames
        self.frames = {}

        # Create and store frames
        for F in (MenuFrame, Option1Frame, Option2Frame):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the menu initially
        self.show_frame("MenuFrame")

    def show_frame(self, page_name):
        """Bring the given frame to the front"""
        frame = self.frames[page_name]
        frame.tkraise()

# Define the Menu Frame
class MenuFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Menu", font=("Arial", 16)).pack(pady=20)
        tk.Button(self, text="Option 1", command=lambda: controller.show_frame("Option1Frame")).pack()
        tk.Button(self, text="Option 2", command=lambda: controller.show_frame("Option2Frame")).pack()

# Define Option 1 Frame
class Option1Frame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Option 1 Screen", font=("Arial", 16)).pack(pady=20)
        tk.Button(self, text="Back to Menu", command=lambda: controller.show_frame("MenuFrame")).pack()

# Define Option 2 Frame
class Option2Frame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Option 2 Screen", font=("Arial", 16)).pack(pady=20)
        tk.Button(self, text="Back to Menu", command=lambda: controller.show_frame("MenuFrame")).pack()

# Run the application
if __name__ == "__main__":
    app = App()
    app.mainloop()
