# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here

    if start > end:
        return -1

    mid = (start+end)//2

    if target == arr[mid]:
        print(target,"Found @ index",mid)
        return mid
    elif target > arr[mid]:
        return binary_search(arr,target,mid+1,end)
    else:
        return binary_search(arr,target,start,mid-1)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here

    start = 0
    end = len(arr)-1

    while start <= end:
        mid = (start+end) // 2

        if arr[mid]==target:
            print(target,"Found @ index",mid)
            return mid
        
        if arr[0]>arr[end]: #Check if array is in descending order
            if target < arr[mid]:
                start = mid+1
            else:
                end = mid-1
        else:
            if target < arr[mid]:
                end = mid-1
            else:
                start = mid+1

    return -1


binary_search([-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9], 8, -9, 9)