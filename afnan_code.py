# Phase 1: Data Generation and Initial sorting using insertion sort

def generate_sorted_data(size):   # this is for an array of smaller size
    '''
    This function generates an array of given size using random integers between 1 and 100, and sorts the array using insertion sort
    size: int
    '''
    my_array = arrays.Array(size)   # creates an array of given size
    for i in range(len(my_array)):
        a = random.randint(1,100)   
        my_array[i] = a             # assigning each index in the array to a random integer between 1 and 100  
    for i in range(1,len(my_array)):
        key = my_array[i]           # assigning the element to be sorted in the iteration as key
        prev_i = i-1
        while prev_i>=0 and my_array[prev_i] > key:  # comparing all the elements in the unsorted part
            my_array[prev_i+1] = my_array[prev_i]
            prev_i = prev_i - 1
        my_array[prev_i+1] = key    # setting the element after the previous as the key
    return my_array

# Phase 4: Search Performance Comparison
def search_perf_compare(sorted_array, target):
    '''
    This function compares the search times between linear search and binary search using the per_counter() function from time module
    sorted_array: array(list)
    target: int
    '''
    linear_start = perf_counter()
    linear_search(sorted_array, target)
    linear_end = perf_counter()
    linear_time = linear_end - linear_start  # difference in time before and after linear search

    binary_start = perf_counter()
    binary_search(sorted_array, target)
    binary_end = perf_counter()
    binary_time = binary_end - binary_start  # difference in time before and after binary search


    if binary_time < linear_time:
        print("This proves that binary search is more efficient when compared to linear search for searching over large sorted datasets")

sorted_array = [15, 22, 34, 39, 44, 55, 67, 72, 89, 90]
target = 72
search_perf_compare(sorted_array, target)