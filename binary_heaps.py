# Heaps implementation

class min_heap(object):
    def __init__(self, element):
        self.heap_arr = [element]
        
    def insert_element(self, element):
        #Add element to the end of the array (next available space in heap)
        self.heap_arr.append(element)
        # Re-adjust to maintain heap
        self.insert_readjustment()
    
    def swap_element(self, new_element, parent_element):
        k = self.heap_arr[new_element]
        self.heap_arr[new_element] = self.heap_arr[parent_element]
        self.heap_arr[parent_element] = k
        
    def insert_readjustment(self):
        new_element = len(self.heap_arr) - 1
        parent_element = int((new_element + 1)//2)-1
        while True:
            if self.heap_arr[new_element] > self.heap_arr[parent_element]:
                break
            else:
                if new_element == 0:
                    break
                else:
                    #Swap elements
                    self.swap_element(new_element, parent_element)
                    new_element = parent_element
                    parent_element = int((new_element + 1)//2)-1
                    
    def del_element(self):
        #Swap last element with the first one
        last_el = len(self.heap_arr) - 1
        self.swap_element(last_el,0)
        self.heap_arr.pop()
        # Top down re-adjustment to maintain heap
        self.del_readjustment()
        
    def del_readjustment(self):
        if len(self.heap_arr) <= 2:
            return
        parent_el = 0
        if self.heap_arr[(parent_el + 1)*2 - 1] < self.heap_arr[(parent_el + 1)*2 ]:
            child_el = (parent_el + 1)*2 - 1
        else:
            child_el = (parent_el + 1)*2 
        
        while True:
            if self.heap_arr[parent_el] < self.heap_arr[child_el]:
                break
            else:
                self.swap_element(parent_el, child_el)
                parent_el = child_el
                
                if (parent_el + 1)*2 > len(self.heap_arr):
                    break
                else:
                    if self.heap_arr[(parent_el + 1)*2 - 1] < self.heap_arr[(parent_el + 1)*2 ]:
                        child_el = (parent_el + 1)*2 - 1
                    else:
                        child_el = (parent_el + 1)*2

        
    
#############################################
########### Better implementation ###########
#############################################
"""
Min Heap Implementation in Python
"""
class MinHeap:
    def __init__(self):
        """
        On this implementation the heap list is initialized with a value
        """
        self.heap_list = [0]
        self.current_size = 0
 
    def sift_up(self, i):
        """
        Moves the value up in the tree to maintain the heap property.
        """
        # While the element is not the root or the left element
        while i // 2 > 0:
            # If the element is less than its parent swap the elements
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            # Move the index to the parent to keep the properties
            i = i // 2
 
    def insert(self, k):
        """
        Inserts a value into the heap
        """
        # Append the element to the heap
        self.heap_list.append(k)
        # Increase the size of the heap.
        self.current_size += 1
        # Move the element to its position from bottom to the top
        self.sift_up(self.current_size)
 
    def sift_down(self, i):
        # if the current node has at least one child
        while (i * 2) <= self.current_size:
            # Get the index of the min child of the current node
            mc = self.min_child(i)
            # Swap the values of the current element is greater than its min child
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc
 
    def min_child(self, i):
        # If the current node has only one child, return the index of the unique child
        if (i * 2)+1 > self.current_size:
            return i * 2
        else:
            # Herein the current node has two children
            # Return the index of the min child according to their values
            if self.heap_list[i*2] < self.heap_list[(i*2)+1]:
                return i * 2
            else:
                return (i * 2) + 1
 
    def delete_min(self):
        # Equal to 1 since the heap list was initialized with a value
        if len(self.heap_list) == 1:
            return 'Empty heap'
 
        # Get root of the heap (The min value of the heap)
        root = self.heap_list[1]
 
        # Move the last value of the heap to the root
        self.heap_list[1] = self.heap_list[self.current_size]
 
        # Pop the last value since a copy was set on the root
        #*self.heap_list, _ = self.heap_list
        #self.heap_list.pop(self.current_size)
        
        # Decrease the size of the heap
        self.current_size -= 1
 
        # Move down the root (value at index 1) to keep the heap property
        self.sift_down(1)
 
        # Return the min value of the heap
        return root
        
    def heap_sort(self, type):
        while self.current_size > 0:
            # delete the min element
            top_el = self.delete_min()
            
            # insert deleted element at the end of the heap list
            if type == "ascending":
                self.heap_list.pop(self.current_size + 1)
                self.heap_list.append(top_el)
            elif type == "descending":
                self.heap_list[self.current_size +1] = top_el
            else:
                print("Wrong input")
                break
            
        return  self.heap_list


"""
Driver program
"""
# Same tree as above example.
my_heap = MinHeap()
my_heap.insert(5)
my_heap.insert(6)
my_heap.insert(7)
my_heap.insert(9)
my_heap.insert(13)
my_heap.insert(11)
my_heap.insert(10)

print(my_heap.heap_list)
#print(my_heap.delete_min()) # removing min node i.e 5 
print(my_heap.heap_sort("descending")[1:])
