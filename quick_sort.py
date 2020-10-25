"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    # Base Case
    if len(array) <= 1:
        return array
    
    #### Implement split point detection ####
    #Initializing pivot and markers
    pivot = 0
    leftmark = 1
    rightmark = len(array) -1
    print("\n")
    print(array)
    print("Pivot = {}".format(array[pivot]))
    print("Initial Left mark = {}".format(array[leftmark]))
    print("Initial Right mark = {}".format(array[rightmark]))
    
    if leftmark == rightmark:
        #Just swap values
        #Swap pivot to split point
        l = array[pivot]
        array[pivot] = array[rightmark]
        array[rightmark] = l
        return array
    
    while rightmark > leftmark:
        
        while array[leftmark] <= array[pivot] and leftmark < rightmark:
            leftmark += 1
            print("leftmark value = {}".format(array[leftmark]))
            
        while array[rightmark] > array[pivot]:
            rightmark -= 1
            print("rightmark value = {}".format(array[rightmark]))
        
        if rightmark < leftmark:
            break
        # Swap value
        k = array[leftmark]
        array[leftmark] = array[rightmark]
        array[rightmark] = k
        
    #Swap pivot to split point
    l = array[pivot]
    array[pivot] = array[rightmark]
    array[rightmark] = l
    print("pivot swapped array: {}".format(array))
    
    # Split array into two parts for recursion
    part1 = array[:rightmark]
    part2 = array[rightmark + 1:]
    splitpoint = array[rightmark]
    
    sorted1 = quicksort(part1)
    sorted2 = quicksort(part2)
    
    return sorted1 + [splitpoint] + sorted2

#test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
test = [5,2,3,1,4, 9, 0]
print quicksort(test)



######## Another Implementation ###########
def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)
