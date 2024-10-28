'''Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.'''
# O(nlogn)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        unique_nums = sorted(set(nums))
        if len(unique_nums) == 1:
            return 1
        start = unique_nums[0]
        streak = 1
        max_streak = 0
        for n in unique_nums[1:]:
            if start+1==n:
                streak = streak+1
            else:
                streak = 1
            start = n
            max_streak = max(max_streak, streak)
        return max_streak

# O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in nums:
            if n - 1 not in num_set:
                length = 1

                while n + length in num_set:
                    length += 1
                
                longest = max(longest, length)
        
        return longest
