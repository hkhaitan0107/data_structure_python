#Binary Tree Traversal

class node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class binary_tree(object):
    def __init__(self, root):
        self.root = root
    
    def binary_tree_preorder(self):
        return self.helper_bt_preorder(self.root)
        
    def helper_bt_preorder(self, start):
        if start:
            val = str(start.value)
            if start.left:
                left = self.helper_bt_preorder(start.left)
                val = val + "-" + str(left)
            if start.right:
                right = self.helper_bt_preorder(start.right)
                val = val + "-" + str(right)
            return val
        else:
            return
        
    def binary_tree_inorder(self):
        return self.helper_bt_inorder(self.root)
        
    def helper_bt_inorder(self, start):
        if start:
            val = str(start.value)
            
            if start.left:
                left = self.helper_bt_inorder(start.left)
                val = str(left) + "-" + val
            
            if start.right:
                right = self.helper_bt_inorder(start.right)
                val = val + "-" + str(right)
            return val
        else:
            return
                
    def binary_tree_postorder(self):
        return self.helper_bt_postorder(self.root)
        
    def helper_bt_postorder(self, start):
        if start:
            
            if start.left:
                left = str(self.helper_bt_postorder(start.left)) + "-"
                #val = str(left) + "-" + val
            else:
                left = ""
            
            if start.right:
                right = str(self.helper_bt_postorder(start.right)) + "-"
                #val = val + "-" + str(right)
            else:
                right = ""
                
            val = left + right + str(start.value)
            return val
        else:
            return

n3 = node(10)
n2 = node(15)
n1 = node(3)
n4 = node(30)
n5 = node(2)
n6 = node(9)
n7 = node(8)
n8 = node(6)
n9 = node(5)

bt = binary_tree(n3)
bt.root.left = n2
bt.root.left.left = n1
bt.root.left.right = n8
bt.root.left.left.left = n9

bt.root.right = n4
bt.root.right.right = n5
bt.root.right.right.left = n6
bt.root.right.right.right = n7

#print(bt.root.left.left.value)
print(bt.binary_tree_postorder())