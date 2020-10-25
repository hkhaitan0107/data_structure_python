##### De-duping Linked list #######
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
            
    def swap_elements(self, element):
        next_element = element.next
        element.next = next_element.next
        next_element.next = element
        
    def del_element(self, value):
        if self.head.value == value:
            self.head = self.head.next
        else:
            current = self.head.next
            prev = self.head
            
            while current.next:
                if current.value == value:
                    prev.next = current.next
                prev = current
                current = current.next
    
    def del_next_element(self, element):
      element.next = element.next.next

    def remove_duplicate(self):
        if self.head == None or self.head.next == None:
            return
        
        start = self.head

        while start.next.next:
            next_pointer = start.next
            prev = start
            while next_pointer.next:
                if start.value == next_pointer.value:
                    self.del_next_element(prev)
                prev = next_pointer
                next_pointer = next_pointer.next
            start = start.next
        
    def get_value(self, position):
      if position < 1:
        return None
      if position == 1:
        return self.head.value
      
      current = self.head
      i = 1
      while i < position:
        if current.next:
          current = current.next
        else:
          return None
        i += 1
      return current.value
            

e1 = node(1)
e2 = node(3)
e3 = node(4)
e4 = node(3)
e5 = node(5)
ll = linkedlist(e1)
ll.add_element(e2)
ll.add_element(e3)
ll.add_element(e4)
ll.add_element(e5)

print(ll.get_value(5))

ll.remove_duplicate()