class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    
    def __init__(self, root = None):
        self.root = root
        
    def level_order_traversal(self, arr):
        len_arr = len(arr)
        arr.insert(0, 0)
        
        return self.level_order_tree_helper(arr, None, 1, len_arr)
    
    def level_order_tree_helper(self, arr, root, i, n):
        if i <= n:
            root = Node(arr[i])
            
            root.left = self.level_order_tree_helper(arr, root.left, 2*i, n)
            root.right = self.level_order_tree_helper(arr, root.right, (2*i)+1, n)
            
        return root

##### Driver Code #####

bt1=BinaryTree()
bt1.root = bt1.level_order_traversal([1,2,3])

print(bt1.root.value)
print(bt1.root.left.value)
print(bt1.root.right.value)
