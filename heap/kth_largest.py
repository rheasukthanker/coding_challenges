'''Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?'''
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k>len(nums):
            return nums
        q = nums[:k]
        heapq.heapify(q)
        for i in range(k, len(nums)):
            if nums[i] > q[0]:
                heapq.heappush(q, nums[i])
                heapq.heappop(q)
        return heapq.heappop(q)
