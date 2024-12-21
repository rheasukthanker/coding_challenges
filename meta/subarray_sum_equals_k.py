'''Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.'''


# Prefixsum of i : sum of all elements in an array before index i
# Property of prefixsum sum([i,j]) = prefixsum(j)-prefixsum(i-1)
# Let k be some sum value we are searching for prefixsum(i-1) = prefixsum(j) - k

# naive: brute force approach on O(n**2), iterate though all possible sub-arrays, when sum equals k add 1 to result
# advanced: Maintain a dictionary where index is prefix_sum and value is number of times prefix sum appears. Add zero to prefix sum dictionary as individual elements are also a sub array. Traverse once through array computing prefix sum, if prefix_sum-k is in dictionary add value of d[prefixsum-k] ie occurent of prefixsum complement to answer. Also add prefix sum to dictionary or increment count of occurence if it already exists
# TT O(n)
# ST O(n)
class Solution:
	def subarraySum(self, nums: List[int], k: int) -> int:

		result = 0 
		prefix_sum = 0
		d = {0 : 1}

		for num in nums:
		
			prefix_sum = prefix_sum + num

			if prefix_sum - k in d:
			
				result = result + d[prefix_sum - k]

			if prefix_sum not in d:
			
				d[prefix_sum] = 1
			else:
				d[prefix_sum] = d[prefix_sum] + 1

		return result
