# Check if the binary tree is balanced
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTree(object):
    def __init__(self, root=None):
        self.root = root
        
    def array_to_bt(self, arr):
        l = len(arr)
        arr.insert(0, 0)
        return self.array_to_bt_helper(arr, None, 1, l)
        
    def array_to_bt_helper(self, arr, root, i, n):
        if i<=n:
            el = arr[i]
            root = Node(el)
            root.left = self.array_to_bt_helper(arr, root.left, 2*i, n)
            root.right = self.array_to_bt_helper(arr, root.right, (2*i)+1, n)
            
        return root
        
    def check_balanced_tree(self, start):
        if start:
            check_left, left_ht = self.check_balanced_tree(start.left)
            check_right, right_ht = self.check_balanced_tree(start.right)
            
            if check_left == False or check_right == False:
                return False, max(left_ht, right_ht) + 1
                
            elif abs(left_ht - right_ht) <= 1:
                return True, max(left_ht, right_ht) + 1
            else:
                return False, max(left_ht, right_ht) + 1
                
        return True, 0

# Driver Code        
bt1=BinaryTree()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)

bt1.root = n1
bt1.root.left = n2
bt1.root.right = n3
bt1.root.right.right = n4
bt1.root.right.right.left = n5
bt1.root.right.right.right = n6

check_balanced_bt, ht = bt1.check_balanced_tree(bt1.root)
print(check_balanced_bt, ht)