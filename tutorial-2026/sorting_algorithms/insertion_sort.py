"""
It sorts the array by inserting each element into its correct position. 
At any point, the left side of the array is sorted while the right side is unsorted. 
We choose the first element in the unsorted array and insert it into the sorted array in the correct position. 
We then repeat this process for the next element in the unsorted array.
Time complexity O(n^2)
Space complexity O(1) in place mod of the array
"""
arr = [2,7,1,3,6,5,4]

def insertion_sort(arr):  

    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        while  j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

print(insertion_sort(arr))
