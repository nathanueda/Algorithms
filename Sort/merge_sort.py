"""
Merge Sort Algorithm:
1. If the list is only one element it is already sorted, return.
2. Else, divide the list recursively into two halves until it can no more be 
divided.
3. Merge the smaller lists into one new list in sorted order.
"""

"""
Time Complexity: O(NlogN)
    - Directly correlated with the number of times the aray can be divided in 
    half. 
Space Complexity: O(N)
    - This is typically the case. 
"""

def merge(l_sub_list: list, r_sub_list: list) -> list:
    """
    Merges two sorted sublists to form a single sorted list.
    @param l_sub_list: one of the two sublists to be merged together. 
    @param r_sub_list: one of the two sublists to be merged together. 
    @return: A single sorted list contain all elements from left_sub_list and
    right_sub_list.
    """
    n = len(l_sub_list) + len(r_sub_list)
    combined_list = [None] * n

    l_index = 0
    r_index = 0
    c_index = 0
    
    # Sorts the sublists into the combined list until the smaller sublist has 
    # been fully merged. 
    while l_index < len(l_sub_list) and r_index < len(r_sub_list):
        if l_sub_list[l_index] < r_sub_list[r_index]:
            combined_list[c_index] = l_sub_list[l_index]
            l_index += 1
        else:
            combined_list[c_index] = r_sub_list[r_index]
            r_index += 1
        c_index += 1
    
    # Only one of the below while loops will be executed (whichever sublist was
    # larger will have its loop executed).
    while l_index < len(l_sub_list):
        combined_list[c_index] = l_sub_list[l_index]
        l_index += 1
        c_index += 1
    
    while r_index < len(r_sub_list):
        combined_list[c_index] = r_sub_list[r_index]
        r_index += 1
        c_index += 1
    
    return combined_list

def merge_sort(list_to_sort: list) -> list:
    """
    A recursive sorting algorithm that continously divides the list in half 
    again and again until there are n sublists each containing one element. It 
    then merges these sublists back together produced ordered sublists until
    there is only one final list. 
    @param list_to_sort: The list to sort.
    @return: The sorted list. 
    """
    n = len(list_to_sort)
    if n <= 1:
        return list_to_sort
    else:
        # Sort left half.
        l_half_sorted = merge_sort(list_to_sort[:n//2])
        # Sort right half.
        r_half_sorted = merge_sort(list_to_sort[n//2:])
        # Merge the left and right halves.
        return merge(l_half_sorted, r_half_sorted)

"""
Examples:
items = [11, 8, 3, 1, 0, 34, 5, 6]
merge_sort(items)
items = [0, 1, 3, 5, 6, 8, 11, 34]

items = []
merge_sort(items)
items = []

items = [0, 1, 3, 5, 6, 8, 11, 34]
merge_sort(items)
items = [0, 1, 3, 5, 6, 8, 11, 34]
"""

"""
Notes:
- Mergesort is a divide and conquer algorithm. 
- Merge sort is more efficient than quicksort for some types of lists if the 
data to be sorted can only be efficiently accessed sequentially
- Merge sort is often the best choice for sorting a linked list since in this 
situation it is relatively easy to implement a merge sort in such a way that it r
equires only O(1) extra space.
"""