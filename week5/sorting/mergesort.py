def mergeSort(nlist):
    print("Splitting ",nlist)
    # insert your code to complete the mergeSort function
    if len(nlist) > 1:
        # Find the middle of the array
        mid = len(nlist) // 2
        # Divide the left side of array
        left = nlist[:mid]
        # Divide the right side of array
        right = nlist[mid:]
        # Sort first half
        mergeSort(left)
        # sort second half
        mergeSort(right)
    
        print("Merging ",nlist)
        return merge(nlist, left, right)

def merge(nlist,lefthalf,righthalf):
    i=j=k=0       
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            nlist[k]=lefthalf[i]
            i=i+1
        else:
            nlist[k]=righthalf[j]
            j=j+1
        k=k+1

    while i < len(lefthalf):
        nlist[k]=lefthalf[i]
        i=i+1
        k=k+1

    while j < len(righthalf):
        nlist[k]=righthalf[j]
        j=j+1
        k=k+1
    return nlist

arr = [ 55 ,  31 ,  26 ,  20 ,  63 ,  7 ,  51 ,  74 ,  81 ,  40 ]
print(mergeSort(arr))