#https://leetcode.com/problems/permutations/
# Time complexity: O(n⋅n!), Space complexity O(n)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return
            for num in nums:
                if num not in curr:
                   curr.append(num)
                   backtrack(curr)
                   curr.pop()
        ans = []
        backtrack([])
        return ans 
        
