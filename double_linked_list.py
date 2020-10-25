####### Implementing doubly linked linked list ##########

class node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
class linkedlist(object):
    def __init__(self, head):
        self.head = head
        
    def append_node(self, node):
        if self.head == None:
            self.head = node
            
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
            node.prev = current
            
    def get_node_value(self, position):
        if self.head == None:
            return None
        else:
            start = self.head
            for i in range(position-1):
                if start == None:
                    return None
                start = start.next
            return start.value
            
    def insert_node_start(self, node):
        if self.head == None:
            self.head = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        
    def insert_element(self, node, position):
        if position == 1:
            self.insert_node_start(node)
        else:
            start = self.head
            for i in range(position - 2):
                if start == None:
                    return None
                else:
                    start = start.next
            node.next = start.next
            node.prev = start
            
            start.next.prev = node
            start.next = node
            
    def del_element_start(self, position):
        if position == 1:
            self.head.next = self.head
            
        else:
            start = self.head
            for i in range(position - 2):
                if start == None:
                    return None
                else:
                    start = start.next
            start.next = start.next.next
            start.next.prev = start
            
e1 = node(1)
e2 = node(2)
e3 = node(3)
e4 = node(4)
e5 = node(5)
e6 = node(8)

ll = linkedlist(e1)
ll.append_node(e2)
ll.append_node(e3)
ll.append_node(e4)
ll.append_node(e5)

print(ll.get_node_value(2))
#print(ll.get_node_value(3))

ll.del_element_start(2)            
print(ll.get_node_value(2))
                