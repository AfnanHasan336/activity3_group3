def binary_search(sorted_array, target):
    '''
    This function permits to perform binary search to find a target within a sorted array from the previously defined function in Phase 1
    and returns the index of the target when it finds it, or returns None if not found.
    sorted_array: array(list)
    target: int
    '''
    start = 0
    end = len(sorted_array) - 1   # initializations of start and end as index 0 and len - 1
    while end >= start:           # base case, as long as end is greater than start
        mid = (start + end) // 2  

        if target == sorted_array[mid]:
            return mid            
        elif target > sorted_array[mid]:
            start = mid + 1       # if target is bigger than mid, we move to the right of array, so start point is on the right of mid
        else:
            end = mid - 1         # if target is smaller than mid, we move to the left of array, so end point is on the left of mid
    return None
def linear_search(sorted_array, target):
    '''
    This function performs linear search on a sorted array to find a given target
    sorted_array: array(list)
    target: int
    '''
    for i in range(len(sorted_array)):  # iterating thought the array
        if target == sorted_array[i]:   # checking if given target is equal to the element at index "i"
            return True
    return False