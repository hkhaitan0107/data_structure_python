# Implementing three stacks using a single array

class set_of_stacks(object):
    def __init__(self, top, limit):
        self.stack_dict = {1:[top]}
        self.limit = limit
        self.counter = 1

    def push(self, element):
        if self.counter % self.limit == 0:
            self.stack_dict[int(self.counter/self.limit) + 1] = [element]
        else:
            self.stack_dict[int(self.counter/self.limit) + 1].insert(0, element)
            
        self.counter += 1
            
    def pop(self):
        if self.stack_dict[1] == []:
            return "Empty Stack"
        elif self.counter % self.limit == 1:
            k = self.stack_dict[int(self.counter/self.limit) + 1].pop(0)
            del self.stack_dict[int(self.counter/self.limit) + 1]
            self.counter -= 1
            return k
        else:
            self.counter -= 1
            return self.stack_dict[int(self.counter/self.limit) + 1].pop(0)
            
    def peek(self):
        return self.stack_dict[int(self.counter/self.limit) + 1][0]
        
    def popAt(self, index):
        if index > int(self.counter/self.limit) + 1:
            return None
        
ss = set_of_stacks(10, 5)
ss.push(3)
ss.push(6)
ss.push(4)
ss.push(9)
ss.push(2)
ss.push(1)
ss.push(8)
print(ss.peek())
print(ss.pop())
print(ss.pop())
print(ss.pop())
print(ss.pop())
print(ss.peek())

######### Second implementation ###########
# Implementing three stacks using a single array

class set_of_stacks(object):
    def __init__(self, top, limit):
        self.stack_dict = {1:[top]}
        self.limit = limit
        self.stack_counter = 1

    def push(self, element):
        if len(self.stack_dict[self.stack_counter]) == self.limit:
            self.stack_dict[self.stack_counter+ 1] = [element]
            self.stack_counter += 1
        else:
            self.stack_dict[self.stack_counter].insert(0, element)
            
    def pop(self):
        if self.stack_dict[1] == []:
            return "Empty Stack"
        elif len(self.stack_dict[self.stack_counter]) == 1:
            k = self.stack_dict[self.stack_counter].pop(0)
            del self.stack_dict[self.stack_counter]
            self.stack_counter -= 1
            return k
        else:
            return self.stack_dict[self.stack_counter].pop(0)
            
    def peek(self):
        return self.stack_dict[self.stack_counter][0]
        
    def popAt(self, index):
        if index > self.stack_counter:
            return None
        else:
            return self.stack_dict[index].pop(0)

ss = set_of_stacks(10, 5)
ss.push(3)
ss.push(6)
ss.push(4)
ss.push(9)
ss.push(2)
ss.push(1)
ss.push(8)
print(ss.peek())

print(ss.popAt(1))