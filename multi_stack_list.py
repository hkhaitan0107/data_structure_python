# Implementing three stacks using a single array

class multi_stack(object):
    def __init__(self, num_stacks):
        self.top_array = [None] * num_stacks
        
    def push(self, stack_num, element):
        if stack_num > len(self.top_array):
            return None
            
        if self.top_array[stack_num - 1] == None:
            self.top_array[stack_num - 1] = [element]
        else:
            self.top_array[stack_num - 1].insert(0, [element])
            
    def pop(self, stack_num):
        if stack_num > len(self.top_array) or self.top_array[stack_num - 1] == None:
            return None
        
        else:
            return self.top_array[stack_num - 1].pop(0)
        
    def peek(self, stack_num):
        if stack_num > len(self.top_array):
            return None
        else:
            return self.top_array[stack_num - 1][0]
            
three_stack = multi_stack(3)
three_stack.push(1, 5)
three_stack.push(1, 7)
three_stack.push(1, 2)

three_stack.push(2, 2)
three_stack.push(2, 3)

print(three_stack.pop(1)[0])

print(three_stack.peek(1)[0])
print(three_stack.pop(2)[0])
