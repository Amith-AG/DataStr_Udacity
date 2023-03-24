class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        start=self.root
        while start:
           if start.value==new_val:
               return
           elif start.value>new_val:
               if start.left:
                   start=start.left
               else:
                   start.left=Node(new_val)
                   return
           else:
               if start.right:
                   start=start.right
               else:
                   start.right=Node(new_val)
                   return
        

    def search(self, find_val):
        start=self.root
        while start:
            if start.value==find_val:
                return True
            elif start.value>find_val:
                if start.left:
                    start=start.left
                else:
                    return False
            else:
                if start.right:
                    start=start.right
                else:
                    return False

    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)