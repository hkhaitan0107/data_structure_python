## Bubble Sort ##

def bubble_sort(alist):
    if len(alist) <= 1:
        return alist
    
    for i in range(len(alist)):
        for j in range(len(alist) - i - 1):
            if alist[j + 1] <= alist[j]:
                k = alist[j]
                alist[j] = alist[j+1]
                alist[j+1] = k
                
    return alist
    
l = [4,2,1,3]    
print(bubble_sort(l))