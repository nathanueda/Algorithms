"""
linear_search_unsorted Algorithm:
1. Start from the leftmost element of the data structure and one by one comapre 
the query to each element in the data structure.
2. If the query matches with an element, return true.
3. If the query doesn't match with any element, return false.

"""

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""

def linear_search_unsorted(query, items):
    """
    Searches for a query within an unsorted data structure.
    Unoptimized for a sorted data structure.
    @param query: value to search for.
    @param items: data structure (list or tuple) to search for query in.
    @return: True if query is present in items, false otherwise.
    """
    for item in items:
        if item == query:
            return True
    return False

"""
Examples: 
linear_search_unsorted(5, [5, 6, 1, 4, 2])
@return: True

linear_search_unsorted(2, [5, 6, 1, 4, 2])
@return: True

linear_search_unsorted(1, [5, 6, 1, 4, 2])
@return: True

linear_search_unsorted(11, [5, 6, 1, 4, 2])
@return: False

linear_search_unsorted('hello', [5, 'bye', 1, 4, 'hello'])
@return: True
"""

"""
Notes:
- Rarely the most efficient searching algorithm. 
"""
