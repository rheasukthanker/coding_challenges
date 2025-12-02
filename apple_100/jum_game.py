#https://leetcode.com/problems/jump-game/
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        current_start = 0
        current_end = 0
        jumps = 0
        n = len(nums)
        if n==1:
            return True
        if n==2:
            if nums[0]>=1:
                return True
            else:
                return False
        for i in range(n-1):
            current_start = max(current_start,i+nums[i])
            if i==current_end:
                current_end = current_start
                if current_end>=n-1:
                    return True
        return False