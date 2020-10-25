# Palindrome in a linked list
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
                
    def detect_palindrome(self):
        left_index = self.head
        right_index = self.head
    
        while right_index.next:
            right_index = right_index.next
        #print(right_index.value)
        while True:
            current = left_index
            while current.next != right_index:
                current = current.next
            if left_index.value != current.next.value:
                return False
            else:
                print("left index: {}, right index: {}".format(left_index.value, current.next.value))
                left_index = left_index.next
                right_index = current
            
            if (left_index == right_index) or (left_index == right_index.next):
                break
        return True    

n1 = Node(1)
n2 = Node(2)
n3 = Node(2)
n4 = Node(1)
n5 = Node(1)

ll = Linkedlist(n1)
ll.append_node(n2)
ll.append_node(n3)
ll.append_node(n4)
#ll.append_node(n5)

print(ll.detect_palindrome())