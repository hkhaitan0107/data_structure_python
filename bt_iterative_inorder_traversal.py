# In Order Binary tree traversal
class node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class stack(object):
    def __init__(self):
        self.st_list = []
        
    def push(self, value):
        self.st_list.insert(0, value)
        
    def pop(self):
        if len(self.st_list) > 0:
            return self.st_list.pop(0)
        else:    
            return None
            
    def peek(self):
        if len(self.st_list) > 0:
            return self.st_list[0]
        else:    
            return None

class binary_tree(object):
    def __init__(self, root_node):
        self.root = root_node
        
    def iterative_inorder_traversal(self):
        if self.root == None:
            return None
        st1 = stack()
        tracker = self.root
        while True:
            if tracker != None:
                st1.push(tracker)
                tracker = tracker.left
            else:
                if st1.peek() == None:
                    break
                k = st1.pop()
                print(k.value)
                tracker = k.right

n1 = node(4)
n2 = node(2)
n3 = node(6)
n4 = node(5)
n5 = node(3)
n6 = node(1)

bt = binary_tree(n1)
bt.root.left = n2
bt.root.left.left = n4
bt.root.left.right = n5

bt.root.right = n3
bt.root.right.right = n6

bt.iterative_inorder_traversal()

