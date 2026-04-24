"""
Bucket sort is a sorting algorithm that distributes the elements of an array into several groups, called buckets.
Each bucket is then sorted individually, either using a different sorting algorithm, or by recursively applying the bucket
sorting algorithm. 
Time complexity O(n)
Space complexity O(n+k) 
"""
arr = [2,7,1,3,6,5,4]
def bucket_sort(arr):
    if not arr:
        return arr
        
    # Find range of values
    max_val, min_val = max(arr), min(arr)
    
    # Create buckets
    bucket_range = (max_val - min_val) / len(arr)
    buckets = [[] for _ in range(len(arr) + 1)]
    
    # Distribute input array values into buckets
    for i in arr:
        if i == max_val:
            bucket_idx = len(arr) - 1
        else:
            bucket_idx = int((i - min_val) / bucket_range)
        buckets[bucket_idx].append(i)
    
    # Sort individual buckets
    for bucket in buckets:
        bucket.sort()
    
    # Concatenate all buckets into final array
    result = []
    for bucket in buckets:
        result.extend(bucket)
    
    return result

print(bucket_sort(arr))