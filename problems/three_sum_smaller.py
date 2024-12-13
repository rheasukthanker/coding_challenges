#Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target
# The time complexity is O(n**2), and the space complexity is O(log(n)). Here, n is the length of the array nums

class Solution(object):
 def threeSumSmaller(self, nums, target):
    count = 0
    nums.sort()
    for i in range(len(nums)):
        j, k = i+1, len(nums)-1
        while j < k:
            s = nums[i] + nums[j] + nums[k]
            if s < target:
                # if (i,j,k) works, then (i,j,k), (i,j,k-1),..., 
                # (i,j,j+1) all work, totally (k-j) triplets
                count += k-j
                j += 1
            else:
                k -= 1
    return count
