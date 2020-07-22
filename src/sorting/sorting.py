# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # Your code here
    indexA,indexB = (0,)*2
    for i in range(elements):
        if indexA == len(arrA): 
            # Reached all the len of the arr, then will simply add the values for b
            merged_arr[i] = arrB[indexB]
            indexB+=1
        elif indexB == len(arrB): 
            # Reached all the len of the arr, then will simply add the values for a
            merged_arr[i] = arrA[indexA]
            indexA+=1
        # Now we compare values
        elif arrB[indexB] > arrA[indexA]:
            merged_arr[i] = arrA[indexA]
            indexA+=1
        else:
            merged_arr[i] = arrB[indexB]
            indexB+=1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr)<=1:
        return arr

    # arrLeft = arr[:len(arr)//2]
    # arrRight = arr[len(arr)//2:]

    arrLeft = merge_sort(arr[:len(arr)//2])
    arrRight = merge_sort(arr[len(arr)//2:])

    arr = merge(arrLeft,arrRight)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass


print(merge_sort([1512,123,124,15,15212,124,15,15212,124,15,15212,124,15,15212,124,15,15212,6]))