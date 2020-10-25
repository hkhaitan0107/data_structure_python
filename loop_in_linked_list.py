# Finding loop in a linked list
class Node(object):
    def __init__(self, val):
        self.value = val
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
            while current:
                print(current.value)
                current = current.next
                
    def detect_loop(self):
        runner1 = self.head
        runner2 = self.head
        while runner2.next:
            print("Runner 1: {}; Runner 2: {}".format(runner1.value, runner2.value))
            runner1 = runner1.next
            runner2 = runner2.next.next
            if runner1.next == runner2.next:
                return True
            
        return False

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

ll = Linkedlist(n1)
ll.append_node(n2)
ll.append_node(n3)
ll.append_node(n4)
ll.append_node(n5)

n5.next = ll.head

print(ll.detect_loop())