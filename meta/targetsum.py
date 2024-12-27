'''You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.'''
# Total sum = m TC: O(nm), SC: O(m)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1 # one way to get to 0
        for i in range(len(nums)):
            next_dp = defaultdict(int)
            for curr_sum, count in dp.items():
                next_dp[curr_sum+nums[i]] +=count
                next_dp[curr_sum-nums[i]] +=count
            dp = next_dp
        return dp[target]
