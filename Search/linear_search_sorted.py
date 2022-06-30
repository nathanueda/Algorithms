"""
linear_search_sorted Algorithm:
1. Start from the leftmost element of the data structure and one by one comapre 
the query to each element in the data structure.
2. If the query matches with an element, return true.
3. Else if the item in the data structure is larger than the query, return 
false.
4. If the query doesn't match with any element, return false.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def linear_search_sorted(query, items):
    """
    Searches for a query within a sorted data structure.
    @param query: value to search for.
    @param items: data structure (list or tuple) to search for query in.
    @return: True if query is present in items, false otherwise.
    """
    for item in items:
        if item == query:
            return True 
        elif item > query:
            break
    return False