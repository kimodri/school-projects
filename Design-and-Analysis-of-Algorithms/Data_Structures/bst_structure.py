import random
random.seed(42)
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

class Tree:
    def __init__(self):
        self.root = None
        self.level = 0
    
    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node 
        else:
            self._insert(value, self.root)

    def _insert(self, value, curr_node):
        new_node = Node(value)
        if value < curr_node.data:
            if curr_node.left is None:
                curr_node.left = new_node
                curr_node.left.parent = curr_node 
            else:
                self._insert(value, curr_node.left)
        elif value > curr_node.data:
            if curr_node.right is None:
                curr_node.right = new_node
                curr_node.parent = curr_node
            else:
                self._insert(value, curr_node.right)
    
    def search(self, value):
        if self.root != None:
            return self._search(value, self.root)
        else:
            return False
        
    def _search(self, value, cur_node):
        if value == cur_node.data:
            return True
        elif value < cur_node.data and cur_node.left != None:
            self._search(value, cur_node.left)
        elif value > cur_node.data and cur_node.right != None:
            self._search(value, cur_node.right)
        return False
    def delete(self):
        pass

    def print_tree_ind(self):
        if self.root != None:
            self._print_tree_ind(self.root)

    def _print_tree_ind(self, cur_node):
        if cur_node != None:
            self._print_tree_ind(cur_node.left)
            print(cur_node.data)
            self._print_tree_ind(cur_node.right)

    

    def display_struct(self):
        pass
        

if __name__ == '__main__':
    myBst = Tree()
    myBst.insert(random.randint(1, 20))
    myBst.insert(random.randint(1, 20))
    myBst.insert(random.randint(1, 20))
    myBst.insert(random.randint(1, 20))
    myBst.insert(random.randint(1, 20))
    myBst.insert(random.randint(1, 20))
    myBst.insert(random.randint(1, 20))
    myBst.insert(random.randint(1, 20))
    myBst.insert(random.randint(1, 20))
    myBst.insert(random.randint(1, 20))
    myBst.insert(random.randint(1, 20))
    myBst.insert(random.randint(1, 20))

    myBst.print_tree_ind()
    print(myBst.search(0))
    print(myBst.search(2))
    print(myBst.search(9))
    print(myBst.search(0))
