"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""
import math

def binary_search(input_array, value):
    search_len = len(input_array)
    #print("Input length = {}".format(search_len))
    index = 0
    
    while search_len >=1:
        mid = int(math.floor(len(input_array)/2)) + 1
        #print("mid value = {}".format(input_array[mid-1]))
        if value > input_array[mid - 1]:
            input_array = input_array[mid:]
            index += mid
        elif value < input_array[mid - 1]:
            input_array = input_array[:mid-1]
        elif value == input_array[mid - 1]:
            index += mid - 1
            return index
            
        search_len = len(input_array)
        
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)