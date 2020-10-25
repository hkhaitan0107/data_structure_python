class stack(object):
    def __init__(self):
        self.st = []
        
    def push(self, node):
        self.st.insert(0, node)
        
    def pop(self):
        if len(self.st) > 0:
            return self.st.pop(0)
        else:
            return None
            
    def peek(self):
        if len(self.st) > 0:
            return self.st[-1]
        else:
            return None
        
class node(object):
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        
class binary_tree(object):
    def __init__(self, root):
        self.root = root
        
    def iterative_post_order(self):
        iter_st1 = stack()
        iter_st1.push(self.root)
        iter_st2 = stack()
        while iter_st1.peek() != None:
            pop_node = iter_st1.pop()
            if pop_node.left:
                iter_st1.push(pop_node.left)
                
            if pop_node.right:
                iter_st1.push(pop_node.right)
                
            iter_st2.push(pop_node)
        
        while iter_st2.peek() != None:
            print(iter_st2.pop().value)
                
    def iterative_pre_order(self):
        iter_stack = stack()
        iter_stack.push(self.root)
        
        while iter_stack.peek() != None:
            lookup_node = iter_stack.pop()
            print(lookup_node.value)
            
            if lookup_node.right:
                iter_stack.push(lookup_node.right)
            if lookup_node.left:
                iter_stack.push(lookup_node.left)
                
            
                
n1 = node(1)
n2 = node(-1)
n3 = node(11)
n4 = node(-2)
n5 = node(-3)
n6 = node(21)
n7 = node(6)
n8 = node(-5)


bt = binary_tree(n1)
bt.root.left = n2
bt.root.left.left = n4
bt.root.left.right = n5
bt.root.left.right.right = n8

bt.root.right = n3
bt.root.right.left = n6
bt.root.right.right = n7

bt.iterative_pre_order()