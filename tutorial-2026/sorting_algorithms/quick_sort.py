"""
Quick sort is a divide and conquer algorithm that picks an element as pivot and partitions the given array around the picked pivot.
Time complexity O(n*logn)
Space complexity O(logn) 
"""

arr = [2,7,1,3,6,5,4]
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

print(quick_sort(arr))