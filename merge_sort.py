def mergeSort(alist):
    # print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge1 = mergeSort(lefthalf)
        merge2 = mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(merge1) and j < len(merge2):
            if merge1[i] <= merge2[j]:
                alist[k]=merge1[i]
                i=i+1
            else:
                alist[k]=merge2[j]
                j=j+1
            k=k+1

        while i < len(merge1):
            alist[k]=merge1[i]
            i=i+1
            k=k+1

        while j < len(merge2):
            alist[k]=merge2[j]
            j=j+1
            k=k+1

        return alist

    return alist
