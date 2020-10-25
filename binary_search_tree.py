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
        
    def binary_tree_comparison(self, tree2):
        return self.helper_bt_comparison(self.root, tree2.root)
        
    def helper_bt_comparison(self, start1, start2):
        if start1 and start2:
            if start1.value == start2.value:
                print("tree1 node {} = tree2 node {}".format(start1.value, start2.value))
                left_branch = self.helper_bt_comparison(start1.left, start2.left)
                right_branch = self.helper_bt_comparison(start1.right, start2.right)
                return (left_branch and right_branch)
            else:
                print("tree1 node {} != tree2 node {}".format(start1.value, start2.value))
                return False
        elif start1 == None and start2 == None:
            return True
        else:
            return False
            
    def size_of_binary_tree(self):
        return self.helper_bt_size(self.root)
        
    def helper_bt_size(self, start):
        if start:
            left_count = 1 + self.helper_bt_size(start.left)
            print("left size = {}; node = {}".format(left_count, start.value))
            right_count = self.helper_bt_size(start.right)
            print("Right size = {}; node = {}".format(right_count, start.value))
            return left_count + right_count
        else:
            return 0
            
    def height_binary_tree(self):
        return self.helper_bt_height(self.root)
        
    def helper_bt_height(self, start):
        if start:
            left_branch = self.helper_bt_height(start.left)
            right_branch = self.helper_bt_height(start.right)
            if left_branch >= right_branch:
                return 1 + left_branch
            else:
                return 1 + right_branch
        else:
            return 0
            
    def root_to_leaf_sum(self, sum_1):
        sum_2 = 0
        return self.helper_root_to_leaf_sum(self.root, sum_1, sum_2)
        
    def helper_root_to_leaf_sum(self, start, sum_1, sum_2):
        if start:
            val = start.value
            sum_2 = sum_2 + val
            left_branch = self.helper_root_to_leaf_sum(start.left, sum_1, sum_2)
            right_branch = self.helper_root_to_leaf_sum(start.right, sum_1, sum_2)
            return left_branch or right_branch
        else:
            if sum_1 == sum_2:
                return True
            else:
                return False
    
    def check_binary_search_tree(self):
        return self.helper_check_bst(self.root, -10000, 10000)
        
    def helper_check_bst(self, start, min_val, max_val):
        if start:
            if start.value > min_val and start.value < max_val:
                left_check = self.helper_check_bst(start.left, min_val, start.value)
                right_check = self.helper_check_bst(start.right, start.value, max_val)
                return left_check and right_check
            return False
        else:
            return True
        

n3 = node(10)
n2 = node(15)
n1 = node(3)
n4 = node(30)
n5 = node(2)
n6 = node(9)
n7 = node(8)
n8 = node(6)
n9 = node(5)
n10 = node(45)

bt = binary_tree(n3)
bt.root.left = n2
bt.root.left.left = n1
bt.root.left.right = n8
bt.root.left.left.left = n9

bt.root.right = n4
bt.root.right.right = n5
bt.root.right.right.left = n6
bt.root.right.right.right = n7
bt.root.right.right.right.left = n10

print(bt.root_to_leaf_sum(52))
print(bt.root.left.left.value)
print(bt.binary_tree_postorder())
n3_2 = node(10)
n2_2 = node(15)
n1_2 = node(3)
n4_2 = node(30)
n5_2 = node(2)
n6_2 = node(9)
n7_2 = node(8)
n8_2 = node(6)
n9_2 = node(5)
n10_2 = node(45)

bt2 = binary_tree(n3_2)
bt2.root.left = n2_2
bt2.root.left.left = n1_2
bt2.root.left.right = n8_2
bt2.root.left.left.left = n9_2

bt2.root.right = n4_2
bt2.root.right.right = n5_2
bt2.root.right.right.left = n6_2
bt2.root.right.right.right = n7_2

print(bt.binary_tree_comparison(bt2))
print(bt.binary_tree_postorder())


n1 = node(1)
n3 = node(3)
n4 = node(4)
n5 = node(5)
n6 = node(6)
n7 = node(7)
n9 = node(3)

bt = binary_tree(n5)
bt.root.left = n3
bt.root.left.left = n1
bt.root.left.right = n4

bt.root.right = n7
bt.root.right.left = n6
bt.root.right.right = n9
print(bt.check_binary_search_tree())