from Data_Structures.ll_structure import *

class BST:
    def __init__(self):
        """
        Initializes an empty BST
        """
        self.root = None

    def insert(self, data):
        """
        Inserts a new node with the given data into the BST
        """
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
        """
        Searches for a value in the BST
        """
        inorder_list = self.inorder()
        return inorder_list.search(value)

    def delete(self, value):
        """
        Deletes a node with the given value from the BST
        """
        if not self.search(value):
            print("No such element exists!")
            return
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        """
        Recursive helper function to delete a node
        """
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

    def _min_value_node(self, node):
        """
        Helper function to find the smallest value in a subtree
        """
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        """
        Performs an inorder traversal of the BST
        """
        inorder_list = List()

        def _inorder(node):
            if node is not None:
                _inorder(node.left)
                inorder_list.insert(node.data)
                _inorder(node.right)

        _inorder(self.root)
        return inorder_list

    def preorder(self):
        """
        Performs a preorder traversal of the BST
        """
        preorder_list = List()

        def _preorder(node):
            if node is not None:
                preorder_list.insert(node.data)
                _preorder(node.left)
                _preorder(node.right)

        _preorder(self.root)
        return preorder_list

    def postorder(self):
        """
        Performs a postorder traversal of the BST
        """
        postorder_list = List()

        def _postorder(node):
            if node is not None:
                _postorder(node.left)
                _postorder(node.right)
                postorder_list.insert(node.data)  

        _postorder(self.root)
        return postorder_list

    def printTree(self, node=None, level=0):
        """Prints the BST in a tree-like structure
        """
        if node is None:
            if level == 0: 
                node = self.root
            else:
                return  

        if node is not None:
            self.printTree(node.right, level + 1)  
            print(' ' * 4 * level + '-> ' + str(node.data))  
            self.printTree(node.left, level + 1)  



# if __name__ == '__main__':
#     myBst = BST()
#     myBst.insert(50)
#     myBst.insert(30)
#     myBst.insert(70)
#     myBst.insert(20)
#     myBst.insert(40)
#     myBst.insert(60)
#     myBst.insert(80)
#     myBst.inorder()
#     myBst.printTree()

#     myBst.delete(30)

#     myBst.inorder()
#     myBst.printTree()