class disk(object):
    def __init__(self, size):
        self.size = size

class tower(object):
    def __init__(self, name):
        self.top_disk = []
        self.name = name
    
    def push(self, disk):
        self.top_disk.insert(0, disk)
    
    def pop(self):
        if len(self.top_disk) == 0:
            return None
        return self.top_disk.pop(0)
        
    def peek(self):
        if self.top_disk == []:
            return None
        return self.top_disk[0].size
    
class tower_of_hanoi(object):
    def __init__(self, t1, t2, t3):
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
    
    def move_first_to_last(self, n):
        self.move_disk(self.t1, self.t3, self.t2, n)
    
    def move_top(self, t_from, t_to):
        disk = t_from.pop()
        t_to.push(disk)
        print("Disk {} pushed from {} to {}".format(t_from.peek(), t_from.name, t_to.name))

    def move_disk(self, t_from, t_to, t_buf, n):
        if n <= 0:
            return
        # Move n-1 disk to buffer
        self.move_disk(t_from, t_buf, t_to, n-1)
        self.move_top(t_from, t_to)
        self.move_disk(t_buf, t_to, t_from, n-1)
        return
                
d1 = disk(1)
d2 = disk(2)
d3 = disk(3)
d4 = disk(4)

t1 = tower("tower 1")
t1.push(d4)
t1.push(d3)
t1.push(d2)
t1.push(d1)

t2 = tower("tower 2")
t3 = tower("tower 3")

print(t1.peek())
print(t2.peek())
print(t3.peek())

t_o_h = tower_of_hanoi(t1, t2, t3)
t_o_h.move_first_to_last(4)

print("\nAfter the move")
print(t3.pop().size)
print(t3.pop().size)
print(t3.pop().size)
print(t3.pop().size)