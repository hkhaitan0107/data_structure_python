class queue(object):
    def __init__(self, node):
        self.que = [node]
        
    def enqueue(self, node):
        self.que.insert(0, node)
    
    def dequeue(self):
        if len(self.que) > 0:
            return self.que.pop()
        else:
            return None
        
    def peek(self):
        if len(self.que) > 0:
            #print(len(self.que))
            return self.que[-1]
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
        
    def level_order_traversal(self):
        traversal_queue = queue(self.root)
        
        while traversal_queue.peek() != None:
            lookup_node = traversal_queue.dequeue()
            print(lookup_node.value)
            
            if lookup_node.left:
                traversal_queue.enqueue(lookup_node.left)
                
            if lookup_node.right:
                traversal_queue.enqueue(lookup_node.right)
                
n1 = node(10)
n2 = node(9)
n3 = node(-10)
n4 = node(11)
n5 = node(16)
n6 = node(21)
n7 = node(15)
n8 = node(18)
n9 = node(19)

bt = binary_tree(n1)
bt.root.left = n2
bt.root.left.left = n4
bt.root.left.left.right = n7

bt.root.right = n3
bt.root.right.left = n5
bt.root.right.right = n6
bt.root.right.left.left = n8
bt.root.right.right.right = n9

bt.level_order_traversal()