#### Deleting element from singly linked linked list #####

class node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
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
    
    def del_node_middle(self, del_node):
        current = self.head
        while current.next:
            if current.next == del_node:
                current.next = del_node.next
                break
            current = current.next

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
            
    def sum_elements_reverse(self, start):
        if start.next == None:
            return start.value
            
        sum = start.value + self.sum_elements_reverse(start.next) * 10
        return sum
        
    def sum_elements(self):
        if self.head == None:
            return 0
        start = self.head
        sum_node = 0
        while start:
            sum_node = sum_node * 10 + start.value
            start = start.next
        return sum_node
        
e1 = node(7)
e2 = node(1)
e3 = node(6)

ll = linkedlist(e1)
ll.append_node(e2)
ll.append_node(e3)

print(ll.get_node_value(3))
print(ll.sum_elements_reverse(ll.head))
print(ll.sum_elements())