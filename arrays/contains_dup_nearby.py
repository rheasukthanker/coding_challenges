'''Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.'''

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i,n in enumerate(nums):
            if n in d and (abs(i-d[n]))<=k:
                return True
            d[n] = i
        return False
