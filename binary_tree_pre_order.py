class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        return self.preorder_search(self.root, find_val)

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        
        return self.preorder_print(self.root, [])

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        if start.value == find_val:
            return True
        elif start.right == None:
            return False
        elif start.left == None:
            return self.preorder_search(start.right, find_val)
        else:
            if start.left.value == find_val or start.right.value == find_val:
                return True
            else:
                return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        
        traversal.append(start.value)
        
        if start.left == None and start.right == None:
            return traversal
            
        elif start.left == None:
            return self.preorder_print(start.right, traversal)
        
        elif start.right == None:
            return self.preorder_print(start.left, traversal)
            
        else:
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
            
        return traversal


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.left.right.left = Node(6)
tree.root.left.right.right = Node(7)

# Test search
# Should be True
print tree.search(1)
# Should be False
print tree.search(7)

# Test print_tree
# Should be 1-2-4-5-3
print tree.print_tree()


##### Better Implementation
class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        return self.preorder_search(tree.root, find_val)

    def print_tree(self):
        return self.preorder_print(tree.root, "")[:-1]

    def preorder_search(self, start, find_val):
        if start:
            if start.value == find_val:
                return True
            else:
                return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)
        return False

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal