'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.'''
# Naive: Iterate thorugh all pairs TC O(n**2), SC O(1)
# Use hashmaps: Iterate through all pairs TC O(n), SC O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,n in enumerate(nums):
            if target-n in d:
                return [i,d[target-n]]
            d[n] = i
