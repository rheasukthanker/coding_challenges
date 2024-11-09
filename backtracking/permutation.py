'''Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums[:]]
        
        res = []

        for _ in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            print(perms)
            for p in perms:
                p.append(n)
            
            res.extend(perms)
            nums.append(n)
        
        return res
