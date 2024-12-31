# Naive: O(n**3), iterate over all triplets space O(1)
# Advanced: Use hash, dups : TC: O(n**2), SC: O(n)
# https://leetcode.com/problems/3sum/description/?envType=company&envId=facebook&favoriteSlug=facebook-three-months
# What I understand
# 1. Duplicates, ensures that an element is processed only once (note that results are unique)
# 2. Seen: saves the latest observed value of j corresponding to i
# 3. results: a set, add sorted list
# 4. Iterate though num pairs, if complement exists and complement corresponds to nums[i], add the thruple
# 5. If doesn't exist, add digit in j to correspond to index i 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        duplicates = set() # numbers processed so far
        seen = {} # complements seen so far
        results = set() # results array to return
        len_nums = len(nums)
        for i in range(len_nums):
            if nums[i] not in duplicates:
               duplicates.add(nums[i])
            else:
                continue
            for j in range(i+1, len_nums):
                complement = -nums[i]-nums[j]
                if complement in seen and seen[complement]==i:
                    pair = sorted((nums[i], nums[j], complement))
                    results.add(tuple(pair))
                else:
                    seen[nums[j]] = i
        return list(results)
