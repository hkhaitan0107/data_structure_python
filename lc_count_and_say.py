class Queue(object):
    def __init__(self):
        self.que = []
        
    def enqueue(self, val):
        if len(self.que) > 0:
            self.que.insert(0, val)
        else:
            self.que = [val]
            
    def dequeue(self):
        if len(self.que) > 0:
            return self.que.pop()
        else:
            return None
            
    def peek(self):
        if len(self.que) > 0:
            return self.que[-1]
        else:
            return None
            
    def clear_que(self):
        self.que = []
            
def count_and_say(n):
    if n == 1:
        return '1'
        
    k = count_and_say(n-1)
    print("Recurssion number = {}".format(n))
    print(k)
    k_queue = Queue()
    
    while len(k) > 0:
        k_last = k[-1]
        k_queue.enqueue(k_last)
        
        k = k[:-1]
    
    top_el = k_queue.peek()
    
    counter = 0
    count_n_say_str = ''
    while k_queue.peek() != None:
        if top_el == k_queue.peek():
            counter += 1
            k_queue.dequeue()
        else:    
            count_n_say_str = str(counter) + top_el + count_n_say_str
            top_el = k_queue.peek()
            counter = 0
    count_n_say_str = str(counter) + top_el + count_n_say_str
    return count_n_say_str
    
print("\nFinal Count & say number: {}".format(count_and_say(5)))