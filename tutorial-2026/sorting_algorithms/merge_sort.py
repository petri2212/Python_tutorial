"""
Merge sort is a divide and conquer algorithm that divides the input array into two halves, 
calls itself for the two halves, and then merges the two sorted halves.
Time complexity O(n*logn)
Space complexity O(n) 
"""

arr = [2,7,1,3,6,5,4]
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
        
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])#save if already ordered
    result.extend(right[j:])#
    return result


print(merge_sort(arr))