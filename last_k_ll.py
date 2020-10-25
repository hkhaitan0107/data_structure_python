class node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class linkedlist(object):
    def __init__(self, head):
        self.head = head

    def add_element(self, element):
        if self.head == None:
            self.head = element
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = element
            
    def last_kth_element(self, k):
        current = self.head
        k_next = self.head
        
        for i in range(k-1):
            if k_next.next != None:
                k_next = k_next.next
            else:
                print("Out of Bound")
                return None
                
        while k_next.next:
            current = current.next
            k_next = k_next.next
        
        return current.value
        
e1 = node(1)
e2 = node(2)
e3 = node(3)
e4 = node(4)
e5 = node(5)

ll = linkedlist(e1)
ll.add_element(e2)
ll.add_element(e3)
ll.add_element(e4)
ll.add_element(e5)

print(ll.last_kth_element(2))