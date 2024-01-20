def find_subarray_with_given_sum(arr, target_sum):
    curr_sum = 0
    index_map = {}
    for i, num in enumerate(arr):
        curr_sum += num
        if curr_sum == target_sum:
            return True
        if curr_sum - target_sum in index_map:
            return True
        index_map[curr_sum] = i
        print(index_map)
    return False
 
arr = [1,1,3,1,1,5]
target_sum = 6
 
subarray = find_subarray_with_given_sum(arr, target_sum)
print("Array Exists", subarray)
