#https://leetcode.com/problems/jump-game-ii/
class Solution:
    def jump(self, nums: List[int]) -> int:
        current_start = 0
        current_end = 0
        jumps = 0
        n = len(nums)
        for i in range(n-1):
            current_start = max(current_start,i+nums[i])
            if i == current_end:
                jumps=jumps+1
                current_end=current_start
        return jumps