"""
Partitioning Algorithm:
1. Set the rightmost value to be the pivot (although we could choose any index 
so long as we are consistent). Assign variables to hold the left 
most index of the array and the right most index of the array (excluding the 
pivot itself) labeled left_index and right_index.
2. While the value held at left_index is less than the pivot, increment 
left_index by one. When the value held at left_index is greater than or equal to
the pivot, stop.
3. While the value held at right_index is greater than the pivot, decrement 
right_index by one. When the value held at right_index is less than or equal to 
the pivot or reaches the beginning of the array, stop.
4. If left_index has reached or gone beyond right index, skip to step 5. 
Otherwise, swap the values at left_index and right_index of the array and repeat
steps 2-4.
5. Swap the pivot with the value at left_index.
"""

"""
Quick Sort Algorithm:
1. Partition the array. The pivot is now in its proper place.
2. Treat the subarrays to the left and right of the pivot as their own arrays 
and recursively repeat steps 1 and 2. This means we will partition each 
subarray, continuously resulting in even smaller sub-subarrays to the left and 
right of each subarray's pivot. We then continue to partition those 
sub-subarrays.
3. Once we have a subarray that has zero or one elements, that is our base case 
and we do nothing. 
"""

"""
Partition Time/Space Complexity
- Each partition has:
    - Comparisons where we compare each of the values at hand to the pivot.
        - Since we compare each element of the array with the pivot, there are 
        at least N comparisons.
    - Swaps to conduct when appropriate on the values at the left and right 
    indices.
        - At most, there are N/2 swaps.

O(N + N/2) = O(N)
Time Complexity: O(N)
Space Complexity: O(1)
"""

"""
Quick Sort Time/Space Complexity:
- Uses multiple partitions. 
- Typically, each partition divides the array into subarrays roughly half the 
size of the array. 
- Partitioning continues until the subarray is of size 1. For an array of size 
N, the number of times we can half the array until we reach a size of 1 will 
usually take logN times. However, if the array is inversely ordered, it will
take N times.

Average Case Time Complexity: O(NlogN)
Worst Case Time Complexity: O(N^2)

- The space complexity directly correlates with the number of recursive calls
made. 

Average Space Complexity: O(logN)
Worst Case Space Complexity: O(N)
"""

def partition(items: list, left_index: int, right_index: int) -> int:
    """
    Sorts the array such that every value less than the pivot is to the left of 
    the pivot and every value greater than the pivot is to the right of the 
    pivot.
    @param items: The list to sort around the pivot.
    @param left_index: The left most index of the array.
    @param right_index: The right most index of the array.
    @return: Final value of left_index.
    """
    pivot_index = right_index
    pivot = items[pivot_index]
    # Moving one index left of the pivot index.
    right_index -= 1

    while (True):
        """
        Try and find an element that is to the left of the pivot that should be 
        on the right.
        """
        while(items[left_index] < pivot):
            left_index += 1

        """
        Try and find an element that is to the right of the pivot that should be
        on the left.
        """
        while(pivot < items[right_index]):
            right_index -= 1
        
        if left_index >= right_index:
            break 
        # Swap elements.
        else:
            items[left_index], items[right_index] = \
            items[right_index], items[left_index]
            left_index += 1
        
    items[left_index], items[pivot_index] = \
    items[pivot_index], items[left_index]      

    return left_index
        
def quick_sort(items: list, left_index: int, right_index: int):
    """
    A recursive sorting algorithm that partitions an array around a pivot.
    @param items: The list to sort.
    @param left_index: The left most index of the array.
    @param right_index: The right most index of the array.
    """
    # Base case: the array has 0 or 1 elements.
    if (right_index - left_index <= 0):
        return
    else:
        # Partition the range of the subarrary.
        pivot_index = partition(items, left_index, right_index)
        # Recursive call on all elements left of the pivot.
        quick_sort(items, left_index, pivot_index - 1)
        # Recursive call on all elements right of the pivot.
        quick_sort(items, pivot_index + 1, right_index)

"""
Examples:
items = [0, 5, 2, 1, 6, 3]
partition(items, 0, 5)    
@return: 3
items = [0, 1, 2, 3, 6, 5]

items = []
quick_sort(items, 0, 0)
items = []

items = [0, 5, 2, 1, 6, 3]
quick_sort(items, 0, 5)
items = [0, 1, 2, 3, 5, 6]
"""

"""
Notes:
- Quick sort is a divide and conquer algorithm.
- Although the worst case running time is similar to many of the other sorting
algorithms at O(n^2) (for inversely sorted arrays), it is still often the best
practical choice for sorting because it is remarkably efficient on average.
- Sorts in place.
- Quick sort relies on a concept called partitioning.
- Partitioning involves taking a random value from the array, labeling this the
pivot, and ensuring that:
    - Every number less than the pivot is to the left of the pivot.
    - Every number greater than the pivot is to the right of the pivot.
- After completing a partition, the array is likely still unsorted; however, the
pivot will be in its correct index within the array.
"""