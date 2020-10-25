class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTree(object):
    def __init__(self, root):
        self.root = root
        
    def in_order_bt_traversal(self):
        ret_list = self.helper_in_order_traversal(self.root)
        return ret_list
        
    def helper_in_order_traversal(self, start):
        if start:
            left = self.helper_in_order_traversal(start.left)
            right = self.helper_in_order_traversal(start.right)
            
            if left:
                return_list = left + [start.value]
            else:
                return_list = [start.value]
            if right:
                return_list += right
            
            return return_list
        else:
            return None
            
    def pallindrome_check(self, arr):
        if len(arr) <= 1:
            return True
        if arr[0] == arr[-1]:
            return self.pallindrome_check(arr[1:-1])
        else:
            return False
    
    def check_symmetrical_tree(self):
        # Get in-order traversal output
        in_order_tr = self.in_order_bt_traversal()
        
        #Check Pallindrome
        return self.pallindrome_check(in_order_tr)
            
##### Driver Code #####
n1 = Node(1)
n2 = Node(2)
n3 = Node(2)
bt1=BinaryTree(n1)
bt1.root.left = n2
bt1.root.right = n3
print(bt1.check_symmetrical_tree())