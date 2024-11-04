'''A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        low, high = 0, n-1
        while low <= high:
            mid = ((high-low)//2) + low
            # Peak element is present in right side
            if mid < n-1 and nums[mid] < nums[mid+1]:
                low = mid+1
            # Peak element is present in left side
            elif mid > 0 and nums[mid] < nums[mid-1]:
                high = mid-1
            else:
                return mid
