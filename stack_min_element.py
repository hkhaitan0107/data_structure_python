# Implementing three stacks using a single array

class stack(object):
    def __init__(self, top):
        self.top = [top]
        self.min = [top]
        
    def push(self, element):
        if self.top == []:
            self.top[0] = element
            self.min[0] = element
        else:
            self.top.insert(0, element)
            if element < self.min[0]:
                self.min.insert(0, element)
            
    def pop(self):
        if self.top == []:
            return "Empty Stack"
        else:
            if self.top[0] == self.min[0]:
                self.min.pop(0)
            return self.top.pop(0)
        
    def peek(self):
        return self.top[0]
        
    def min_el(self):
        return self.min[0]