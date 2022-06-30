"""
Binary Search Algorithm:
1. Begin with an interval covering the whole array.
2. If the query we are searchig for is equal to the value t the index in the 
middle of the interval, return the index of the midpoint.
3. Else if the query we are seraching for is less than the value at the index in 
the middle of the interval, narrow this interval to the left half of the data 
structure.
4. Else if the query we are searching for is greater than the value at the index 
in the middle of the interval, narrow this interval to the right half of the 
data structure. 
5. Repeat steps 2-4 until the query is found or the interval is empty.

Time Complexity: O(logn)
Space Complexity: O(1)
"""

def binary_search(query, items):
    """
    Searches for a query within a sorted data structure (list or tuple).
    @param query: value to search for.
    @param items: data structure (list or tuple) to search for query in.
    @return: Index of query if present in items, None otherwise.
    """
    left = 0 
    right = len(items) - 1

    while left <= right:
        midpoint = (left + right) // 2

        if query == items[midpoint]:
            return midpoint
        elif query < items[midpoint]:
            right = midpoint - 1
        elif query > items[midpoint]:
            left = midpoint + 1
    
    return None