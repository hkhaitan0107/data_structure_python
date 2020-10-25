class heapify(object):
    def __init__(self, list_el):
        self.heap_list = [0] + list_el
        self.heap_size = len(list_el)
    
    def heapify(self):
        #current_size = len(self.heap_list) - 1
        self.heapify_helper(1)        
        return self.heap_list
    
    def heapify_helper(self, current_index):
        if current_index == self.heap_size:
            return
        
        self.heapify_helper(current_index + 1)
        #print(current_index)
        self.heapify_sift_down(current_index)
        print(self.heap_list)
    
    def heapify_sift_down(self, current_index):
        if current_index * 2 > self.heap_size:
            return
        min_c = self.min_child(current_index)
        self.heap_list[min_c], self.heap_list[current_index] = self.heap_list[current_index], self.heap_list[min_c]
        
    def min_child(self, current_index):
        if (current_index*2)+1 > self.heap_size:
            return (current_index*2)
        else:
            if self.heap_list[(current_index*2)+1] > self.heap_list[(current_index*2)]:
                return (current_index*2)
            else:
                return (current_index*2) + 1

my_heap = heapify([4,8,2,1])
print(my_heap.heapify())