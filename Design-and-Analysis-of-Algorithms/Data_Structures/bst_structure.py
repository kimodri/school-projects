import random
random.seed(42)
from queue_structure import Queue
from ll_structure import *

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return
        
        cur = self.root
        while True:  
            if data < cur.data:
                if cur.left is None: 
                    cur.left = new_node
                    return
                cur = cur.left
            elif data > cur.data:
                if cur.right is None:  
                    cur.right = new_node
                    return
                cur = cur.right
            else:
                print("The element is already in the BST!")
                return


    def search(self, value):
        list = self.inorder()
        return list.search(value)
        
    def delete(self, value):
        if not self.search(value):
            print("No such element exists!")
            return
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return node

        # Locate the node to delete
        if value < node.data:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.data:
            node.right = self._delete_recursive(node.right, value)
        else:  
            # CASE 1: No children (Leaf node)
            if node.left is None and node.right is None:
                return None
            
            # CASE 2: One child (Left or Right)
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # CASE 3: Two children (Find inorder successor)
            successor = self._min_value_node(node.right)
            node.data = successor.data
            node.right = self._delete_recursive(node.right, successor.data)
        
        return node

    # Helper function to find the smallest value in a subtree
    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        inorderList = List()
        def _inorder(node):
            if node is not None:
                _inorder(node.left)
                inorderList.insert(node.data)
                _inorder(node.right)
        _inorder(self.root)
        inorderList.display()
        return inorderList 
    
    #  Create functions that call the display

    # Preorder Traversal (NLR: Node, Left, Right)
    def preorder(self):
        preorderList = List()
        def _preorder(node):
            if node is not None:
                preorderList.insert(node.data)
                _preorder(node.left)
                _preorder(node.right)
        _preorder(self.root)
        preorderList.display()
        return preorderList

    # Postorder Traversal (LRN: Left, Right, Node)
    def postorder(self):
        postorderList = List()
        def _postorder(node):
            if node is not None:
                _postorder(node.left)
                _postorder(node.right)
                postorderList.insert(node.data) # Visit root last
        _postorder(self.root)
        postorderList.display()
        return postorderList
    
    def printTree(self, node=None, level=0):
        if node is None:
            if level == 0:  # Ensure we only assign self.root on the first call
                node = self.root
            else:
                return  # Stop recursion if node is None

        if node is not None:
            self.printTree(node.right, level + 1)  # Print right subtree first
            print(' ' * 4 * level + '-> ' + str(node.data))  # Print current node
            self.printTree(node.left, level + 1)  # Print left subtree


            

if __name__ == '__main__':
    myBst = BST()
    myBst.insert(50)
    myBst.insert(30)
    myBst.insert(70)
    myBst.insert(20)
    myBst.insert(40)
    myBst.insert(60)
    myBst.insert(80)
    myBst.inorder()
    myBst.printTree()

    myBst.delete(60)

    myBst.inorder()
    myBst.printTree()