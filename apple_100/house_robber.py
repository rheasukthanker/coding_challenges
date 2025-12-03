#https://leetcode.com/problems/house-robber/
class Solution:
    def rob(self, nums: List[int]) -> int:
        # Special handling for empty case.
        if not nums:
            return 0

        N = len(nums)

        rob_next_plus_one = 0
        rob_next = nums[N - 1]

        # DP table calculations.
        # robFrom(i)=max(robFrom(i+1),robFrom(i+2)+nums(i))
        for i in range(N - 2, -1, -1):

            # Same as recursive solution.
            current = max(rob_next, rob_next_plus_one + nums[i])

            # Update the variables
            rob_next_plus_one = rob_next
            rob_next = current

        return rob_next