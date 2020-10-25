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
            
            
    def reverse_level_order(self):
        track_queue = [[self.root]]
        level_order_list = []
        
        while track_queue != [[]]:
            current = track_queue.pop()
            k = []
            level_nodes = []
            for i in current:
                if level_nodes == []:
                    level_nodes = [i.value]
                else:
                    level_nodes.append(i.value)
                #print("Current Node: {}".format(i.value))    
                
                left_child = []
                right_child = []
                if i.left:
                    left_child = [i.left]
                if i.right:
                    right_child = [i.right]
                child_nodes = left_child + right_child
                k += child_nodes
                
            #print("Level Nodes: {}".format(level_nodes))        
            if len(level_order_list) == 0:
                level_order_list = [level_nodes]
            else:
                level_order_list.insert(0, level_nodes)
            #print("Level Nodes: {}".format(level_order_list))        
            track_queue.insert(0, k)
        
        return level_order_list
                
                
                
                
##### Driver Code #####

bt1=BinaryTree()
bt1.root = bt1.level_order_traversal([1, 2, 3, 4, 5, 6])

print(bt1.root.value)
print(bt1.root.left.value)
print(bt1.root.right.value)

print(bt1.reverse_level_order())
