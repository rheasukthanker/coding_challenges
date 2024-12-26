'''Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.'''
class Solution:
    def subsets(self, nums):
        self.output = []
        self.n, self.k = len(nums), None
        for self.k in range(self.n + 1):
            self.backtrack(0, [], nums)
        return self.output

    def backtrack(self, first, curr, nums):
        if len(curr) == self.k:
            self.output.append(curr[:])
        for i in range(first, self.n):
            curr.append(nums[i])
            self.backtrack(i + 1, curr, nums)
            curr.pop()


#Time complexity: O(N×(2**N)) to generate all subsets and then copy them into the output list.

#Space complexity: O(N). We are using O(N) space to maintain curr, and are modifying curr in-place with backtracking. Note that for space complexity analysis, we do not count space that is only used for the purpose of returning output, so the output array is ignored.
