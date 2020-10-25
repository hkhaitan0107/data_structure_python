class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTree(object):
    def __init__(self, root):
        self.root = root
        
    def compare_binary_tree(self, t2):
        return self.tree_compare_helper(self.root, t2.root)
        
    def tree_compare_helper(self, t1_node, t2_node):
        if t1_node and t2_node:
            if t1_node.value == t2_node.value:
                left_branch = self.tree_compare_helper(t1_node.left, t2_node.left)
                right_branch = self.tree_compare_helper(t1_node.right, t2_node.right)
                return left_branch and right_branch
            else:
                return False
                
        if t1_node == None and t2_node == None:
            return True
        else:
            return False
            
##### Driver Code #####
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

bt1 = BinaryTree(n1)
bt1.root.left = n2
bt1.root.right = n3

n4 = Node(1)
n5 = Node(2)
n6 = Node(3)

bt2 = BinaryTree(n4)
bt2.root.left = n6
bt2.root.right = n5

print(bt1.compare_binary_tree(bt2))