class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Linkedlist(object):
    def __init__(self, head):
        self.head = head
        
    def append_node(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
                
            current.next = new_node
    
    def print_linked_list(self):
        if self.head == None:
            print("Empty Linked List")
        else:
            current = self.head
            while current.next:
                print(current.value)
                current = current.next
            print(current.value)
                
    def partition_x(self, val):
        if self.head == None:
            return
        lt_list = []
        gt_list = []
        eq_list = []
        current = self.head
        while current:
            if current.value < val:
                lt_list.insert(0, current)
            elif current.value > val:
                gt_list.insert(0, current)
            else:
                eq_list.insert(0, current)
                
            current = current.next
        #x_node = eq_list.pop()
        if len(lt_list) > 0:
            self.head = lt_list.pop()
        else:
            self.head = eq_list.pop()
        current = self.head
        while len(lt_list) > 0:
            current.next = lt_list.pop()
            current = current.next
            
        while len(eq_list)>0:
            current.next = eq_list.pop()
            current = current.next
        
        while len(gt_list)>0:
            current.next = gt_list.pop()
            current = current.next
            
        
n1 = Node(5)
n2 = Node(7)
n3 = Node(2)
n4 = Node(1)
n5 = Node(8)

ll = Linkedlist(n1)
ll.append_node(n2)
ll.append_node(n3)
ll.append_node(n4)
ll.append_node(n5)

#ll.print_linked_list()
ll.partition_x(5)
ll.print_linked_list()